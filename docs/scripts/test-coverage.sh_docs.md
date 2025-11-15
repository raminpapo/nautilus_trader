# Documentation: `scripts/test-coverage.sh`
**Generated:** 2025-11-15T19:40:05.530091Z
**File Size:** 1007 bytes
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

- **Path:** `scripts/test-coverage.sh`
- **Size:** 1,007 bytes
- **Lines:** 35
- **Extension:** `.sh`
- **Type:** text

---

## Source Code

```bash
#!/bin/bash
set -eo pipefail

# Function to update Cython version in pyproject.toml
update_cython_version() {
  local old_version="3.1.3"
  local new_version="3.0.11"

  # Create backup of original file
  cp pyproject.toml pyproject.toml.bak

  # Update all occurrences of the pinned Cython version (case-insensitive on "cython")
  # Example matches: "cython==3.1.3" or "Cython==3.1.3"
  if sed -i.tmp \
    -e "s/[cC]ython==${old_version}/cython==${new_version}/g" \
    pyproject.toml; then
    echo "Updated Cython version to ${new_version}"
    rm -f pyproject.toml.tmp
  else
    echo "Error: Failed to update Cython version in pyproject.toml" >&2
    mv pyproject.toml.bak pyproject.toml
    exit 1
  fi
}

# TODO: Temporarily change Cython version in pyproject.toml while we require v3.0.11 for coverage
update_cython_version
uv lock --no-upgrade

export PROFILE_MODE=true
uv sync --all-groups --all-extras
uv run --no-sync pytest \
  --cov-report=term \
  --cov-report=xml \
  --cov=nautilus_trader
```


---

## Overview

This file is located at `scripts/test-coverage.sh` within the repository.


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

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


