# Documentation: http_get_wallet_balance.json

## File Metadata

- **Path**: `crates/adapters/bybit/test_data/http_get_wallet_balance.json`
- **Size**: 2,302 bytes
- **Lines**: 63
- **Language**: JSON

## Original Source

```json
{
    "retCode": 0,
    "retMsg": "OK",
    "result": {
        "list": [
            {
                "totalEquity": "3.31216591",
                "accountIMRate": "0",
                "totalMarginBalance": "3.00326056",
                "totalInitialMargin": "0",
                "accountType": "UNIFIED",
                "totalAvailableBalance": "3.00326056",
                "accountMMRate": "0",
                "totalPerpUPL": "0",
                "totalWalletBalance": "3.00326056",
                "accountLTV": "0",
                "totalMaintenanceMargin": "0",
                "coin": [
                    {
                        "availableToBorrow": "3",
                        "bonus": "0",
                        "accruedInterest": "0",
                        "availableToWithdraw": "0",
                        "totalOrderIM": "0",
                        "equity": "0",
                        "totalPositionMM": "0",
                        "usdValue": "0",
                        "unrealisedPnl": "0",
                        "borrowAmount": "0.0",
                        "totalPositionIM": "0",
                        "walletBalance": "0",
                        "cumRealisedPnl": "0",
                        "locked": "0",
                        "collateralSwitch": true,
                        "marginCollateral": true,
                        "coin": "BTC",
                        "spotBorrow": "0"
                    },
                    {
                        "availableToBorrow": "5000",
                        "bonus": "0",
                        "accruedInterest": "0",
                        "availableToWithdraw": "1000.50",
                        "equity": "1000.50",
                        "usdValue": "1000.50",
                        "unrealisedPnl": "0",
                        "borrowAmount": "0",
                        "walletBalance": "1000.50",
                        "cumRealisedPnl": "50.25",
                        "locked": "0",
                        "collateralSwitch": true,
                        "marginCollateral": true,
                        "coin": "USDT",
                        "spotBorrow": "0"
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

Total unique keywords extracted: 3


**Identifiers**: `BTC`, `UNIFIED`, `USDT`

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
pytest crates/adapters/bybit/test_data/http_get_wallet_balance.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.509850Z*
