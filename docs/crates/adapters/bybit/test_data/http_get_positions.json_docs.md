# Documentation: http_get_positions.json

## File Metadata

- **Path**: `crates/adapters/bybit/test_data/http_get_positions.json`
- **Size**: 3,166 bytes
- **Lines**: 115
- **Language**: JSON

## Original Source

```json
{
  "retCode": 0,
  "retMsg": "OK",
  "result": {
    "list": [
      {
        "positionIdx": 0,
        "riskId": 1,
        "riskLimitValue": "150",
        "symbol": "BTCUSDT",
        "side": "Buy",
        "size": "0.5",
        "avgPrice": "50000.00",
        "positionValue": "25000",
        "tradeMode": 0,
        "positionStatus": "Normal",
        "autoAddMargin": 1,
        "adlRankIndicator": 2,
        "leverage": "10",
        "positionBalance": "2500.00",
        "markPrice": "50500.00",
        "liqPrice": "45000.00",
        "bustPrice": "44500.00",
        "positionMM": "250.00",
        "positionIM": "2500.00",
        "tpslMode": "Full",
        "takeProfit": "55000.00",
        "stopLoss": "48000.00",
        "trailingStop": "0.00",
        "unrealisedPnl": "250.00",
        "curRealisedPnl": "100.00",
        "cumRealisedPnl": "500.00",
        "seq": 5723621632,
        "isReduceOnly": false,
        "mmrSysUpdatedTime": "",
        "leverageSysUpdatedTime": "",
        "createdTime": "1676538056258",
        "updatedTime": "1697673600012"
      },
      {
        "positionIdx": 0,
        "riskId": 1,
        "riskLimitValue": "100",
        "symbol": "ETHUSDT",
        "side": "Sell",
        "size": "5.0",
        "avgPrice": "3000.00",
        "positionValue": "15000",
        "tradeMode": 0,
        "positionStatus": "Normal",
        "autoAddMargin": 0,
        "adlRankIndicator": 3,
        "leverage": "5",
        "positionBalance": "3000.00",
        "markPrice": "2950.00",
        "liqPrice": "3500.00",
        "bustPrice": "3550.00",
        "positionMM": "300.00",
        "positionIM": "3000.00",
        "tpslMode": "Full",
        "takeProfit": "2800.00",
        "stopLoss": "3100.00",
        "trailingStop": "0.00",
        "unrealisedPnl": "250.00",
        "curRealisedPnl": "-50.00",
        "cumRealisedPnl": "200.00",
        "seq": 5723621633,
        "isReduceOnly": false,
        "mmrSysUpdatedTime": "",
        "leverageSysUpdatedTime": "",
        "createdTime": "1676538156358",
        "updatedTime": "1697673700112"
      },
      {
        "positionIdx": 0,
        "riskId": 1,
        "riskLimitValue": "50",
        "symbol": "SOLUSDT",
        "side": "",
        "size": "0",
        "avgPrice": "0",
        "positionValue": "0",
        "tradeMode": 0,
        "positionStatus": "Normal",
        "autoAddMargin": 1,
        "adlRankIndicator": 0,
        "leverage": "10",
        "positionBalance": "0",
        "markPrice": "150.00",
        "liqPrice": "",
        "bustPrice": "",
        "positionMM": "0",
        "positionIM": "0",
        "tpslMode": "Full",
        "takeProfit": "0.00",
        "stopLoss": "0.00",
        "trailingStop": "0.00",
        "unrealisedPnl": "0",
        "curRealisedPnl": "0",
        "cumRealisedPnl": "0",
        "seq": 5723621634,
        "isReduceOnly": false,
        "mmrSysUpdatedTime": "",
        "leverageSysUpdatedTime": "",
        "createdTime": "1676538256458",
        "updatedTime": "1697673800212"
      }
    ],
    "nextPageCursor": "",
    "category": "linear"
  },
  "retExtInfo": {},
  "time": 1697673900000
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 7


**Identifiers**: `BTCUSDT`, `Buy`, `ETHUSDT`, `Full`, `Normal`, `SOLUSDT`, `Sell`

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
pytest crates/adapters/bybit/test_data/http_get_positions.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.507236Z*
