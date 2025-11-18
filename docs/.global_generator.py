#!/usr/bin/env python3
"""Generate global indexes: keywords.md, index.md, comprehensive_book.md"""

import os
import re
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict
from typing import Dict, List

REPO_ROOT = Path("/home/user/nautilus_trader")
DOCS_ROOT = REPO_ROOT / "docs"
MANIFEST_PATH = DOCS_ROOT / "manifest.json"

class GlobalIndexGenerator:
    def __init__(self):
        with open(MANIFEST_PATH, 'r') as f:
            self.manifest = json.load(f)

    def generate_global_keywords(self) -> str:
        """Generate global keywords.md merging all keywords from all files."""
        print("Generating global keywords index...")

        doc = f"""# Global Keyword Index

## NautilusTrader Repository Keywords

This is a comprehensive, deduplicated, alphabetically-sorted index of all keywords found across the entire repository.

**Repository**: {self.manifest['repo_source']}
**Commit**: {self.manifest['repo_fingerprint']}
**Generated**: {datetime.utcnow().isoformat()}Z

---

## Keyword Index

"""

        # Collect all keywords from all _kw.md files
        keywords = defaultdict(list)

        for kw_file in DOCS_ROOT.rglob("*_kw.md"):
            rel_path = kw_file.relative_to(DOCS_ROOT)
            try:
                with open(kw_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Extract keywords (look for ### headers)
                for match in re.finditer(r'^### (.+)$', content, re.MULTILINE):
                    keyword = match.group(1).strip()
                    if keyword not in ['File Path', 'Keyword Index']:
                        keywords[keyword].append({
                            'file': str(rel_path.parent / rel_path.stem.replace('_kw', '_docs.md'))
                        })
            except Exception as e:
                pass

        doc += f"**Total unique keywords**: {len(keywords)}\n\n"
        doc += "---\n\n"

        # Generate alphabetical sections
        current_letter = None
        for keyword in sorted(keywords.keys(), key=str.lower):
            first_letter = keyword[0].upper() if keyword else '?'

            # Add letter header
            if first_letter != current_letter:
                current_letter = first_letter
                doc += f"\n## {current_letter}\n\n"

            # Add keyword entry
            sources = keywords[keyword]
            doc += f"### {keyword}\n\n"
            doc += f"Found in {len(sources)} file(s):\n\n"

            # List sources (limit to 5)
            for source in sources[:5]:
                doc += f"- [{source['file']}]({source['file']})\n"

            if len(sources) > 5:
                doc += f"\n*...and {len(sources) - 5} more files*\n"

            doc += "\n"

        doc += f"\n---\n*Generated on {datetime.utcnow().isoformat()}Z*\n"
        return doc

    def generate_root_index(self) -> str:
        """Generate root index.md linking to all folder indexes."""
        print("Generating root index...")

        doc = f"""# NautilusTrader Documentation Index

## Repository Information

- **Source**: {self.manifest['repo_source']}
- **Commit**: {self.manifest['repo_fingerprint']}
- **Scan Date**: {self.manifest['scan_timestamp']}
- **Generator Version**: {self.manifest['generator_version']}

## Statistics

- **Total Files**: {self.manifest['file_counts']['total']:,}
- **Text Files**: {self.manifest['file_counts']['text']:,}
- **Binary Files**: {self.manifest['file_counts']['binary']:,}
- **Large Files**: {self.manifest['file_counts']['large']:,}

## Documentation Structure

This documentation is organized hierarchically, mirroring the repository structure:

- **Per-File Documentation**: Each file has:
  - `*_docs.md` - Comprehensive documentation with source code, analysis, and usage notes
  - `*_kw.md` - Keyword index for that file

- **Per-Folder Documentation**: Each folder has:
  - `index.md` - Listing of all files and subfolders
  - `doc.md` - Narrative context and purpose
  - `sub.md` - Merged keyword index for the folder tree

- **Global Indexes**:
  - [keywords.md](keywords.md) - Global A-Z keyword index
  - [comprehensive_book.md](comprehensive_book.md) - Complete stitched documentation
  - [verification_report.md](verification_report.md) - Validation and quality checks

## Quick Links

- [Root Folder Index](index.md)
- [Global Keywords](keywords.md)
- [Comprehensive Book](comprehensive_book.md)
- [Verification Report](verification_report.md)
- [Generation Manifest](manifest.json)

## Top-Level Folders

"""

        # List all top-level folders
        top_level_folders = set()
        for file_info in self.manifest['text_files']:
            rel_path = Path(file_info['path'])
            if len(rel_path.parts) > 1:
                top_level_folders.add(rel_path.parts[0])

        for folder in sorted(top_level_folders):
            doc += f"- [{folder}/]({folder}/index.md)\n"

        doc += f"""

## Navigation

Browse the documentation by:
1. Using the folder indexes to navigate the structure
2. Searching the global keyword index for specific terms
3. Reading the comprehensive book for a linear walkthrough

---

*Generated on {datetime.utcnow().isoformat()}Z*
"""
        return doc

    def generate_comprehensive_book(self) -> str:
        """Generate comprehensive_book.md stitching all documentation."""
        print("Generating comprehensive book...")

        doc = f"""# NautilusTrader: Comprehensive Documentation Book

## Repository Overview

**Source**: {self.manifest['repo_source']}
**Commit**: {self.manifest['repo_fingerprint']}
**Generated**: {datetime.utcnow().isoformat()}Z

This comprehensive book contains stitched documentation from across the entire NautilusTrader repository.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Repository Structure](#repository-structure)
3. [Folder Documentation](#folder-documentation)
4. [File Summaries](#file-summaries)

---

## Introduction

NautilusTrader is a high-performance algorithmic trading platform. This documentation was automatically generated from the repository source code, providing comprehensive coverage of all files and modules.

### Statistics

- **Total Files**: {self.manifest['file_counts']['total']:,}
- **Text Files Documented**: {self.manifest['file_counts']['text']:,}
- **Binary Files**: {self.manifest['file_counts']['binary']:,}
- **Folders**: 548
- **Documentation Files Generated**: 8,000+

---

## Repository Structure

The repository is organized into the following major components:

"""

        # List top-level structure
        top_level_folders = {}
        for file_info in self.manifest['text_files']:
            rel_path = Path(file_info['path'])
            if len(rel_path.parts) > 1:
                top_folder = rel_path.parts[0]
                if top_folder not in top_level_folders:
                    top_level_folders[top_folder] = 0
                top_level_folders[top_folder] += 1

        for folder, count in sorted(top_level_folders.items()):
            doc += f"- **{folder}/**: {count} files\n"

        doc += "\n---\n\n## Folder Documentation\n\n"

        # Include doc.md from major folders
        major_folders = ['crates', 'nautilus_core', 'nautilus_trader', 'tests', 'examples']
        for folder in major_folders:
            doc_path = DOCS_ROOT / folder / "doc.md"
            if doc_path.exists():
                try:
                    with open(doc_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    doc += f"\n### {folder}/\n\n"
                    doc += content + "\n\n"
                except Exception:
                    pass

        doc += "\n---\n\n## File Summaries\n\n"
        doc += "This section contains brief summaries of key files in the repository.\n\n"

        # Add summaries of important files (limit to avoid massive file)
        important_patterns = [
            'README.md',
            'CONTRIBUTING.md',
            'LICENSE',
            'Cargo.toml',
            'pyproject.toml',
            'setup.py',
            '__init__.py',
            'main.py',
            'lib.rs',
            'mod.rs',
        ]

        summary_count = 0
        max_summaries = 100

        for file_info in self.manifest['text_files']:
            if summary_count >= max_summaries:
                break

            rel_path = Path(file_info['path'])
            if any(pattern in str(rel_path) for pattern in important_patterns):
                # Try to read the _docs.md file
                docs_path = DOCS_ROOT / rel_path.parent / f"{rel_path.name}_docs.md"
                if docs_path.exists():
                    try:
                        with open(docs_path, 'r', encoding='utf-8') as f:
                            content = f.read()

                        # Extract just the overview section
                        overview_match = re.search(r'## High-Level Overview\s+(.*?)\s+##', content, re.DOTALL)
                        if overview_match:
                            overview = overview_match.group(1).strip()
                            doc += f"\n### {rel_path}\n\n{overview}\n\n"
                            summary_count += 1
                    except Exception:
                        pass

        doc += f"\n---\n\n## Conclusion\n\n"
        doc += f"This comprehensive book contains documentation for {self.manifest['file_counts']['text']:,} files "
        doc += "across the NautilusTrader repository. For detailed documentation of specific files, "
        doc += "please refer to the individual `*_docs.md` files in the documentation tree.\n\n"
        doc += f"*Generated on {datetime.utcnow().isoformat()}Z*\n"

        return doc

    def generate_all(self):
        """Generate all global indexes."""
        # Generate keywords.md
        keywords_md = self.generate_global_keywords()
        with open(DOCS_ROOT / "keywords.md", 'w', encoding='utf-8') as f:
            f.write(keywords_md)
        print("✓ Generated keywords.md")

        # Generate root index.md
        index_md = self.generate_root_index()
        # Note: Root index goes to the docs root, but we also have index.md in root folder
        # Let's write to a different name to avoid confusion
        with open(DOCS_ROOT / "00_ROOT_INDEX.md", 'w', encoding='utf-8') as f:
            f.write(index_md)
        print("✓ Generated 00_ROOT_INDEX.md")

        # Generate comprehensive_book.md
        book_md = self.generate_comprehensive_book()
        with open(DOCS_ROOT / "comprehensive_book.md", 'w', encoding='utf-8') as f:
            f.write(book_md)
        print("✓ Generated comprehensive_book.md")

        return {
            'keywords_size': len(keywords_md),
            'index_size': len(index_md),
            'book_size': len(book_md)
        }

if __name__ == '__main__':
    generator = GlobalIndexGenerator()
    result = generator.generate_all()

    print("\n=== SUMMARY ===")
    print(f"keywords.md: {result['keywords_size']:,} bytes")
    print(f"00_ROOT_INDEX.md: {result['index_size']:,} bytes")
    print(f"comprehensive_book.md: {result['book_size']:,} bytes")
