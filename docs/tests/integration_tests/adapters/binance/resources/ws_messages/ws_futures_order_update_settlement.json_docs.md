# Documentation: `tests/integration_tests/adapters/binance/resources/ws_messages/ws_futures_order_update_settlement.json`
**Generated:** 2025-11-15T19:40:07.641889Z
**File Size:** 899 bytes
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

- **Path:** `tests/integration_tests/adapters/binance/resources/ws_messages/ws_futures_order_update_settlement.json`
- **Size:** 899 bytes
- **Lines:** 46
- **Extension:** `.json`
- **Type:** text

---

## Source Code

```json
{
  "stream": "ORDER_TRADE_UPDATE",
  "data": {
    "e": "ORDER_TRADE_UPDATE",
    "E": 1759347763300,
    "T": 1759347763300,
    "o": {
      "s": "BTCUSDT",
      "c": "settlement_autoclose-1111222233334444",
      "S": "BUY",
      "o": "MARKET",
      "f": "GTC",
      "q": "0.050",
      "p": "0",
      "ap": "51000.00",
      "sp": null,
      "x": "CALCULATED",
      "X": "FILLED",
      "i": 6543210987,
      "l": "0.050",
      "z": "0.050",
      "L": "51000.00",
      "N": "USDT",
      "n": "2.55000000",
      "T": 1759347763300,
      "t": 4455667788,
      "b": "0",
      "a": "0",
      "m": false,
      "R": false,
      "wt": "CONTRACT_PRICE",
      "ot": "MARKET",
      "ps": "SHORT",
      "cp": false,
      "AP": null,
      "cr": null,
      "pP": false,
      "si": 0,
      "ss": 0,
      "rp": "25.00",
      "gtd": 0,
      "W": null,
      "V": null
    }
  }
}
```


---

## Overview

This file is located at `tests/integration_tests/adapters/binance/resources/ws_messages/ws_futures_order_update_settlement.json` within the repository.

This is a configuration file.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `tests/integration_tests/adapters/binance/resources/ws_messages`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


