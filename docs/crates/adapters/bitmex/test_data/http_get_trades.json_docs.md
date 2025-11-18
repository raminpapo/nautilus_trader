# Documentation: http_get_trades.json

## File Metadata

- **Path**: `crates/adapters/bitmex/test_data/http_get_trades.json`
- **Size**: 1,165 bytes
- **Lines**: 41
- **Language**: JSON

## Original Source

```json
[
    {
        "timestamp": "2024-11-25T10:35:00.789Z",
        "symbol": "XBTUSD",
        "side": "Buy",
        "size": 100,
        "price": 98950.0,
        "tickDirection": "PlusTick",
        "trdMatchID": "00000000-006d-1000-0000-000e8737d540",
        "grossValue": 101065,
        "homeNotional": 0.00101065,
        "foreignNotional": 100.0,
        "trdType": "Regular"
    },
    {
        "timestamp": "2024-11-25T10:35:01.123Z",
        "symbol": "XBTUSD",
        "side": "Buy",
        "size": 100,
        "price": 98951.0,
        "tickDirection": "PlusTick",
        "trdMatchID": "00000000-006d-1000-0000-000e8737d541",
        "grossValue": 101055,
        "homeNotional": 0.00101055,
        "foreignNotional": 100.0,
        "trdType": "Regular"
    },
    {
        "timestamp": "2024-11-25T10:34:45.234Z",
        "symbol": "XBTUSD",
        "side": "Sell",
        "size": 50,
        "price": 98949.5,
        "tickDirection": "MinusTick",
        "trdMatchID": "00000000-006d-1000-0000-000e8737d539",
        "grossValue": 50535,
        "homeNotional": 0.00050535,
        "foreignNotional": 50.0,
        "trdType": "Regular"
    }
]
```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 6


**Identifiers**: `Buy`, `MinusTick`, `PlusTick`, `Regular`, `Sell`, `XBTUSD`

## Related Files

This file is located in `crates/adapters/bitmex/test_data/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/adapters/bitmex/test_data/http_get_trades.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.108646Z*
