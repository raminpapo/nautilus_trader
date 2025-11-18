# Documentation: http_get_orders_algo_history.json

## File Metadata

- **Path**: `crates/adapters/okx/test_data/http_get_orders_algo_history.json`
- **Size**: 784 bytes
- **Lines**: 36
- **Language**: JSON

## Original Source

```json
{
  "code": "0",
  "msg": "",
  "data": [
    {
      "algoId": "987654321",
      "algoClOrdId": "client_algo_2",
      "clOrdId": "cl_ord_123",
      "ordId": "ord_456",
      "instId": "ETH-USDT-SWAP",
      "instType": "SWAP",
      "ordType": "trigger",
      "state": "effective",
      "side": "sell",
      "posSide": "short",
      "sz": "10",
      "triggerPx": "3000",
      "triggerPxType": "mark",
      "ordPx": "2990",
      "actualSz": "10",
      "actualPx": "2995",
      "actualSide": "sell",
      "triggerTime": "1622559940237",
      "tdMode": "cross",
      "cTime": "1622559930237",
      "uTime": "1622559940237",
      "pxVar": "",
      "pxSpread": "",
      "pxLimit": "",
      "szLimit": "",
      "amendPxOnTriggerType": "",
      "tag": ""
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


**Identifiers**: `ETH`, `SWAP`, `USDT`

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
pytest crates/adapters/okx/test_data/http_get_orders_algo_history.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:00.550260Z*
