# Documentation: http_get_assets.json

## File Metadata

- **Path**: `crates/adapters/coinbase_intx/test_data/http_get_assets.json`
- **Size**: 852 bytes
- **Lines**: 30
- **Language**: JSON

## Original Source

```json
[
  {
    "asset_id": "1",
    "asset_uuid": "2b92315d-eab7-5bef-84fa-089a131333f5",
    "asset_name": "USDC",
    "status": "ACTIVE",
    "collateral_weight": 1.0,
    "supported_networks_enabled": false,
    "min_borrow_qty": "10",
    "max_borrow_qty": "1000000",
    "loan_collateral_requirement_multiplier": 1.0,
    "ecosystem_collateral_limit_breached": false,
    "loan_initial_margin": "0.1",
    "max_loan_leverage": "3"
  },
  {
    "asset_id": "118059611751202816",
    "asset_uuid": "5b71fc48-3dd3-540c-809b-f8c94d0e68b5",
    "asset_name": "BTC",
    "status": "ACTIVE",
    "collateral_weight": 0.9,
    "supported_networks_enabled": true,
    "min_borrow_qty": "0",
    "max_borrow_qty": "0",
    "loan_collateral_requirement_multiplier": 0.0,
    "account_collateral_limit": "0",
    "ecosystem_collateral_limit_breached": false
  }
]

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 3


**Identifiers**: `ACTIVE`, `BTC`, `USDC`

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
pytest crates/adapters/coinbase_intx/test_data/http_get_assets.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.645585Z*
