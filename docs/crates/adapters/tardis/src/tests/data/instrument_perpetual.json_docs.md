# Documentation: `crates/adapters/tardis/src/tests/data/instrument_perpetual.json`
**Generated:** 2025-11-15T19:40:01.509752Z
**File Size:** 797 bytes
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

- **Path:** `crates/adapters/tardis/src/tests/data/instrument_perpetual.json`
- **Size:** 797 bytes
- **Lines:** 36
- **Extension:** `.json`
- **Type:** text

---

## Source Code

```json
{
  "id": "XBTUSD",
  "datasetId": "XBTUSD",
  "exchange": "bitmex",
  "baseCurrency": "BTC",
  "quoteCurrency": "USD",
  "settlementCurrency": "BTC",
  "type": "perpetual",
  "active": true,
  "availableSince": "2019-03-30T00:00:00.000Z",
  "priceIncrement": 0.1,
  "amountIncrement": 100,
  "minTradeAmount": 100,
  "makerFee": 0.0005,
  "takerFee": 0.0005,
  "inverse": true,
  "contractType": "inverse_perpetual",
  "contractMultiplier": 1,
  "underlyingIndex": ".BXBT",
  "changes": [
    {
      "until": "2021-06-08T04:30:00.000Z",
      "amountIncrement": 1,
      "minTradeAmount": 1
    },
    {
      "until": "2024-07-31T04:00:00.000Z",
      "priceIncrement": 0.5
    },
    {
      "until": "2024-10-22T00:00:00.000Z",
      "makerFee": 0.0002,
      "takerFee": 0.00075
    }
  ]
}
```


---

## Overview

This file is located at `crates/adapters/tardis/src/tests/data/instrument_perpetual.json` within the repository.

This is a configuration file.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/tardis/src/tests/data`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


