# Documentation: `tests/integration_tests/adapters/betfair/resources/requests/betting_place_order_bsp.json`
**Generated:** 2025-11-15T19:40:05.575615Z
**File Size:** 509 bytes
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

- **Path:** `tests/integration_tests/adapters/betfair/resources/requests/betting_place_order_bsp.json`
- **Size:** 509 bytes
- **Lines:** 22
- **Extension:** `.json`
- **Type:** text

---

## Source Code

```json
{
  "method": "SportsAPING/v1.0/placeOrders",
  "params": {
    "marketId": "1.179082386",
    "instructions": [
      {
        "customerOrderRef": "O-20210410-022422-001",
        "selectionId": "50214",
        "handicap": null,
        "marketOnCloseOrder": {
          "liability": "10.0"
        },
        "orderType": "MARKET_ON_CLOSE",
        "side": "BACK"
      }
    ],
    "customerStrategyRef": "S-001",
    "customerRef": "be7dffa046f2fce5d820c7634d022ca1"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```


---

## Overview

This file is located at `tests/integration_tests/adapters/betfair/resources/requests/betting_place_order_bsp.json` within the repository.

This is a configuration file.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `tests/integration_tests/adapters/betfair/resources/requests`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


