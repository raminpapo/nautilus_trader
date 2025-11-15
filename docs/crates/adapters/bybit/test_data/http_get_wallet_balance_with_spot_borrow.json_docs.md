# Documentation: `crates/adapters/bybit/test_data/http_get_wallet_balance_with_spot_borrow.json`
**Generated:** 2025-11-15T19:40:00.713221Z
**File Size:** 1490 bytes
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

- **Path:** `crates/adapters/bybit/test_data/http_get_wallet_balance_with_spot_borrow.json`
- **Size:** 1,490 bytes
- **Lines:** 43
- **Extension:** `.json`
- **Type:** text

---

## Source Code

```json
{
    "retCode": 0,
    "retMsg": "OK",
    "result": {
        "list": [
            {
                "totalEquity": "3000.00",
                "accountIMRate": "0",
                "totalMarginBalance": "2500.00",
                "totalInitialMargin": "0",
                "accountType": "UNIFIED",
                "totalAvailableBalance": "2500.00",
                "accountMMRate": "0",
                "totalPerpUPL": "0",
                "totalWalletBalance": "2500.00",
                "accountLTV": "0",
                "totalMaintenanceMargin": "0",
                "coin": [
                    {
                        "availableToBorrow": "5000",
                        "bonus": "0",
                        "accruedInterest": "0.50",
                        "availableToWithdraw": "800.00",
                        "equity": "1000.00",
                        "usdValue": "1000.00",
                        "unrealisedPnl": "0",
                        "borrowAmount": "200.00",
                        "walletBalance": "1200.00",
                        "cumRealisedPnl": "100.00",
                        "locked": "0",
                        "collateralSwitch": true,
                        "marginCollateral": true,
                        "coin": "USDT",
                        "spotHedgingQty": "0",
                        "spotBorrow": "200.00"
                    }
                ]
            }
        ]
    },
    "retExtInfo": {},
    "time": 1234567890
}
```


---

## Overview

This file is located at `crates/adapters/bybit/test_data/http_get_wallet_balance_with_spot_borrow.json` within the repository.

This is a configuration file.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/bybit/test_data`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


