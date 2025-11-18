# Documentation: ws_account_order_filled.json

## File Metadata

- **Path**: `crates/adapters/bybit/test_data/ws_account_order_filled.json`
- **Size**: 1,428 bytes
- **Lines**: 53
- **Language**: JSON

## Original Source

```json
{
  "id": "5923240c6880ab-c59f-420b-9adb-3639adc9dd90",
  "topic": "order",
  "creationTime": 1672364262474,
  "data": [
    {
      "symbol": "BTCUSDT",
      "orderId": "5cf98598-39a7-459e-97bf-76ca765ee020",
      "side": "Buy",
      "orderType": "Limit",
      "cancelType": "UNKNOWN",
      "price": "30000.50",
      "qty": "0.100",
      "orderIv": "",
      "timeInForce": "GTC",
      "orderStatus": "Filled",
      "orderLinkId": "test-client-order-001",
      "lastPriceOnCreated": "29950.00",
      "reduceOnly": false,
      "leavesQty": "0",
      "leavesValue": "0",
      "cumExecQty": "0.100",
      "cumExecValue": "3000.05",
      "avgPrice": "30000.50",
      "blockTradeId": "",
      "positionIdx": 0,
      "cumExecFee": "1.650028",
      "createdTime": "1672364262444",
      "updatedTime": "1672364262457",
      "rejectReason": "",
      "stopOrderType": "Stop",
      "tpslMode": "Full",
      "triggerPrice": "29500.00",
      "takeProfit": "31000.00",
      "stopLoss": "29000.00",
      "tpTriggerBy": "MarkPrice",
      "slTriggerBy": "LastPrice",
      "tpLimitPrice": "0",
      "slLimitPrice": "0",
      "triggerDirection": 0,
      "triggerBy": "MarkPrice",
      "closeOnTrigger": false,
      "category": "linear",
      "placeType": "order",
      "smpType": "None",
      "smpGroup": 0,
      "smpOrderId": "",
      "feeCurrency": "USDT",
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


**Identifiers**: `BTCUSDT`, `Buy`, `CreateByUser`, `Filled`, `Full`, `GTC`, `LastPrice`, `Limit`, `MarkPrice`, `None`, `Stop`, `UNKNOWN`, `USDT`

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
pytest crates/adapters/bybit/test_data/ws_account_order_filled.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.516946Z*
