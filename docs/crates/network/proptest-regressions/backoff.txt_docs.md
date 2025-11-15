# Documentation: `crates/network/proptest-regressions/backoff.txt`
**Generated:** 2025-11-15T19:40:03.196861Z
**File Size:** 557 bytes
**Extension:** .txt
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

- **Path:** `crates/network/proptest-regressions/backoff.txt`
- **Size:** 557 bytes
- **Lines:** 8
- **Extension:** `.txt`
- **Type:** text

---

## Source Code

```
# Seeds for failure cases proptest has generated in the past. It is
# automatically read and these particular cases re-run before any
# novel cases are generated.
#
# It is recommended to check this file in to source control so that
# everyone who runs the test benefits from these saved cases.
cc 5689afb07d7f1d849884e4862623843045ed3d60fda16be22cbc54d2c4f042c1 # shrinks to (initial, max, factor, jitter_ms, immediate_first) = (1ms, 1.98s, 3.958823983700926, 808, true), iterations = 12
cc 931fbad69048776408b8ccaf3f5c5317503272dc16323deec163183edd881e6f
```


---

## Overview

This file is located at `crates/network/proptest-regressions/backoff.txt` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/network/proptest-regressions`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


