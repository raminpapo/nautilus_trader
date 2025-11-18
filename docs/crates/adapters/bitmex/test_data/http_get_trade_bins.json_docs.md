# Documentation: http_get_trade_bins.json

## File Metadata

- **Path**: `crates/adapters/bitmex/test_data/http_get_trade_bins.json`
- **Size**: 1,169 bytes
- **Lines**: 47
- **Language**: JSON

## Original Source

```json
[
    {
        "timestamp": "2024-11-25T10:30:00.000Z",
        "symbol": "XBTUSD",
        "open": 98900.0,
        "high": 98980.5,
        "low": 98890.0,
        "close": 98950.0,
        "trades": 45,
        "volume": 150000,
        "vwap": 98932.5,
        "lastSize": 100,
        "turnover": 152047500,
        "homeNotional": 1.52047500,
        "foreignNotional": 150000.0
    },
    {
        "timestamp": "2024-11-25T10:31:00.000Z",
        "symbol": "XBTUSD",
        "open": 98950.0,
        "high": 98965.0,
        "low": 98940.0,
        "close": 98960.0,
        "trades": 32,
        "volume": 95000,
        "vwap": 98952.3,
        "lastSize": 200,
        "turnover": 96005185,
        "homeNotional": 0.96005185,
        "foreignNotional": 95000.0
    },
    {
        "timestamp": "2024-11-25T10:32:00.000Z",
        "symbol": "XBTUSD",
        "open": 98960.0,
        "high": 98975.0,
        "low": 98955.0,
        "close": 98970.0,
        "trades": 28,
        "volume": 78000,
        "vwap": 98963.8,
        "lastSize": 150,
        "turnover": 78805164,
        "homeNotional": 0.78805164,
        "foreignNotional": 78000.0
    }
]
```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 1


**Identifiers**: `XBTUSD`

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
pytest crates/adapters/bitmex/test_data/http_get_trade_bins.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.107551Z*
