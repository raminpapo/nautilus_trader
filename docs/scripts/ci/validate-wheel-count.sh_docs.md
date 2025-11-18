# Documentation: validate-wheel-count.sh

## File Metadata

- **Path**: `scripts/ci/validate-wheel-count.sh`
- **Size**: 779 bytes
- **Lines**: 31
- **Language**: Shell

## Original Source

```bash
#!/usr/bin/env bash
set -euo pipefail

# Validate wheel count matches expected count
# Usage: validate-wheel-count.sh <expected_count>

if [ $# -ne 1 ]; then
  echo "Usage: $0 <expected_count>" >&2
  exit 1
fi

expected_count=$1

if ! [[ "$expected_count" =~ ^[0-9]+$ ]]; then
  echo "ERROR: expected_count must be a positive integer, got: $expected_count" >&2
  exit 1
fi

echo "Validating wheel count in dist/ directory..."

wheel_count=$(find dist/ -name "nautilus_trader-*.whl" -type f | wc -l)

if [ "$wheel_count" -ne "$expected_count" ]; then
  echo "ERROR: Expected $expected_count wheels, found $wheel_count" >&2
  echo "Downloaded wheels:" >&2
  find dist/ -name "nautilus_trader-*.whl" -type f -ls >&2
  exit 1
fi

echo "✓ Validated: Found all $expected_count wheels"

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 8


**Identifiers**: `Downloaded`, `ERROR`, `Expected`, `Found`, `Usage`, `Validate`, `Validated`, `Validating`

## Related Files

This file is located in `scripts/ci/`. Related files may include:
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
*Generated on 2025-11-18T21:55:06.153909Z*
