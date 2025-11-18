# Documentation: rust-toolchain.sh

## File Metadata

- **Path**: `scripts/rust-toolchain.sh`
- **Size**: 737 bytes
- **Lines**: 25
- **Language**: Shell

## Original Source

```bash
#!/bin/bash
set -euo pipefail

# Resolve rust-toolchain.toml relative to this script's location
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TOOLCHAIN_FILE="${SCRIPT_DIR}/../rust-toolchain.toml"

# Check that rust-toolchain.toml exists
if [[ ! -f "$TOOLCHAIN_FILE" ]]; then
  echo "Error: rust-toolchain.toml not found at $TOOLCHAIN_FILE" >&2
  exit 1
fi

# Extract toolchain version
VERSION=$(awk -F'"' '/version[[:space:]]*=/{gsub(/[[:space:]]/,"",$2); print $2; exit}' "$TOOLCHAIN_FILE")

# Validate that we got a version
if [[ -z "$VERSION" ]]; then
  echo "Error: Could not extract toolchain version from $TOOLCHAIN_FILE" >&2
  exit 1
fi

# Output version (without trailing newline for consistency)
echo -n "$VERSION"

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 11


**Identifiers**: `BASH_SOURCE`, `Check`, `Could`, `Error`, `Extract`, `Output`, `Resolve`, `SCRIPT_DIR`, `TOOLCHAIN_FILE`, `VERSION`, `Validate`

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
*Generated on 2025-11-18T21:55:06.165985Z*
