# Documentation: http_get_positions.json

## File Metadata

- **Path**: `crates/adapters/okx/test_data/http_get_positions.json`
- **Size**: 1,121 bytes
- **Lines**: 52
- **Language**: JSON

## Original Source

```json
{
  "code": "0",
  "data": [
    {
      "instId": "BTC-USDT-SWAP",
      "instType": "SWAP",
      "mgnMode": "isolated",
      "posId": "12345",
      "posSide": "long",
      "pos": "0.5",
      "baseBal": "0.5",
      "ccy": "BTC",
      "fee": "0.01",
      "lever": "10.0",
      "last": "10000",
      "markPx": "10000",
      "liqPx": "9000",
      "mmr": "0.1",
      "interest": "0",
      "tradeId": "111",
      "notionalUsd": "5000",
      "avgPx": "10000",
      "upl": "0",
      "uplRatio": "0",
      "uTime": "1622559930237",
      "margin": "0.5",
      "mgnRatio": "0.01",
      "adl": "0",
      "cTime": "1622559930237",
      "realizedPnl": "0",
      "uplLastPx": "0",
      "uplRatioLastPx": "0",
      "availPos": "0.5",
      "bePx": "0",
      "fundingFee": "0",
      "idxPx": "0",
      "liqPenalty": "0",
      "optVal": "0",
      "pendingCloseOrdLiabVal": "0",
      "pnl": "0",
      "posCcy": "BTC",
      "quoteBal": "5000",
      "quoteBorrowed": "0",
      "quoteInterest": "0",
      "spotInUseAmt": "0",
      "spotInUseCcy": "BTC",
      "usdPx": "10000"
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

Total unique keywords extracted: 3


**Identifiers**: `BTC`, `SWAP`, `USDT`

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
pytest crates/adapters/okx/test_data/http_get_positions.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:00.557455Z*
