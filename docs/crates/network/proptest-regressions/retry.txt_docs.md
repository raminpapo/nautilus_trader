# Documentation: `crates/network/proptest-regressions/retry.txt`
**Generated:** 2025-11-15T19:40:03.198613Z
**File Size:** 902 bytes
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

- **Path:** `crates/network/proptest-regressions/retry.txt`
- **Size:** 902 bytes
- **Lines:** 11
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
cc 92d6a183a29ef3cdbb304d0947dcd49f0f61c6fbd0ef6684fdabd86e86127e19 # shrinks to jitter_ms = 0, base_delay_ms = 50
cc f166544819b7c556ff78a632cc61ab0b3ad23eb8ad5df8bfa06846dd42c2328f # shrinks to max_elapsed_ms = 37, delay_per_retry = 5, max_retries = 3
cc 955dbfd4e07a55762de27ec05e0bb9449e8478c5d028617d3a42953b157fda88 # shrinks to max_elapsed_ms = 19, delay_per_retry = 32
cc 1f7b6a390f6dd8a928732a1eaac3acc04ed6be8da7e0df9b9e396358f7f31758 # shrinks to jitter_ms = 0, base_delay_ms = 28
cc 756838c4ec902a43e02f41f9ca0d9c2be51cdc19b38550a873f65337874bfc5a # shrinks to jitter_ms = 5, base_delay_ms = 27
```


---

## Overview

This file is located at `crates/network/proptest-regressions/retry.txt` within the repository.


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


