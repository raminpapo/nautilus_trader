# Documentation: http_get_orders_history_with_duplicate.json

## File Metadata

- **Path**: `crates/adapters/bybit/test_data/http_get_orders_history_with_duplicate.json`
- **Size**: 2,650 bytes
- **Lines**: 98
- **Language**: JSON

## Original Source

```json
{
  "retCode": 0,
  "retMsg": "OK",
  "result": {
    "list": [
      {
        "orderId": "open-order-1",
        "orderLinkId": "client-open-1",
        "blockTradeId": null,
        "symbol": "ETHUSDT",
        "price": "3930.41",
        "qty": "0.010",
        "side": "Buy",
        "isLeverage": "0",
        "positionIdx": 0,
        "orderStatus": "New",
        "cancelType": "",
        "rejectReason": "",
        "avgPrice": null,
        "leavesQty": "0.010",
        "leavesValue": "39.3041",
        "cumExecQty": "0",
        "cumExecValue": "0",
        "cumExecFee": "0",
        "timeInForce": "GTC",
        "orderType": "Limit",
        "stopOrderType": "",
        "orderIv": null,
        "triggerPrice": "0",
        "takeProfit": "0",
        "stopLoss": "0",
        "tpTriggerBy": "LastPrice",
        "slTriggerBy": "LastPrice",
        "triggerDirection": 0,
        "triggerBy": "LastPrice",
        "lastPriceOnCreated": "3936.41",
        "reduceOnly": false,
        "closeOnTrigger": false,
        "smpType": "None",
        "smpGroup": 0,
        "smpOrderId": "0",
        "tpslMode": "Full",
        "tpLimitPrice": "0",
        "slLimitPrice": "0",
        "placeType": "order",
        "createdTime": "1761355905606",
        "updatedTime": "1761355905606"
      },
      {
        "orderId": "closed-order-1",
        "orderLinkId": "client-closed-1",
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
  "time": 1761355905611
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 13


**Identifiers**: `BTCUSDT`, `Buy`, `CancelByUser`, `Cancelled`, `ETHUSDT`, `Full`, `GTC`, `LastPrice`, `Limit`, `MarkPrice`, `New`, `None`, `StopLoss`

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
pytest crates/adapters/bybit/test_data/http_get_orders_history_with_duplicate.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.504549Z*
