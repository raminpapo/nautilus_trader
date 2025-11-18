# Documentation: check_pyo3_conventions.sh

## File Metadata

- **Path**: `.pre-commit-hooks/check_pyo3_conventions.sh`
- **Size**: 1,675 bytes
- **Lines**: 54
- **Language**: Shell

## Original Source

```bash
#!/usr/bin/env bash
# Enforces PyO3 naming conventions:
# - Functions with #[pyo3(name = "...")] must have Rust names prefixed with py_

set -euo pipefail

# Exit cleanly if ripgrep is not installed
if ! command -v rg &> /dev/null; then
  echo "WARNING: ripgrep not found, skipping PyO3 convention checks"
  exit 0
fi

# Color output
RED='\033[0;31m'
NC='\033[0m' # No Color

# Track if we found violations
VIOLATIONS=0

echo "Checking PyO3 naming conventions..."

# Use ripgrep multiline mode to find violations in one pass
# Pattern: #[pyo3(name = ...)] followed by fn that doesn't start with py_
# This is much faster than bash loop processing
while IFS=: read -r file line_num match; do
  [[ -z "$file" ]] && continue

  # Extract function name from the match
  if [[ "$match" =~ fn[[:space:]]+([a-zA-Z_][a-zA-Z0-9_]*) ]]; then
    fn_name="${BASH_REMATCH[1]}"

    # Skip if already has py_ prefix
    [[ "$fn_name" =~ ^py_ ]] && continue

    echo -e "${RED}Error:${NC} PyO3 function missing py_ prefix in $file:$line_num"
    echo "  Function: fn $fn_name()"
    echo "  Expected: fn py_$fn_name()"
    echo
    VIOLATIONS=$((VIOLATIONS + 1))
  fi
done < <(rg -U -n '#\[pyo3\(name = "[^"]+"\)\](\s*\n|\s*#[^\n]*\n)*\s*(pub\s+)?(async\s+)?fn\s+[a-zA-Z_][a-zA-Z0-9_]*' crates --type rust 2> /dev/null || true)

if [ $VIOLATIONS -gt 0 ]; then
  echo -e "${RED}Found $VIOLATIONS PyO3 naming convention violation(s)${NC}"
  echo
  echo "Convention:"
  echo "  - Rust functions exposed via PyO3 must be prefixed with py_"
  echo "  - Use #[pyo3(name = \"name\")] to expose without the py_ prefix in Python"
  exit 1
fi

echo "✓ All PyO3 naming conventions are valid"
exit 0

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 25


**Identifiers**: `All`, `BASH_REMATCH`, `Checking`, `Color`, `Convention`, `Enforces`, `Error`, `Exit`, `Expected`, `Extract`, `Found`, `Function`, `Functions`, `IFS`, `Pattern`, `PyO3`, `Python`, `RED`, `Rust`, `Skip`, `This`, `Track`, `Use`, `VIOLATIONS`, `WARNING`

## Related Files

This file is located in `.pre-commit-hooks/`. Related files may include:
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
*Generated on 2025-11-18T21:54:58.849620Z*
