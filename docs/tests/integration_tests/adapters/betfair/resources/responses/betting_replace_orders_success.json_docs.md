# Documentation: `tests/integration_tests/adapters/betfair/resources/responses/betting_replace_orders_success.json`
**Generated:** 2025-11-15T19:40:07.376889Z
**File Size:** 1019 bytes
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

- **Path:** `tests/integration_tests/adapters/betfair/resources/responses/betting_replace_orders_success.json`
- **Size:** 1,019 bytes
- **Lines:** 40
- **Extension:** `.json`
- **Type:** text

---

## Source Code

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "customerRef": "1628815542932-1.186291565-rpl-0",
    "marketId": "1.186291565",
    "instructionReports": [
      {
        "cancelInstructionReport": {
          "instruction": {
            "betId": "1"
          },
          "sizeCancelled": 5.0,
          "cancelledDate": "2021-08-13T00:45:43.000Z",
          "status": "SUCCESS"
        },
        "placeInstructionReport": {
          "instruction": {
            "selectionId": 40521960,
            "limitOrder": {
              "size": 5.0,
              "price": 50.0,
              "persistenceType": "LAPSE"
            },
            "orderType": "LIMIT",
            "side": "BACK"
          },
          "betId": "240808766933",
          "placedDate": "2021-08-13T00:45:43.000Z",
          "averagePriceMatched": 0.0,
          "sizeMatched": 0.0,
          "status": "SUCCESS",
          "orderStatus": "EXECUTABLE"
        },
        "status": "SUCCESS"
      }
    ],
    "status": "SUCCESS"
  }
}
```


---

## Overview

This file is located at `tests/integration_tests/adapters/betfair/resources/responses/betting_replace_orders_success.json` within the repository.

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


