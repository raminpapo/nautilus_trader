# Documentation: ws_orders_algo.json

## File Metadata

- **Path**: `crates/adapters/okx/test_data/ws_orders_algo.json`
- **Size**: 3,513 bytes
- **Lines**: 138
- **Language**: JSON

## Original Source

```json
{
  "arg": {
    "channel": "orders-algo",
    "instType": "SWAP"
  },
  "data": [
    {
      "algoId": "706620792746729472",
      "algoClOrdId": "STOP001BTCUSDT20250120",
      "clOrdId": "",
      "ordId": "",
      "instId": "BTC-USDT-SWAP",
      "instType": "SWAP",
      "ordType": "trigger",
      "state": "live",
      "side": "sell",
      "posSide": "long",
      "sz": "0.01",
      "triggerPx": "95000",
      "triggerPxType": "last",
      "ordPx": "-1",
      "tdMode": "isolated",
      "lever": "2.0",
      "reduceOnly": "true",
      "actualPx": "",
      "actualSz": "0",
      "notionalUsd": "950",
      "triggerTime": "",
      "tag": "",
      "cTime": "1737400000000",
      "uTime": "1737400000000"
    },
    {
      "algoId": "706620792746729473",
      "algoClOrdId": "STOP002BTCUSDT20250120",
      "clOrdId": "",
      "ordId": "",
      "instId": "BTC-USDT-SWAP",
      "instType": "SWAP",
      "ordType": "trigger",
      "state": "live",
      "side": "buy",
      "posSide": "short",
      "sz": "0.02",
      "triggerPx": "105000",
      "triggerPxType": "mark",
      "ordPx": "106000",
      "tdMode": "isolated",
      "lever": "2.0",
      "reduceOnly": "false",
      "actualPx": "",
      "actualSz": "0",
      "notionalUsd": "2100",
      "triggerTime": "",
      "tag": "",
      "cTime": "1737400100000",
      "uTime": "1737400100000"
    },
    {
      "algoId": "706620792746729474",
      "algoClOrdId": "STOP003BTCUSDT20250120",
      "clOrdId": "706620792746729474_0",
      "ordId": "706620792746729999",
      "instId": "BTC-USDT-SWAP",
      "instType": "SWAP",
      "ordType": "trigger",
      "state": "order_placed",
      "side": "sell",
      "posSide": "long",
      "sz": "0.01",
      "triggerPx": "102000",
      "triggerPxType": "last",
      "ordPx": "-1",
      "tdMode": "isolated",
      "lever": "2.0",
      "reduceOnly": "true",
      "actualPx": "101950",
      "actualSz": "0.01",
      "notionalUsd": "1020",
      "triggerTime": "1737400200000",
      "tag": "",
      "cTime": "1737400050000",
      "uTime": "1737400200000"
    },
    {
      "algoId": "706620792746729475",
      "algoClOrdId": "STOP004BTCUSDT20250120",
      "clOrdId": "",
      "ordId": "",
      "instId": "BTC-USDT-SWAP",
      "instType": "SWAP",
      "ordType": "trigger",
      "state": "canceled",
      "side": "buy",
      "posSide": "short",
      "sz": "0.015",
      "triggerPx": "98000",
      "triggerPxType": "index",
      "ordPx": "98500",
      "tdMode": "isolated",
      "lever": "2.0",
      "reduceOnly": "false",
      "actualPx": "",
      "actualSz": "0",
      "notionalUsd": "1470",
      "triggerTime": "",
      "tag": "user_cancel",
      "cTime": "1737399900000",
      "uTime": "1737400300000"
    },
    {
      "algoId": "706620792746729476",
      "algoClOrdId": "STOP005BTCUSDT20250120",
      "clOrdId": "706620792746729476_0",
      "ordId": "706620792746730000",
      "instId": "BTC-USDT-SWAP",
      "instType": "SWAP",
      "ordType": "trigger",
      "state": "filled",
      "side": "sell",
      "posSide": "long",
      "sz": "0.005",
      "triggerPx": "103000",
      "triggerPxType": "last",
      "ordPx": "102900",
      "tdMode": "isolated",
      "lever": "2.0",
      "reduceOnly": "true",
      "actualPx": "102920",
      "actualSz": "0.005",
      "notionalUsd": "514.60",
      "triggerTime": "1737400400000",
      "tag": "",
      "cTime": "1737399800000",
      "uTime": "1737400400000"
    }
  ]
}
```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 8


**Identifiers**: `BTC`, `STOP001BTCUSDT20250120`, `STOP002BTCUSDT20250120`, `STOP003BTCUSDT20250120`, `STOP004BTCUSDT20250120`, `STOP005BTCUSDT20250120`, `SWAP`, `USDT`

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
pytest crates/adapters/okx/test_data/ws_orders_algo.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:00.585017Z*
