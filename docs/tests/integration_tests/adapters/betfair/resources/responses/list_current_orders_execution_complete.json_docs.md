# Documentation: `tests/integration_tests/adapters/betfair/resources/responses/list_current_orders_execution_complete.json`
**Generated:** 2025-11-15T19:40:07.384104Z
**File Size:** 2230 bytes
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

- **Path:** `tests/integration_tests/adapters/betfair/resources/responses/list_current_orders_execution_complete.json`
- **Size:** 2,230 bytes
- **Lines:** 80
- **Extension:** `.json`
- **Type:** text

---

## Source Code

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "currentOrders": [
      {
        "betId": "228059754671",
        "marketId": "1.180575118",
        "selectionId": 39980,
        "handicap": 0.0,
        "priceSize": {
          "price": 5.0,
          "size": 10.0
        },
        "bspLiability": 0.0,
        "side": "BACK",
        "status": "EXECUTABLE",
        "persistenceType": "LAPSE",
        "orderType": "LIMIT",
        "placedDate": "2021-03-24T06:47:02.000Z",
        "averagePriceMatched": 0.0,
        "sizeMatched": 0.0,
        "sizeRemaining": 10.0,
        "sizeLapsed": 0.0,
        "sizeCancelled": 0.0,
        "sizeVoided": 0.0,
        "regulatorCode": "MALTA LOTTERIES AND GAMBLING AUTHORITY"
      },
      {
        "betId": "228059821049",
        "marketId": "1.180575118",
        "selectionId": 217709,
        "handicap": 0.0,
        "priceSize": {
          "price": 1.9,
          "size": 10.0
        },
        "bspLiability": 0.0,
        "side": "BACK",
        "status": "EXECUTION_COMPLETE",
        "persistenceType": "LAPSE",
        "orderType": "LIMIT",
        "placedDate": "2021-03-24T06:49:41.000Z",
        "matchedDate": "2021-03-24T06:49:41.000Z",
        "averagePriceMatched": 1.9,
        "sizeMatched": 10.0,
        "sizeRemaining": 0.0,
        "sizeLapsed": 0.0,
        "sizeCancelled": 0.0,
        "sizeVoided": 0.0,
        "regulatorCode": "MALTA LOTTERIES AND GAMBLING AUTHORITY"
      },
      {
        "betId": "228059869313",
        "marketId": "1.180575118",
        "selectionId": 217709,
        "handicap": 0.0,
        "priceSize": {
          "price": 1.92,
          "size": 10.0
        },
        "bspLiability": 0.0,
        "side": "LAY",
        "status": "EXECUTION_COMPLETE",
        "persistenceType": "LAPSE",
        "orderType": "LIMIT",
        "placedDate": "2021-03-24T06:51:50.000Z",
        "matchedDate": "2021-03-24T06:51:50.000Z",
        "averagePriceMatched": 1.92,
        "sizeMatched": 10.0,
        "sizeRemaining": 0.0,
        "sizeLapsed": 0.0,
        "sizeCancelled": 0.0,
        "sizeVoided": 0.0,
        "regulatorCode": "MALTA LOTTERIES AND GAMBLING AUTHORITY"
      }
    ],
    "moreAvailable": false
  }
}
```


---

## Overview

This file is located at `tests/integration_tests/adapters/betfair/resources/responses/list_current_orders_execution_complete.json` within the repository.

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

**Security:** This file may contain sensitive patterns: auth. Ensure proper handling of secrets.

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


