# Documentation: `.pre-commit-hooks/check_todo_exclamation.sh`
**Generated:** 2025-11-15T19:40:00.232340Z
**File Size:** 1186 bytes
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

- **Path:** `.pre-commit-hooks/check_todo_exclamation.sh`
- **Size:** 1,186 bytes
- **Lines:** 39
- **Extension:** `.sh`
- **Type:** text

---

## Source Code

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


---

## Overview

This file is located at `.pre-commit-hooks/check_todo_exclamation.sh` within the repository.


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


