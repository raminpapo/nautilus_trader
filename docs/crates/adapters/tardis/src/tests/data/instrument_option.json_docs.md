# Documentation: instrument_option.json

## File Metadata

- **Path**: `crates/adapters/tardis/src/tests/data/instrument_option.json`
- **Size**: 566 bytes
- **Lines**: 23
- **Language**: JSON

## Original Source

```json
{
  "id": "BTC-25APR25-200000-P",
  "datasetId": "BTC-25APR25-200000-P",
  "exchange": "deribit",
  "baseCurrency": "BTC",
  "quoteCurrency": "BTC",
  "type": "option",
  "active": true,
  "availableSince": "2025-01-31T00:00:00.000Z",
  "expiry": "2025-04-25T08:00:00.000Z",
  "priceIncrement": 0.0001,
  "amountIncrement": 0.1,
  "minTradeAmount": 0.1,
  "makerFee": 0.0003,
  "takerFee": 0.0003,
  "inverse": true,
  "contractType": "put_option",
  "contractMultiplier": 1,
  "strikePrice": 200000,
  "optionType": "put",
  "listing": "2025-01-31T20:38:40.000Z"
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 1


**Identifiers**: `BTC`

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
pytest crates/adapters/tardis/src/tests/data/instrument_option.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:00.764789Z*
