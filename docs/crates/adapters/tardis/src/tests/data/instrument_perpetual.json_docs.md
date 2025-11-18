# Documentation: instrument_perpetual.json

## File Metadata

- **Path**: `crates/adapters/tardis/src/tests/data/instrument_perpetual.json`
- **Size**: 797 bytes
- **Lines**: 37
- **Language**: JSON

## Original Source

```json
{
  "id": "XBTUSD",
  "datasetId": "XBTUSD",
  "exchange": "bitmex",
  "baseCurrency": "BTC",
  "quoteCurrency": "USD",
  "settlementCurrency": "BTC",
  "type": "perpetual",
  "active": true,
  "availableSince": "2019-03-30T00:00:00.000Z",
  "priceIncrement": 0.1,
  "amountIncrement": 100,
  "minTradeAmount": 100,
  "makerFee": 0.0005,
  "takerFee": 0.0005,
  "inverse": true,
  "contractType": "inverse_perpetual",
  "contractMultiplier": 1,
  "underlyingIndex": ".BXBT",
  "changes": [
    {
      "until": "2021-06-08T04:30:00.000Z",
      "amountIncrement": 1,
      "minTradeAmount": 1
    },
    {
      "until": "2024-07-31T04:00:00.000Z",
      "priceIncrement": 0.5
    },
    {
      "until": "2024-10-22T00:00:00.000Z",
      "makerFee": 0.0002,
      "takerFee": 0.00075
    }
  ]
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 4


**Identifiers**: `BTC`, `BXBT`, `USD`, `XBTUSD`

## Related Files

This file is located in `crates/adapters/tardis/src/tests/data/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/adapters/tardis/src/tests/data/instrument_perpetual.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:00.766564Z*
