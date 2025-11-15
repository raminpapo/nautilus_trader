# Documentation: `scripts/python-version.sh`
**Generated:** 2025-11-15T19:40:05.526248Z
**File Size:** 938 bytes
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

- **Path:** `scripts/python-version.sh`
- **Size:** 938 bytes
- **Lines:** 36
- **Extension:** `.sh`
- **Type:** text

---

## Source Code

```bash
#!/bin/bash
set -euo pipefail

# Detect available Python interpreter (honor PYTHON env var, then probe common names)
detect_python() {
  if [[ -n "${PYTHON:-}" ]] && command -v "$PYTHON" &> /dev/null; then
    echo "$PYTHON"
  elif command -v python3 &> /dev/null; then
    echo "python3"
  elif command -v python &> /dev/null; then
    echo "python"
  elif command -v py &> /dev/null; then
    # Windows py launcher
    echo "py -3"
  else
    return 1
  fi
}

# Find Python interpreter
PYTHON_CMD=$(detect_python) || {
  echo "Error: No Python interpreter found (tried: \$PYTHON, python3, python, py)" >&2
  exit 1
}

# Get Python version
VERSION=$($PYTHON_CMD --version 2>&1 | cut -d' ' -f2 | tr -d '\n\r ')

# Validate that we got a version
if [[ -z "$VERSION" ]]; then
  echo "Error: Could not extract Python version from '$PYTHON_CMD'" >&2
  exit 1
fi

# Output version (without trailing newline for consistency)
echo -n "$VERSION"
```


---

## Overview

This file is located at `scripts/python-version.sh` within the repository.


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


