# Documentation: check_testing_conventions.sh

## File Metadata

- **Path**: `.pre-commit-hooks/check_testing_conventions.sh`
- **Size**: 2,485 bytes
- **Lines**: 72
- **Language**: Shell

## Original Source

```bash
#!/usr/bin/env bash
# Enforces testing conventions:
# 1. Rust: Prefer #[rstest] over #[test] for consistency and parametrization support

set -euo pipefail

# Color output
RED='\033[0;31m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

# Track if we found violations
VIOLATIONS=0

################################################################################
# Check for ripgrep availability
################################################################################

if ! command -v rg &> /dev/null; then
  echo -e "${YELLOW}WARNING: ripgrep (rg) not found, skipping testing convention checks${NC}"
  echo "Install ripgrep to enable this check: https://github.com/BurntSushi/ripgrep"
  exit 0
fi

################################################################################
# Check Rust files for #[test] instead of #[rstest]
################################################################################

echo "Checking Rust testing conventions..."

# Create a temporary file to store the search results
rust_results=$(mktemp)
trap 'rm -f "$rust_results"' EXIT

# Search for #[test] attribute in Rust files
# We want to find standalone #[test], not #[tokio::test] or #[rstest]
# Pattern: lines with #[test] but not #[test(...)] or #[tokio::test] or followed by #[rstest]
rg -n '^\s*#\[test\]' crates tests --type rust 2> /dev/null > "$rust_results" || true

while IFS=: read -r file line_num line_content; do
  # Skip empty lines
  [[ -z "$file" ]] && continue

  # Trim leading whitespace from line for display
  trimmed_line="${line_content#"${line_content%%[![:space:]]*}"}"

  echo -e "${RED}Error:${NC} Found #[test] instead of #[rstest] in $file:$line_num"
  echo "  Found: $trimmed_line"
  echo "  Expected: #[rstest]"
  echo "  Reason: Use #[rstest] for consistency and parametrization support"
  echo
  VIOLATIONS=$((VIOLATIONS + 1))
done < "$rust_results"

################################################################################
# Report results
################################################################################

if [ $VIOLATIONS -gt 0 ]; then
  echo -e "${RED}Found $VIOLATIONS testing convention violation(s)${NC}"
  echo
  echo "Convention:"
  echo "  - Rust: Use #[rstest] instead of #[test] for consistency"
  echo "  - #[tokio::test] is acceptable for async tests without parametrization"
  echo
  echo "To fix: Replace #[test] with #[rstest] in your test functions"
  exit 1
fi

echo "✓ All testing conventions are valid"
exit 0

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 29


**Identifiers**: `All`, `BurntSushi`, `Check`, `Checking`, `Color`, `Convention`, `Create`, `EXIT`, `Enforces`, `Error`, `Expected`, `Found`, `IFS`, `Install`, `Pattern`, `Prefer`, `RED`, `Reason`, `Replace`, `Report`, `Rust`, `Search`, `Skip`, `Track`, `Trim`, `Use`, `VIOLATIONS`, `WARNING`, `YELLOW`

## Related Files

This file is located in `.pre-commit-hooks/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest .pre-commit-hooks/check_testing_conventions.sh

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:58.850969Z*
