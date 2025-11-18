# Documentation: http_get_fee-rate-tiers.json

## File Metadata

- **Path**: `crates/adapters/coinbase_intx/test_data/http_get_fee-rate-tiers.json`
- **Size**: 848 bytes
- **Lines**: 25
- **Language**: JSON

## Original Source

```json
[
  {
    "fee_tier_type": "REGULAR",
    "instrument_type": "PERPETUAL_FUTURE",
    "fee_tier_id": "1",
    "fee_tier_name": "Public Tier 6",
    "maker_fee_rate": "0.00020000000000000000958434720477185919662588275969028472900390625",
    "taker_fee_rate": "0.0004000000000000000191686944095437183932517655193805694580078125",
    "min_balance": "0",
    "min_volume": "0",
    "require_balance_and_volume": false
  },
  {
    "fee_tier_type": "REGULAR",
    "instrument_type": "PERPETUAL_FUTURE",
    "fee_tier_id": "2",
    "fee_tier_name": "Public Tier 5",
    "maker_fee_rate": "0.00016000000000000001308848862624500952733797021210193634033203125",
    "taker_fee_rate": "0.0004000000000000000191686944095437183932517655193805694580078125",
    "min_balance": "50000",
    "min_volume": "1000000",
    "require_balance_and_volume": true
  }
]

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 4


**Identifiers**: `PERPETUAL_FUTURE`, `Public`, `REGULAR`, `Tier`

## Related Files

This file is located in `crates/adapters/coinbase_intx/test_data/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/adapters/coinbase_intx/test_data/http_get_fee-rate-tiers.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.648098Z*
