# Documentation: check_logging_macro_usage.sh

## File Metadata

- **Path**: `.pre-commit-hooks/check_logging_macro_usage.sh`
- **Size**: 3,149 bytes
- **Lines**: 90
- **Language**: Shell

## Original Source

```bash
#!/usr/bin/env bash
# Enforces logging macro usage conventions:
# - Logging macros (trace, debug, info, warn, error) must be fully qualified
# - Use log::debug!(...) or tracing::info!(...) instead of importing the macros
# - Other imports from log/tracing crates are allowed (Level, LevelFilter, etc.)
#
# Handles both single-line and multi-line use statements (e.g., rustfmt-wrapped imports)
# Handles all visibility modifiers: pub, pub(crate), pub(super), pub(self), pub(in path)

set -euo pipefail

# Exit cleanly if ripgrep is not installed
if ! command -v rg &> /dev/null; then
  echo "WARNING: ripgrep not found, skipping logging macro usage checks"
  exit 0
fi

# Color output
RED='\033[0;31m'
NC='\033[0m' # No Color

# Track if we found violations
VIOLATIONS=0

# Pattern to find files with potential violations
# Uses word boundaries to match forbidden macros in use statements
FILE_PATTERN='^\s*(pub(\([^)]*\))?\s+)?use\s+(log|tracing)::[^;]*\b(trace|debug|info|warn|error)\b'

# Find files containing potential violations
candidate_files=$(rg -l "$FILE_PATTERN" crates --type rust 2> /dev/null || true)

# Process each candidate file to check for actual violations
while IFS= read -r file; do
  [[ -z "$file" ]] && continue

  # Skip style guide docs
  if [[ "$file" == *"logging_style_guide"* ]] || [[ "$file" == *"LOGGING"* ]]; then
    continue
  fi

  # Read file and accumulate multi-line use statements
  line_num=0
  in_use_statement=false
  use_statement=""
  use_start_line=0

  while IFS= read -r line; do
    line_num=$((line_num + 1))

    # Detect start of use log:: or use tracing:: statement
    if echo "$line" | grep -qE '^\s*(pub(\([^)]*\))?\s+)?use\s+(log|tracing)::'; then
      in_use_statement=true
      use_statement="$line"
      use_start_line=$line_num
    elif [ "$in_use_statement" = true ]; then
      # Continue accumulating multiline statement
      use_statement="$use_statement $line"
    fi

    # Check if statement is complete (ends with semicolon)
    if [ "$in_use_statement" = true ] && echo "$use_statement" | grep -qE ';\s*$'; then
      # Normalize: remove comments and extra whitespace
      normalized=$(echo "$use_statement" | sed -e 's|//.*||g' -e 's/[[:space:]]\+/ /g' -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')

      # Check if normalized statement contains a forbidden macro as a word
      if echo "$normalized" | grep -qE '\b(trace|debug|info|warn|error)\b'; then
        echo -e "${RED}Error:${NC} Invalid logging macro import in $file:$use_start_line"
        echo "  Found: $normalized"
        echo "  Logging macros (trace, debug, info, warn, error) must be fully qualified."
        echo "  Use log::debug!(...) or tracing::info!(...) instead of importing the macros."
        echo
        VIOLATIONS=$((VIOLATIONS + 1))
      fi

      # Reset for next use statement
      in_use_statement=false
      use_statement=""
      use_start_line=0
    fi
  done < "$file"
done <<< "$candidate_files"

if [ $VIOLATIONS -gt 0 ]; then
  echo -e "${RED}Found $VIOLATIONS logging macro import violation(s)${NC}"
  exit 1
fi

echo "✓ All logging macro usage is fully qualified"
exit 0

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 31


**Identifiers**: `All`, `Check`, `Color`, `Continue`, `Detect`, `Enforces`, `Error`, `Exit`, `FILE_PATTERN`, `Find`, `Found`, `Handles`, `IFS`, `Invalid`, `LOGGING`, `Level`, `LevelFilter`, `Logging`, `Normalize`, `Other`, `Pattern`, `Process`, `RED`, `Read`, `Reset`, `Skip`, `Track`, `Use`, `Uses`, `VIOLATIONS` *(+1 more)*

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
*Generated on 2025-11-18T21:54:58.846899Z*
