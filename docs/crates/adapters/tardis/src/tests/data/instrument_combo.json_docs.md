# Documentation: instrument_combo.json

## File Metadata

- **Path**: `crates/adapters/tardis/src/tests/data/instrument_combo.json`
- **Size**: 528 bytes
- **Lines**: 22
- **Language**: JSON

## Original Source

```json
{
  "id": "BTC-FS-28MAR25_PERP",
  "exchange": "deribit",
  "baseCurrency": "BTC",
  "quoteCurrency": "USD",
  "type": "combo",
  "active": true,
  "availableSince": "2024-03-29T00:00:00.000Z",
  "expiry": "2025-03-28T08:00:00.000Z",
  "priceIncrement": 0.5,
  "amountIncrement": 10,
  "minTradeAmount": 10,
  "makerFee": 0,
  "takerFee": 0,
  "inverse": true,
  "contractType": "spread",
  "contractMultiplier": 1,
  "underlyingIndex": "btc_usd",
  "listing": "2024-03-29T08:48:59.000Z",
  "datasetId": "BTC-FS-28MAR25_PERP"
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
pytest crates/adapters/tardis/src/tests/data/instrument_combo.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:00.761107Z*
