#!/usr/bin/env python3
"""
Documentation Generator - Per-file Documentation and Keywords
Part of the World's Best Repo Book Generator
"""

import os
import re
import json
import hashlib
from pathlib import Path
from datetime import datetime
from collections import defaultdict, Counter
import keyword
import string

class FileDocGenerator:
    """Generate comprehensive documentation for a single file"""

    def __init__(self, file_info: dict, repo_root: Path, docs_root: Path):
        self.file_info = file_info
        self.repo_root = Path(repo_root)
        self.docs_root = Path(docs_root)
        self.file_path = Path(file_info['absolute_path'])
        self.rel_path = Path(file_info['path'])
        self.content = None
        self.lines = []
        self.keywords = []
        self.functions = []
        self.classes = []
        self.imports = []
        self.errors = []

    def read_file(self):
        """Read file content safely"""
        try:
            with open(self.file_path, 'r', encoding='utf-8', errors='replace') as f:
                self.content = f.read()
                self.lines = self.content.splitlines()
            return True
        except Exception as e:
            self.errors.append(f"Failed to read file: {e}")
            return False

    def analyze_python(self):
        """Analyze Python source code"""
        import_pattern = re.compile(r'^\s*(?:from\s+[\w.]+\s+)?import\s+(.+)', re.MULTILINE)
        class_pattern = re.compile(r'^\s*class\s+(\w+)(?:\(([^)]*)\))?:', re.MULTILINE)
        function_pattern = re.compile(r'^\s*def\s+(\w+)\s*\(([^)]*)\)', re.MULTILINE)

        # Extract imports
        for match in import_pattern.finditer(self.content):
            self.imports.append(match.group(0).strip())

        # Extract classes
        for match in class_pattern.finditer(self.content):
            class_name = match.group(1)
            bases = match.group(2) or ''
            self.classes.append({'name': class_name, 'bases': bases, 'line': match.start()})

        # Extract functions
        for match in function_pattern.finditer(self.content):
            func_name = match.group(1)
            params = match.group(2)
            self.functions.append({'name': func_name, 'params': params, 'line': match.start()})

    def analyze_rust(self):
        """Analyze Rust source code"""
        struct_pattern = re.compile(r'\bstruct\s+(\w+)', re.MULTILINE)
        fn_pattern = re.compile(r'\bfn\s+(\w+)\s*(?:<[^>]*>)?\s*\(([^)]*)\)', re.MULTILINE)
        impl_pattern = re.compile(r'\bimpl\s+(?:<[^>]*>)?\s*(\w+)', re.MULTILINE)

        for match in struct_pattern.finditer(self.content):
            self.classes.append({'name': match.group(1), 'type': 'struct'})

        for match in fn_pattern.finditer(self.content):
            self.functions.append({'name': match.group(1), 'params': match.group(2)})

        for match in impl_pattern.finditer(self.content):
            self.classes.append({'name': match.group(1), 'type': 'impl'})

    def analyze_c_cpp(self):
        """Analyze C/C++ source code"""
        function_pattern = re.compile(r'\b(?:static\s+)?(?:inline\s+)?(?:\w+(?:\s*\*)?)\s+(\w+)\s*\([^)]*\)\s*\{', re.MULTILINE)
        class_pattern = re.compile(r'\b(?:class|struct)\s+(\w+)', re.MULTILINE)

        for match in function_pattern.finditer(self.content):
            self.functions.append({'name': match.group(1)})

        for match in class_pattern.finditer(self.content):
            self.classes.append({'name': match.group(1)})

    def extract_keywords(self):
        """Extract keywords from the file"""
        # Tokenize identifiers
        identifier_pattern = re.compile(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b')
        tokens = identifier_pattern.findall(self.content)

        # Filter out Python keywords and common words
        stopwords = set(keyword.kwlist) | {'self', 'cls', 'def', 'class', 'import', 'from', 'return',
                                            'if', 'else', 'elif', 'for', 'while', 'try', 'except',
                                            'with', 'as', 'pass', 'break', 'continue', 'raise', 'assert',
                                            'true', 'false', 'none', 'null', 'void', 'int', 'str', 'bool'}

        # Count tokens
        token_counts = Counter(t for t in tokens if t.lower() not in stopwords and len(t) > 2)

        # Get top keywords
        self.keywords = [
            {'keyword': kw, 'count': count}
            for kw, count in token_counts.most_common(200)
        ]

        # Add function and class names as important keywords
        for func in self.functions:
            if func['name'] not in [k['keyword'] for k in self.keywords]:
                self.keywords.insert(0, {'keyword': func['name'], 'count': -1, 'type': 'function'})

        for cls in self.classes:
            if cls['name'] not in [k['keyword'] for k in self.keywords]:
                self.keywords.insert(0, {'keyword': cls['name'], 'count': -1, 'type': 'class'})

    def analyze_file(self):
        """Analyze file based on type"""
        ext = self.file_path.suffix.lower()

        if ext in {'.py', '.pyx', '.pxd', '.pxi'}:
            self.analyze_python()
        elif ext in {'.rs'}:
            self.analyze_rust()
        elif ext in {'.c', '.h', '.cpp', '.hpp', '.cc', '.cxx'}:
            self.analyze_c_cpp()

        self.extract_keywords()

    def generate_docs_md(self) -> str:
        """Generate comprehensive documentation markdown"""
        doc_parts = []

        # Header
        doc_parts.append(f"# Documentation: `{self.rel_path}`\n")
        doc_parts.append(f"**Generated:** {datetime.utcnow().isoformat()}Z\n")
        doc_parts.append(f"**File Size:** {self.file_info['size']} bytes\n")
        doc_parts.append(f"**Extension:** {self.file_info['extension']}\n")
        doc_parts.append(f"**Type:** {self.file_info['type']}\n")
        doc_parts.append("\n---\n\n")

        # Table of Contents
        doc_parts.append("## Table of Contents\n\n")
        doc_parts.append("1. [File Metadata](#file-metadata)\n")
        doc_parts.append("2. [Source Code](#source-code)\n")
        doc_parts.append("3. [Overview](#overview)\n")
        doc_parts.append("4. [Detailed Analysis](#detailed-analysis)\n")
        doc_parts.append("5. [Usage Examples](#usage-examples)\n")
        doc_parts.append("6. [Related Files](#related-files)\n")
        doc_parts.append("7. [Notes](#notes)\n")
        doc_parts.append("\n---\n\n")

        # File Metadata
        doc_parts.append("## File Metadata\n\n")
        doc_parts.append(f"- **Path:** `{self.rel_path}`\n")
        doc_parts.append(f"- **Size:** {self.file_info['size']:,} bytes\n")
        doc_parts.append(f"- **Lines:** {len(self.lines):,}\n")
        doc_parts.append(f"- **Extension:** `{self.file_info['extension']}`\n")
        doc_parts.append(f"- **Type:** {self.file_info['type']}\n")
        if self.imports:
            doc_parts.append(f"- **Imports:** {len(self.imports)}\n")
        if self.classes:
            doc_parts.append(f"- **Classes:** {len(self.classes)}\n")
        if self.functions:
            doc_parts.append(f"- **Functions:** {len(self.functions)}\n")
        doc_parts.append("\n---\n\n")

        # Source Code
        doc_parts.append("## Source Code\n\n")
        if len(self.content) > 500000:  # 500KB limit for inline display
            doc_parts.append(f"*Source code is too large ({len(self.content)} bytes) for inline display.*\n")
            doc_parts.append(f"*Please refer to the original file: `{self.rel_path}`*\n\n")
        else:
            # Determine language for syntax highlighting
            lang_map = {
                '.py': 'python', '.pyx': 'python', '.pxd': 'python', '.pxi': 'python',
                '.rs': 'rust', '.toml': 'toml',
                '.c': 'c', '.h': 'c', '.cpp': 'cpp', '.hpp': 'cpp',
                '.js': 'javascript', '.jsx': 'javascript', '.ts': 'typescript', '.tsx': 'typescript',
                '.sh': 'bash', '.bash': 'bash',
                '.yaml': 'yaml', '.yml': 'yaml', '.json': 'json', '.xml': 'xml',
                '.sql': 'sql', '.md': 'markdown', '.rst': 'rst',
            }
            lang = lang_map.get(self.file_path.suffix.lower(), '')

            doc_parts.append(f"```{lang}\n")
            doc_parts.append(self.content)
            if not self.content.endswith('\n'):
                doc_parts.append('\n')
            doc_parts.append("```\n\n")

        doc_parts.append("\n---\n\n")

        # Overview
        doc_parts.append("## Overview\n\n")
        doc_parts.append(self._generate_overview())
        doc_parts.append("\n---\n\n")

        # Detailed Analysis
        doc_parts.append("## Detailed Analysis\n\n")
        doc_parts.append(self._generate_detailed_analysis())
        doc_parts.append("\n---\n\n")

        # Usage Examples
        doc_parts.append("## Usage Examples\n\n")
        doc_parts.append(self._generate_usage_examples())
        doc_parts.append("\n---\n\n")

        # Related Files
        doc_parts.append("## Related Files\n\n")
        doc_parts.append(self._generate_related_files())
        doc_parts.append("\n---\n\n")

        # Notes
        doc_parts.append("## Notes\n\n")
        doc_parts.append(self._generate_notes())
        doc_parts.append("\n")

        return ''.join(doc_parts)

    def _generate_overview(self) -> str:
        """Generate high-level overview"""
        parts = []

        # File purpose based on name and location
        parts.append(f"This file is located at `{self.rel_path}` within the repository.\n\n")

        if self.file_path.name == '__init__.py':
            parts.append("This is a Python package initialization file that may expose package contents or execute initialization code.\n\n")
        elif self.file_path.name in {'setup.py', 'setup.cfg', 'pyproject.toml'}:
            parts.append("This is a Python package configuration file used for building and distributing the package.\n\n")
        elif self.file_path.name in {'Cargo.toml', 'Cargo.lock'}:
            parts.append("This is a Rust package configuration file managed by Cargo.\n\n")
        elif self.file_path.suffix == '.md':
            parts.append("This is a Markdown documentation file.\n\n")
        elif self.file_path.suffix in {'.yaml', '.yml', '.toml', '.json', '.ini', '.cfg'}:
            parts.append("This is a configuration file.\n\n")

        # Summary of contents
        if self.classes:
            parts.append(f"**Classes defined:** {', '.join(c['name'] for c in self.classes[:10])}")
            if len(self.classes) > 10:
                parts.append(f" and {len(self.classes) - 10} more")
            parts.append("\n\n")

        if self.functions:
            parts.append(f"**Functions defined:** {', '.join(f['name'] for f in self.functions[:10])}")
            if len(self.functions) > 10:
                parts.append(f" and {len(self.functions) - 10} more")
            parts.append("\n\n")

        if self.imports:
            parts.append(f"**Import statements:** {len(self.imports)}\n\n")

        return ''.join(parts)

    def _generate_detailed_analysis(self) -> str:
        """Generate detailed analysis of code structure"""
        parts = []

        # Classes
        if self.classes:
            parts.append("### Classes\n\n")
            for cls in self.classes:
                parts.append(f"#### `{cls['name']}`\n\n")
                if 'bases' in cls and cls['bases']:
                    parts.append(f"**Inherits from:** {cls['bases']}\n\n")
                if 'type' in cls:
                    parts.append(f"**Type:** {cls['type']}\n\n")
                parts.append("\n")

        # Functions
        if self.functions:
            parts.append("### Functions\n\n")
            for func in self.functions[:50]:  # Limit to first 50
                parts.append(f"#### `{func['name']}({func.get('params', '')})`\n\n")
                parts.append("\n")
            if len(self.functions) > 50:
                parts.append(f"*... and {len(self.functions) - 50} more functions*\n\n")

        # Imports
        if self.imports:
            parts.append("### Imports\n\n")
            for imp in self.imports[:30]:  # Limit to first 30
                parts.append(f"- `{imp}`\n")
            if len(self.imports) > 30:
                parts.append(f"\n*... and {len(self.imports) - 30} more imports*\n")
            parts.append("\n")

        if not parts:
            parts.append("*No structured code elements detected in this file.*\n\n")

        return ''.join(parts)

    def _generate_usage_examples(self) -> str:
        """Generate usage examples"""
        parts = []

        if self.file_path.suffix == '.py':
            parts.append("### Importing\n\n")
            parts.append("```python\n")
            # Generate example import
            module_path = str(self.rel_path.with_suffix('')).replace(os.sep, '.')
            if self.classes:
                parts.append(f"from {module_path} import {self.classes[0]['name']}\n")
            elif self.functions:
                parts.append(f"from {module_path} import {self.functions[0]['name']}\n")
            else:
                parts.append(f"import {module_path}\n")
            parts.append("```\n\n")
        else:
            parts.append("*Usage examples are specific to the file type and context.*\n\n")

        return ''.join(parts)

    def _generate_related_files(self) -> str:
        """Generate related files section"""
        parts = []

        # Look for related files based on imports or structure
        if self.imports:
            parts.append("This file imports from the following modules:\n\n")
            for imp in self.imports[:10]:
                parts.append(f"- `{imp}`\n")
            if len(self.imports) > 10:
                parts.append(f"\n*... and {len(self.imports) - 10} more*\n")
            parts.append("\n")

        # Related files in same directory
        parent_dir = self.rel_path.parent
        parts.append(f"**Directory:** `{parent_dir}`\n\n")
        parts.append(f"See [folder index](./index.md) for related files.\n\n")

        return ''.join(parts)

    def _generate_notes(self) -> str:
        """Generate notes section"""
        parts = []

        # Performance notes
        if self.file_info['size'] > 1024 * 1024:  # > 1MB
            parts.append(f"**Performance:** This is a large file ({self.file_info['size'] / 1024 / 1024:.2f} MB). Consider optimization or splitting if appropriate.\n\n")

        # Security notes
        sensitive_patterns = [
            'password', 'secret', 'token', 'api_key', 'private_key',
            'credential', 'auth', 'session'
        ]
        content_lower = self.content.lower()
        found_sensitive = [p for p in sensitive_patterns if p in content_lower]
        if found_sensitive:
            parts.append(f"**Security:** This file may contain sensitive patterns: {', '.join(found_sensitive)}. Ensure proper handling of secrets.\n\n")

        # Testing notes
        if 'test' in str(self.rel_path).lower():
            parts.append("**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.\n\n")

        if not parts:
            parts.append("*No special notes for this file.*\n\n")

        return ''.join(parts)

    def generate_keywords_md(self) -> str:
        """Generate keywords markdown"""
        parts = []

        parts.append(f"# Keywords: `{self.rel_path}`\n\n")
        parts.append(f"**Generated:** {datetime.utcnow().isoformat()}Z\n\n")
        parts.append("---\n\n")

        # Alphabetical keyword index
        parts.append("## Keyword Index\n\n")

        # Group by first letter
        keywords_by_letter = defaultdict(list)
        for kw in self.keywords:
            first_letter = kw['keyword'][0].upper()
            keywords_by_letter[first_letter].append(kw)

        for letter in sorted(keywords_by_letter.keys()):
            parts.append(f"### {letter}\n\n")
            for kw in sorted(keywords_by_letter[letter], key=lambda x: x['keyword']):
                kw_name = kw['keyword']
                kw_type = kw.get('type', 'identifier')
                count = kw.get('count', 0)

                parts.append(f"#### `{kw_name}`\n\n")
                parts.append(f"- **Type:** {kw_type}\n")
                if count >= 0:
                    parts.append(f"- **Occurrences:** {count}\n")
                parts.append(f"- **Source:** [{self.rel_path}](./{self.rel_path.name}_docs.md)\n")
                parts.append("\n")

        return ''.join(parts)

    def generate(self):
        """Main generation method"""
        if not self.read_file():
            return False

        self.analyze_file()

        # Determine output paths
        doc_file_name = f"{self.rel_path.name}_docs.md"
        kw_file_name = f"{self.rel_path.name}_kw.md"

        output_dir = self.docs_root / self.rel_path.parent
        output_dir.mkdir(parents=True, exist_ok=True)

        # Generate and save docs
        docs_content = self.generate_docs_md()
        docs_path = output_dir / doc_file_name
        with open(docs_path, 'w', encoding='utf-8') as f:
            f.write(docs_content)

        # Generate and save keywords
        kw_content = self.generate_keywords_md()
        kw_path = output_dir / kw_file_name
        with open(kw_path, 'w', encoding='utf-8') as f:
            f.write(kw_content)

        return {
            'file': str(self.rel_path),
            'docs_path': str(docs_path),
            'kw_path': str(kw_path),
            'docs_size': len(docs_content),
            'kw_size': len(kw_content),
            'keywords_count': len(self.keywords),
            'classes_count': len(self.classes),
            'functions_count': len(self.functions),
        }


def process_files_batch(manifest_path: Path, repo_root: Path, docs_root: Path,
                         batch_size: int = 100, max_files: int = None):
    """Process files in batches"""
    # Load manifest
    with open(manifest_path, 'r') as f:
        manifest = json.load(f)

    # Filter text files
    text_files = [f for f in manifest['files'] if f['type'] == 'text']

    if max_files:
        text_files = text_files[:max_files]

    print(f"Processing {len(text_files)} text files...")

    # Progress tracking
    progress_file = docs_root / '.progress' / 'file_processing.jsonl'
    progress_file.parent.mkdir(parents=True, exist_ok=True)

    processed_count = 0
    error_count = 0
    total_docs_size = 0

    with open(progress_file, 'w') as progress_f:
        for i, file_info in enumerate(text_files):
            try:
                generator = FileDocGenerator(file_info, repo_root, docs_root)
                result = generator.generate()

                if result:
                    processed_count += 1
                    total_docs_size += result['docs_size'] + result['kw_size']

                    # Log progress
                    progress_f.write(json.dumps(result) + '\n')
                    progress_f.flush()

                    if (i + 1) % batch_size == 0:
                        print(f"  Processed {i + 1}/{len(text_files)} files...")
                else:
                    error_count += 1

            except Exception as e:
                error_count += 1
                error_log = {
                    'file': file_info['path'],
                    'error': str(e)
                }
                progress_f.write(json.dumps(error_log) + '\n')
                progress_f.flush()
                print(f"  ERROR processing {file_info['path']}: {e}")

    print(f"\nProcessing complete:")
    print(f"  Processed: {processed_count}")
    print(f"  Errors: {error_count}")
    print(f"  Total docs size: {total_docs_size / 1024 / 1024:.2f} MB")

    return {
        'processed': processed_count,
        'errors': error_count,
        'total_docs_size': total_docs_size
    }


if __name__ == '__main__':
    import sys

    repo_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
    manifest_path = repo_root / 'docs' / 'manifest.json'
    docs_root = repo_root / 'docs'

    max_files = int(sys.argv[2]) if len(sys.argv) > 2 else None

    result = process_files_batch(manifest_path, repo_root, docs_root, max_files=max_files)

    print(f"\nFinal Summary:")
    print(json.dumps(result, indent=2))
