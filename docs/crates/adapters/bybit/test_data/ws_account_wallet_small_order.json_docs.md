# Documentation: ws_account_wallet_small_order.json

## File Metadata

- **Path**: `crates/adapters/bybit/test_data/ws_account_wallet_small_order.json`
- **Size**: 895 bytes
- **Lines**: 35
- **Language**: JSON

## Original Source

```json
{
  "id": "test-small-order-id",
  "topic": "wallet",
  "creationTime": 1762960669000,
  "data": [
    {
      "accountIMRate": "0",
      "accountMMRate": "0",
      "accountLTV": "0",
      "totalEquity": "51333.82543837",
      "totalWalletBalance": "51333.82543837",
      "totalMarginBalance": "51333.82543837",
      "totalAvailableBalance": "0",
      "totalPerpUpl": "0",
      "totalInitialMargin": "50.028",
      "totalMaintenanceMargin": "5.0028",
      "coin": [
        {
          "coin": "USDT",
          "equity": "51333.82543837",
          "walletBalance": "51333.82543837",
          "availableToWithdraw": "0",
          "availableToBorrow": "",
          "borrowAmount": "0",
          "accruedInterest": "0",
          "totalOrderIM": "50.028",
          "totalPositionIM": "0",
          "totalPositionMM": "0",
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

Total unique keywords extracted: 1


**Identifiers**: `USDT`

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
pytest crates/adapters/bybit/test_data/ws_account_wallet_small_order.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.529236Z*
