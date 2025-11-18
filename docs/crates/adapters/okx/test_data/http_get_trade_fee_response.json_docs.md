# Documentation: http_get_trade_fee_response.json

## File Metadata

- **Path**: `crates/adapters/okx/test_data/http_get_trade_fee_response.json`
- **Size**: 357 bytes
- **Lines**: 22
- **Language**: JSON

## Original Source

```json
{
  "code": "0",
  "msg": "",
  "data": [
    {
      "category": "1",
      "delivery": "",
      "exercise": "",
      "instType": "SPOT",
      "level": "Lv1",
      "maker": "-0.0008",
      "makerU": "",
      "makerUSDC": "",
      "taker": "-0.001",
      "takerU": "",
      "takerUSDC": "",
      "ts": "1608623626000",
      "uly": ""
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


**Identifiers**: `Lv1`, `SPOT`

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
pytest crates/adapters/okx/test_data/http_get_trade_fee_response.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:00.559189Z*
