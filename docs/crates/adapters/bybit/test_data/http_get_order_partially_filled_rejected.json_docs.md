# Documentation: http_get_order_partially_filled_rejected.json

## File Metadata

- **Path**: `crates/adapters/bybit/test_data/http_get_order_partially_filled_rejected.json`
- **Size**: 1,439 bytes
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
        "orderId": "5cf98598-39a7-459e-97bf-76ca765ee021",
        "orderLinkId": "O-20251001-164609-APEX-000-49",
        "blockTradeId": null,
        "symbol": "BTCUSDT",
        "price": "30000",
        "qty": "0.010",
        "side": "Buy",
        "isLeverage": "0",
        "positionIdx": 0,
        "orderStatus": "Rejected",
        "cancelType": "UNKNOWN",
        "rejectReason": "INSUFFICIENT_MARGIN",
        "avgPrice": "30000",
        "leavesQty": "0.005",
        "leavesValue": "150",
        "cumExecQty": "0.005",
        "cumExecValue": "150",
        "cumExecFee": "0.0825",
        "timeInForce": "GTC",
        "orderType": "Limit",
        "stopOrderType": "",
        "orderIv": null,
        "triggerPrice": "0",
        "takeProfit": "0",
        "stopLoss": "0",
        "tpTriggerBy": "",
        "slTriggerBy": "",
        "triggerDirection": 0,
        "triggerBy": "",
        "lastPriceOnCreated": "29950",
        "reduceOnly": false,
        "closeOnTrigger": false,
        "smpType": "None",
        "smpGroup": 0,
        "smpOrderId": "0",
        "tpslMode": "Full",
        "tpLimitPrice": "0",
        "slLimitPrice": "0",
        "placeType": "order",
        "createdTime": "1672364262444",
        "updatedTime": "1672364262457"
      }
    ],
    "nextPageCursor": ""
  },
  "retExtInfo": {},
  "time": 1672364262500
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 10


**Identifiers**: `APEX`, `BTCUSDT`, `Buy`, `Full`, `GTC`, `INSUFFICIENT_MARGIN`, `Limit`, `None`, `Rejected`, `UNKNOWN`

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
pytest crates/adapters/bybit/test_data/http_get_order_partially_filled_rejected.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.501854Z*
