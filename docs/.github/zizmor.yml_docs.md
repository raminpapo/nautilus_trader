# Documentation: zizmor.yml

## File Metadata

- **Path**: `.github/zizmor.yml`
- **Size**: 544 bytes
- **Lines**: 14
- **Language**: YAML

## Original Source

```yaml
# Zizmor configuration for GitHub Actions security auditing
#
# The github-env rule flags all writes to $GITHUB_ENV as potentially dangerous.
# While this is a valid security concern in general, our usage is safe because:
# - All values written are from trusted sources (system commands, file reads)
# - No user-controlled or external input is written to GITHUB_ENV
# - These are standard patterns in GitHub Actions workflows
#
# We disable this rule to reduce noise from low-confidence false positives.

rules:
  github-env:
    disable: true

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a YAML configuration file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 8


**Identifiers**: `Actions`, `All`, `GITHUB_ENV`, `GitHub`, `The`, `These`, `While`, `Zizmor`

## Related Files

This file is located in `.github/`. Related files may include:
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
*Generated on 2025-11-18T21:54:58.831173Z*
