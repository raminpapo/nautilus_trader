# Documentation: http_get_position_tiers.json

## File Metadata

- **Path**: `crates/adapters/okx/test_data/http_get_position_tiers.json`
- **Size**: 339 bytes
- **Lines**: 21
- **Language**: JSON

## Original Source

```json
{
  "code": "0",
  "msg": "",
  "data": [
    {
      "baseMaxLoan": "50",
      "imr": "0.1",
      "instId": "BTC-USDT",
      "maxLever": "10",
      "maxSz": "50",
      "minSz": "0",
      "mmr": "0.03",
      "optMgnFactor": "0",
      "quoteMaxLoan": "500000",
      "tier": "1",
      "uly": "",
      "instFamily": ""
    }
  ]
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 2


**Identifiers**: `BTC`, `USDT`

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
pytest crates/adapters/okx/test_data/http_get_position_tiers.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:00.556032Z*
