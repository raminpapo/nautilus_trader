#!/usr/bin/env python3
"""Repository scanner and classifier for documentation generation."""

import os
import json
import hashlib
import mimetypes
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple

REPO_ROOT = Path("/home/user/nautilus_trader")
DOCS_ROOT = REPO_ROOT / "docs"
FILE_LIST = Path("/tmp/repo_files.txt")

# Binary file extensions to skip
BINARY_EXTENSIONS = {
    '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.ico', '.svg',
    '.pdf', '.zip', '.tar', '.gz', '.bz2', '.xz', '.7z',
    '.so', '.dylib', '.dll', '.exe', '.bin', '.o', '.a',
    '.whl', '.pyc', '.pyo', '.class', '.jar',
    '.wasm', '.ttf', '.woff', '.woff2', '.eot',
    '.mp3', '.mp4', '.avi', '.mov', '.wav',
    '.db', '.sqlite', '.sqlite3',
}

# Very large file threshold
LARGE_FILE_THRESHOLD = 10 * 1024 * 1024  # 10MB

def classify_file(filepath: Path) -> Tuple[str, dict]:
    """Classify a file as text, binary, or large."""
    try:
        stat = filepath.stat()
        size = stat.st_size

        # Check extension
        ext = filepath.suffix.lower()
        if ext in BINARY_EXTENSIONS:
            return 'binary', {'reason': 'binary_extension', 'size': size}

        # Check size
        if size > LARGE_FILE_THRESHOLD:
            return 'large', {'reason': 'large_file', 'size': size}

        # Try to detect if file is text
        try:
            with open(filepath, 'r', encoding='utf-8', errors='strict') as f:
                f.read(1024)  # Try to read first 1KB
            return 'text', {'size': size}
        except (UnicodeDecodeError, PermissionError):
            # Try latin-1 as fallback
            try:
                with open(filepath, 'r', encoding='latin-1', errors='strict') as f:
                    f.read(1024)
                return 'text', {'size': size, 'encoding': 'latin-1'}
            except:
                return 'binary', {'reason': 'decode_error', 'size': size}

    except Exception as e:
        return 'error', {'reason': str(e)}

def scan_repository() -> Dict:
    """Scan repository and create initial manifest."""

    # Read file list
    with open(FILE_LIST, 'r') as f:
        all_files = [line.strip() for line in f if line.strip()]

    # Classify files
    text_files = []
    binary_files = []
    large_files = []
    error_files = []

    total_size = 0

    for filepath_str in all_files:
        filepath = Path(filepath_str)
        rel_path = filepath.relative_to(REPO_ROOT)

        classification, metadata = classify_file(filepath)

        file_info = {
            'path': str(rel_path),
            'absolute_path': str(filepath),
            'size': metadata.get('size', 0),
        }

        if classification == 'text':
            text_files.append(file_info)
            total_size += metadata.get('size', 0)
        elif classification == 'binary':
            binary_files.append(file_info)
        elif classification == 'large':
            large_files.append(file_info)
        elif classification == 'error':
            error_files.append({**file_info, 'error': metadata.get('reason', 'unknown')})

    # Create manifest
    manifest = {
        'generator_version': '1.0.0',
        'repo_source': 'raminpapo/nautilus_trader',
        'repo_fingerprint': '617c5780bf4908421baf8bcec35851e489b9b3c3',
        'scan_timestamp': datetime.utcnow().isoformat() + 'Z',
        'file_counts': {
            'total': len(all_files),
            'text': len(text_files),
            'binary': len(binary_files),
            'large': len(large_files),
            'error': len(error_files),
        },
        'total_size_bytes': total_size,
        'text_files': text_files,
        'binary_files': binary_files,
        'large_files': large_files,
        'error_files': error_files,
    }

    return manifest

if __name__ == '__main__':
    print("Scanning repository...")
    manifest = scan_repository()

    # Save manifest
    DOCS_ROOT.mkdir(exist_ok=True)
    manifest_path = DOCS_ROOT / 'manifest.json'

    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)

    print(f"Scan complete!")
    print(f"Total files: {manifest['file_counts']['total']}")
    print(f"Text files: {manifest['file_counts']['text']}")
    print(f"Binary files: {manifest['file_counts']['binary']}")
    print(f"Large files: {manifest['file_counts']['large']}")
    print(f"Error files: {manifest['file_counts']['error']}")
    print(f"Manifest saved to: {manifest_path}")
