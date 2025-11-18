# Documentation: ws_account_position.json

## File Metadata

- **Path**: `crates/adapters/bybit/test_data/ws_account_position.json`
- **Size**: 1,227 bytes
- **Lines**: 46
- **Language**: JSON

## Original Source

```json
{
  "id": "1003076014fb7eedb-c7e6-45d6-a8c1-270f0169171a",
  "topic": "position",
  "creationTime": 1762199126022,
  "data": [
    {
      "positionIdx": 0,
      "tradeMode": 0,
      "riskId": 11,
      "riskLimitValue": "900000",
      "symbol": "ETHUSDT",
      "side": "Sell",
      "size": "0.01",
      "entryPrice": "3641.075",
      "sessionAvgPrice": "",
      "leverage": "30",
      "positionValue": "36.42075",
      "positionBalance": "0",
      "markPrice": "3641.33",
      "positionIM": "1.23480936",
      "positionMM": "0.20281586",
      "positionIMByMp": "1.23480936",
      "positionMMByMp": "0.20281586",
      "takeProfit": "0",
      "stopLoss": "0",
      "trailingStop": "0",
      "unrealisedPnl": "-0.00255",
      "cumRealisedPnl": "-25.06579337",
      "curRealisedPnl": "0.0094814",
      "createdTime": "1730805600084",
      "updatedTime": "1762199125472",
      "tpslMode": "Full",
      "liqPrice": "51764.83003276",
      "bustPrice": "",
      "category": "linear",
      "positionStatus": "Normal",
      "adlRankIndicator": 2,
      "autoAddMargin": 0,
      "leverageSysUpdatedTime": "",
      "mmrSysUpdatedTime": "",
      "seq": 325852190774,
      "isReduceOnly": false
    }
  ]
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 4


**Identifiers**: `ETHUSDT`, `Full`, `Normal`, `Sell`

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
pytest crates/adapters/bybit/test_data/ws_account_position.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.525430Z*
