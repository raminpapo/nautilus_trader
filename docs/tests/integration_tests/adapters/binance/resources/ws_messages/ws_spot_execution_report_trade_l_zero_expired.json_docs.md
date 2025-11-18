# Documentation: ws_spot_execution_report_trade_l_zero_expired.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/binance/resources/ws_messages/ws_spot_execution_report_trade_l_zero_expired.json`
- **Size**: 707 bytes
- **Lines**: 38
- **Language**: JSON

## Original Source

```json
{
  "stream": "executionReport",
  "data": {
    "e": "executionReport",
    "E": 1759347763167,
    "s": "BTCUSDT",
    "c": "O-12345-test-l-zero-expired",
    "S": "BUY",
    "o": "LIMIT",
    "f": "GTD",
    "q": "0.01000000",
    "p": "50000.00000000",
    "P": "0.00000000",
    "F": "0.00000000",
    "g": -1,
    "C": "",
    "x": "TRADE",
    "X": "EXPIRED",
    "r": "NONE",
    "i": 1234567891,
    "l": "0.00000000",
    "z": "0.00000000",
    "L": "0.00000000",
    "n": "0",
    "N": null,
    "T": 1759347763167,
    "t": -1,
    "I": 4644480641,
    "w": false,
    "m": false,
    "M": false,
    "O": 1759347763000,
    "Z": "0.00000000",
    "Y": "0.00000000",
    "Q": "0.00000000"
  }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 7


**Identifiers**: `BTCUSDT`, `BUY`, `EXPIRED`, `GTD`, `LIMIT`, `NONE`, `TRADE`

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
pytest tests/integration_tests/adapters/binance/resources/ws_messages/ws_spot_execution_report_trade_l_zero_expired.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.704095Z*
