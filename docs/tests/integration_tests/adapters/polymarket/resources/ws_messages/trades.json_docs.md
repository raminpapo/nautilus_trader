# Documentation: trades.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/polymarket/resources/ws_messages/trades.json`
- **Size**: 1,205 bytes
- **Lines**: 32
- **Language**: JSON

## Original Source

```json
{
  "id": "0c357886-b9d3-44bb-9aa9-72d8abc90e6e",
  "taker_order_id": "0x4505aada9831d06078a005c8ec96396a78c8f06035bf763b40fc16d27a250043",
  "market": "0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917",
  "asset_id": "21742633143463906290569050155826241533067272736897614950488156847949938836455",
  "side": "BUY",
  "size": "5",
  "fee_rate_bps": "0",
  "price": "0.489",
  "status": "CONFIRMED",
  "match_time": "1726043102",
  "last_update": "1726043282",
  "outcome": "Yes",
  "bucket_index": 0,
  "owner": "3e2c94ca-8124-c4c1-c7ea-be1ea21b71fe",
  "maker_address": "0xa3D82Ed56F4c68d2328Fb8c29e568Ba2cAF7d7c8",
  "transaction_hash": "0x5fbfe1691c52958dfa3f98dc75ef516f5a9d4b370aead26598d06e3db069839f",
  "maker_orders": [
    {
      "order_id": "0x6dd169f87692751b75b4ed673158721cdbf56ec49f29aa94a6aaa05b93b1b0ab",
      "owner": "62880c97-4a03-c6fa-2665-e6072ffc6ae6",
      "maker_address": "0x1bFDF7224C358405A486b5FD8489f13c2aDcb5f3",
      "matched_amount": "5",
      "price": "0.489",
      "fee_rate_bps": "0",
      "asset_id": "21742633143463906290569050155826241533067272736897614950488156847949938836455",
      "outcome": "Yes"
    }
  ],
  "trader_side": "TAKER"
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 4


**Identifiers**: `BUY`, `CONFIRMED`, `TAKER`, `Yes`

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
pytest tests/integration_tests/adapters/polymarket/resources/ws_messages/trades.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:07.146967Z*
