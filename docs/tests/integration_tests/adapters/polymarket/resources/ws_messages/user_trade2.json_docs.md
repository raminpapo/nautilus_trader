# Documentation: user_trade2.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/polymarket/resources/ws_messages/user_trade2.json`
- **Size**: 1,334 bytes
- **Lines**: 36
- **Language**: JSON

## Original Source

```json
{
  "asset_id": "21742633143463906290569050155826241533067272736897614950488156847949938836455",
  "bucket_index": 0,
  "event_type": "trade",
  "fee_rate_bps": "0",
  "id": "f50e8ab2-652d-4dc8-9c82-8e46197fe98d",
  "last_update": "1725958682",
  "maker_address": "0xa3D82Ed56F4c68d2328Fb8c29e568Ba2cAF7d7c8",
  "maker_orders": [
    {
      "asset_id": "21742633143463906290569050155826241533067272736897614950488156847949938836455",
      "fee_rate_bps": "0",
      "maker_address": "0x629BC4a1E53e1d475beB7ea3D388791e96Dd995A",
      "matched_amount": "5",
      "order_id": "0xa39ab90ec5515224a2a39c9ef967b51d10bda754902a318cac84135018b5885a",
      "outcome": "Yes",
      "owner": "ce168652-c146-2d93-a45c-f36cc52ae6f6",
      "price": "0.52"
    }
  ],
  "market": "0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917",
  "match_time": "1725958681",
  "outcome": "Yes",
  "owner": "3e2c94ca-8124-c4c1-c7ea-be1ea21b71fe",
  "price": "0.52",
  "side": "BUY",
  "size": "5",
  "status": "MATCHED",
  "taker_order_id": "0x5b605a0e8e40f3402d3cb3bc19edad6733ed23fbc079d2a09ee399c3487ace81",
  "timestamp": "1725958682125",
  "trade_owner": "3e2c94ca-8124-c4c1-c7ea-be1ea21b71fe",
  "trader_side": "TAKER",
  "transaction_hash": "0xa667ef3b363b70731c59e3d4fff50d7bdb3d6b165d49e448032cab68c82e3c66",
  "type": "TRADE"
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 5


**Identifiers**: `BUY`, `MATCHED`, `TAKER`, `TRADE`, `Yes`

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
pytest tests/integration_tests/adapters/polymarket/resources/ws_messages/user_trade2.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:07.150192Z*
