# Documentation: `tests/integration_tests/adapters/polymarket/resources/http_responses/orderbook_history.json`
**Generated:** 2025-11-15T19:40:07.912864Z
**File Size:** 1815 bytes
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

- **Path:** `tests/integration_tests/adapters/polymarket/resources/http_responses/orderbook_history.json`
- **Size:** 1,815 bytes
- **Lines:** 57
- **Extension:** `.json`
- **Type:** text

---

## Source Code

```json
{
  "snapshots": [
    {
      "timestamp": 1729000000000,
      "hash": "0xabc123",
      "market": "0x4319532e181605cb15b1bd677759a3bc7f7394b2fdf145195b700eeaedfd5221",
      "asset_id": "60487116984468020978247225474488676749601001829886755968952521846780452448915",
      "bids": [
        {"price": "0.51", "size": "100.5"},
        {"price": "0.50", "size": "250.0"},
        {"price": "0.49", "size": "500.25"}
      ],
      "asks": [
        {"price": "0.52", "size": "150.75"},
        {"price": "0.53", "size": "300.0"},
        {"price": "0.54", "size": "450.5"}
      ]
    },
    {
      "timestamp": 1729000060000,
      "hash": "0xdef456",
      "market": "0x4319532e181605cb15b1bd677759a3bc7f7394b2fdf145195b700eeaedfd5221",
      "asset_id": "60487116984468020978247225474488676749601001829886755968952521846780452448915",
      "bids": [
        {"price": "0.52", "size": "120.0"},
        {"price": "0.51", "size": "280.5"},
        {"price": "0.50", "size": "520.0"}
      ],
      "asks": [
        {"price": "0.53", "size": "140.25"},
        {"price": "0.54", "size": "290.0"},
        {"price": "0.55", "size": "480.75"}
      ]
    },
    {
      "timestamp": 1729000120000,
      "hash": "0x789abc",
      "market": "0x4319532e181605cb15b1bd677759a3bc7f7394b2fdf145195b700eeaedfd5221",
      "asset_id": "60487116984468020978247225474488676749601001829886755968952521846780452448915",
      "bids": [
        {"price": "0.53", "size": "110.5"},
        {"price": "0.52", "size": "260.0"},
        {"price": "0.51", "size": "510.25"}
      ],
      "asks": [
        {"price": "0.54", "size": "130.0"},
        {"price": "0.55", "size": "270.5"},
        {"price": "0.56", "size": "460.0"}
      ]
    }
  ],
  "pagination": {
    "count": 3,
    "limit": 500,
    "has_more": false
  }
}
```


---

## Overview

This file is located at `tests/integration_tests/adapters/polymarket/resources/http_responses/orderbook_history.json` within the repository.

This is a configuration file.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `tests/integration_tests/adapters/polymarket/resources/http_responses`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


