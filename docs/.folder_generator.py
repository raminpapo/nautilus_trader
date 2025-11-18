#!/usr/bin/env python3
"""Generate folder-level documentation (index.md, doc.md, sub.md)."""

import os
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict
from typing import Dict, List, Set

REPO_ROOT = Path("/home/user/nautilus_trader")
DOCS_ROOT = REPO_ROOT / "docs"
MANIFEST_PATH = DOCS_ROOT / "manifest.json"

class FolderDocGenerator:
    def __init__(self):
        with open(MANIFEST_PATH, 'r') as f:
            self.manifest = json.load(f)

        self.text_files = self.manifest['text_files']
        self.folders_processed = 0

    def get_all_folders(self) -> List[Path]:
        """Get all unique folders in the repository."""
        folders = set()

        for file_info in self.text_files:
            rel_path = Path(file_info['path'])
            # Add all parent folders
            current = rel_path.parent
            while str(current) != '.':
                folders.add(current)
                current = current.parent

        # Add root
        folders.add(Path('.'))

        return sorted(list(folders))

    def get_folder_contents(self, folder: Path) -> Dict:
        """Get direct contents of a folder (files and subfolders)."""
        files = []
        subfolders = set()

        for file_info in self.text_files:
            rel_path = Path(file_info['path'])

            if rel_path.parent == folder:
                files.append(rel_path.name)

            # Check if this file is in a subfolder of current folder
            if len(rel_path.parts) > len(folder.parts) + 1:
                if rel_path.parent.parts[:len(folder.parts)] == folder.parts:
                    subfolder = Path(*rel_path.parts[:len(folder.parts) + 1])
                    subfolders.add(subfolder.name if folder != Path('.') else subfolder)

        return {
            'files': sorted(files),
            'subfolders': sorted(list(subfolders))
        }

    def generate_index_md(self, folder: Path, contents: Dict) -> str:
        """Generate index.md for a folder."""
        folder_name = str(folder) if str(folder) != '.' else 'Root'

        doc = f"""# Index: {folder_name}

## Folder Path
`{folder}/`

## Contents

"""

        # List subfolders
        if contents['subfolders']:
            doc += "### Subfolders\n\n"
            for subfolder in contents['subfolders']:
                # Link to subfolder's index
                if folder == Path('.'):
                    link_path = f"{subfolder}/index.md"
                else:
                    link_path = f"{subfolder}/index.md"
                doc += f"- [{subfolder}/]({link_path})\n"
            doc += "\n"

        # List files
        if contents['files']:
            doc += "### Files\n\n"
            for filename in contents['files']:
                # Link to file's documentation
                doc_link = f"{filename}_docs.md"
                kw_link = f"{filename}_kw.md"
                doc += f"- **{filename}**\n"
                doc += f"  - [Documentation]({doc_link})\n"
                doc += f"  - [Keywords]({kw_link})\n"
            doc += "\n"

        if not contents['files'] and not contents['subfolders']:
            doc += "*This folder appears to be empty or contains only ignored files.*\n\n"

        doc += f"\n---\n*Generated on {datetime.utcnow().isoformat()}Z*\n"
        return doc

    def generate_doc_md(self, folder: Path, contents: Dict) -> str:
        """Generate doc.md for a folder (narrative context)."""
        folder_name = str(folder) if str(folder) != '.' else 'Root'

        doc = f"""# Documentation: {folder_name}

## Folder Overview

**Path**: `{folder}/`

This folder is part of the NautilusTrader repository structure.

"""

        # Infer purpose from folder name
        purpose = self._infer_folder_purpose(folder)
        doc += f"### Purpose\n\n{purpose}\n\n"

        # Statistics
        doc += f"### Contents Summary\n\n"
        doc += f"- **Subfolders**: {len(contents['subfolders'])}\n"
        doc += f"- **Files**: {len(contents['files'])}\n\n"

        if contents['subfolders']:
            doc += "### Subfolder Organization\n\n"
            for subfolder in contents['subfolders']:
                doc += f"- **{subfolder}/**: {self._infer_folder_purpose(folder / subfolder)}\n"
            doc += "\n"

        doc += "### Navigation\n\n"
        doc += f"- [Index](index.md) - Complete listing of contents\n"
        doc += f"- [Keywords](sub.md) - Merged keyword index\n"

        if folder != Path('.'):
            doc += f"- [Parent Folder](../index.md)\n"

        doc += f"\n---\n*Generated on {datetime.utcnow().isoformat()}Z*\n"
        return doc

    def _infer_folder_purpose(self, folder: Path) -> str:
        """Infer folder purpose from name and location."""
        folder_str = str(folder).lower()
        name = folder.name.lower() if folder != Path('.') else 'root'

        # Common patterns
        if 'test' in name:
            return "Contains test files and test utilities."
        elif name in ['src', 'source']:
            return "Contains source code files."
        elif name == 'bin':
            return "Contains executable binaries and scripts."
        elif name in ['lib', 'libs', 'library']:
            return "Contains library code and modules."
        elif name in ['examples', 'example']:
            return "Contains example code and demonstrations."
        elif name in ['docs', 'doc', 'documentation']:
            return "Contains documentation files."
        elif name in ['config', 'configs', 'configuration']:
            return "Contains configuration files."
        elif name == 'assets':
            return "Contains asset files (images, resources, etc.)."
        elif name in ['util', 'utils', 'utilities']:
            return "Contains utility functions and helper code."
        elif name == 'models':
            return "Contains data models and schemas."
        elif name == 'adapters':
            return "Contains adapter implementations for external services."
        elif name == 'core':
            return "Contains core functionality and base implementations."
        elif name == 'common':
            return "Contains common code shared across modules."
        elif name == 'data':
            return "Contains data-related code or data files."
        elif name in ['api', 'apis']:
            return "Contains API definitions and implementations."
        elif name == 'client':
            return "Contains client-side code."
        elif name == 'server':
            return "Contains server-side code."
        elif 'python' in name:
            return "Contains Python bindings or Python-specific code."
        elif name == 'websocket' or name == 'ws':
            return "Contains WebSocket client and handler implementations."
        elif name == 'http':
            return "Contains HTTP client and request handling code."
        elif name == 'execution':
            return "Contains order execution and trading logic."
        elif name == 'crates':
            return "Contains Rust crate modules."
        elif folder == Path('.'):
            return "Root directory of the NautilusTrader repository."
        else:
            return f"Contains {name}-related functionality and implementations."

    def collect_folder_keywords(self, folder: Path) -> Dict[str, List[Dict]]:
        """Collect all keywords from files in this folder and subfolders."""
        keywords = defaultdict(list)

        # Get all _kw.md files in this folder and subfolders
        doc_folder = DOCS_ROOT / folder
        if not doc_folder.exists():
            return keywords

        # Recursively find all _kw.md files
        for kw_file in doc_folder.rglob("*_kw.md"):
            rel_to_folder = kw_file.relative_to(doc_folder)
            # Read keywords from file
            try:
                with open(kw_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Extract keywords (simplified - just look for ### headers)
                import re
                for match in re.finditer(r'^### (.+)$', content, re.MULTILINE):
                    keyword = match.group(1).strip()
                    if keyword not in ['File Path', 'Keyword Index']:
                        keywords[keyword].append({
                            'file': str(rel_to_folder),
                            'source': kw_file.stem.replace('_kw', '')
                        })
            except Exception as e:
                pass

        return keywords

    def generate_sub_md(self, folder: Path) -> str:
        """Generate sub.md (merged keywords from all files in folder tree)."""
        folder_name = str(folder) if str(folder) != '.' else 'Root'

        doc = f"""# Keywords Index: {folder_name}

## Folder Path
`{folder}/`

## Merged Keyword Index

This index contains all keywords from files in this folder and its subfolders, organized alphabetically.

"""

        # Collect keywords
        keywords = self.collect_folder_keywords(folder)

        if not keywords:
            doc += "*No keywords found in this folder.*\n"
        else:
            doc += f"**Total unique keywords**: {len(keywords)}\n\n"

            # Sort and display
            for keyword in sorted(keywords.keys()):
                sources = keywords[keyword]
                doc += f"### {keyword}\n\n"
                doc += f"Found in {len(sources)} file(s):\n\n"
                for source_info in sources[:10]:  # Limit to first 10
                    doc += f"- [{source_info['source']}]({source_info['file']})\n"
                if len(sources) > 10:
                    doc += f"\n*...and {len(sources) - 10} more files*\n"
                doc += "\n"

        doc += f"\n---\n*Generated on {datetime.utcnow().isoformat()}Z*\n"
        return doc

    def process_folder(self, folder: Path) -> int:
        """Process a single folder and generate all documentation."""
        # Get folder contents
        contents = self.get_folder_contents(folder)

        # Generate documentation
        index_md = self.generate_index_md(folder, contents)
        doc_md = self.generate_doc_md(folder, contents)
        sub_md = self.generate_sub_md(folder)

        # Create output directory
        doc_folder = DOCS_ROOT / folder
        doc_folder.mkdir(parents=True, exist_ok=True)

        # Write files
        with open(doc_folder / "index.md", 'w', encoding='utf-8') as f:
            f.write(index_md)

        with open(doc_folder / "doc.md", 'w', encoding='utf-8') as f:
            f.write(doc_md)

        with open(doc_folder / "sub.md", 'w', encoding='utf-8') as f:
            f.write(sub_md)

        self.folders_processed += 1
        return 3  # 3 files created

    def process_all_folders(self):
        """Process all folders in the repository."""
        folders = self.get_all_folders()
        print(f"Processing {len(folders)} folders...")

        total_docs = 0
        for i, folder in enumerate(folders):
            docs_created = self.process_folder(folder)
            total_docs += docs_created

            if (i + 1) % 50 == 0:
                print(f"Progress: {i + 1}/{len(folders)} folders processed")

        print(f"Complete! Processed {len(folders)} folders, created {total_docs} documentation files.")
        return {
            'folders_processed': len(folders),
            'docs_created': total_docs
        }

if __name__ == '__main__':
    generator = FolderDocGenerator()
    result = generator.process_all_folders()

    print("\n=== SUMMARY ===")
    print(f"Folders processed: {result['folders_processed']}")
    print(f"Docs created: {result['docs_created']}")
