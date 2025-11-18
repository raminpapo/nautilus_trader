# Documentation: http_get_orders_history.json

## File Metadata

- **Path**: `crates/adapters/bybit/test_data/http_get_orders_history.json`
- **Size**: 1,398 bytes
- **Lines**: 55
- **Language**: JSON

## Original Source

```json
{
  "retCode": 0,
  "retMsg": "OK",
  "result": {
    "list": [
      {
        "orderId": "abcdef123456",
        "orderLinkId": "client-1",
        "blockTradeId": null,
        "symbol": "BTCUSDT",
        "price": "30000",
        "qty": "0.010",
        "side": "Buy",
        "isLeverage": "1",
        "positionIdx": 0,
        "orderStatus": "Cancelled",
        "cancelType": "CancelByUser",
        "rejectReason": "",
        "avgPrice": null,
        "leavesQty": "0.010",
        "leavesValue": "300",
        "cumExecQty": "0",
        "cumExecValue": "0",
        "cumExecFee": "0",
        "timeInForce": "GTC",
        "orderType": "Limit",
        "stopOrderType": "StopLoss",
        "orderIv": null,
        "triggerPrice": "0",
        "takeProfit": "0",
        "stopLoss": "0",
        "tpTriggerBy": "MarkPrice",
        "slTriggerBy": "LastPrice",
        "triggerDirection": 0,
        "triggerBy": "MarkPrice",
        "lastPriceOnCreated": "0",
        "reduceOnly": false,
        "closeOnTrigger": false,
        "smpType": "None",
        "smpGroup": 0,
        "smpOrderId": "0",
        "tpslMode": "Full",
        "tpLimitPrice": "0",
        "slLimitPrice": "0",
        "placeType": "order",
        "createdTime": "1700000000000",
        "updatedTime": "1700000005000"
      }
    ],
    "nextPageCursor": ""
  },
  "retExtInfo": {},
  "time": 1700000006000
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 11


**Identifiers**: `BTCUSDT`, `Buy`, `CancelByUser`, `Cancelled`, `Full`, `GTC`, `LastPrice`, `Limit`, `MarkPrice`, `None`, `StopLoss`

## Related Files

This file is located in `crates/adapters/bybit/test_data/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/adapters/bybit/test_data/http_get_orders_history.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.503002Z*
