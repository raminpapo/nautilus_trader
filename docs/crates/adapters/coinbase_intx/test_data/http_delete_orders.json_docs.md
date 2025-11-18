# Documentation: http_delete_orders.json

## File Metadata

- **Path**: `crates/adapters/coinbase_intx/test_data/http_delete_orders.json`
- **Size**: 680 bytes
- **Lines**: 26
- **Language**: JSON

## Original Source

```json
{
  "order_id": "2v2ckc1g-1-0",
  "order_uuid": "cb1df22f-05c1-8000-8000-326c0c004000",
  "client_order_id": "f346ca69-11b4-4e1b-ae47-85971290c771",
  "side": "SELL",
  "instrument_id": "114jqqhr-0-0",
  "instrument_uuid": "e9360798-6a10-45d6-af05-67c30eb91e2d",
  "symbol": "ETH-PERP",
  "portfolio_id": "3mnk39ap-1-21",
  "portfolio_uuid": "cc0958ad-0c7d-4445-a812-1370fe46d0d4",
  "type": "LIMIT",
  "price": "3000",
  "size": "0.01",
  "tif": "GTC",
  "stp_mode": "BOTH",
  "event_type": "CANCELED",
  "order_status": "DONE",
  "leaves_qty": "0.01",
  "exec_qty": "0",
  "avg_price": "0",
  "fee": "0",
  "post_only": false,
  "close_only": false,
  "text": "client cancel"
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 8


**Identifiers**: `BOTH`, `CANCELED`, `DONE`, `ETH`, `GTC`, `LIMIT`, `PERP`, `SELL`

## Related Files

This file is located in `crates/adapters/coinbase_intx/test_data/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/adapters/coinbase_intx/test_data/http_delete_orders.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.644218Z*
