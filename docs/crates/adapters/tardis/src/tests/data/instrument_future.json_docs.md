# Documentation: instrument_future.json

## File Metadata

- **Path**: `crates/adapters/tardis/src/tests/data/instrument_future.json`
- **Size**: 532 bytes
- **Lines**: 22
- **Language**: JSON

## Original Source

```json
{
  "id": "BTC-14FEB25",
  "datasetId": "BTC-14FEB25",
  "exchange": "deribit",
  "baseCurrency": "BTC",
  "quoteCurrency": "USD",
  "type": "future",
  "active": true,
  "availableSince": "2025-01-31T00:00:00.000Z",
  "expiry": "2025-02-14T08:00:00.000Z",
  "priceIncrement": 2.5,
  "amountIncrement": 10,
  "minTradeAmount": 10,
  "makerFee": -0.0001,
  "takerFee": 0.0005,
  "inverse": true,
  "contractType": "inverse_future",
  "contractMultiplier": 1,
  "underlyingIndex": "btc_usd",
  "listing": "2025-01-31T08:00:21.000Z"
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 2


**Identifiers**: `BTC`, `USD`

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
pytest crates/adapters/tardis/src/tests/data/instrument_future.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:00.763250Z*
