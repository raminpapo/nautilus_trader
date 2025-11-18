# Documentation: ws_futures_order_update_settlement.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/binance/resources/ws_messages/ws_futures_order_update_settlement.json`
- **Size**: 899 bytes
- **Lines**: 47
- **Language**: JSON

## Original Source

```json
{
  "stream": "ORDER_TRADE_UPDATE",
  "data": {
    "e": "ORDER_TRADE_UPDATE",
    "E": 1759347763300,
    "T": 1759347763300,
    "o": {
      "s": "BTCUSDT",
      "c": "settlement_autoclose-1111222233334444",
      "S": "BUY",
      "o": "MARKET",
      "f": "GTC",
      "q": "0.050",
      "p": "0",
      "ap": "51000.00",
      "sp": null,
      "x": "CALCULATED",
      "X": "FILLED",
      "i": 6543210987,
      "l": "0.050",
      "z": "0.050",
      "L": "51000.00",
      "N": "USDT",
      "n": "2.55000000",
      "T": 1759347763300,
      "t": 4455667788,
      "b": "0",
      "a": "0",
      "m": false,
      "R": false,
      "wt": "CONTRACT_PRICE",
      "ot": "MARKET",
      "ps": "SHORT",
      "cp": false,
      "AP": null,
      "cr": null,
      "pP": false,
      "si": 0,
      "ss": 0,
      "rp": "25.00",
      "gtd": 0,
      "W": null,
      "V": null
    }
  }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 10


**Identifiers**: `BTCUSDT`, `BUY`, `CALCULATED`, `CONTRACT_PRICE`, `FILLED`, `GTC`, `MARKET`, `ORDER_TRADE_UPDATE`, `SHORT`, `USDT`

## Related Files

This file is located in `tests/integration_tests/adapters/binance/resources/ws_messages/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/binance/resources/ws_messages/ws_futures_order_update_settlement.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.677136Z*
