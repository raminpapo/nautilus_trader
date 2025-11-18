# Documentation: v4_candles_channel_data.json

## File Metadata

- **Path**: `tests/test_data/dydx/websocket/v4_candles_channel_data.json`
- **Size**: 566 bytes
- **Lines**: 22
- **Language**: JSON

## Original Source

```json
{
    "channel": "v4_candles",
    "connection_id": "8c25ab80-2124-4f60-82bf-9040cabc03af",
    "contents": {
        "baseTokenVolume": "6.364",
        "close": "3247.6",
        "high": "3247.6",
        "low": "3246.5",
        "open": "3246.5",
        "resolution": "1MIN",
        "startedAt": "2024-07-26T17:54:00.000Z",
        "startingOpenInterest": "16119.209",
        "ticker": "ETH-USD",
        "trades": 10,
        "usdVolume": "20663.2167"
    },
    "id": "ETH-USD/1MIN",
    "message_id": 3,
    "type": "channel_data",
    "version": "1.0.0"
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 2


**Identifiers**: `ETH`, `USD`

## Related Files

This file is located in `tests/test_data/dydx/websocket/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/test_data/dydx/websocket/v4_candles_channel_data.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:08.501133Z*
