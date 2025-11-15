# Documentation: `scripts/ci/validate-wheel-count.sh`
**Generated:** 2025-11-15T19:40:05.516532Z
**File Size:** 781 bytes
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

- **Path:** `scripts/ci/validate-wheel-count.sh`
- **Size:** 781 bytes
- **Lines:** 30
- **Extension:** `.sh`
- **Type:** text

---

## Source Code

```bash
#!/usr/bin/env bash
set -euo pipefail

# Validate wheel count matches expected count
# Usage: validate-wheel-count.sh <expected_count>

if [ $# -ne 1 ]; then
  echo "Usage: $0 <expected_count>" >&2
  exit 1
fi

expected_count=$1

if ! [[ "$expected_count" =~ ^[0-9]+$ ]]; then
  echo "ERROR: expected_count must be a positive integer, got: $expected_count" >&2
  exit 1
fi

echo "Validating wheel count in dist/ directory..."

wheel_count=$(find dist/ -name "nautilus_trader-*.whl" -type f | wc -l)

if [ "$wheel_count" -ne "$expected_count" ]; then
  echo "ERROR: Expected $expected_count wheels, found $wheel_count" >&2
  echo "Downloaded wheels:" >&2
  find dist/ -name "nautilus_trader-*.whl" -type f -ls >&2
  exit 1
fi

echo "✓ Validated: Found all $expected_count wheels"
```


---

## Overview

This file is located at `scripts/ci/validate-wheel-count.sh` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `scripts/ci`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


