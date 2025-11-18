# Documentation: bug_report.md

## File Metadata

- **Path**: `.github/ISSUE_TEMPLATE/bug_report.md`
- **Size**: 2,731 bytes
- **Lines**: 69
- **Language**: Markdown

## Original Source

```markdown
---
name: Bug Report
about: Bug – behavior that contradicts the platform's documented or intended design
labels:
  - bug
---

# Bug Report

Use this template only for issues that fit the **Bug** definition.

| Term                          | Definition |
|-------------------------------|------------|
| **Bug**                       | Behavior that contradicts the platform’s documented or intended design as per code, docs, or specs. (i.e., the implementation is incorrect.) |
| **Expectation&nbsp;mismatch** | Behavior that follows the platform’s documented or intended design but differs from what you expected. (i.e., the design/spec might be the problem.) |
| **Enhancement request**       | A request for new functionality or behavior that is not implied by existing design. (i.e., *“It would be great if the platform could…”*) |

**Note:**

- Submitting this issue automatically applies the `bug` label.
- `bug`-labeled issues are triaged with higher priority because they require corrective implementation work.
- **Expectation mismatches** and design-level concerns should be opened as [Discussions](https://github.com/nautechsystems/nautilus_trader/discussions), or RFCs instead, where they can be validated and discussed to consensus before any work is scheduled.
- The absence of a feature is typically not an expectation mismatch, and should be filed as an enhancement request.

## Confirmation

**Before opening a bug report, please confirm:**

- [ ] I’ve re-read the relevant sections of the documentation.
- [ ] I’ve searched existing issues and discussions to avoid duplicates.
- [ ] I’ve reviewed or skimmed the source code (or examples) to confirm the behavior is not by design.
- [ ] I’ve tested this issue using a recent *development* wheel (`dev` develop or `a` nightly) and can still reproduce it.

Checking a recent development wheel can save time because the issue may already have been fixed.
You can install a development wheel by running:

```bash
pip install -U nautilus_trader --pre --index-url https://packages.nautechsystems.io/simple
```

See the [development-wheels](https://github.com/nautechsystems/nautilus_trader#development-wheels) section for more details.

### Expected Behavior

Add here...

### Actual Behavior

Add here...

### Steps to Reproduce the Problem

1.
2.
3.

### Code Snippets or Logs

<!-- If applicable, provide relevant code snippets, error logs, or stack traces. Use code blocks for clarity. -->

<!-- Consider starting from our Minimal Reproducible Example template: -->
<!-- https://github.com/nautechsystems/nautilus_trader/tree/develop/examples/other/minimal_reproducible_example -->

### Specifications

- OS platform:
- Python version:
- `nautilus_trader` version:

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a Markdown documentation file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 33


**Identifiers**: `Actual`, `Add`, `Before`, `Behavior`, `Bug`, `Checking`, `Code`, `Confirmation`, `Consider`, `Definition`, `Discussions`, `Enhancement`, `Example`, `Expectation`, `Expected`, `Logs`, `Minimal`, `Note`, `Problem`, `Python`, `RFCs`, `Report`, `Reproduce`, `Reproducible`, `See`, `Snippets`, `Specifications`, `Steps`, `Submitting`, `Term` *(+3 more)*

## Related Files

This file is located in `.github/ISSUE_TEMPLATE/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

Tests for this file may be located in:
- `tests/` directory in the same folder
- Corresponding test module in the project

Run the full test suite to verify functionality.

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:58.798035Z*
