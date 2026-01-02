#!/usr/bin/env python3
"""
Revision Tracker for The Wheel of Meat
=======================================
CLI for updating revision-manifest.json status.

Usage:
    python revision_tracker.py start [chapter] [scene]
    python revision_tracker.py pass-complete [chapter] [scene] [pass_name]
    python revision_tracker.py complete [chapter] [scene]
    python revision_tracker.py report
    python revision_tracker.py status [chapter]

Pass names: tic_scan, forbidden_pattern, voice_check, sensory_audit, continuity
"""

import json
import argparse
from pathlib import Path
from datetime import datetime

# ============================================================================
# CONFIGURATION
# ============================================================================

BASE_DIR = Path(__file__).parent.parent.resolve()
MANIFEST_PATH = BASE_DIR / "reference" / "revision-manifest.json"

VALID_PASSES = [
    "tic_scan",
    "forbidden_pattern",
    "voice_check",
    "sensory_audit",
    "continuity"
]

# ============================================================================
# MANIFEST OPERATIONS
# ============================================================================

def load_manifest() -> dict:
    """Load the revision manifest."""
    if not MANIFEST_PATH.exists():
        print(f"ERROR: Manifest not found: {MANIFEST_PATH}")
        exit(1)

    with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_manifest(manifest: dict):
    """Save the revision manifest."""
    with open(MANIFEST_PATH, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2)
    print(f"Manifest saved: {MANIFEST_PATH}")


def find_scene(manifest: dict, chapter: str, scene: str) -> tuple:
    """Find a scene in the manifest. Returns (chapter_key, scene_key) or (None, None)."""
    ch_key = str(chapter)

    if ch_key not in manifest['chapters']:
        return None, None

    chapter_data = manifest['chapters'][ch_key]

    # Try exact match first
    if scene in chapter_data['scenes']:
        return ch_key, scene

    # Try partial match
    for scene_key in chapter_data['scenes']:
        if scene in scene_key or scene_key in scene:
            return ch_key, scene_key

    return ch_key, None


# ============================================================================
# COMMANDS
# ============================================================================

def cmd_start(args, manifest):
    """Mark a scene as in-progress."""
    ch_key, scene_key = find_scene(manifest, args.chapter, args.scene)

    if ch_key is None:
        print(f"ERROR: Chapter {args.chapter} not found")
        return False

    if scene_key is None:
        print(f"ERROR: Scene '{args.scene}' not found in chapter {args.chapter}")
        print(f"Available scenes: {list(manifest['chapters'][ch_key]['scenes'].keys())}")
        return False

    scene_data = manifest['chapters'][ch_key]['scenes'][scene_key]
    old_status = scene_data['status']
    scene_data['status'] = 'in_progress'

    # Update metadata
    if old_status == 'needs_revision':
        manifest['metadata']['needs_revision'] -= 1
        manifest['metadata']['revision_in_progress'] += 1

    save_manifest(manifest)
    print(f"Started revision: Chapter {ch_key} - {scene_key}")
    print(f"  Status: {old_status} → in_progress")
    print(f"  Passes remaining: {scene_data['passes_remaining']}")
    return True


def cmd_pass_complete(args, manifest):
    """Mark a pass as complete for a scene."""
    if args.pass_name not in VALID_PASSES:
        print(f"ERROR: Invalid pass name '{args.pass_name}'")
        print(f"Valid passes: {VALID_PASSES}")
        return False

    ch_key, scene_key = find_scene(manifest, args.chapter, args.scene)

    if ch_key is None or scene_key is None:
        print(f"ERROR: Scene not found: Chapter {args.chapter} - {args.scene}")
        return False

    scene_data = manifest['chapters'][ch_key]['scenes'][scene_key]

    # Move pass from remaining to complete
    if args.pass_name in scene_data['passes_remaining']:
        scene_data['passes_remaining'].remove(args.pass_name)
        if args.pass_name not in scene_data['passes_complete']:
            scene_data['passes_complete'].append(args.pass_name)

    scene_data['last_revised'] = datetime.now().strftime('%Y-%m-%d')

    # Check if all passes complete
    if not scene_data['passes_remaining']:
        scene_data['status'] = 'revision_complete'
        if manifest['metadata']['revision_in_progress'] > 0:
            manifest['metadata']['revision_in_progress'] -= 1
        manifest['metadata']['revision_complete'] += 1
        print(f"ALL PASSES COMPLETE - Scene marked as revision_complete")

    save_manifest(manifest)
    print(f"Pass complete: Chapter {ch_key} - {scene_key} - {args.pass_name}")
    print(f"  Remaining passes: {scene_data['passes_remaining'] or 'NONE'}")
    return True


def cmd_complete(args, manifest):
    """Mark a scene as fully revised."""
    ch_key, scene_key = find_scene(manifest, args.chapter, args.scene)

    if ch_key is None or scene_key is None:
        print(f"ERROR: Scene not found: Chapter {args.chapter} - {args.scene}")
        return False

    scene_data = manifest['chapters'][ch_key]['scenes'][scene_key]
    old_status = scene_data['status']

    # Mark all passes complete
    scene_data['passes_complete'] = VALID_PASSES.copy()
    scene_data['passes_remaining'] = []
    scene_data['status'] = 'revision_complete'
    scene_data['last_revised'] = datetime.now().strftime('%Y-%m-%d')

    # Update metadata
    if old_status == 'needs_revision':
        manifest['metadata']['needs_revision'] -= 1
    elif old_status == 'in_progress':
        manifest['metadata']['revision_in_progress'] -= 1
    manifest['metadata']['revision_complete'] += 1

    save_manifest(manifest)
    print(f"Scene complete: Chapter {ch_key} - {scene_key}")
    print(f"  Status: {old_status} → revision_complete")
    return True


def cmd_report(args, manifest):
    """Generate a progress report."""
    meta = manifest['metadata']

    print("=" * 60)
    print("REVISION PROGRESS REPORT")
    print("=" * 60)
    print()
    print(f"Total Scenes:        {meta['total_scenes']}")
    print(f"Revision Complete:   {meta['revision_complete']} ({meta['revision_complete']/meta['total_scenes']*100:.1f}%)")
    print(f"In Progress:         {meta['revision_in_progress']}")
    print(f"Needs Revision:      {meta['needs_revision']}")
    print()

    # Per-chapter breakdown
    print("CHAPTER BREAKDOWN:")
    print("-" * 60)
    print(f"{'Ch':<4} {'Title':<30} {'Complete':>10} {'Remaining':>10}")
    print("-" * 60)

    for ch_key in sorted(manifest['chapters'].keys(), key=int):
        ch_data = manifest['chapters'][ch_key]
        scenes = ch_data['scenes']
        complete = sum(1 for s in scenes.values() if s['status'] == 'revision_complete')
        total = len(scenes)
        remaining = total - complete

        title = ch_data['title'][:28]
        print(f"{ch_key:<4} {title:<30} {complete:>10} {remaining:>10}")

    print("-" * 60)
    print()

    # Scenes in progress
    in_progress = []
    for ch_key, ch_data in manifest['chapters'].items():
        for scene_key, scene_data in ch_data['scenes'].items():
            if scene_data['status'] == 'in_progress':
                in_progress.append((ch_key, scene_key, scene_data['passes_remaining']))

    if in_progress:
        print("SCENES IN PROGRESS:")
        for ch, scene, remaining in in_progress:
            print(f"  Ch{ch}: {scene}")
            print(f"    Passes remaining: {remaining}")
        print()

    return True


def cmd_status(args, manifest):
    """Show status for a specific chapter."""
    ch_key = str(args.chapter)

    if ch_key not in manifest['chapters']:
        print(f"ERROR: Chapter {ch_key} not found")
        return False

    ch_data = manifest['chapters'][ch_key]

    print(f"CHAPTER {ch_key}: {ch_data['title']}")
    print(f"Type: {ch_data['type']}")
    print(f"Status: {ch_data['status']}")
    print()
    print("SCENES:")
    print("-" * 70)

    for scene_key, scene_data in ch_data['scenes'].items():
        status = scene_data['status']
        passes_done = len(scene_data['passes_complete'])
        passes_total = passes_done + len(scene_data['passes_remaining'])

        status_icon = {
            'revision_complete': '✓',
            'in_progress': '→',
            'needs_revision': '○'
        }.get(status, '?')

        print(f"  {status_icon} {scene_key}")
        print(f"      Status: {status} | Passes: {passes_done}/{passes_total}")
        if scene_data['passes_remaining']:
            print(f"      Remaining: {', '.join(scene_data['passes_remaining'])}")

    print("-" * 70)
    return True


# ============================================================================
# MAIN
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Track revision progress in revision-manifest.json"
    )
    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # start command
    start_parser = subparsers.add_parser('start', help='Start revising a scene')
    start_parser.add_argument('chapter', help='Chapter number')
    start_parser.add_argument('scene', help='Scene file name')

    # pass-complete command
    pass_parser = subparsers.add_parser('pass-complete', help='Mark a pass as complete')
    pass_parser.add_argument('chapter', help='Chapter number')
    pass_parser.add_argument('scene', help='Scene file name')
    pass_parser.add_argument('pass_name', help='Pass name (tic_scan, forbidden_pattern, voice_check, sensory_audit, continuity)')

    # complete command
    complete_parser = subparsers.add_parser('complete', help='Mark scene as fully revised')
    complete_parser.add_argument('chapter', help='Chapter number')
    complete_parser.add_argument('scene', help='Scene file name')

    # report command
    subparsers.add_parser('report', help='Show progress report')

    # status command
    status_parser = subparsers.add_parser('status', help='Show chapter status')
    status_parser.add_argument('chapter', help='Chapter number')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    manifest = load_manifest()

    commands = {
        'start': cmd_start,
        'pass-complete': cmd_pass_complete,
        'complete': cmd_complete,
        'report': cmd_report,
        'status': cmd_status
    }

    if args.command in commands:
        success = commands[args.command](args, manifest)
        return 0 if success else 1
    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
