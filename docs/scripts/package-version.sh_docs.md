# Documentation: `scripts/package-version.sh`
**Generated:** 2025-11-15T19:40:05.524008Z
**File Size:** 1574 bytes
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

- **Path:** `scripts/package-version.sh`
- **Size:** 1,574 bytes
- **Lines:** 54
- **Extension:** `.sh`
- **Type:** text

---

## Source Code

```bash
#!/usr/bin/env bash
set -euo pipefail

# Resolve pyproject.toml relative to this script's location
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYPROJECT_FILE="${SCRIPT_DIR}/../pyproject.toml"

# Check that pyproject.toml exists
if [[ ! -f "$PYPROJECT_FILE" ]]; then
  echo "Error: pyproject.toml not found at $PYPROJECT_FILE" >&2
  exit 1
fi

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

# Try to parse using Python's `tomllib` (Python 3.11+) if available
PYTHON_CMD=$(detect_python 2> /dev/null) || PYTHON_CMD=""

if [[ -n "$PYTHON_CMD" ]] && $PYTHON_CMD -c "import tomllib" &> /dev/null; then
  VERSION=$($PYTHON_CMD -c "
import tomllib
with open('$PYPROJECT_FILE', 'rb') as f:
    data = tomllib.load(f)
print(data['project']['version'])
" | tr -d '\n\r ')
else
  # Fallback: grep & sed one-liner (works without Python)
  VERSION=$(grep -E '^version\s*=' "$PYPROJECT_FILE" |
    sed -E 's/^version\s*=\s*\"([^\"]*)\".*/\1/' |
    tr -d '\n\r ')
fi

# Validate that we got a version
if [[ -z "$VERSION" ]]; then
  echo "Error: Could not extract version from $PYPROJECT_FILE" >&2
  exit 1
fi

# Output version (without trailing newline for consistency)
echo -n "$VERSION"
```


---

## Overview

This file is located at `scripts/package-version.sh` within the repository.


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


