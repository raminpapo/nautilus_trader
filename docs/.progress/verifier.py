#!/usr/bin/env python3
"""
Documentation Verifier
Part of the World's Best Repo Book Generator
"""

import os
import re
import json
import hashlib
from pathlib import Path
from datetime import datetime
from collections import defaultdict

class DocumentationVerifier:
    """Verify documentation integrity and generate report"""

    def __init__(self, repo_root: Path, docs_root: Path, manifest_path: Path):
        self.repo_root = Path(repo_root)
        self.docs_root = Path(docs_root)
        self.manifest_path = Path(manifest_path)
        self.manifest = None
        self.errors = []
        self.warnings = []
        self.stats = defaultdict(int)
        self.checksums = {}

    def load_manifest(self):
        """Load manifest"""
        with open(self.manifest_path, 'r') as f:
            self.manifest = json.load(f)

    def compute_file_checksum(self, file_path: Path) -> str:
        """Compute SHA256 checksum of a file"""
        try:
            sha256 = hashlib.sha256()
            with open(file_path, 'rb') as f:
                for chunk in iter(lambda: f.read(8192), b''):
                    sha256.update(chunk)
            return sha256.hexdigest()
        except Exception as e:
            return f"ERROR: {e}"

    def verify_file_docs_exist(self):
        """Verify that documentation exists for all text files"""
        print("Verifying file documentation...")

        for file_info in self.manifest['files']:
            if file_info['type'] != 'text':
                continue

            file_path = Path(file_info['path'])
            doc_file = self.docs_root / file_path.parent / f"{file_path.name}_docs.md"
            kw_file = self.docs_root / file_path.parent / f"{file_path.name}_kw.md"

            if not doc_file.exists():
                self.errors.append(f"Missing documentation: {doc_file}")
                self.stats['missing_docs'] += 1
            else:
                self.stats['docs_found'] += 1
                # Compute checksum
                self.checksums[str(doc_file.relative_to(self.docs_root))] = self.compute_file_checksum(doc_file)

            if not kw_file.exists():
                self.errors.append(f"Missing keywords: {kw_file}")
                self.stats['missing_kw'] += 1
            else:
                self.stats['kw_found'] += 1
                # Compute checksum
                self.checksums[str(kw_file.relative_to(self.docs_root))] = self.compute_file_checksum(kw_file)

    def verify_folder_docs_exist(self):
        """Verify that documentation exists for all folders"""
        print("Verifying folder documentation...")

        all_folders = [''] + self.manifest['folders']  # Include root

        for folder in all_folders:
            folder_path = Path(folder) if folder else Path('.')
            index_file = self.docs_root / folder_path / 'index.md'
            doc_file = self.docs_root / folder_path / 'doc.md'
            sub_file = self.docs_root / folder_path / 'sub.md'

            if not index_file.exists():
                self.errors.append(f"Missing folder index: {index_file}")
                self.stats['missing_folder_index'] += 1
            else:
                self.stats['folder_index_found'] += 1
                self.checksums[str(index_file.relative_to(self.docs_root))] = self.compute_file_checksum(index_file)

            if not doc_file.exists():
                self.errors.append(f"Missing folder doc: {doc_file}")
                self.stats['missing_folder_doc'] += 1
            else:
                self.stats['folder_doc_found'] += 1
                self.checksums[str(doc_file.relative_to(self.docs_root))] = self.compute_file_checksum(doc_file)

            if not sub_file.exists():
                self.errors.append(f"Missing folder sub: {sub_file}")
                self.stats['missing_folder_sub'] += 1
            else:
                self.stats['folder_sub_found'] += 1
                self.checksums[str(sub_file.relative_to(self.docs_root))] = self.compute_file_checksum(sub_file)

    def verify_global_files(self):
        """Verify that global files exist"""
        print("Verifying global files...")

        required_files = ['index.md', 'keywords.md', 'comprehensive_book.md', 'manifest.json']

        for filename in required_files:
            file_path = self.docs_root / filename
            if not file_path.exists():
                self.errors.append(f"Missing global file: {file_path}")
                self.stats[f'missing_{filename}'] += 1
            else:
                self.stats[f'found_{filename}'] += 1
                self.checksums[filename] = self.compute_file_checksum(file_path)

    def validate_links(self):
        """Validate relative links in documentation (sample check)"""
        print("Validating links (sample check)...")

        # Sample a subset of files to check links
        sample_files = []

        # Check root index
        sample_files.append(self.docs_root / 'index.md')

        # Check a few folder indexes
        for folder in self.manifest['folders'][:10]:
            index_file = self.docs_root / Path(folder) / 'index.md'
            if index_file.exists():
                sample_files.append(index_file)

        link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

        for file_path in sample_files:
            if not file_path.exists():
                continue

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                for match in link_pattern.finditer(content):
                    link_text = match.group(1)
                    link_target = match.group(2)

                    # Skip external links
                    if link_target.startswith('http://') or link_target.startswith('https://'):
                        continue

                    # Skip anchors
                    if link_target.startswith('#'):
                        continue

                    # Remove anchor from relative link
                    link_target = link_target.split('#')[0]

                    if not link_target:
                        continue

                    # Resolve relative link
                    target_path = (file_path.parent / link_target).resolve()

                    if not target_path.exists():
                        self.warnings.append(f"Broken link in {file_path.relative_to(self.docs_root)}: {link_target}")
                        self.stats['broken_links'] += 1
                    else:
                        self.stats['valid_links'] += 1

            except Exception as e:
                self.warnings.append(f"Error checking links in {file_path}: {e}")

    def list_skipped_files(self):
        """List files that were skipped"""
        print("Listing skipped files...")

        for file_info in self.manifest['files']:
            if file_info['type'] == 'binary':
                self.stats['binary_skipped'] += 1
            elif file_info['type'] == 'error':
                self.stats['error_files'] += 1
                self.warnings.append(f"File with errors: {file_info['path']} - {file_info.get('error', 'unknown')}")

    def generate_report(self) -> str:
        """Generate verification report"""
        parts = []

        parts.append("# Documentation Verification Report\n\n")
        parts.append(f"**Generated:** {datetime.utcnow().isoformat()}Z\n")
        parts.append(f"**Repository:** {self.manifest['repo_source']}\n")
        parts.append(f"**Commit:** {self.manifest['commit_sha']}\n")
        parts.append("\n---\n\n")

        # Summary
        parts.append("## Summary\n\n")
        parts.append(f"- **Total errors:** {len(self.errors)}\n")
        parts.append(f"- **Total warnings:** {len(self.warnings)}\n")
        parts.append(f"- **Files scanned:** {self.manifest['files_scanned']:,}\n")
        parts.append(f"- **Folders scanned:** {self.manifest['folders_scanned']:,}\n")
        parts.append("\n---\n\n")

        # Statistics
        parts.append("## Statistics\n\n")
        for key in sorted(self.stats.keys()):
            parts.append(f"- **{key}:** {self.stats[key]:,}\n")
        parts.append("\n---\n\n")

        # Errors
        if self.errors:
            parts.append("## Errors\n\n")
            for error in self.errors[:100]:  # Limit to first 100
                parts.append(f"- {error}\n")
            if len(self.errors) > 100:
                parts.append(f"\n*... and {len(self.errors) - 100} more errors*\n")
            parts.append("\n---\n\n")
        else:
            parts.append("## Errors\n\n")
            parts.append("*No errors found!*\n\n")
            parts.append("---\n\n")

        # Warnings
        if self.warnings:
            parts.append("## Warnings\n\n")
            for warning in self.warnings[:100]:  # Limit to first 100
                parts.append(f"- {warning}\n")
            if len(self.warnings) > 100:
                parts.append(f"\n*... and {len(self.warnings) - 100} more warnings*\n")
            parts.append("\n---\n\n")
        else:
            parts.append("## Warnings\n\n")
            parts.append("*No warnings!*\n\n")
            parts.append("---\n\n")

        # Skipped files
        parts.append("## Skipped Files\n\n")
        parts.append(f"- **Binary files:** {self.stats.get('binary_skipped', 0):,}\n")
        parts.append(f"- **Files with errors:** {self.stats.get('error_files', 0):,}\n")
        parts.append("\n---\n\n")

        # Checksums
        parts.append("## File Checksums\n\n")
        parts.append(f"Total files checksummed: {len(self.checksums):,}\n\n")
        parts.append("See `manifest.json` for complete checksum list.\n\n")
        parts.append("---\n\n")

        parts.append("*End of Verification Report*\n")

        return ''.join(parts)

    def verify_all(self):
        """Run all verification checks"""
        self.load_manifest()

        self.verify_file_docs_exist()
        self.verify_folder_docs_exist()
        self.verify_global_files()
        self.validate_links()
        self.list_skipped_files()

        # Generate report
        report_content = self.generate_report()
        report_path = self.docs_root / 'verification_report.md'
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report_content)

        print(f"\nVerification report written to: {report_path}")

        # Update manifest with checksums
        self.manifest['checksums'] = self.checksums
        self.manifest['verification_timestamp'] = datetime.utcnow().isoformat() + 'Z'
        self.manifest['verification_stats'] = dict(self.stats)
        self.manifest['verification_errors'] = len(self.errors)
        self.manifest['verification_warnings'] = len(self.warnings)

        with open(self.manifest_path, 'w', encoding='utf-8') as f:
            json.dump(self.manifest, f, indent=2)

        print(f"Manifest updated with checksums and verification stats")

        return {
            'errors': len(self.errors),
            'warnings': len(self.warnings),
            'stats': dict(self.stats),
            'checksums': len(self.checksums)
        }


if __name__ == '__main__':
    import sys

    repo_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
    docs_root = repo_root / 'docs'
    manifest_path = docs_root / 'manifest.json'

    verifier = DocumentationVerifier(repo_root, docs_root, manifest_path)
    result = verifier.verify_all()

    print("\nVerification Summary:")
    print(json.dumps(result, indent=2))
