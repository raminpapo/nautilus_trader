# Documentation: `tests/test_data/dydx/websocket/trade_deleveraged.json`
**Generated:** 2025-11-15T19:40:08.245044Z
**File Size:** 1070 bytes
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

- **Path:** `tests/test_data/dydx/websocket/trade_deleveraged.json`
- **Size:** 1,070 bytes
- **Lines:** 36
- **Extension:** `.json`
- **Type:** text

---

## Source Code

```json
{
    "channel": "v4_trades",
    "connection_id": "796abe49-c178-417e-b3d1-7da7de91b931",
    "contents": {
        "trades": [
            {
                "createdAt": "2024-08-05T01:09:28.338Z",
                "id": "015034b9000000020000000e",
                "price": "2322.8",
                "side": "BUY",
                "size": "4.303",
                "type": "LIMIT"
            },
            {
                "createdAt": "2024-08-05T01:09:28.338Z",
                "id": "015034b90000000200000011",
                "price": "2322.8",
                "side": "BUY",
                "size": "4.303",
                "type": "LIMIT"
            },
            {
                "createdAt": "2024-08-05T01:09:28.338Z",
                "id": "015034b90000000200000026",
                "price": "2340.7442700369913687",
                "side": "SELL",
                "size": "0.811",
                "type": "DELEVERAGED"
            }
        ]
    },
    "id": "ETH-USD",
    "message_id": 14299286,
    "type": "channel_data",
    "version": "2.1.0"
}
```


---

## Overview

This file is located at `tests/test_data/dydx/websocket/trade_deleveraged.json` within the repository.

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


