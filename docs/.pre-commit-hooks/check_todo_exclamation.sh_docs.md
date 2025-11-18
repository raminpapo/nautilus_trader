# Documentation: check_todo_exclamation.sh

## File Metadata

- **Path**: `.pre-commit-hooks/check_todo_exclamation.sh`
- **Size**: 1,186 bytes
- **Lines**: 40
- **Language**: Shell

## Original Source

```bash
#!/usr/bin/env bash

# Check for TODO! patterns that shouldn't be committed
#
# This hook fails if any file contains "TODO!" which is used to mark
# temporary changes that should not be committed to the repository.
set -e

# Search for TODO! in source files, excluding documentation, virtual envs, and build artifacts
matches=$(grep -R --binary-files=without-match -n "TODO!" \
  --exclude-dir=.git \
  --exclude-dir=target \
  --exclude-dir=build \
  --exclude-dir=.pytest_cache \
  --exclude-dir=__pycache__ \
  --exclude-dir=.venv \
  --exclude-dir=venv \
  --exclude-dir=node_modules \
  --exclude="*.md" \
  --exclude=".pre-commit-config.yaml" \
  --exclude-dir=.pre-commit-hooks \
  . || true)

if [[ -n "$matches" ]]; then
  # Count the number of matches to use proper grammar
  count=$(echo "$matches" | wc -l)
  if [[ $count -eq 1 ]]; then
    echo "TODO! marker detected (should not be committed):"
    echo "$matches"
    echo ""
    echo "Please resolve this TODO! marker before committing."
  else
    echo "TODO! markers detected (should not be committed):"
    echo "$matches"
    echo ""
    echo "Please resolve these TODO! markers before committing."
  fi
  exit 1
fi

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 6


**Identifiers**: `Check`, `Count`, `Please`, `Search`, `TODO`, `This`

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
*Generated on 2025-11-18T21:54:58.852170Z*
