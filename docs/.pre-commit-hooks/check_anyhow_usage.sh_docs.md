# Documentation: `.pre-commit-hooks/check_anyhow_usage.sh`
**Generated:** 2025-11-15T19:40:00.225491Z
**File Size:** 2937 bytes
**Extension:** .sh
**Type:** text

---

## Table of Contents

1. [File Metadata](#file-metadata)
2. [Source Code](#source-code)
3. [Overview](#overview)
4. [Detailed Analysis](#detailed-analysis)
5. [Usage Examples](#usage-examples)
6. [Related Files](#related-files)
7. [Notes](#notes)

---

## File Metadata

- **Path:** `.pre-commit-hooks/check_anyhow_usage.sh`
- **Size:** 2,937 bytes
- **Lines:** 90
- **Extension:** `.sh`
- **Type:** text

---

## Source Code

```bash
#!/usr/bin/env bash
# Enforces anyhow usage conventions:
# 1. Only import anyhow::Context (use anyhow::bail!, anyhow::Result, etc. fully qualified)
# 2. Use anyhow::bail!(...) instead of return Err(anyhow::anyhow!(...))

set -euo pipefail

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
done < <(
  if command -v rg &> /dev/null; then
    # Use ripgrep (faster)
    rg -n "$PATTERN" crates --type rust 2> /dev/null || true
  else
    # Fall back to grep + find
    find crates -name '*.rs' -type f -exec grep -Hn "$PATTERN" {} + 2> /dev/null || true
  fi
)

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
done < <(
  if command -v rg &> /dev/null; then
    rg -n 'return\s+Err\(anyhow::anyhow!' crates --type rust 2> /dev/null || true
  else
    find crates -name '*.rs' -type f -exec grep -Hn 'return[[:space:]]\+Err(anyhow::anyhow!' {} + 2> /dev/null || true
  fi
)

if [ $USAGE_VIOLATIONS -gt 0 ]; then
  echo -e "${RED}Found $USAGE_VIOLATIONS anyhow usage violation(s)${NC}"
  exit 1
fi

echo "✓ All anyhow imports and usage are valid"
exit 0
```


---

## Overview

This file is located at `.pre-commit-hooks/check_anyhow_usage.sh` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `.pre-commit-hooks`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


