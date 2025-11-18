# Documentation: price_change_v2.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/polymarket/resources/ws_messages/price_change_v2.json`
- **Size**: 1,026 bytes
- **Lines**: 35
- **Language**: JSON

## Original Source

```json
{
  "market": "0x5f65177b394277fd294cd75650044e32ba009a95022d88a0c1d565897d72f8f1",
  "price_changes": [
    {
      "asset_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",
      "price": "0.6",
      "side": "BUY",
      "size": "3300",
      "hash": "bf32b3746fff40c76c98021b7f3f07261169dd26",
      "best_bid": "0.6",
      "best_ask": "0.7"
    },
    {
      "asset_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",
      "price": "0.5",
      "side": "BUY",
      "size": "3400",
      "hash": "af32b3746fff40c76c98021b7f3f07261169dd27",
      "best_bid": "0.6",
      "best_ask": "0.7"
    },
    {
      "asset_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",
      "price": "0.7",
      "side": "BUY",
      "size": "3400",
      "hash": "cf32b3746fff40c76c98021b7f3f07261169dd28",
      "best_bid": "0.6",
      "best_ask": "0.7"
    }
  ],
  "event_type": "price_change",
  "timestamp": "1729084877448"
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 1


**Identifiers**: `BUY`

## Related Files

This file is located in `tests/integration_tests/adapters/polymarket/resources/ws_messages/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/polymarket/resources/ws_messages/price_change_v2.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:07.143956Z*
