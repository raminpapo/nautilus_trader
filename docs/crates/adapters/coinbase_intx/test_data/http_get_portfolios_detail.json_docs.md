# Documentation: http_get_portfolios_detail.json

## File Metadata

- **Path**: `crates/adapters/coinbase_intx/test_data/http_get_portfolios_detail.json`
- **Size**: 1,230 bytes
- **Lines**: 2
- **Language**: JSON

## Original Source

```json
{"summary":{"collateral":"997.5","unrealized_pnl":"0","unrealized_pnl_percent":"0","position_notional":"0","open_position_notional":"0","pending_fees":"0","borrow":"0","accrued_interest":"0","rolling_debt":"0","balance":"997.5","buying_power":"997.5","portfolio_initial_margin":0.2000000000000000,"portfolio_current_margin":0,"portfolio_maintenance_margin":0.1320000000000000,"portfolio_close_out_margin":0.0666,"in_liquidation":false,"portfolio_initial_margin_notional":0,"portfolio_current_margin_notional":0,"portfolio_maintenance_margin_notional":0,"portfolio_close_out_margin_notional":0,"margin_override":0.2000000000000000,"lock_up_initial_margin":0.2000000000000000,"loan_collateral_requirement":"0","position_offset_notional":0},"balances":[{"asset_id":"0-0-1","asset_name":"USDC","asset_uuid":"2b92315d-eab7-5bef-84fa-089a131333f5","quantity":"997.5000000000000","hold":"0","hold_available_for_collateral":"0","transfer_hold":"0","collateral_value":"997.5","max_withdraw_amount":"997.5000000000000","loan":"0","loan_collateral_requirement":"0.0","pledged_collateral_quantity":"997.5000000000000","loan_initial_margin_contribution":"0.0","collateral_backed_overdraft_loan":"0","user_requested_loan":"0"}],"positions":[]}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 1


**Identifiers**: `USDC`

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
pytest crates/adapters/coinbase_intx/test_data/http_get_portfolios_detail.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.657227Z*
