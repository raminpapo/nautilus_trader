# Documentation: http_get_executions.json

## File Metadata

- **Path**: `crates/adapters/bybit/test_data/http_get_executions.json`
- **Size**: 2,029 bytes
- **Lines**: 73
- **Language**: JSON

## Original Source

```json
{
  "retCode": 0,
  "retMsg": "OK",
  "result": {
    "nextPageCursor": "132766%3A2%2C132766%3A2",
    "category": "linear",
    "list": [
      {
        "symbol": "BTCUSDT",
        "orderId": "8c065341-7b52-4ca9-ac2c-37e31ac55c94",
        "orderLinkId": "test-order-001",
        "side": "Buy",
        "orderPrice": "50000.00",
        "orderQty": "0.100",
        "leavesQty": "0.000",
        "createType": "CreateByUser",
        "orderType": "Limit",
        "stopOrderType": "",
        "execFee": "0.0150",
        "execId": "e0cbe81d-0f18-5866-9415-cf319b5dab3b",
        "execPrice": "50000.00",
        "execQty": "0.100",
        "execType": "Trade",
        "execValue": "5000.00",
        "execTime": "1672282722429",
        "feeCurrency": "USDT",
        "isMaker": true,
        "feeRate": "0.0003",
        "tradeIv": "",
        "markIv": "",
        "markPrice": "50010.50",
        "indexPrice": "50005.25",
        "underlyingPrice": "",
        "blockTradeId": "",
        "closedSize": "0.000",
        "seq": 4688002127
      },
      {
        "symbol": "ETHUSDT",
        "orderId": "7b954230-6a41-3ba8-bc20-26d20ab44b83",
        "orderLinkId": "test-order-002",
        "side": "Sell",
        "orderPrice": "3000.00",
        "orderQty": "1.000",
        "leavesQty": "0.500",
        "createType": "CreateByUser",
        "orderType": "Limit",
        "stopOrderType": "",
        "execFee": "0.9000",
        "execId": "f1dce92e-1g29-6977-a526-dg420c6ecb4c",
        "execPrice": "3000.00",
        "execQty": "0.500",
        "execType": "Trade",
        "execValue": "1500.00",
        "execTime": "1672282822529",
        "feeCurrency": "USDT",
        "isMaker": false,
        "feeRate": "0.0006",
        "tradeIv": "",
        "markIv": "",
        "markPrice": "2998.75",
        "indexPrice": "2999.50",
        "underlyingPrice": "",
        "blockTradeId": "",
        "closedSize": "0.000",
        "seq": 4688002128
      }
    ]
  },
  "retExtInfo": {},
  "time": 1672283754510
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 8


**Identifiers**: `BTCUSDT`, `Buy`, `CreateByUser`, `ETHUSDT`, `Limit`, `Sell`, `Trade`, `USDT`

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
pytest crates/adapters/bybit/test_data/http_get_executions.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.493324Z*
