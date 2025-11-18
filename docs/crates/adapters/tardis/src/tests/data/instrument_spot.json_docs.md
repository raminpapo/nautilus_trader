# Documentation: instrument_spot.json

## File Metadata

- **Path**: `crates/adapters/tardis/src/tests/data/instrument_spot.json`
- **Size**: 470 bytes
- **Lines**: 23
- **Language**: JSON

## Original Source

```json
{
  "id": "BTC_USDC",
  "exchange": "deribit",
  "baseCurrency": "BTC",
  "quoteCurrency": "USDC",
  "type": "spot",
  "active": true,
  "availableSince": "2023-04-24T00:00:00.000Z",
  "priceIncrement": 1,
  "amountIncrement": 0.0001,
  "minTradeAmount": 0.0001,
  "makerFee": 0,
  "takerFee": 0,
  "listing": "2023-04-24T13:00:02.000Z",
  "changes": [
    {
      "until": "2024-04-02T12:10:00.000Z",
      "priceIncrement": 0.01
    }
  ],
  "datasetId": "BTC_USDC"
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 3


**Identifiers**: `BTC`, `BTC_USDC`, `USDC`

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
pytest crates/adapters/tardis/src/tests/data/instrument_spot.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:00.768083Z*
