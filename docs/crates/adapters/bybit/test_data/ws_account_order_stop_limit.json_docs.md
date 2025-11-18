# Documentation: ws_account_order_stop_limit.json

## File Metadata

- **Path**: `crates/adapters/bybit/test_data/ws_account_order_stop_limit.json`
- **Size**: 1,367 bytes
- **Lines**: 53
- **Language**: JSON

## Original Source

```json
{
  "id": "5923240c6880ab-c59f-420b-9adb-3639adc9dd92",
  "topic": "order",
  "creationTime": 1672364262474,
  "data": [
    {
      "symbol": "BTCUSDT",
      "orderId": "test-stop-limit-001",
      "side": "Sell",
      "orderType": "Limit",
      "cancelType": "UNKNOWN",
      "price": "44500.00",
      "qty": "0.100",
      "orderIv": "",
      "timeInForce": "GTC",
      "orderStatus": "Untriggered",
      "orderLinkId": "test-client-stop-limit-001",
      "lastPriceOnCreated": "50000.00",
      "reduceOnly": false,
      "leavesQty": "0.100",
      "leavesValue": "4450.00",
      "cumExecQty": "0",
      "cumExecValue": "0",
      "avgPrice": "",
      "blockTradeId": "",
      "positionIdx": 0,
      "cumExecFee": "0",
      "createdTime": "1672364262444",
      "updatedTime": "1672364262457",
      "rejectReason": "",
      "stopOrderType": "Stop",
      "tpslMode": "",
      "triggerPrice": "45000.00",
      "takeProfit": "",
      "stopLoss": "",
      "tpTriggerBy": "",
      "slTriggerBy": "",
      "tpLimitPrice": "",
      "slLimitPrice": "",
      "triggerDirection": 2,
      "triggerBy": "LastPrice",
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

Total unique keywords extracted: 11


**Identifiers**: `BTCUSDT`, `CreateByUser`, `GTC`, `LastPrice`, `Limit`, `None`, `Sell`, `Stop`, `UNKNOWN`, `USDT`, `Untriggered`

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
pytest crates/adapters/bybit/test_data/ws_account_order_stop_limit.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.522758Z*
