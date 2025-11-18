# Documentation: http_get_account_balance.json

## File Metadata

- **Path**: `crates/adapters/okx/test_data/http_get_account_balance.json`
- **Size**: 1,810 bytes
- **Lines**: 70
- **Language**: JSON

## Original Source

```json
{
  "code": "0",
  "data": [
    {
      "adjEq": "",
      "borrowFroz": "",
      "details": [
        {
          "accAvgPx": "",
          "availBal": "94.42612990333333",
          "availEq": "94.42612990333333",
          "borrowFroz": "",
          "cashBal": "94.42612990333333",
          "ccy": "USDT",
          "clSpotInUseAmt": "",
          "collateralEnabled": false,
          "crossLiab": "",
          "disEq": "5.4682385526666675",
          "eq": "99.89469657000001",
          "eqUsd": "99.88870288820581",
          "fixedBal": "0",
          "frozenBal": "5.468566666666667",
          "imr": "0",
          "interest": "",
          "isoEq": "5.468566666666667",
          "isoLiab": "",
          "isoUpl": "-0.0273000000000002",
          "liab": "",
          "maxLoan": "",
          "maxSpotInUseAmt": "",
          "mgnRatio": "",
          "mmr": "0",
          "notionalLever": "0",
          "openAvgPx": "",
          "ordFrozen": "0",
          "rewardBal": "0",
          "smtSyncEq": "0",
          "spotBal": "",
          "spotCopyTradingEq": "0",
          "spotInUseAmt": "",
          "spotIsoBal": "0",
          "spotUpl": "",
          "spotUplRatio": "",
          "stgyEq": "0",
          "totalPnl": "",
          "totalPnlRatio": "",
          "twap": "0",
          "uTime": "1744498994783",
          "upl": "-0.0273000000000002",
          "uplLiab": ""
        }
      ],
      "imr": "",
      "isoEq": "5.4682385526666675",
      "mgnRatio": "",
      "mmr": "",
      "notionalUsd": "",
      "notionalUsdForBorrow": "",
      "notionalUsdForFutures": "",
      "notionalUsdForOption": "",
      "notionalUsdForSwap": "",
      "ordFroz": "",
      "totalEq": "99.88870288820581",
      "uTime": "1744499648556",
      "upl": ""
    }
  ],
  "msg": ""
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

This file is located in `crates/adapters/okx/test_data/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/adapters/okx/test_data/http_get_account_balance.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:00.528548Z*
