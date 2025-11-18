# Documentation: ws_account_order.json

## File Metadata

- **Path**: `crates/adapters/bybit/test_data/ws_account_order.json`
- **Size**: 1,351 bytes
- **Lines**: 53
- **Language**: JSON

## Original Source

```json
{
  "topic": "order",
  "id": "9b8d7cf0-1234-4567-8abc-00d0beef0001",
  "creationTime": 1700000007000,
  "data": [
    {
      "category": "linear",
      "symbol": "BTCUSDT",
      "orderId": "abcdef123456",
      "side": "Buy",
      "orderType": "Limit",
      "cancelType": "CancelByUser",
      "price": "30000",
      "qty": "0.010",
      "orderIv": "0",
      "timeInForce": "GTC",
      "orderStatus": "Cancelled",
      "orderLinkId": "client-1",
      "lastPriceOnCreated": "0",
      "reduceOnly": false,
      "leavesQty": "0.010",
      "leavesValue": "300",
      "cumExecQty": "0",
      "cumExecValue": "0",
      "avgPrice": "0",
      "blockTradeId": "0",
      "positionIdx": 0,
      "cumExecFee": "0",
      "createdTime": "1700000000000",
      "updatedTime": "1700000005000",
      "rejectReason": "",
      "triggerPrice": "0",
      "takeProfit": "0",
      "stopLoss": "0",
      "tpTriggerBy": "MarkPrice",
      "slTriggerBy": "LastPrice",
      "tpLimitPrice": "0",
      "slLimitPrice": "0",
      "closeOnTrigger": false,
      "placeType": "order",
      "smpType": "None",
      "smpGroup": 0,
      "smpOrderId": "0",
      "feeCurrency": "USDT",
      "triggerBy": "MarkPrice",
      "stopOrderType": "StopLoss",
      "triggerDirection": 0,
      "tpslMode": "Full",
      "createType": "CreateByUser"
    }
  ]
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 13


**Identifiers**: `BTCUSDT`, `Buy`, `CancelByUser`, `Cancelled`, `CreateByUser`, `Full`, `GTC`, `LastPrice`, `Limit`, `MarkPrice`, `None`, `StopLoss`, `USDT`

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
pytest crates/adapters/bybit/test_data/ws_account_order.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.513780Z*
