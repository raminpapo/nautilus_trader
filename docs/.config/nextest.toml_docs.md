# Documentation: `.config/nextest.toml`
**Generated:** 2025-11-15T19:40:00.215323Z
**File Size:** 437 bytes
**Extension:** .toml
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

- **Path:** `.config/nextest.toml`
- **Size:** 437 bytes
- **Lines:** 18
- **Extension:** `.toml`
- **Type:** text

---

## Source Code

```toml
[test-groups]
serial-tests = { max-threads = 1 }

[profile.default]
# Default settings

[[profile.default.overrides]]
filter = 'test(serial_tests)'
test-group = 'serial-tests'

[[profile.default.overrides]]
filter = 'test(test_order_book)'
slow-timeout = { period = "300s" }

# Websocket tests can be flaky due to timing on low-spec runners, give them extra retries
[[profile.default.overrides]]
filter = 'binary(websocket)'
retries = 3
```


---

## Overview

This file is located at `.config/nextest.toml` within the repository.

This is a configuration file.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `.config`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


