# Documentation: ws_orders_optimal_limit_ioc.json

## File Metadata

- **Path**: `crates/adapters/okx/test_data/ws_orders_optimal_limit_ioc.json`
- **Size**: 1,471 bytes
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
      "accFillSz": "0.1",
      "algoClOrdId": "",
      "algoId": "",
      "attachAlgoClOrdId": "",
      "attachAlgoOrds": [],
      "avgPx": "103750.25",
      "cTime": "1746947319601",
      "cancelSource": "",
      "cancelSourceReason": "",
      "category": "normal",
      "ccy": "USDT",
      "clOrdId": "OPTIMAL-IOC-TEST-001",
      "execType": "M",
      "fee": "-0.051875125",
      "feeCcy": "USDT",
      "fillPx": "103750.25",
      "fillSz": "0.1",
      "fillTime": "1746947319602",
      "instId": "BTC-USDT-SWAP",
      "instType": "SWAP",
      "isTpLimit": "false",
      "lever": "5.0",
      "linkedAlgoOrd": {
        "algoId": ""
      },
      "ordId": "2497956918703120387",
      "ordType": "optimal_limit_ioc",
      "pnl": "0",
      "posSide": "long",
      "px": "",
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
      "stpMode": "cancel_maker",
      "sz": "0.1",
      "tag": "",
      "tdMode": "isolated",
      "tgtCcy": "",
      "tpOrdPx": "",
      "tpTriggerPx": "",
      "tpTriggerPxType": "",
      "tradeId": "1518905532",
      "uTime": "1746947319602"
    }
  ]
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 6


**Identifiers**: `BTC`, `IOC`, `OPTIMAL`, `SWAP`, `TEST`, `USDT`

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
pytest crates/adapters/okx/test_data/ws_orders_optimal_limit_ioc.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:00.600835Z*
