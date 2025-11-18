# Documentation: ws_account_wallet.json

## File Metadata

- **Path**: `crates/adapters/bybit/test_data/ws_account_wallet.json`
- **Size**: 1,367 bytes
- **Lines**: 48
- **Language**: JSON

## Original Source

```json
{
  "id": "592324d2bce751-ad38-48eb-8f42-4671d1fb4d4e",
  "topic": "wallet",
  "creationTime": 1700034722104,
  "data": [
    {
      "accountIMRate": "0",
      "accountMMRate": "0",
      "accountLTV": "0",
      "totalEquity": "10262.91335023",
      "totalWalletBalance": "9684.46297164",
      "totalMarginBalance": "9684.46297164",
      "totalAvailableBalance": "9556.6056555",
      "totalPerpUpl": "0",
      "totalInitialMargin": "127.8573161",
      "totalMaintenanceMargin": "12.78573161",
      "coin": [
        {
          "coin": "BTC",
          "equity": "0.00102964",
          "walletBalance": "0.00102964",
          "availableToWithdraw": "0.00092964",
          "availableToBorrow": "",
          "borrowAmount": "0",
          "accruedInterest": "0",
          "totalOrderIM": "0.00010000",
          "totalPositionIM": "0",
          "totalPositionMM": "0",
          "spotBorrow": "0"
        },
        {
          "coin": "USDT",
          "equity": "10226.20575506",
          "walletBalance": "9647.75537647",
          "availableToWithdraw": "9519.89806037",
          "availableToBorrow": "",
          "borrowAmount": "0",
          "accruedInterest": "0",
          "totalOrderIM": "0",
          "totalPositionIM": "127.8573161",
          "totalPositionMM": "12.78573161",
          "spotBorrow": "0"
        }
      ]
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

This file is located in `crates/adapters/bybit/test_data/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/adapters/bybit/test_data/ws_account_wallet.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.527952Z*
