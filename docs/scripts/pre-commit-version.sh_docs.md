# Documentation: `scripts/pre-commit-version.sh`
**Generated:** 2025-11-15T19:40:05.525072Z
**File Size:** 791 bytes
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

- **Path:** `scripts/pre-commit-version.sh`
- **Size:** 791 bytes
- **Lines:** 24
- **Extension:** `.sh`
- **Type:** text

---

## Source Code

```bash
#!/bin/bash
set -euo pipefail

# Resolve pyproject.toml relative to this script's location
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYPROJECT="${SCRIPT_DIR}/../pyproject.toml"

# Check that pyproject.toml exists
if [[ ! -f "$PYPROJECT" ]]; then
  echo "Error: pyproject.toml not found at $PYPROJECT" >&2
  exit 1
fi

# Extract pre-commit version, handling optional whitespace around >=
VERSION=$(awk -F'>=' '/pre-commit[[:space:]]*>=/ {split($2, a, ","); gsub(/[[:space:]"]/,"",a[1]); print a[1]; exit}' "$PYPROJECT")

# Validate that we got a version
if [[ -z "$VERSION" ]]; then
  echo "Error: Could not extract pre-commit version from $PYPROJECT" >&2
  exit 1
fi

# Output version (without trailing newline for consistency with other version scripts)
echo -n "$VERSION"
```


---

## Overview

This file is located at `scripts/pre-commit-version.sh` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `scripts`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


