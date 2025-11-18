# Documentation: ws_spot_execution_report_trade.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/binance/resources/ws_messages/ws_spot_execution_report_trade.json`
- **Size**: 729 bytes
- **Lines**: 38
- **Language**: JSON

## Original Source

```json
{
  "stream": "executionReport",
  "data": {
    "e": "executionReport",
    "E": 1759347763167,
    "s": "ETHUSDT",
    "c": "O-12345-test-trade",
    "S": "BUY",
    "o": "LIMIT",
    "f": "GTC",
    "q": "1.00000000",
    "p": "2500.00000000",
    "P": "0.00000000",
    "F": "0.00000000",
    "g": -1,
    "C": "",
    "x": "TRADE",
    "X": "PARTIALLY_FILLED",
    "r": "NONE",
    "i": 1234567890,
    "l": "0.50000000",
    "z": "0.50000000",
    "L": "2499.50000000",
    "n": "0.00050000",
    "N": "ETH",
    "T": 1759347763167,
    "t": 98765432,
    "I": 4644480641,
    "w": true,
    "m": true,
    "M": false,
    "O": 1759347763100,
    "Z": "1249.75000000",
    "Y": "1249.75000000",
    "Q": "0.00000000"
  }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 8


**Identifiers**: `BUY`, `ETH`, `ETHUSDT`, `GTC`, `LIMIT`, `NONE`, `PARTIALLY_FILLED`, `TRADE`

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
pytest tests/integration_tests/adapters/binance/resources/ws_messages/ws_spot_execution_report_trade.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.699784Z*
