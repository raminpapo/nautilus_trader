# Documentation: check_anyhow_usage.sh

## File Metadata

- **Path**: `.pre-commit-hooks/check_anyhow_usage.sh`
- **Size**: 2,717 bytes
- **Lines**: 83
- **Language**: Shell

## Original Source

```bash
#!/usr/bin/env bash
# Enforces anyhow usage conventions:
# 1. Only import anyhow::Context (use anyhow::bail!, anyhow::Result, etc. fully qualified)
# 2. Use anyhow::bail!(...) instead of return Err(anyhow::anyhow!(...))

set -euo pipefail

# Exit cleanly if ripgrep is not installed
if ! command -v rg &> /dev/null; then
  echo "WARNING: ripgrep not found, skipping anyhow usage checks"
  exit 0
fi

# Color output
RED='\033[0;31m'
NC='\033[0m' # No Color

# Track if we found violations
VIOLATIONS=0

# Pattern to search for
PATTERN='^[[:space:]]*use anyhow::'

# Stream results to avoid holding everything in memory
while IFS=: read -r file line_num line_content; do
  # Skip empty lines from search results
  [[ -z "$file" ]] && continue

  # Skip the anyhow style guide doc if it exists (contains examples of what NOT to do)
  if [[ "$file" == *"anyhow_style_guide"* ]] || [[ "$file" == *"ANYHOW"* ]]; then
    continue
  fi

  # Trim leading/trailing whitespace and remove trailing comments
  # This normalizes "use anyhow::Context;", "  use anyhow::Context;  ", "use anyhow::Context; // comment"
  normalized=$(echo "$line_content" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*\/\/.*//' -e 's/[[:space:]]*$//')

  # Skip if this is exactly "use anyhow::Context;"
  if [[ "$normalized" == "use anyhow::Context;" ]]; then
    continue
  fi

  # We have a violation
  echo -e "${RED}Error:${NC} Invalid anyhow import in $file:$line_num"
  echo "  Found: $line_content"
  echo "  Only 'use anyhow::Context;' is allowed."
  echo "  Use fully qualified paths for other items (anyhow::bail!, anyhow::Result, etc.)"
  echo
  VIOLATIONS=$((VIOLATIONS + 1))
done < <(rg -n "$PATTERN" crates --type rust 2> /dev/null || true)

if [ $VIOLATIONS -gt 0 ]; then
  echo -e "${RED}Found $VIOLATIONS anyhow import violation(s)${NC}"
  exit 1
fi

# Check for return Err(anyhow::anyhow!(...)) anti-pattern (should use anyhow::bail! instead)
USAGE_VIOLATIONS=0

while IFS=: read -r file line_num line_content; do
  # Skip empty lines
  [[ -z "$file" ]] && continue

  # Skip style guide docs
  if [[ "$file" == *"anyhow_style_guide"* ]] || [[ "$file" == *"ANYHOW"* ]]; then
    continue
  fi

  echo -e "${RED}Error:${NC} Use anyhow::bail! instead of return Err(anyhow::anyhow!) in $file:$line_num"
  echo "  Found: $line_content"
  echo "  Replace 'return Err(anyhow::anyhow!(...))' with 'anyhow::bail!(...)'"
  echo
  USAGE_VIOLATIONS=$((USAGE_VIOLATIONS + 1))
done < <(rg -n 'return\s+Err\(anyhow::anyhow!' crates --type rust 2> /dev/null || true)

if [ $USAGE_VIOLATIONS -gt 0 ]; then
  echo -e "${RED}Found $USAGE_VIOLATIONS anyhow usage violation(s)${NC}"
  exit 1
fi

echo "✓ All anyhow imports and usage are valid"
exit 0

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 28


**Identifiers**: `ANYHOW`, `All`, `Check`, `Color`, `Context`, `Enforces`, `Err`, `Error`, `Exit`, `Found`, `IFS`, `Invalid`, `NOT`, `Only`, `PATTERN`, `Pattern`, `RED`, `Replace`, `Result`, `Skip`, `Stream`, `This`, `Track`, `Trim`, `USAGE_VIOLATIONS`, `Use`, `VIOLATIONS`, `WARNING`

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
*Generated on 2025-11-18T21:54:58.840438Z*
