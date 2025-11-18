# Documentation: ws_spot_execution_report_calculated.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/binance/resources/ws_messages/ws_spot_execution_report_calculated.json`
- **Size**: 724 bytes
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
    "c": "autoclose-123456789",
    "S": "SELL",
    "o": "LIMIT",
    "f": "GTC",
    "q": "0.01000000",
    "p": "50000.00000000",
    "P": "0.00000000",
    "F": "0.00000000",
    "g": -1,
    "C": "",
    "x": "CALCULATED",
    "X": "FILLED",
    "r": "NONE",
    "i": 1234567890,
    "l": "0.01000000",
    "z": "0.01000000",
    "L": "49500.00000000",
    "n": "2.475",
    "N": "USDT",
    "T": 1759347763167,
    "t": 98765432,
    "I": 4644480641,
    "w": false,
    "m": false,
    "M": false,
    "O": 1759347763000,
    "Z": "495.00000000",
    "Y": "495.00000000",
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


**Identifiers**: `BTCUSDT`, `CALCULATED`, `FILLED`, `GTC`, `LIMIT`, `NONE`, `SELL`, `USDT`

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
pytest tests/integration_tests/adapters/binance/resources/ws_messages/ws_spot_execution_report_calculated.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.684452Z*
