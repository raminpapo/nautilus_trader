# Documentation: `tests/integration_tests/adapters/binance/resources/ws_messages/ws_futures_order_update_new_limit_if_touched_price_match.json`
**Generated:** 2025-11-15T19:40:07.638889Z
**File Size:** 894 bytes
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

- **Path:** `tests/integration_tests/adapters/binance/resources/ws_messages/ws_futures_order_update_new_limit_if_touched_price_match.json`
- **Size:** 894 bytes
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
    "E": 1759347763200,
    "T": 1759347763200,
    "o": {
      "s": "ETHUSDT",
      "c": "O-12345-test-limit-if-touched-price-match",
      "S": "BUY",
      "o": "TAKE_PROFIT",
      "f": "GTC",
      "q": "1.000",
      "p": "2505.25",
      "ap": "0.00",
      "sp": "2500.00",
      "x": "NEW",
      "X": "NEW",
      "i": 8765432102,
      "l": "0.000",
      "z": "0.000",
      "L": "0.00",
      "N": null,
      "n": null,
      "T": 1759347763200,
      "t": 0,
      "b": "0",
      "a": "0",
      "m": false,
      "R": false,
      "wt": "CONTRACT_PRICE",
      "ot": "TAKE_PROFIT",
      "ps": "LONG",
      "cp": false,
      "AP": null,
      "cr": null,
      "pP": false,
      "si": 0,
      "ss": 0,
      "rp": "0.00",
      "gtd": 0,
      "W": 1759347763200,
      "V": null
    }
  }
}
```


---

## Overview

This file is located at `tests/integration_tests/adapters/binance/resources/ws_messages/ws_futures_order_update_new_limit_if_touched_price_match.json` within the repository.

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


