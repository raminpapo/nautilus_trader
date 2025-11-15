# Documentation: `scripts/test-performance.sh`
**Generated:** 2025-11-15T19:40:05.532096Z
**File Size:** 129 bytes
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

- **Path:** `scripts/test-performance.sh`
- **Size:** 129 bytes
- **Lines:** 4
- **Extension:** `.sh`
- **Type:** text

---

## Source Code

```bash
#!/bin/bash

uv sync --all-groups --all-extras
uv run --no-sync pytest tests/performance_tests --benchmark-disable-gc --codspeed
```


---

## Overview

This file is located at `scripts/test-performance.sh` within the repository.


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


