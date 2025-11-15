# Documentation: `tests/integration_tests/adapters/betfair/resources/responses/betting_place_order_success.json`
**Generated:** 2025-11-15T19:40:07.375783Z
**File Size:** 765 bytes
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

- **Path:** `tests/integration_tests/adapters/betfair/resources/responses/betting_place_order_success.json`
- **Size:** 765 bytes
- **Lines:** 31
- **Extension:** `.json`
- **Type:** text

---

## Source Code

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "customerRef": "O-20210327-090738-001-001-2",
    "status": "SUCCESS",
    "marketId": "1.181005744",
    "instructionReports": [
      {
        "status": "SUCCESS",
        "instruction": {
          "selectionId": 86362,
          "handicap": 0.0,
          "limitOrder": {
            "size": 10.0,
            "price": 2.58,
            "persistenceType": "PERSIST"
          },
          "customerOrderRef": "O-20210327-090738-001-001-2",
          "orderType": "LIMIT",
          "side": "LAY"
        },
        "betId": "228302937743",
        "placedDate": "2021-03-27T09:07:38.000Z",
        "averagePriceMatched": 0.0,
        "sizeMatched": 0.0,
        "orderStatus": "EXECUTABLE"
      }
    ]
  }
}
```


---

## Overview

This file is located at `tests/integration_tests/adapters/betfair/resources/responses/betting_place_order_success.json` within the repository.

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


