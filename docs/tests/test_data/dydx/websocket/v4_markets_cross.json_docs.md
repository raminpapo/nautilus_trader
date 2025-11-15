# Documentation: `tests/test_data/dydx/websocket/v4_markets_cross.json`
**Generated:** 2025-11-15T19:40:08.282470Z
**File Size:** 1193 bytes
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

- **Path:** `tests/test_data/dydx/websocket/v4_markets_cross.json`
- **Size:** 1,193 bytes
- **Lines:** 35
- **Extension:** `.json`
- **Type:** text

---

## Source Code

```json
{
    "type": "channel_data",
    "connection_id": "3f42a31a-07a0-4c4b-b74e-bfa3dbf03012",
    "message_id": 768900,
    "channel": "v4_markets",
    "version": "1.0.0",
    "contents": {
        "trading": {
            "FTM-USD": {
                "id": "86",
                "clobPairId": "86",
                "ticker": "FTM-USD",
                "marketId": 86,
                "status": "FINAL_SETTLEMENT",
                "quantumConversionExponent": -9,
                "atomicResolution": -5,
                "subticksPerTick": 1000000,
                "stepBaseQuantums": 1000000,
                "marketType": "CROSS",
                "initialMarginFraction": "0.2",
                "maintenanceMarginFraction": "0.1",
                "openInterestLowerCap": "5000000",
                "openInterestUpperCap": "10000000",
                "tickSize": "0.0001",
                "stepSize": "10",
                "priceChange24H": "-0.0036333222",
                "volume24H": "292953.744",
                "trades24H": 2656,
                "nextFundingRate": "0",
                "openInterest": "564710",
                "baseOpenInterest": "263330"
            }
        }
    }
}
```


---

## Overview

This file is located at `tests/test_data/dydx/websocket/v4_markets_cross.json` within the repository.

This is a configuration file.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `tests/test_data/dydx/websocket`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


