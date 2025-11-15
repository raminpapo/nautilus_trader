# Documentation: `tests/mem_leak_tests/README.md`
**Generated:** 2025-11-15T19:40:08.015336Z
**File Size:** 666 bytes
**Extension:** .md
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

- **Path:** `tests/mem_leak_tests/README.md`
- **Size:** 666 bytes
- **Lines:** 25
- **Extension:** `.md`
- **Type:** text

---

## Source Code

```markdown
# Performance tests

This subpackage provides a suite of performance tests, including scripts which can be run
to profile memory and thread resource usage.

Memory profiling is conducted using [memray](https://github.com/bloomberg/memray).
The package is not a development dependency because it doesn't currently support windows.

You can install the package via PyPI:

```bash
pip install memray
```

To profile using memray, first invoke the script using the memray CLI:

```bash
memray run --live-port 8100 --live-remote tests/mem_leak_tests/memray_backtest.py
```

Then from another shell, connect to the memray profiler dashboard:

```bash
memray live 8100
```
```


---

## Overview

This file is located at `tests/mem_leak_tests/README.md` within the repository.

This is a Markdown documentation file.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `tests/mem_leak_tests`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


