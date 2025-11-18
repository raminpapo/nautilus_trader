# Documentation: ws_account_order_sell_market_if_touched.json

## File Metadata

- **Path**: `crates/adapters/bybit/test_data/ws_account_order_sell_market_if_touched.json`
- **Size**: 1,356 bytes
- **Lines**: 53
- **Language**: JSON

## Original Source

```json
{
  "id": "5923240c6880ab-c59f-420b-9adb-3639adc9dd95",
  "topic": "order",
  "creationTime": 1672364262474,
  "data": [
    {
      "symbol": "BTCUSDT",
      "orderId": "test-sell-mit-001",
      "side": "Sell",
      "orderType": "Market",
      "cancelType": "UNKNOWN",
      "price": "",
      "qty": "0.100",
      "orderIv": "",
      "timeInForce": "GTC",
      "orderStatus": "Untriggered",
      "orderLinkId": "test-client-sell-mit-001",
      "lastPriceOnCreated": "50000.00",
      "reduceOnly": false,
      "leavesQty": "0.100",
      "leavesValue": "5500.00",
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
      "triggerPrice": "55000.00",
      "takeProfit": "",
      "stopLoss": "",
      "tpTriggerBy": "",
      "slTriggerBy": "",
      "tpLimitPrice": "",
      "slLimitPrice": "",
      "triggerDirection": 1,
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


**Identifiers**: `BTCUSDT`, `CreateByUser`, `GTC`, `LastPrice`, `Market`, `None`, `Sell`, `Stop`, `UNKNOWN`, `USDT`, `Untriggered`

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
pytest crates/adapters/bybit/test_data/ws_account_order_sell_market_if_touched.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.521537Z*
