# Documentation: ws_funding_rate.json

## File Metadata

- **Path**: `crates/adapters/okx/test_data/ws_funding_rate.json`
- **Size**: 275 bytes
- **Lines**: 17
- **Language**: JSON

## Original Source

```json
{
  "arg": {
    "channel": "funding-rate",
    "instId": "BTC-USDT-SWAP"
  },
  "data": [
    {
      "instId": "BTC-USDT-SWAP",
      "fundingRate": "0.0001",
      "nextFundingRate": "0.0002",
      "fundingTime": "1744590349506",
      "ts": "1744590349506"
    }
  ]
}


```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 3


**Identifiers**: `BTC`, `SWAP`, `USDT`

## Related Files

This file is located in `crates/adapters/okx/test_data/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/adapters/okx/test_data/ws_funding_rate.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:00.577500Z*
