# Documentation: `scripts/rust-toolchain.sh`
**Generated:** 2025-11-15T19:40:05.528859Z
**File Size:** 737 bytes
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

- **Path:** `scripts/rust-toolchain.sh`
- **Size:** 737 bytes
- **Lines:** 24
- **Extension:** `.sh`
- **Type:** text

---

## Source Code

```bash
#!/bin/bash
set -euo pipefail

# Resolve rust-toolchain.toml relative to this script's location
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TOOLCHAIN_FILE="${SCRIPT_DIR}/../rust-toolchain.toml"

# Check that rust-toolchain.toml exists
if [[ ! -f "$TOOLCHAIN_FILE" ]]; then
  echo "Error: rust-toolchain.toml not found at $TOOLCHAIN_FILE" >&2
  exit 1
fi

# Extract toolchain version
VERSION=$(awk -F'"' '/version[[:space:]]*=/{gsub(/[[:space:]]/,"",$2); print $2; exit}' "$TOOLCHAIN_FILE")

# Validate that we got a version
if [[ -z "$VERSION" ]]; then
  echo "Error: Could not extract toolchain version from $TOOLCHAIN_FILE" >&2
  exit 1
fi

# Output version (without trailing newline for consistency)
echo -n "$VERSION"
```


---

## Overview

This file is located at `scripts/rust-toolchain.sh` within the repository.


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


