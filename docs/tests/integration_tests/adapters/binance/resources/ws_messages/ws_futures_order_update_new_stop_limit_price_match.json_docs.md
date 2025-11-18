# Documentation: ws_futures_order_update_new_stop_limit_price_match.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/binance/resources/ws_messages/ws_futures_order_update_new_stop_limit_price_match.json`
- **Size**: 876 bytes
- **Lines**: 47
- **Language**: JSON

## Original Source

```json
{
  "stream": "ORDER_TRADE_UPDATE",
  "data": {
    "e": "ORDER_TRADE_UPDATE",
    "E": 1759347763200,
    "T": 1759347763200,
    "o": {
      "s": "ETHUSDT",
      "c": "O-12345-test-stop-limit-price-match",
      "S": "SELL",
      "o": "STOP",
      "f": "GTC",
      "q": "1.000",
      "p": "2405.75",
      "ap": "0.00",
      "sp": "2400.00",
      "x": "NEW",
      "X": "NEW",
      "i": 8765432101,
      "l": "0.000",
      "z": "0.000",
      "L": "0.00",
      "N": null,
      "n": null,
      "T": 1759347763200,
      "t": 0,
      "b": "0",
      "a": "0",
      "m": false,
      "R": false,
      "wt": "CONTRACT_PRICE",
      "ot": "STOP",
      "ps": "SHORT",
      "cp": false,
      "AP": null,
      "cr": null,
      "pP": false,
      "si": 0,
      "ss": 0,
      "rp": "0.00",
      "gtd": 0,
      "W": 1759347763200,
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

Total unique keywords extracted: 8


**Identifiers**: `CONTRACT_PRICE`, `ETHUSDT`, `GTC`, `NEW`, `ORDER_TRADE_UPDATE`, `SELL`, `SHORT`, `STOP`

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
pytest tests/integration_tests/adapters/binance/resources/ws_messages/ws_futures_order_update_new_stop_limit_price_match.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.675789Z*
