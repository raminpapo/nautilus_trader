# Documentation: `crates/adapters/bitmex/test_data/http_get_positions.json`
**Generated:** 2025-11-15T19:40:00.404988Z
**File Size:** 2809 bytes
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

- **Path:** `crates/adapters/bitmex/test_data/http_get_positions.json`
- **Size:** 2,809 bytes
- **Lines:** 95
- **Extension:** `.json`
- **Type:** text

---

## Source Code

```json
[
    {
        "account": 1234567,
        "symbol": "XBTUSD",
        "currency": "XBt",
        "underlying": "XBT",
        "quoteCurrency": "USD",
        "commission": 0.00075,
        "initMarginReq": 0.01,
        "maintMarginReq": 0.005,
        "riskLimit": 20000000000,
        "leverage": 10.0,
        "crossMargin": false,
        "deleveragePercentile": 0.5423,
        "rebalancedPnl": 0,
        "prevRealisedPnl": 123456,
        "prevUnrealisedPnl": 0,
        "prevClosePrice": 97409.63,
        "openingTimestamp": "2024-11-25T00:00:00.000Z",
        "openingQty": 0,
        "openingCost": 0,
        "openingComm": 0,
        "openOrderBuyQty": 100,
        "openOrderBuyCost": -101837,
        "openOrderBuyPremium": 0,
        "openOrderSellQty": 0,
        "openOrderSellCost": 0,
        "openOrderSellPremium": 0,
        "execBuyQty": 300,
        "execBuyCost": -305511,
        "execSellQty": 200,
        "execSellCost": 202120,
        "execQty": 100,
        "execCost": -103391,
        "execComm": 227,
        "currentTimestamp": "2024-11-25T10:35:02.000Z",
        "currentQty": 100,
        "currentCost": -103391,
        "currentComm": 227,
        "realisedCost": 0,
        "unrealisedCost": -103391,
        "grossOpenCost": 0,
        "grossOpenPremium": 0,
        "grossExecCost": -103391,
        "isOpen": true,
        "markPrice": 98000.0,
        "markValue": -102041,
        "riskValue": 102041,
        "homeNotional": -0.00102041,
        "foreignNotional": 100.0,
        "posState": "",
        "posCost": -103391,
        "posCost2": -103391,
        "posCross": 0,
        "posInit": 1024,
        "posComm": 284,
        "posLoss": 0,
        "posMargin": 1308,
        "posMaint": 512,
        "posAllowance": 0,
        "taxableMargin": 0,
        "initMargin": 0,
        "maintMargin": 1308,
        "sessionMargin": 0,
        "targetExcessMargin": 0,
        "varMargin": 0,
        "realisedGrossPnl": 0,
        "realisedTax": 0,
        "realisedPnl": -227,
        "unrealisedGrossPnl": 1350,
        "longBankrupt": 0,
        "shortBankrupt": 0,
        "taxBase": 0,
        "indicativeTaxRate": null,
        "indicativeTax": 0,
        "unrealisedTax": 0,
        "unrealisedPnl": 1350,
        "unrealisedPnlPcnt": 0.0131,
        "unrealisedRoePcnt": 0.1306,
        "simpleQty": null,
        "simpleCost": null,
        "simpleValue": null,
        "simplePnl": null,
        "simplePnlPcnt": null,
        "avgCostPrice": 98390.88,
        "avgEntryPrice": 98390.88,
        "breakEvenPrice": 98413.15,
        "marginCallPrice": 49195.44,
        "liquidationPrice": 49195.44,
        "bankruptPrice": 49146.58,
        "timestamp": "2024-11-25T10:35:02.123Z",
        "lastPrice": 98000.0,
        "lastValue": -102041
    }
]
```


---

## Overview

This file is located at `crates/adapters/bitmex/test_data/http_get_positions.json` within the repository.

This is a configuration file.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/bitmex/test_data`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: session. Ensure proper handling of secrets.

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


