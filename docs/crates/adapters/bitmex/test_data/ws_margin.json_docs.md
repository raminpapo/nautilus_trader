# Documentation: ws_margin.json

## File Metadata

- **Path**: `crates/adapters/bitmex/test_data/ws_margin.json`
- **Size**: 812 bytes
- **Lines**: 30
- **Language**: JSON

## Original Source

```json
{
    "account": 1234567,
    "currency": "XBt",
    "riskLimit": 20000000000,
    "amount": 100005180,
    "prevRealisedPnl": 0,
    "grossComm": 765,
    "grossOpenCost": 0,
    "grossOpenPremium": 0,
    "grossExecCost": 1020408,
    "grossMarkValue": 1015228,
    "riskValue": 1015228,
    "initMargin": 0,
    "maintMargin": 15949,
    "targetExcessMargin": 0,
    "realisedPnl": -765,
    "unrealisedPnl": 5180,
    "walletBalance": 100005180,
    "marginBalance": 100010360,
    "marginLeverage": 0.0983,
    "marginUsedPcnt": 0.0016,
    "excessMargin": 99994411,
    "availableMargin": 99994411,
    "withdrawableMargin": 99994411,
    "makerFeeDiscount": 0,
    "takerFeeDiscount": 0,
    "timestamp": "2024-11-25T10:35:00.789Z",
    "foreignMarginBalance": 100010360,
    "foreignRequirement": 15949
}
```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 1


**Identifiers**: `XBt`

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
pytest crates/adapters/bitmex/test_data/ws_margin.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.116488Z*
