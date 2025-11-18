# Documentation: order_placement.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/polymarket/resources/ws_messages/order_placement.json`
- **Size**: 737 bytes
- **Lines**: 22
- **Language**: JSON

## Original Source

```json
{
  "asset_id": "21742633143463906290569050155826241533067272736897614950488156847949938836455",
  "associate_trades": null,
  "created_at": "1725842520",
  "event_type": "order",
  "expiration": "0",
  "id": "0x0f76f4dc6eaf3332f4100f2e8a0b4a927351dd64646b7bb12f37df775c657a78",
  "maker_address": "0xa3D82Ed56F4c68d2328Fb8c29e568Ba2cAF7d7c8",
  "market": "0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917",
  "order_owner": "3e2c94ca-8124-c4c1-c7ea-be1ea21b71fe",
  "order_type": "GTC",
  "original_size": "5",
  "outcome": "Yes",
  "owner": "3e2c94ca-8124-c4c1-c7ea-be1ea21b71fe",
  "price": "0.513",
  "side": "BUY",
  "size_matched": "0",
  "status": "LIVE",
  "timestamp": "1725842520990",
  "type": "PLACEMENT"
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 5


**Identifiers**: `BUY`, `GTC`, `LIVE`, `PLACEMENT`, `Yes`

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
pytest tests/integration_tests/adapters/polymarket/resources/ws_messages/order_placement.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:07.140790Z*
