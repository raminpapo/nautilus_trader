# Documentation: ws_orders_trigger.json

## File Metadata

- **Path**: `crates/adapters/okx/test_data/ws_orders_trigger.json`
- **Size**: 1,378 bytes
- **Lines**: 60
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
      "accFillSz": "0.01",
      "avgPx": "101950.0",
      "cTime": "1737400200000",
      "cancelSource": "",
      "cancelSourceReason": "",
      "category": "normal",
      "ccy": "USDT",
      "clOrdId": "706620792746729474_0",
      "execType": "T",
      "fee": "-0.020390",
      "feeCcy": "USDT",
      "fillPx": "101950.0",
      "fillSz": "0.01",
      "fillTime": "1737400200100",
      "instId": "BTC-USDT-SWAP",
      "instType": "SWAP",
      "isTpLimit": "false",
      "lever": "2.0",
      "linkedAlgoOrd": {
        "algoId": "706620792746729474"
      },
      "ordId": "706620792746729999",
      "ordType": "trigger",
      "pnl": "10.5",
      "posSide": "long",
      "px": "",
      "pxType": "",
      "pxUsd": "",
      "pxVol": "",
      "quickMgnType": "",
      "rebate": "0",
      "rebateCcy": "USDT",
      "reduceOnly": "true",
      "side": "sell",
      "slOrdPx": "",
      "slTriggerPx": "",
      "slTriggerPxType": "",
      "source": "algo",
      "state": "filled",
      "stpId": "",
      "stpMode": "cancel_maker",
      "sz": "0.01",
      "tag": "",
      "tdMode": "isolated",
      "tgtCcy": "",
      "tpOrdPx": "",
      "tpTriggerPx": "",
      "tpTriggerPxType": "",
      "tradeId": "1518905530",
      "uTime": "1737400200100"
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
pytest crates/adapters/okx/test_data/ws_orders_trigger.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:00.602946Z*
