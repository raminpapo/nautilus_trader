# Documentation: `crates/adapters/kraken/test_data/http_asset_pairs.json`
**Generated:** 2025-11-15T19:40:01.175904Z
**File Size:** 3046 bytes
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

- **Path:** `crates/adapters/kraken/test_data/http_asset_pairs.json`
- **Size:** 3,046 bytes
- **Lines:** 133
- **Extension:** `.json`
- **Type:** text

---

## Source Code

```json
{
    "error": [],
    "result": {
        "XBTUSDT": {
            "altname": "XBTUSDT",
            "wsname": "XBT/USDT",
            "aclass_base": "currency",
            "base": "XXBT",
            "aclass_quote": "currency",
            "quote": "USDT",
            "lot": "unit",
            "cost_decimals": 5,
            "pair_decimals": 1,
            "lot_decimals": 8,
            "lot_multiplier": 1,
            "leverage_buy": [
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10
            ],
            "leverage_sell": [
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10
            ],
            "fees": [
                [
                    0,
                    0.4
                ],
                [
                    10000,
                    0.35
                ],
                [
                    50000,
                    0.24
                ],
                [
                    100000,
                    0.22
                ],
                [
                    250000,
                    0.2
                ],
                [
                    500000,
                    0.18
                ],
                [
                    1000000,
                    0.16
                ],
                [
                    2500000,
                    0.14
                ],
                [
                    5000000,
                    0.12
                ],
                [
                    10000000,
                    0.1
                ]
            ],
            "fees_maker": [
                [
                    0,
                    0.25
                ],
                [
                    10000,
                    0.2
                ],
                [
                    50000,
                    0.14
                ],
                [
                    100000,
                    0.12
                ],
                [
                    250000,
                    0.1
                ],
                [
                    500000,
                    0.08
                ],
                [
                    1000000,
                    0.06
                ],
                [
                    2500000,
                    0.04
                ],
                [
                    5000000,
                    0.02
                ],
                [
                    10000000,
                    0.0
                ]
            ],
            "fee_volume_currency": "ZUSD",
            "margin_call": 80,
            "margin_stop": 40,
            "ordermin": "0.00005",
            "costmin": "0.5",
            "tick_size": "0.1",
            "status": "online",
            "long_position_limit": 80,
            "short_position_limit": 80
        }
    }
}
```


---

## Overview

This file is located at `crates/adapters/kraken/test_data/http_asset_pairs.json` within the repository.

This is a configuration file.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/kraken/test_data`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


