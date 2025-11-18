# Documentation: check_error_conventions.sh

## File Metadata

- **Path**: `.pre-commit-hooks/check_error_conventions.sh`
- **Size**: 3,623 bytes
- **Lines**: 106
- **Language**: Shell

## Original Source

```bash
#!/usr/bin/env bash
# Enforces error variable naming conventions:
# 1. Rust: Always use Err(e) for error variables [not Err(error), Err(err), etc.]
# 2. Python: Always use 'except Exception as e:' [not as ex, as exc, etc.]

set -euo pipefail

# Exit cleanly if ripgrep is not installed
if ! command -v rg &> /dev/null; then
  echo "WARNING: ripgrep not found, skipping error convention checks"
  exit 0
fi

# Color output
RED='\033[0;31m'
NC='\033[0m' # No Color

# Track if we found violations
VIOLATIONS=0

################################################################################
# Check Rust files for Err(variable) patterns
################################################################################

# We want to catch patterns like:
# - Err(err) => ...
# - Err(error) => ...
# - if let Err(err) = ...
# But NOT:
# - Err(e) => ...
# - Err(e @ ...) => ...

echo "Checking Rust error variable naming..."

# Search directly for the lazy patterns Err(err) and Err(error)
while IFS=: read -r file line_num line_content; do
  [[ -z "$file" ]] && continue

  # Extract which lazy pattern was found
  if [[ "$line_content" =~ Err\((err|error)\) ]]; then
    var_name="${BASH_REMATCH[1]}"
    trimmed_line="${line_content#"${line_content%%[![:space:]]*}"}"

    echo -e "${RED}Error:${NC} Invalid Rust error variable name in $file:$line_num"
    echo "  Found: Err($var_name)"
    echo "  Expected: Err(e) or a descriptive name"
    echo "  Line: $trimmed_line"
    echo
    VIOLATIONS=$((VIOLATIONS + 1))
  fi
done < <(rg -n 'Err\((err|error)\)' crates --type rust 2> /dev/null || true)

################################################################################
# Check Python files for 'except ... as variable:' patterns (all exception types)
################################################################################

echo "Checking Python exception variable naming..."

# Search for except blocks with 'as xxx:' where xxx is not 'e'
# Checks single-line except blocks (except ExceptionType as xxx:)
# Also handles tuples on one line: except (Type1, Type2) as xxx:
# NOTE: Does NOT detect multiline tuple syntax (rare in practice):
#   except (
#       ValueError,
#   ) as xxx:
# Negative lookahead-style: match 'as <anything but e>:'
while IFS=: read -r file line_num line_content; do
  [[ -z "$file" ]] && continue

  # Extract variable name from 'as xxx:' pattern
  if [[ "$line_content" =~ as[[:space:]]+([a-zA-Z_][a-zA-Z0-9_]*)[[:space:]]*: ]]; then
    var_name="${BASH_REMATCH[1]}"

    # Skip if it's 'e'
    [[ "$var_name" == "e" ]] && continue

    trimmed_line="${line_content#"${line_content%%[![:space:]]*}"}"
    echo -e "${RED}Error:${NC} Invalid Python exception variable name in $file:$line_num"
    echo "  Found: as $var_name:"
    echo "  Expected: as e:"
    echo "  Line: $trimmed_line"
    echo
    VIOLATIONS=$((VIOLATIONS + 1))
  fi
done < <(rg -n '^[[:space:]]*except[*]?.*[[:space:]]as[[:space:]]+[a-zA-Z_][a-zA-Z0-9_]*[[:space:]]*:' \
  --type py \
  --type-add 'pyx:*.pyx' \
  --type pyx \
  . 2> /dev/null || true)

################################################################################
# Report results
################################################################################

if [ $VIOLATIONS -gt 0 ]; then
  echo -e "${RED}Found $VIOLATIONS error variable naming violation(s)${NC}"
  echo
  echo "Conventions:"
  echo "  - Rust: Use Err(e) or descriptive names (not Err(err) or Err(error))"
  echo "  - Python: Always use 'as e:' for all exception types (not as exc, as err, etc.)"
  exit 1
fi

echo "✓ All error variable names are valid"
exit 0

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 39


**Identifiers**: `All`, `Also`, `Always`, `BASH_REMATCH`, `But`, `Check`, `Checking`, `Checks`, `Color`, `Conventions`, `Does`, `Enforces`, `Err`, `Error`, `Exception`, `ExceptionType`, `Exit`, `Expected`, `Extract`, `Found`, `IFS`, `Invalid`, `Line`, `NOT`, `NOTE`, `Negative`, `Python`, `RED`, `Report`, `Rust` *(+9 more)*

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
*Generated on 2025-11-18T21:54:58.843729Z*
