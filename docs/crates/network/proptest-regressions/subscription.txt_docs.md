# Documentation: `crates/network/proptest-regressions/subscription.txt`
**Generated:** 2025-11-15T19:40:03.199418Z
**File Size:** 446 bytes
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

- **Path:** `crates/network/proptest-regressions/subscription.txt`
- **Size:** 446 bytes
- **Lines:** 7
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
cc 9d2877e030b66c55adc73c8d7b6efdfaa4cdb1ce93fb91768345582bb5c5c2cf # shrinks to operations = [MarkUnsubscribe("channel1"), MarkSubscribe("channel1")]
```


---

## Overview

This file is located at `crates/network/proptest-regressions/subscription.txt` within the repository.


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


