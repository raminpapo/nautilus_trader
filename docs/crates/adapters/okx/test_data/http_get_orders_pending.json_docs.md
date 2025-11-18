# Documentation: http_get_orders_pending.json

## File Metadata

- **Path**: `crates/adapters/okx/test_data/http_get_orders_pending.json`
- **Size**: 1,342 bytes
- **Lines**: 62
- **Language**: JSON

## Original Source

```json
{
  "code": "0",
  "msg": "",
  "data": [
    {
      "accFillSz": "0",
      "algoClOrdId": "",
      "algoId": "",
      "attachAlgoClOrdId": "",
      "attachAlgoOrds": [],
      "avgPx": "0",
      "cTime": "1746947317000",
      "cancelSource": "",
      "cancelSourceReason": "",
      "category": "normal",
      "ccy": "USDT",
      "clOrdId": "client-order-1",
      "fee": "0",
      "feeCcy": "USDT",
      "fillPx": "0",
      "fillSz": "0",
      "fillTime": "0",
      "instId": "BTC-USDT-SWAP",
      "instType": "SWAP",
      "isTpLimit": "false",
      "lever": "3",
      "linkedAlgoOrd": {
        "algoId": ""
      },
      "ordId": "1234567890123456789",
      "ordType": "limit",
      "pnl": "0",
      "posSide": "long",
      "px": "103500",
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
      "state": "live",
      "stpId": "",
      "stpMode": "cancel_maker",
      "sz": "0.10",
      "tag": "",
      "tdMode": "cross",
      "tgtCcy": "",
      "tpOrdPx": "",
      "tpTriggerPx": "",
      "tpTriggerPxType": "",
      "tradeId": "0",
      "uTime": "1746947317000"
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
pytest crates/adapters/okx/test_data/http_get_orders_pending.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:00.554700Z*
