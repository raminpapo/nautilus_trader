# Documentation: ws_orders_fok.json

## File Metadata

- **Path**: `crates/adapters/okx/test_data/ws_orders_fok.json`
- **Size**: 1,423 bytes
- **Lines**: 65
- **Language**: JSON

## Original Source

```json
{
  "arg": {
    "channel": "orders",
    "instType": "SPOT"
  },
  "data": [
    {
      "accFillSz": "0.05",
      "algoClOrdId": "",
      "algoId": "",
      "attachAlgoClOrdId": "",
      "attachAlgoOrds": [],
      "avgPx": "50000.0",
      "cTime": "1746947317401",
      "cancelSource": "",
      "cancelSourceReason": "",
      "category": "normal",
      "ccy": "USDT",
      "clOrdId": "FOK-TEST-001",
      "execType": "T",
      "fee": "-0.25",
      "feeCcy": "USDT",
      "fillPx": "50000.0",
      "fillSz": "0.05",
      "fillTime": "1746947317402",
      "instId": "BTC-USDT",
      "instType": "SPOT",
      "isTpLimit": "false",
      "lever": "",
      "linkedAlgoOrd": {
        "algoId": ""
      },
      "ordId": "2497956918703120385",
      "ordType": "fok",
      "pnl": "0",
      "posSide": "net",
      "px": "50000.0",
      "pxType": "",
      "pxUsd": "",
      "pxVol": "",
      "quickMgnType": "",
      "rebate": "0",
      "rebateCcy": "USDT",
      "reduceOnly": "false",
      "side": "buy",
      "slOrdPx": "",
      "slTriggerPx": "",
      "slTriggerPxType": "",
      "source": "",
      "state": "filled",
      "stpId": "",
      "stpMode": "",
      "sz": "0.05",
      "tag": "",
      "tdMode": "cash",
      "tgtCcy": "",
      "tpOrdPx": "",
      "tpTriggerPx": "",
      "tpTriggerPxType": "",
      "tradeId": "1518905530",
      "uTime": "1746947317402"
    }
  ]
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 5


**Identifiers**: `BTC`, `FOK`, `SPOT`, `TEST`, `USDT`

## Related Files

This file is located in `crates/adapters/okx/test_data/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/adapters/okx/test_data/ws_orders_fok.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:00.591840Z*
