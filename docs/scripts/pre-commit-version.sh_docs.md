# Documentation: pre-commit-version.sh

## File Metadata

- **Path**: `scripts/pre-commit-version.sh`
- **Size**: 791 bytes
- **Lines**: 25
- **Language**: Shell

## Original Source

```bash
#!/bin/bash
set -euo pipefail

# Resolve pyproject.toml relative to this script's location
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYPROJECT="${SCRIPT_DIR}/../pyproject.toml"

# Check that pyproject.toml exists
if [[ ! -f "$PYPROJECT" ]]; then
  echo "Error: pyproject.toml not found at $PYPROJECT" >&2
  exit 1
fi

# Extract pre-commit version, handling optional whitespace around >=
VERSION=$(awk -F'>=' '/pre-commit[[:space:]]*>=/ {split($2, a, ","); gsub(/[[:space:]"]/,"",a[1]); print a[1]; exit}' "$PYPROJECT")

# Validate that we got a version
if [[ -z "$VERSION" ]]; then
  echo "Error: Could not extract pre-commit version from $PYPROJECT" >&2
  exit 1
fi

# Output version (without trailing newline for consistency with other version scripts)
echo -n "$VERSION"

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 11


**Identifiers**: `BASH_SOURCE`, `Check`, `Could`, `Error`, `Extract`, `Output`, `PYPROJECT`, `Resolve`, `SCRIPT_DIR`, `VERSION`, `Validate`

## Related Files

This file is located in `scripts/`. Related files may include:
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
*Generated on 2025-11-18T21:55:06.162161Z*
