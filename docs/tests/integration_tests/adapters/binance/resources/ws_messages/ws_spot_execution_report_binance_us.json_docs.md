# Documentation: ws_spot_execution_report_binance_us.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/binance/resources/ws_messages/ws_spot_execution_report_binance_us.json`
- **Size**: 773 bytes
- **Lines**: 40
- **Language**: JSON

## Original Source

```json
{
  "stream": "executionReport",
  "data": {
    "e": "executionReport",
    "E": 1759347763167,
    "s": "BTCUSD",
    "c": "T0ESHzso0banw0QiPFZYgj",
    "S": "SELL",
    "o": "LIMIT",
    "f": "GTC",
    "q": "0.00042000",
    "p": "117290.77000000",
    "P": "0.00000000",
    "F": "0.00000000",
    "g": -1,
    "C": "",
    "x": "TRADE",
    "X": "FILLED",
    "r": "NONE",
    "i": 2281896601,
    "l": "0.00042000",
    "z": "0.00042000",
    "L": "117290.77000000",
    "n": "0.00492621",
    "N": "USD",
    "T": 1759347763167,
    "t": 88685053,
    "I": 4644480641,
    "w": false,
    "m": false,
    "M": true,
    "O": 1759347763167,
    "Z": "49.26212340",
    "Y": "49.26212340",
    "Q": "0.00000000",
    "W": 1759347763167,
    "V": "EXPIRE_MAKER"
  }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 10


**Identifiers**: `BTCUSD`, `EXPIRE_MAKER`, `FILLED`, `GTC`, `LIMIT`, `NONE`, `SELL`, `T0ESHzso0banw0QiPFZYgj`, `TRADE`, `USD`

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
pytest tests/integration_tests/adapters/binance/resources/ws_messages/ws_spot_execution_report_binance_us.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.682794Z*
