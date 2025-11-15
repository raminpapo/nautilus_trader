#!/usr/bin/env python3
"""
Repository Scanner and File Classifier
Part of the World's Best Repo Book Generator
"""

import os
import json
import hashlib
import mimetypes
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# Binary file extensions to skip detailed documentation
BINARY_EXTENSIONS = {
    '.pyc', '.pyo', '.so', '.dll', '.dylib', '.a', '.o', '.obj',
    '.exe', '.bin', '.dat', '.db', '.sqlite', '.sqlite3',
    '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.ico', '.svg', '.webp',
    '.mp3', '.mp4', '.avi', '.mov', '.wav', '.flac',
    '.zip', '.tar', '.gz', '.bz2', '.xz', '.7z', '.rar',
    '.whl', '.egg', '.jar', '.war',
    '.ttf', '.otf', '.woff', '.woff2', '.eot',
    '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx'
}

# Text file extensions that should get full documentation
TEXT_EXTENSIONS = {
    '.py', '.pyx', '.pxd', '.pxi',  # Python
    '.rs', '.toml',  # Rust
    '.c', '.h', '.cpp', '.hpp', '.cc', '.cxx',  # C/C++
    '.js', '.jsx', '.ts', '.tsx', '.mjs',  # JavaScript/TypeScript
    '.java', '.kt', '.scala',  # JVM languages
    '.go', '.rs',  # Go, Rust
    '.sh', '.bash', '.zsh', '.fish',  # Shell scripts
    '.md', '.rst', '.txt', '.adoc',  # Documentation
    '.yaml', '.yml', '.json', '.xml', '.toml', '.ini', '.cfg', '.conf',  # Config
    '.sql', '.proto', '.capnp',  # Data/Schema
    '.html', '.css', '.scss', '.sass', '.less',  # Web
    '.Makefile', '.mk', '.cmake',  # Build files
    '.dockerfile', '.containerfile',  # Containers
    '.gitignore', '.gitattributes', '.editorconfig',  # Git/Editor config
}

# Paths to exclude
EXCLUDE_PATHS = {
    '.git', '__pycache__', 'node_modules', '.pytest_cache',
    '.mypy_cache', '.tox', 'venv', '.venv', 'env', '.env',
    'build', 'dist', '.eggs', '*.egg-info',
    'docs',  # Don't scan our own output
}

class RepoScanner:
    def __init__(self, repo_root: str):
        self.repo_root = Path(repo_root).resolve()
        self.files = []
        self.folders = []
        self.stats = defaultdict(int)

    def should_exclude(self, path: Path) -> bool:
        """Check if path should be excluded"""
        parts = path.parts
        for exclude in EXCLUDE_PATHS:
            if exclude in parts or any(p.startswith(exclude) for p in parts):
                return True
        return False

    def classify_file(self, file_path: Path) -> dict:
        """Classify a file and gather metadata"""
        try:
            stat = file_path.stat()
            size = stat.st_size
            ext = file_path.suffix.lower()

            # Determine file type
            if ext in BINARY_EXTENSIONS:
                file_type = 'binary'
            elif ext in TEXT_EXTENSIONS or ext == '':
                # Files with no extension might be text (LICENSE, README, etc)
                file_type = 'text'
            else:
                # Try to guess based on content for unknown extensions
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        f.read(512)  # Try to read a bit
                    file_type = 'text'
                except (UnicodeDecodeError, PermissionError):
                    file_type = 'binary'

            # Check for very large files
            is_large = size > 100 * 1024 * 1024  # 100MB

            rel_path = file_path.relative_to(self.repo_root)

            return {
                'path': str(rel_path),
                'absolute_path': str(file_path),
                'size': size,
                'extension': ext,
                'type': file_type,
                'is_large': is_large,
                'mtime': stat.st_mtime,
            }
        except Exception as e:
            return {
                'path': str(file_path.relative_to(self.repo_root)),
                'error': str(e),
                'type': 'error'
            }

    def scan(self):
        """Recursively scan the repository"""
        print(f"Scanning repository at {self.repo_root}")

        for root, dirs, files in os.walk(self.repo_root):
            root_path = Path(root)

            # Filter out excluded directories
            dirs[:] = [d for d in dirs if not self.should_exclude(root_path / d)]

            # Track folders
            if root_path != self.repo_root and not self.should_exclude(root_path):
                rel_folder = root_path.relative_to(self.repo_root)
                self.folders.append(str(rel_folder))

            # Process files
            for file in files:
                file_path = root_path / file

                if self.should_exclude(file_path):
                    continue

                file_info = self.classify_file(file_path)
                self.files.append(file_info)

                # Update stats
                self.stats['total_files'] += 1
                self.stats['total_bytes'] += file_info.get('size', 0)
                self.stats[f"type_{file_info['type']}"] += 1

                if file_info.get('is_large'):
                    self.stats['large_files'] += 1

        # Sort for deterministic output
        self.files.sort(key=lambda x: x['path'])
        self.folders.sort()

        print(f"Scan complete: {len(self.files)} files, {len(self.folders)} folders")
        return self

    def compute_fingerprint(self, commit_sha: str = None) -> str:
        """Compute a deterministic fingerprint of the repo"""
        if commit_sha:
            return commit_sha

        # Fallback: hash of all file paths and mtimes
        h = hashlib.sha256()
        for f in self.files:
            h.update(f['path'].encode('utf-8'))
            h.update(str(f.get('mtime', 0)).encode('utf-8'))
        return h.hexdigest()

    def save_manifest(self, output_path: Path, commit_sha: str = None, repo_url: str = None):
        """Save the scan results as manifest.json"""
        fingerprint = self.compute_fingerprint(commit_sha)

        manifest = {
            'generator_version': '1.0.0',
            'repo_source': repo_url or str(self.repo_root),
            'repo_fingerprint': fingerprint,
            'commit_sha': commit_sha,
            'scan_timestamp': datetime.utcnow().isoformat() + 'Z',
            'files_scanned': len(self.files),
            'folders_scanned': len(self.folders),
            'total_bytes': self.stats['total_bytes'],
            'stats': dict(self.stats),
            'files': self.files,
            'folders': self.folders,
        }

        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2)

        print(f"Manifest saved to {output_path}")
        return manifest

if __name__ == '__main__':
    import sys

    repo_root = sys.argv[1] if len(sys.argv) > 1 else '.'
    commit_sha = sys.argv[2] if len(sys.argv) > 2 else None
    repo_url = sys.argv[3] if len(sys.argv) > 3 else None

    scanner = RepoScanner(repo_root)
    scanner.scan()

    manifest_path = Path(repo_root) / 'docs' / 'manifest.json'
    manifest = scanner.save_manifest(manifest_path, commit_sha, repo_url)

    print(f"\nSummary:")
    print(f"  Files: {manifest['files_scanned']}")
    print(f"  Folders: {manifest['folders_scanned']}")
    print(f"  Total size: {manifest['total_bytes'] / 1024 / 1024:.2f} MB")
    print(f"  Text files: {manifest['stats'].get('type_text', 0)}")
    print(f"  Binary files: {manifest['stats'].get('type_binary', 0)}")
    print(f"  Fingerprint: {manifest['repo_fingerprint'][:16]}...")
