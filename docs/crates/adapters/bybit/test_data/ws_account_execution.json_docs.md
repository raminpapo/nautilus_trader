# Documentation: ws_account_execution.json

## File Metadata

- **Path**: `crates/adapters/bybit/test_data/ws_account_execution.json`
- **Size**: 973 bytes
- **Lines**: 38
- **Language**: JSON

## Original Source

```json
{
  "topic": "execution",
  "id": "386825804_BTCUSDT_140612148849382",
  "creationTime": 1746270400355,
  "data": [
    {
      "category": "linear",
      "symbol": "BTCUSDT",
      "closedSize": "0.5",
      "execFee": "26.3725275",
      "execId": "0ab1bdf7-4219-438b-b30a-32ec863018f7",
      "execPrice": "95900.1",
      "execQty": "0.5",
      "execType": "Trade",
      "execValue": "47950.05",
      "feeRate": "0.00055",
      "tradeIv": "",
      "markIv": "",
      "blockTradeId": "",
      "markPrice": "95901.48",
      "indexPrice": "",
      "underlyingPrice": "",
      "leavesQty": "0",
      "orderId": "9aac161b-8ed6-450d-9cab-c5cc67c21784",
      "orderLinkId": "test-order-link-001",
      "orderPrice": "94942.5",
      "orderQty": "0.5",
      "orderType": "Market",
      "stopOrderType": "UNKNOWN",
      "side": "Sell",
      "execTime": "1746270400353",
      "isLeverage": "0",
      "isMaker": false,
      "seq": 140612148849382
    }
  ]
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 5


**Identifiers**: `BTCUSDT`, `Market`, `Sell`, `Trade`, `UNKNOWN`

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
pytest crates/adapters/bybit/test_data/ws_account_execution.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.512305Z*
