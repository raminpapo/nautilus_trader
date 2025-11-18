# Documentation: http_get_orders.json

## File Metadata

- **Path**: `crates/adapters/bitmex/test_data/http_get_orders.json`
- **Size**: 2,214 bytes
- **Lines**: 72
- **Language**: JSON

## Original Source

```json
[
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
    },
    {
        "orderID": "550e8400-e29b-41d4-a716-446655440002",
        "clOrdID": "mm_bitmex_2b/oemUeQ4CAJZgP3fjHsB",
        "clOrdLinkID": null,
        "account": 1234567,
        "symbol": "XBTUSD",
        "side": "Sell",
        "simpleOrderQty": null,
        "orderQty": 200,
        "price": 99000,
        "displayQty": null,
        "stopPx": null,
        "pegOffsetValue": null,
        "pegPriceType": null,
        "currency": "USD",
        "settlCurrency": "XBt",
        "ordType": "Limit",
        "timeInForce": "GoodTillCancel",
        "execInst": "ParticipateDoNotInitiate",
        "contingencyType": null,
        "exDestination": "XBME",
        "ordStatus": "Filled",
        "triggered": null,
        "workingIndicator": false,
        "ordRejReason": null,
        "simpleLeavesQty": null,
        "leavesQty": 0,
        "simpleCumQty": null,
        "cumQty": 200,
        "avgPx": 98950.5,
        "multiLegReportingType": "SingleSecurity",
        "text": "Submitted via API.",
        "transactTime": "2024-11-25T10:25:00.000Z",
        "timestamp": "2024-11-25T10:35:00.456Z"
    }
]
```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 14


**Identifiers**: `API`, `Buy`, `Filled`, `GoodTillCancel`, `Limit`, `New`, `ParticipateDoNotInitiate`, `Sell`, `SingleSecurity`, `Submitted`, `USD`, `XBME`, `XBTUSD`, `XBt`

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
pytest crates/adapters/bitmex/test_data/http_get_orders.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.105118Z*
