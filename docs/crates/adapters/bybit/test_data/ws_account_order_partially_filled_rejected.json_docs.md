# Documentation: ws_account_order_partially_filled_rejected.json

## File Metadata

- **Path**: `crates/adapters/bybit/test_data/ws_account_order_partially_filled_rejected.json`
- **Size**: 1,380 bytes
- **Lines**: 53
- **Language**: JSON

## Original Source

```json
{
  "id": "5923240c6880ab-c59f-420b-9adb-3639adc9dd91",
  "topic": "order",
  "creationTime": 1672364262474,
  "data": [
    {
      "symbol": "APEXUSDT",
      "orderId": "5cf98598-39a7-459e-97bf-76ca765ee021",
      "side": "Buy",
      "orderType": "Limit",
      "cancelType": "UNKNOWN",
      "price": "1.500",
      "qty": "100.0",
      "orderIv": "",
      "timeInForce": "GTC",
      "orderStatus": "Rejected",
      "orderLinkId": "O-20251001-164609-APEX-000-49",
      "lastPriceOnCreated": "1.485",
      "reduceOnly": false,
      "leavesQty": "50.0",
      "leavesValue": "75.0",
      "cumExecQty": "50.0",
      "cumExecValue": "75.0",
      "avgPrice": "1.500",
      "blockTradeId": "",
      "positionIdx": 0,
      "cumExecFee": "0.0413",
      "createdTime": "1672364262444",
      "updatedTime": "1672364262457",
      "rejectReason": "UNKNOWN",
      "stopOrderType": "",
      "tpslMode": "Full",
      "triggerPrice": "",
      "takeProfit": "",
      "stopLoss": "",
      "tpTriggerBy": "",
      "slTriggerBy": "",
      "tpLimitPrice": "0",
      "slLimitPrice": "0",
      "triggerDirection": 0,
      "triggerBy": "",
      "closeOnTrigger": false,
      "category": "spot",
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


**Identifiers**: `APEX`, `APEXUSDT`, `Buy`, `CreateByUser`, `Full`, `GTC`, `Limit`, `None`, `Rejected`, `UNKNOWN`, `USDT`

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
pytest crates/adapters/bybit/test_data/ws_account_order_partially_filled_rejected.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.520460Z*
