# Documentation: ws_futures_order_update_liquidation_zero_qty.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/binance/resources/ws_messages/ws_futures_order_update_liquidation_zero_qty.json`
- **Size**: 869 bytes
- **Lines**: 47
- **Language**: JSON

## Original Source

```json
{
  "stream": "ORDER_TRADE_UPDATE",
  "data": {
    "e": "ORDER_TRADE_UPDATE",
    "E": 1759347763250,
    "T": 1759347763250,
    "o": {
      "s": "BTCUSDT",
      "c": "autoclose-7654321098765432",
      "S": "SELL",
      "o": "MARKET",
      "f": "GTC",
      "q": "0.000",
      "p": "0",
      "ap": "0.00",
      "sp": null,
      "x": "CALCULATED",
      "X": "FILLED",
      "i": 7654321098,
      "l": "0.000",
      "z": "0.000",
      "L": "0.00",
      "N": null,
      "n": null,
      "T": 1759347763250,
      "t": 3344556677,
      "b": "0",
      "a": "0",
      "m": false,
      "R": false,
      "wt": "CONTRACT_PRICE",
      "ot": "MARKET",
      "ps": "LONG",
      "cp": false,
      "AP": null,
      "cr": null,
      "pP": false,
      "si": 0,
      "ss": 0,
      "rp": "0.00",
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

Total unique keywords extracted: 9


**Identifiers**: `BTCUSDT`, `CALCULATED`, `CONTRACT_PRICE`, `FILLED`, `GTC`, `LONG`, `MARKET`, `ORDER_TRADE_UPDATE`, `SELL`

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
pytest tests/integration_tests/adapters/binance/resources/ws_messages/ws_futures_order_update_liquidation_zero_qty.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.671557Z*
