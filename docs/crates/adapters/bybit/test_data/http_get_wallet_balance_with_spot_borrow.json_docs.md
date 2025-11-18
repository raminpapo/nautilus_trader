# Documentation: http_get_wallet_balance_with_spot_borrow.json

## File Metadata

- **Path**: `crates/adapters/bybit/test_data/http_get_wallet_balance_with_spot_borrow.json`
- **Size**: 1,490 bytes
- **Lines**: 44
- **Language**: JSON

## Original Source

```json
{
    "retCode": 0,
    "retMsg": "OK",
    "result": {
        "list": [
            {
                "totalEquity": "3000.00",
                "accountIMRate": "0",
                "totalMarginBalance": "2500.00",
                "totalInitialMargin": "0",
                "accountType": "UNIFIED",
                "totalAvailableBalance": "2500.00",
                "accountMMRate": "0",
                "totalPerpUPL": "0",
                "totalWalletBalance": "2500.00",
                "accountLTV": "0",
                "totalMaintenanceMargin": "0",
                "coin": [
                    {
                        "availableToBorrow": "5000",
                        "bonus": "0",
                        "accruedInterest": "0.50",
                        "availableToWithdraw": "800.00",
                        "equity": "1000.00",
                        "usdValue": "1000.00",
                        "unrealisedPnl": "0",
                        "borrowAmount": "200.00",
                        "walletBalance": "1200.00",
                        "cumRealisedPnl": "100.00",
                        "locked": "0",
                        "collateralSwitch": true,
                        "marginCollateral": true,
                        "coin": "USDT",
                        "spotHedgingQty": "0",
                        "spotBorrow": "200.00"
                    }
                ]
            }
        ]
    },
    "retExtInfo": {},
    "time": 1234567890
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 2


**Identifiers**: `UNIFIED`, `USDT`

## Related Files

This file is located in `crates/adapters/bybit/test_data/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/adapters/bybit/test_data/http_get_wallet_balance_with_spot_borrow.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.511011Z*
