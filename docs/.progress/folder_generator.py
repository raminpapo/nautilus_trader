#!/usr/bin/env python3
"""
Folder Documentation Generator
Part of the World's Best Repo Book Generator
"""

import os
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

class FolderDocGenerator:
    """Generate index.md, doc.md, and sub.md for each folder"""

    def __init__(self, folder_path: Path, repo_root: Path, docs_root: Path, manifest: dict):
        self.folder_path = folder_path
        self.repo_root = Path(repo_root)
        self.docs_root = Path(docs_root)
        self.manifest = manifest
        self.rel_folder = folder_path.relative_to(repo_root) if folder_path != repo_root else Path('.')

    def get_folder_contents(self):
        """Get direct children of this folder from manifest"""
        files = []
        subfolders = []

        # Get files in this folder
        for file_info in self.manifest['files']:
            file_path = Path(file_info['path'])
            if file_path.parent == self.rel_folder:
                files.append(file_info)

        # Get subfolders
        for folder in self.manifest['folders']:
            folder_path = Path(folder)
            if folder_path.parent == self.rel_folder:
                subfolders.append(folder)

        return files, subfolders

    def generate_index_md(self) -> str:
        """Generate index.md for the folder"""
        parts = []

        folder_display = str(self.rel_folder) if str(self.rel_folder) != '.' else 'Root'
        parts.append(f"# Index: `{folder_display}`\n\n")
        parts.append(f"**Generated:** {datetime.utcnow().isoformat()}Z\n\n")
        parts.append("---\n\n")

        files, subfolders = self.get_folder_contents()

        # Table of contents
        parts.append("## Contents\n\n")
        if subfolders:
            parts.append(f"- **Subfolders:** {len(subfolders)}\n")
        if files:
            parts.append(f"- **Files:** {len(files)}\n")
        parts.append("\n---\n\n")

        # Subfolders
        if subfolders:
            parts.append("## Subfolders\n\n")
            for subfolder in sorted(subfolders):
                subfolder_name = Path(subfolder).name
                # Relative path from current docs folder to subfolder docs
                rel_link = f"{subfolder_name}/index.md"
                parts.append(f"- [{subfolder_name}/]({rel_link})\n")
            parts.append("\n---\n\n")

        # Files
        if files:
            parts.append("## Files\n\n")
            for file_info in sorted(files, key=lambda x: x['path']):
                file_name = Path(file_info['path']).name
                file_type = file_info['type']
                file_size = file_info['size']

                if file_type == 'text':
                    # Link to documentation
                    doc_link = f"{file_name}_docs.md"
                    kw_link = f"{file_name}_kw.md"
                    parts.append(f"- **{file_name}** ({file_size:,} bytes)\n")
                    parts.append(f"  - [Documentation]({doc_link})\n")
                    parts.append(f"  - [Keywords]({kw_link})\n")
                else:
                    parts.append(f"- **{file_name}** ({file_size:,} bytes) - *{file_type}*\n")

            parts.append("\n")

        return ''.join(parts)

    def generate_doc_md(self) -> str:
        """Generate doc.md with narrative context"""
        parts = []

        folder_display = str(self.rel_folder) if str(self.rel_folder) != '.' else 'Root'
        parts.append(f"# Documentation: `{folder_display}`\n\n")
        parts.append(f"**Generated:** {datetime.utcnow().isoformat()}Z\n\n")
        parts.append("---\n\n")

        files, subfolders = self.get_folder_contents()

        # Purpose and role
        parts.append("## Purpose\n\n")
        parts.append(self._infer_folder_purpose())
        parts.append("\n---\n\n")

        # Structure
        parts.append("## Structure\n\n")
        if subfolders:
            parts.append(f"This folder contains {len(subfolders)} subdirectories:\n\n")
            for subfolder in sorted(subfolders)[:20]:
                parts.append(f"- `{Path(subfolder).name}/`\n")
            if len(subfolders) > 20:
                parts.append(f"\n*... and {len(subfolders) - 20} more*\n")
            parts.append("\n")

        if files:
            parts.append(f"This folder contains {len(files)} files:\n\n")

            # Group by type/extension
            by_ext = defaultdict(list)
            for f in files:
                ext = f['extension'] or 'no extension'
                by_ext[ext].append(f)

            for ext in sorted(by_ext.keys()):
                file_list = by_ext[ext]
                parts.append(f"**{ext}** ({len(file_list)} files):\n")
                for f in sorted(file_list, key=lambda x: x['path'])[:10]:
                    parts.append(f"- `{Path(f['path']).name}`\n")
                if len(file_list) > 10:
                    parts.append(f"  *... and {len(file_list) - 10} more*\n")
                parts.append("\n")

        parts.append("---\n\n")

        # Key concepts
        parts.append("## Key Concepts\n\n")
        parts.append(self._extract_key_concepts(files))
        parts.append("\n")

        return ''.join(parts)

    def _infer_folder_purpose(self) -> str:
        """Infer folder purpose from name and contents"""
        folder_name = self.folder_path.name.lower() if self.folder_path != self.repo_root else 'root'

        purpose_map = {
            'test': "This folder contains test files and testing utilities.",
            'tests': "This folder contains test files and testing utilities.",
            'src': "This folder contains source code files.",
            'lib': "This folder contains library code.",
            'bin': "This folder contains binary executables or executable scripts.",
            'docs': "This folder contains documentation files.",
            'examples': "This folder contains example code and demonstrations.",
            'scripts': "This folder contains utility scripts.",
            'config': "This folder contains configuration files.",
            'build': "This folder contains build artifacts and build-related files.",
            'dist': "This folder contains distribution packages.",
            'assets': "This folder contains static assets (images, fonts, etc.).",
            'data': "This folder contains data files.",
            'models': "This folder contains model definitions or data models.",
            'utils': "This folder contains utility functions and helpers.",
            'core': "This folder contains core functionality and base implementations.",
            'api': "This folder contains API definitions and handlers.",
            'handlers': "This folder contains event handlers or request handlers.",
            'adapters': "This folder contains adapter implementations for external systems.",
            'common': "This folder contains common utilities and shared code.",
        }

        for key, description in purpose_map.items():
            if key in folder_name:
                return description + "\n"

        return f"This folder (`{folder_name}`) contains organized code and resources.\n"

    def _extract_key_concepts(self, files) -> str:
        """Extract key concepts from files in this folder"""
        parts = []

        # Look at file names for patterns
        file_names = [Path(f['path']).stem for f in files if f['type'] == 'text']

        # Common patterns
        has_init = any('__init__' in name for name in file_names)
        has_main = any('main' in name.lower() for name in file_names)
        has_test = any('test' in name.lower() for name in file_names)
        has_config = any(name.lower() in {'config', 'settings', 'conf'} for name in file_names)

        if has_init:
            parts.append("- This appears to be a Python package (contains `__init__.py`)\n")
        if has_main:
            parts.append("- Contains entry point or main execution file\n")
        if has_test:
            parts.append("- Includes test files\n")
        if has_config:
            parts.append("- Contains configuration\n")

        if not parts:
            parts.append("*Key concepts can be inferred from individual file documentation.*\n")

        return ''.join(parts)

    def generate_sub_md(self) -> str:
        """Generate sub.md with merged keywords from descendant files"""
        parts = []

        folder_display = str(self.rel_folder) if str(self.rel_folder) != '.' else 'Root'
        parts.append(f"# Keyword Summary: `{folder_display}`\n\n")
        parts.append(f"**Generated:** {datetime.utcnow().isoformat()}Z\n\n")
        parts.append("---\n\n")

        # Collect keywords from all descendant _kw.md files
        keywords = self._collect_descendant_keywords()

        if not keywords:
            parts.append("*No keywords found in descendant files.*\n\n")
            return ''.join(parts)

        # Group by first letter
        keywords_by_letter = defaultdict(list)
        for kw_info in keywords:
            first_letter = kw_info['keyword'][0].upper()
            keywords_by_letter[first_letter].append(kw_info)

        parts.append("## Alphabetical Index\n\n")

        for letter in sorted(keywords_by_letter.keys()):
            parts.append(f"### {letter}\n\n")
            # Deduplicate and sort
            unique_kws = {}
            for kw_info in keywords_by_letter[letter]:
                kw = kw_info['keyword']
                if kw not in unique_kws:
                    unique_kws[kw] = []
                unique_kws[kw].append(kw_info['file'])

            for kw in sorted(unique_kws.keys())[:100]:  # Limit per letter
                files = unique_kws[kw]
                parts.append(f"#### `{kw}`\n\n")
                parts.append(f"Found in {len(files)} file(s):\n")
                for file_path in files[:5]:  # Limit to 5 files
                    # Create relative link
                    file_name = Path(file_path).name
                    parts.append(f"- [{file_path}]({file_name}_docs.md)\n")
                if len(files) > 5:
                    parts.append(f"- *... and {len(files) - 5} more*\n")
                parts.append("\n")

            if len(unique_kws) > 100:
                parts.append(f"\n*... and {len(unique_kws) - 100} more keywords starting with {letter}*\n\n")

        return ''.join(parts)

    def _collect_descendant_keywords(self):
        """Collect keywords from all descendant keyword files"""
        keywords = []

        # Get all files in this folder and subfolders
        for file_info in self.manifest['files']:
            file_path = Path(file_info['path'])

            # Check if file is in this folder or subfolder
            try:
                file_path.relative_to(self.rel_folder)
            except ValueError:
                continue

            if file_info['type'] != 'text':
                continue

            # Read corresponding keyword file if it exists
            kw_file = self.docs_root / file_path.parent / f"{file_path.name}_kw.md"
            if kw_file.exists():
                # Parse keywords from the file (simple extraction)
                try:
                    with open(kw_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # Extract keywords from markdown headers
                        import re
                        kw_pattern = re.compile(r'^####\s+`([^`]+)`', re.MULTILINE)
                        for match in kw_pattern.finditer(content):
                            keywords.append({
                                'keyword': match.group(1),
                                'file': str(file_path)
                            })
                except Exception:
                    pass

        return keywords

    def generate(self):
        """Generate all folder documentation"""
        output_dir = self.docs_root / self.rel_folder
        output_dir.mkdir(parents=True, exist_ok=True)

        # Generate index.md
        index_content = self.generate_index_md()
        index_path = output_dir / 'index.md'
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_content)

        # Generate doc.md
        doc_content = self.generate_doc_md()
        doc_path = output_dir / 'doc.md'
        with open(doc_path, 'w', encoding='utf-8') as f:
            f.write(doc_content)

        # Generate sub.md
        sub_content = self.generate_sub_md()
        sub_path = output_dir / 'sub.md'
        with open(sub_path, 'w', encoding='utf-8') as f:
            f.write(sub_content)

        return {
            'folder': str(self.rel_folder),
            'index_path': str(index_path),
            'doc_path': str(doc_path),
            'sub_path': str(sub_path),
            'index_size': len(index_content),
            'doc_size': len(doc_content),
            'sub_size': len(sub_content),
        }


def generate_all_folder_docs(repo_root: Path, docs_root: Path, manifest_path: Path):
    """Generate documentation for all folders"""
    # Load manifest
    with open(manifest_path, 'r') as f:
        manifest = json.load(f)

    # Get all folders including root
    all_folders = [repo_root] + [repo_root / f for f in manifest['folders']]

    print(f"Generating folder documentation for {len(all_folders)} folders...")

    results = []
    for folder in sorted(all_folders):
        try:
            generator = FolderDocGenerator(folder, repo_root, docs_root, manifest)
            result = generator.generate()
            results.append(result)
            print(f"  Generated docs for: {result['folder']}")
        except Exception as e:
            print(f"  ERROR generating docs for {folder}: {e}")

    print(f"\nFolder documentation complete: {len(results)} folders processed")
    return results


if __name__ == '__main__':
    import sys

    repo_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
    docs_root = repo_root / 'docs'
    manifest_path = docs_root / 'manifest.json'

    results = generate_all_folder_docs(repo_root, docs_root, manifest_path)

    print(f"\nSummary:")
    print(json.dumps({
        'folders_processed': len(results),
        'total_size': sum(r['index_size'] + r['doc_size'] + r['sub_size'] for r in results)
    }, indent=2))
