# Documentation: subaccount.json

## File Metadata

- **Path**: `tests/test_data/dydx/http/subaccount.json`
- **Size**: 1,302 bytes
- **Lines**: 41
- **Language**: JSON

## Original Source

```json
{
    "subaccount": {
        "address": "dydx1kzsvkf2ghjqlysuffdkhcdctknl4rsvcx5hkm5",
        "assetPositions": {
            "USDC": {
                "assetId": "0",
                "side": "LONG",
                "size": "90.461932",
                "subaccountNumber": 0,
                "symbol": "USDC"
            }
        },
        "equity": "99.206819554",
        "freeCollateral": "98.7695751763",
        "latestProcessedBlockHeight": "18164178",
        "marginEnabled": true,
        "openPerpetualPositions": {
            "ETH-USD": {
                "closedAt": null,
                "createdAt": "2024-08-01T07:09:25.767Z",
                "createdAtHeight": "17933806",
                "entryPrice": "3177.76666666666666666667",
                "exitPrice": null,
                "market": "ETH-USD",
                "maxSize": "0.003",
                "netFunding": "0",
                "realizedPnl": "0",
                "side": "LONG",
                "size": "0.003",
                "status": "OPEN",
                "subaccountNumber": 0,
                "sumClose": "0",
                "sumOpen": "0.003",
                "unrealizedPnl": "-0.78841244600000000000001"
            }
        },
        "subaccountNumber": 0,
        "updatedAtHeight": "17933806"
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 5


**Identifiers**: `ETH`, `LONG`, `OPEN`, `USD`, `USDC`

## Related Files

This file is located in `tests/test_data/dydx/http/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/test_data/dydx/http/subaccount.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:08.439541Z*
