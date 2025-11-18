# Documentation: ws_instrument.json

## File Metadata

- **Path**: `crates/adapters/bitmex/test_data/ws_instrument.json`
- **Size**: 432 bytes
- **Lines**: 16
- **Language**: JSON

## Original Source

```json
{
    "symbol": "XBTUSD",
    "lastPrice": 95123.5,
    "lastTickDirection": "ZeroPlusTick",
    "markPrice": 95125.7,
    "indexPrice": 95124.3,
    "indicativeSettlePrice": 95126.0,
    "openInterest": 123456789,
    "openValue": 1234567890,
    "fairBasis": 1.4,
    "fairBasisRate": 0.00001,
    "fairPrice": 95125.0,
    "markMethod": "FairPrice",
    "indicativeTaxRate": 0.00075,
    "timestamp": "2024-11-25T12:00:00.000Z"
}
```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 3


**Identifiers**: `FairPrice`, `XBTUSD`, `ZeroPlusTick`

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
pytest crates/adapters/bitmex/test_data/ws_instrument.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.114250Z*
