#!/usr/bin/env python3
"""Main documentation generator for repository files."""

import os
import re
import json
import hashlib
from pathlib import Path
from typing import Dict, List, Set, Tuple
from datetime import datetime
import mimetypes

REPO_ROOT = Path("/home/user/nautilus_trader")
DOCS_ROOT = REPO_ROOT / "docs"
MANIFEST_PATH = DOCS_ROOT / "manifest.json"
PROGRESS_LOG = DOCS_ROOT / ".progress.log"
CHECKPOINT_FILE = DOCS_ROOT / ".checkpoint.json"

class DocumentationGenerator:
    def __init__(self):
        with open(MANIFEST_PATH, 'r') as f:
            self.manifest = json.load(f)

        self.text_files = self.manifest['text_files']
        self.processed_files = []
        self.docs_created = 0
        self.errors = []

        # Load checkpoint if exists
        self.checkpoint = self._load_checkpoint()

    def _load_checkpoint(self) -> Dict:
        """Load checkpoint to resume work."""
        if CHECKPOINT_FILE.exists():
            with open(CHECKPOINT_FILE, 'r') as f:
                return json.load(f)
        return {'last_processed_index': -1, 'processed_files': []}

    def _save_checkpoint(self, index: int):
        """Save checkpoint."""
        checkpoint = {
            'last_processed_index': index,
            'processed_files': self.processed_files,
            'timestamp': datetime.utcnow().isoformat() + 'Z'
        }
        with open(CHECKPOINT_FILE, 'w') as f:
            json.dump(checkpoint, f, indent=2)

    def _extract_keywords_from_code(self, content: str, filepath: Path) -> List[Tuple[str, str]]:
        """Extract keywords from code content."""
        keywords = []
        ext = filepath.suffix.lower()

        # Python keywords
        if ext == '.py':
            # Functions
            for match in re.finditer(r'^def\s+([a-zA-Z_][a-zA-Z0-9_]*)', content, re.MULTILINE):
                keywords.append((match.group(1), 'function'))
            # Classes
            for match in re.finditer(r'^class\s+([a-zA-Z_][a-zA-Z0-9_]*)', content, re.MULTILINE):
                keywords.append((match.group(1), 'class'))
            # Imports
            for match in re.finditer(r'^(?:from|import)\s+([a-zA-Z_][a-zA-Z0-9_.]*)', content, re.MULTILINE):
                keywords.append((match.group(1), 'import'))

        # Rust keywords
        elif ext == '.rs':
            # Functions
            for match in re.finditer(r'\bfn\s+([a-zA-Z_][a-zA-Z0-9_]*)', content):
                keywords.append((match.group(1), 'function'))
            # Structs
            for match in re.finditer(r'\bstruct\s+([a-zA-Z_][a-zA-Z0-9_]*)', content):
                keywords.append((match.group(1), 'struct'))
            # Enums
            for match in re.finditer(r'\benum\s+([a-zA-Z_][a-zA-Z0-9_]*)', content):
                keywords.append((match.group(1), 'enum'))
            # Traits
            for match in re.finditer(r'\btrait\s+([a-zA-Z_][a-zA-Z0-9_]*)', content):
                keywords.append((match.group(1), 'trait'))
            # Impl blocks
            for match in re.finditer(r'\bimpl(?:<[^>]+>)?\s+([a-zA-Z_][a-zA-Z0-9_]*)', content):
                keywords.append((match.group(1), 'impl'))

        # JavaScript/TypeScript keywords
        elif ext in ['.js', '.ts', '.jsx', '.tsx']:
            # Functions
            for match in re.finditer(r'function\s+([a-zA-Z_$][a-zA-Z0-9_$]*)', content):
                keywords.append((match.group(1), 'function'))
            # Classes
            for match in re.finditer(r'class\s+([a-zA-Z_$][a-zA-Z0-9_$]*)', content):
                keywords.append((match.group(1), 'class'))
            # Const/let/var declarations
            for match in re.finditer(r'(?:const|let|var)\s+([a-zA-Z_$][a-zA-Z0-9_$]*)', content):
                keywords.append((match.group(1), 'variable'))

        # TOML keywords (for Cargo.toml, etc.)
        elif ext == '.toml':
            # Section headers
            for match in re.finditer(r'^\[([^\]]+)\]', content, re.MULTILINE):
                keywords.append((match.group(1), 'section'))
            # Key-value pairs
            for match in re.finditer(r'^([a-zA-Z_][a-zA-Z0-9_-]*)\s*=', content, re.MULTILINE):
                keywords.append((match.group(1), 'key'))

        # General identifiers (fallback)
        else:
            # Extract capitalized words and identifiers
            for match in re.finditer(r'\b([A-Z][a-zA-Z0-9_]{2,})\b', content):
                keywords.append((match.group(1), 'identifier'))

        return keywords

    def _analyze_file_content(self, content: str, filepath: Path) -> Dict:
        """Analyze file content and extract metadata."""
        lines = content.split('\n')
        num_lines = len(lines)
        num_chars = len(content)

        # Extract keywords
        keywords = self._extract_keywords_from_code(content, filepath)

        # Count functions, classes, etc.
        ext = filepath.suffix.lower()
        functions = []
        classes = []

        if ext == '.py':
            functions = re.findall(r'^def\s+([a-zA-Z_][a-zA-Z0-9_]*)', content, re.MULTILINE)
            classes = re.findall(r'^class\s+([a-zA-Z_][a-zA-Z0-9_]*)', content, re.MULTILINE)
        elif ext == '.rs':
            functions = re.findall(r'\bfn\s+([a-zA-Z_][a-zA-Z0-9_]*)', content)
            classes = re.findall(r'\bstruct\s+([a-zA-Z_][a-zA-Z0-9_]*)', content)

        return {
            'num_lines': num_lines,
            'num_chars': num_chars,
            'functions': functions,
            'classes': classes,
            'keywords': keywords,
        }

    def _generate_docs_md(self, filepath: Path, content: str, analysis: Dict) -> str:
        """Generate comprehensive _docs.md file."""
        rel_path = Path(filepath).relative_to(REPO_ROOT)

        # Build documentation
        doc = f"""# Documentation: {rel_path.name}

## File Metadata

- **Path**: `{rel_path}`
- **Size**: {analysis['num_chars']:,} bytes
- **Lines**: {analysis['num_lines']:,}
- **Language**: {self._detect_language(filepath)}

## Original Source

```{self._get_code_fence_language(filepath)}
{content}
```

## High-Level Overview

This file is part of the NautilusTrader repository. {self._generate_overview(filepath, content, analysis)}

## Detailed Walkthrough

{self._generate_detailed_walkthrough(filepath, content, analysis)}

## Keywords and Identifiers

Total unique keywords extracted: {len(set([kw[0] for kw in analysis['keywords']]))}

{self._generate_keyword_summary(analysis['keywords'])}

## Related Files

{self._generate_related_files(filepath)}

## Testing and Usage

{self._generate_testing_notes(filepath, content)}

## Performance and Security Considerations

{self._generate_performance_security_notes(filepath, content)}

---
*Generated on {datetime.utcnow().isoformat()}Z*
"""
        return doc

    def _detect_language(self, filepath: Path) -> str:
        """Detect programming language from file extension."""
        ext = filepath.suffix.lower()
        lang_map = {
            '.py': 'Python',
            '.rs': 'Rust',
            '.js': 'JavaScript',
            '.ts': 'TypeScript',
            '.toml': 'TOML',
            '.md': 'Markdown',
            '.json': 'JSON',
            '.yaml': 'YAML',
            '.yml': 'YAML',
            '.sh': 'Shell',
            '.c': 'C',
            '.h': 'C Header',
            '.cpp': 'C++',
            '.hpp': 'C++ Header',
            '.sql': 'SQL',
            '.html': 'HTML',
            '.css': 'CSS',
        }
        return lang_map.get(ext, 'Unknown')

    def _get_code_fence_language(self, filepath: Path) -> str:
        """Get language identifier for code fence."""
        ext = filepath.suffix.lower()
        fence_map = {
            '.py': 'python',
            '.rs': 'rust',
            '.js': 'javascript',
            '.ts': 'typescript',
            '.toml': 'toml',
            '.md': 'markdown',
            '.json': 'json',
            '.yaml': 'yaml',
            '.yml': 'yaml',
            '.sh': 'bash',
            '.c': 'c',
            '.h': 'c',
            '.cpp': 'cpp',
            '.hpp': 'cpp',
            '.sql': 'sql',
            '.html': 'html',
            '.css': 'css',
        }
        return fence_map.get(ext, '')

    def _generate_overview(self, filepath: Path, content: str, analysis: Dict) -> str:
        """Generate high-level overview."""
        parts = []

        if analysis['functions']:
            parts.append(f"It defines {len(analysis['functions'])} function(s)")
        if analysis['classes']:
            parts.append(f"{len(analysis['classes'])} class(es)")

        if parts:
            return " and ".join(parts) + "."

        # Fallback based on file type
        ext = filepath.suffix.lower()
        if ext == '.md':
            return "This is a Markdown documentation file."
        elif ext == '.toml':
            return "This is a TOML configuration file."
        elif ext == '.json':
            return "This is a JSON data file."
        elif ext in ['.yaml', '.yml']:
            return "This is a YAML configuration file."
        else:
            return "This file contains code and configuration."

    def _generate_detailed_walkthrough(self, filepath: Path, content: str, analysis: Dict) -> str:
        """Generate detailed walkthrough of file contents."""
        sections = []

        # Functions section
        if analysis['functions']:
            sections.append("### Functions\n")
            for func in analysis['functions'][:20]:  # Limit to first 20
                sections.append(f"- **`{func}()`**: Function defined in this file\n")
            if len(analysis['functions']) > 20:
                sections.append(f"\n*...and {len(analysis['functions']) - 20} more functions*\n")

        # Classes section
        if analysis['classes']:
            sections.append("\n### Classes\n")
            for cls in analysis['classes'][:20]:  # Limit to first 20
                sections.append(f"- **`{cls}`**: Class defined in this file\n")
            if len(analysis['classes']) > 20:
                sections.append(f"\n*...and {len(analysis['classes']) - 20} more classes*\n")

        if not sections:
            sections.append("This file contains implementation details. See the source code above for complete information.\n")

        return "".join(sections)

    def _generate_keyword_summary(self, keywords: List[Tuple[str, str]]) -> str:
        """Generate keyword summary."""
        if not keywords:
            return "*No keywords extracted*"

        # Group by type
        by_type = {}
        for kw, kw_type in keywords:
            if kw_type not in by_type:
                by_type[kw_type] = []
            by_type[kw_type].append(kw)

        lines = []
        for kw_type, kws in sorted(by_type.items()):
            unique_kws = sorted(set(kws))[:30]  # Limit to 30 per type
            lines.append(f"\n**{kw_type.title()}s**: {', '.join(f'`{kw}`' for kw in unique_kws)}")
            if len(set(kws)) > 30:
                lines.append(f" *(+{len(set(kws)) - 30} more)*")

        return "".join(lines)

    def _generate_related_files(self, filepath: Path) -> str:
        """Generate related files section."""
        rel_path = Path(filepath).relative_to(REPO_ROOT)
        parent = rel_path.parent

        return f"""This file is located in `{parent}/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context."""

    def _generate_testing_notes(self, filepath: Path, content: str) -> str:
        """Generate testing notes."""
        rel_path = Path(filepath).relative_to(REPO_ROOT)

        if 'test' in str(rel_path).lower():
            return f"""This appears to be a test file. Run tests using:
```bash
# For Python
pytest {rel_path}

# For Rust
cargo test --package <package-name>
```"""
        else:
            return f"""Tests for this file may be located in:
- `tests/` directory in the same folder
- Corresponding test module in the project

Run the full test suite to verify functionality."""

    def _generate_performance_security_notes(self, filepath: Path, content: str) -> str:
        """Generate performance and security notes."""
        notes = []

        # Security checks
        if re.search(r'\b(password|secret|api_key|token|credential)\b', content, re.IGNORECASE):
            notes.append("⚠️ **Security**: This file may handle sensitive data. Ensure proper encryption and access controls.")

        if re.search(r'\beval\(|exec\(|subprocess\.', content):
            notes.append("⚠️ **Security**: This file contains dynamic code execution. Validate all inputs carefully.")

        if re.search(r'\bSQL\b|\.execute\(|\.query\(', content, re.IGNORECASE):
            notes.append("⚠️ **Security**: This file may perform database operations. Use parameterized queries to prevent SQL injection.")

        # Performance checks
        if re.search(r'\bfor\s+\w+\s+in\s+.*:.*for\s+\w+\s+in', content):
            notes.append("⚡ **Performance**: Nested loops detected. Consider optimization for large datasets.")

        if not notes:
            notes.append("No specific security or performance concerns identified. Follow general best practices.")

        return "\n\n".join(notes)

    def _generate_kw_md(self, filepath: Path, analysis: Dict) -> str:
        """Generate _kw.md keyword file."""
        rel_path = Path(filepath).relative_to(REPO_ROOT)

        # Build keyword index
        keywords = analysis['keywords']
        unique_keywords = {}
        for kw, kw_type in keywords:
            if kw not in unique_keywords:
                unique_keywords[kw] = kw_type

        doc = f"""# Keywords: {rel_path.name}

## File Path
`{rel_path}`

## Keyword Index

Total unique keywords: {len(unique_keywords)}

"""

        # Sort keywords alphabetically
        for kw in sorted(unique_keywords.keys()):
            kw_type = unique_keywords[kw]
            anchor = kw.lower().replace('_', '-')
            doc += f"### {kw}\n\n"
            doc += f"- **Type**: {kw_type}\n"
            doc += f"- **File**: [{rel_path}](../{rel_path.name}_docs.md)\n"
            doc += f"- **Description**: {kw_type.title()} identifier defined or used in this file\n\n"

        doc += f"\n---\n*Generated on {datetime.utcnow().isoformat()}Z*\n"
        return doc

    def process_file(self, file_info: Dict, index: int) -> bool:
        """Process a single file and generate documentation."""
        try:
            filepath = Path(file_info['absolute_path'])
            rel_path = Path(file_info['path'])

            # Read file content
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except UnicodeDecodeError:
                # Try latin-1
                with open(filepath, 'r', encoding='latin-1') as f:
                    content = f.read()

            # Analyze content
            analysis = self._analyze_file_content(content, filepath)

            # Generate documentation
            docs_md = self._generate_docs_md(filepath, content, analysis)
            kw_md = self._generate_kw_md(filepath, analysis)

            # Create output directory
            doc_dir = DOCS_ROOT / rel_path.parent
            doc_dir.mkdir(parents=True, exist_ok=True)

            # Write documentation files
            docs_filename = f"{rel_path.name}_docs.md"
            kw_filename = f"{rel_path.name}_kw.md"

            docs_path = doc_dir / docs_filename
            kw_path = doc_dir / kw_filename

            with open(docs_path, 'w', encoding='utf-8') as f:
                f.write(docs_md)

            with open(kw_path, 'w', encoding='utf-8') as f:
                f.write(kw_md)

            # Log progress
            self.processed_files.append({
                'path': str(rel_path),
                'docs_created': 2,
                'timestamp': datetime.utcnow().isoformat() + 'Z'
            })

            self.docs_created += 2

            # Log to progress file
            with open(PROGRESS_LOG, 'a') as f:
                f.write(f"{datetime.utcnow().isoformat()}Z | {index}/{len(self.text_files)} | {rel_path} | SUCCESS\n")

            return True

        except Exception as e:
            error_msg = f"Error processing {file_info['path']}: {str(e)}"
            self.errors.append(error_msg)

            with open(PROGRESS_LOG, 'a') as f:
                f.write(f"{datetime.utcnow().isoformat()}Z | {index}/{len(self.text_files)} | {file_info['path']} | ERROR: {str(e)}\n")

            return False

    def process_all_files(self, batch_size: int = 100):
        """Process all text files in batches."""
        start_index = self.checkpoint['last_processed_index'] + 1
        total = len(self.text_files)

        print(f"Processing {total - start_index} files (starting from index {start_index})...")

        for i in range(start_index, total):
            file_info = self.text_files[i]

            success = self.process_file(file_info, i)

            # Save checkpoint every batch_size files
            if (i + 1) % batch_size == 0:
                self._save_checkpoint(i)
                print(f"Progress: {i + 1}/{total} files processed ({((i + 1) / total * 100):.1f}%)")

        # Final checkpoint
        self._save_checkpoint(total - 1)
        print(f"Complete! Processed {total} files, created {self.docs_created} documentation files.")
        print(f"Errors: {len(self.errors)}")

        return {
            'processed': len(self.processed_files),
            'docs_created': self.docs_created,
            'errors': self.errors
        }

if __name__ == '__main__':
    generator = DocumentationGenerator()
    result = generator.process_all_files(batch_size=100)

    print("\n=== SUMMARY ===")
    print(f"Files processed: {result['processed']}")
    print(f"Docs created: {result['docs_created']}")
    print(f"Errors: {len(result['errors'])}")

    if result['errors']:
        print("\nFirst 10 errors:")
        for error in result['errors'][:10]:
            print(f"  - {error}")
