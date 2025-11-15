# Documentation: `tests/integration_tests/adapters/betfair/resources/responses/betting_place_order_error.json`
**Generated:** 2025-11-15T19:40:07.374449Z
**File Size:** 655 bytes
**Extension:** .json
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

- **Path:** `tests/integration_tests/adapters/betfair/resources/responses/betting_place_order_error.json`
- **Size:** 655 bytes
- **Lines:** 28
- **Extension:** `.json`
- **Type:** text

---

## Source Code

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "customerRef": "O-20210331-202018-001-001-2",
    "status": "FAILURE",
    "errorCode": "PERMISSION_DENIED",
    "marketId": "1.181106170",
    "instructionReports": [
      {
        "status": "FAILURE",
        "errorCode": "ERROR_IN_ORDER",
        "instruction": {
          "selectionId": 235,
          "handicap": 0.0,
          "limitOrder": {
            "size": 10.0,
            "price": 1.8,
            "persistenceType": "PERSIST"
          },
          "customerOrderRef": "O-20210331-202018-001-001-2",
          "orderType": "LIMIT",
          "side": "LAY"
        }
      }
    ]
  }
}
```


---

## Overview

This file is located at `tests/integration_tests/adapters/betfair/resources/responses/betting_place_order_error.json` within the repository.

This is a configuration file.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `tests/integration_tests/adapters/betfair/resources/responses`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


