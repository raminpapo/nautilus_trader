# Documentation: ws_orders_liquidation.json

## File Metadata

- **Path**: `crates/adapters/okx/test_data/ws_orders_liquidation.json`
- **Size**: 1,445 bytes
- **Lines**: 65
- **Language**: JSON

## Original Source

```json
{
  "arg": {
    "channel": "orders",
    "instType": "SWAP"
  },
  "data": [
    {
      "accFillSz": "0.5",
      "algoClOrdId": "",
      "algoId": "",
      "attachAlgoClOrdId": "",
      "attachAlgoOrds": [],
      "avgPx": "40000.0",
      "cTime": "1746947317401",
      "cancelSource": "",
      "cancelSourceReason": "",
      "category": "full_liquidation",
      "ccy": "USDT",
      "clOrdId": "",
      "execType": "T",
      "fee": "-20.0",
      "feeCcy": "USDT",
      "fillPx": "40000.0",
      "fillSz": "0.5",
      "fillTime": "1746947317402",
      "instId": "BTC-USDT-SWAP",
      "instType": "SWAP",
      "isTpLimit": "false",
      "lever": "10.0",
      "linkedAlgoOrd": {
        "algoId": ""
      },
      "ordId": "2497956918703120999",
      "ordType": "market",
      "pnl": "-5000",
      "posSide": "long",
      "px": "",
      "pxType": "",
      "pxUsd": "",
      "pxVol": "",
      "quickMgnType": "",
      "rebate": "0",
      "rebateCcy": "USDT",
      "reduceOnly": "false",
      "side": "sell",
      "slOrdPx": "",
      "slTriggerPx": "",
      "slTriggerPxType": "",
      "source": "",
      "state": "filled",
      "stpId": "",
      "stpMode": "cancel_maker",
      "sz": "0.5",
      "tag": "",
      "tdMode": "isolated",
      "tgtCcy": "",
      "tpOrdPx": "",
      "tpTriggerPx": "",
      "tpTriggerPxType": "",
      "tradeId": "1518905999",
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

Total unique keywords extracted: 3


**Identifiers**: `BTC`, `SWAP`, `USDT`

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
pytest crates/adapters/okx/test_data/ws_orders_liquidation.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:00.599212Z*
