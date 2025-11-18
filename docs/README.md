# NautilusTrader Documentation

## Overview

This directory contains **automatically generated comprehensive documentation** for the entire NautilusTrader repository.

**Generated on**: 2025-11-18T21:59:23.020279Z
**Repository Commit**: 617c5780bf4908421baf8bcec35851e489b9b3c3
**Total Documentation Files**: 8,075

---

## Documentation Structure

The documentation is organized as a **mirrored tree** of the repository structure, with extensive documentation for every file and folder.

### File-Level Documentation

Every text file in the repository has two associated documentation files:

1. **`<filename>_docs.md`** - Comprehensive documentation including:
   - File metadata (path, size, language)
   - Complete source code
   - High-level overview
   - Detailed walkthrough (functions, classes, etc.)
   - Keywords and identifiers
   - Related files
   - Testing and usage notes
   - Performance and security considerations

2. **`<filename>_kw.md`** - Keyword index including:
   - Extracted keywords (functions, classes, variables, etc.)
   - Keyword types and descriptions
   - Links to detailed documentation

### Folder-Level Documentation

Every folder in the repository has three associated documentation files:

1. **`index.md`** - Table of contents:
   - Lists all files in the folder
   - Lists all subfolders
   - Links to detailed documentation

2. **`doc.md`** - Narrative documentation:
   - Folder purpose and role
   - Contents summary
   - Organization and structure
   - Navigation links

3. **`sub.md`** - Merged keyword index:
   - Keywords from all files in the folder tree
   - Alphabetically organized
   - Links to source files

### Global Indexes

- **`00_ROOT_INDEX.md`** - Root navigation index with statistics
- **`keywords.md`** - Complete A-Z keyword index for entire repository (~6.2 MB)
- **`comprehensive_book.md`** - Stitched documentation as a single book (~21 KB)
- **`verification_report.md`** - Quality checks, statistics, and validation
- **`manifest.json`** - Complete file manifest with metadata

---

## How to Use This Documentation

### Browsing by Structure

1. Start with `00_ROOT_INDEX.md` for an overview
2. Navigate to a folder using its `index.md`
3. Read the folder's `doc.md` for context
4. View individual file documentation using `*_docs.md` files

### Searching for Keywords

1. Open `keywords.md` for the global A-Z keyword index
2. Find your keyword and see all files where it appears
3. Navigate to specific file documentation
4. Use folder `sub.md` files for scoped keyword searches

### Reading Linearly

1. Open `comprehensive_book.md` for a stitched walkthrough
2. Read folder documentation in order
3. Follow references to detailed file documentation

---

## File Statistics

| Type | Count | Description |
|------|-------|-------------|
| Per-file docs | 3,168 | Comprehensive file documentation |
| Per-file keywords | 3,168 | File keyword indexes |
| Folder indexes | 556 | Folder content listings |
| Folder docs | 548 | Folder narrative documentation |
| Folder keywords | 548 | Folder keyword merges |
| Global indexes | 87 | Repository-wide indexes |
| **TOTAL** | **8,075** | **All documentation files** |

**Total Size**: 121.8 MB

---

## Resuming or Expanding Documentation

The documentation generation process is **resumable** and **idempotent**:

### Resume Interrupted Generation

```bash
python3 docs/.doc_generator.py --resume
```

### Regenerate Documentation

```bash
# Full regeneration
python3 docs/.repo_scanner.py
python3 docs/.doc_generator.py
python3 docs/.folder_generator.py
python3 docs/.global_generator.py
python3 docs/.verification_generator.py
```

### Expand Specific Sections

Edit the generator scripts to:
- Increase word count targets per file
- Add more file summaries to comprehensive_book.md
- Include additional analysis sections
- Generate custom reports

---

## Quality and Verification

See `verification_report.md` for:
- Complete file counts and statistics
- Link validation results
- Security considerations
- Known limitations
- Reproducibility information

---

## Generator Scripts

The following Python scripts were used to generate this documentation:

- `.repo_scanner.py` - Repository file scanner and classifier
- `.doc_generator.py` - Per-file documentation generator
- `.folder_generator.py` - Per-folder documentation generator
- `.global_generator.py` - Global index generator
- `.verification_generator.py` - Verification and reporting

These scripts are included in the `docs/` folder for transparency and reproducibility.

---

## Principles

This documentation was generated following these principles:

1. **Truth-first**: No invented files, code, or claims
2. **Deterministic**: Same repo → same docs
3. **Verifiable**: Manifests, checksums, and verification reports
4. **Resumable**: Checkpointed generation process
5. **Link-safe**: All internal links are relative and validated

---

## Support

For questions or issues with this documentation:
1. Check `verification_report.md` for known limitations
2. Review `manifest.json` for file metadata
3. Examine generator scripts for implementation details
4. Re-run generators to refresh documentation

---

*Generated by the World's Best Repo Book Generator v1.0.0*
*2025-11-18T21:59:23.020308Z*
