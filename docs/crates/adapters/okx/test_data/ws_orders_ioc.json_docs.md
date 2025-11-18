# Documentation: ws_orders_ioc.json

## File Metadata

- **Path**: `crates/adapters/okx/test_data/ws_orders_ioc.json`
- **Size**: 1,436 bytes
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
      "accFillSz": "0.02",
      "algoClOrdId": "",
      "algoId": "",
      "attachAlgoClOrdId": "",
      "attachAlgoOrds": [],
      "avgPx": "50100.5",
      "cTime": "1746947318501",
      "cancelSource": "",
      "cancelSourceReason": "",
      "category": "normal",
      "ccy": "USDT",
      "clOrdId": "IOC-TEST-001",
      "execType": "T",
      "fee": "-0.1002",
      "feeCcy": "USDT",
      "fillPx": "50100.5",
      "fillSz": "0.02",
      "fillTime": "1746947318502",
      "instId": "BTC-USDT",
      "instType": "SPOT",
      "isTpLimit": "false",
      "lever": "",
      "linkedAlgoOrd": {
        "algoId": ""
      },
      "ordId": "2497956918703120386",
      "ordType": "ioc",
      "pnl": "0",
      "posSide": "net",
      "px": "50100.0",
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
      "state": "partially_filled",
      "stpId": "",
      "stpMode": "",
      "sz": "0.05",
      "tag": "",
      "tdMode": "cash",
      "tgtCcy": "",
      "tpOrdPx": "",
      "tpTriggerPx": "",
      "tpTriggerPxType": "",
      "tradeId": "1518905531",
      "uTime": "1746947318502"
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


**Identifiers**: `BTC`, `IOC`, `SPOT`, `TEST`, `USDT`

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
pytest crates/adapters/okx/test_data/ws_orders_ioc.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:00.597266Z*
