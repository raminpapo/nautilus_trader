# Documentation: ws_order.json

## File Metadata

- **Path**: `crates/adapters/bitmex/test_data/ws_order.json`
- **Size**: 949 bytes
- **Lines**: 35
- **Language**: JSON

## Original Source

```json
{
    "orderID": "550e8400-e29b-41d4-a716-446655440001",
    "clOrdID": "mm_bitmex_1a/oemUeQ4CAJZgP3fjHsA",
    "clOrdLinkID": null,
    "account": 1234567,
    "symbol": "XBTUSD",
    "side": "Buy",
    "simpleOrderQty": null,
    "orderQty": 100,
    "price": 98000,
    "displayQty": null,
    "stopPx": null,
    "pegOffsetValue": null,
    "pegPriceType": null,
    "currency": "USD",
    "settlCurrency": "XBt",
    "ordType": "Limit",
    "timeInForce": "GoodTillCancel",
    "execInst": null,
    "contingencyType": null,
    "exDestination": "XBME",
    "ordStatus": "New",
    "triggered": null,
    "workingIndicator": true,
    "ordRejReason": null,
    "simpleLeavesQty": null,
    "leavesQty": 100,
    "simpleCumQty": null,
    "cumQty": 0,
    "avgPx": null,
    "multiLegReportingType": "SingleSecurity",
    "text": "Submitted via API.",
    "transactTime": "2024-11-25T10:30:00.000Z",
    "timestamp": "2024-11-25T10:30:00.123Z"
}
```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 11


**Identifiers**: `API`, `Buy`, `GoodTillCancel`, `Limit`, `New`, `SingleSecurity`, `Submitted`, `USD`, `XBME`, `XBTUSD`, `XBt`

## Related Files

This file is located in `crates/adapters/bitmex/test_data/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/adapters/bitmex/test_data/ws_order.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.117616Z*
