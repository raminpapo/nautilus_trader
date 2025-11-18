# Documentation: http_asset_pairs.json

## File Metadata

- **Path**: `crates/adapters/kraken/test_data/http_asset_pairs.json`
- **Size**: 3,046 bytes
- **Lines**: 134
- **Language**: JSON

## Original Source

```json
{
    "error": [],
    "result": {
        "XBTUSDT": {
            "altname": "XBTUSDT",
            "wsname": "XBT/USDT",
            "aclass_base": "currency",
            "base": "XXBT",
            "aclass_quote": "currency",
            "quote": "USDT",
            "lot": "unit",
            "cost_decimals": 5,
            "pair_decimals": 1,
            "lot_decimals": 8,
            "lot_multiplier": 1,
            "leverage_buy": [
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10
            ],
            "leverage_sell": [
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10
            ],
            "fees": [
                [
                    0,
                    0.4
                ],
                [
                    10000,
                    0.35
                ],
                [
                    50000,
                    0.24
                ],
                [
                    100000,
                    0.22
                ],
                [
                    250000,
                    0.2
                ],
                [
                    500000,
                    0.18
                ],
                [
                    1000000,
                    0.16
                ],
                [
                    2500000,
                    0.14
                ],
                [
                    5000000,
                    0.12
                ],
                [
                    10000000,
                    0.1
                ]
            ],
            "fees_maker": [
                [
                    0,
                    0.25
                ],
                [
                    10000,
                    0.2
                ],
                [
                    50000,
                    0.14
                ],
                [
                    100000,
                    0.12
                ],
                [
                    250000,
                    0.1
                ],
                [
                    500000,
                    0.08
                ],
                [
                    1000000,
                    0.06
                ],
                [
                    2500000,
                    0.04
                ],
                [
                    5000000,
                    0.02
                ],
                [
                    10000000,
                    0.0
                ]
            ],
            "fee_volume_currency": "ZUSD",
            "margin_call": 80,
            "margin_stop": 40,
            "ordermin": "0.00005",
            "costmin": "0.5",
            "tick_size": "0.1",
            "status": "online",
            "long_position_limit": 80,
            "short_position_limit": 80
        }
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 5


**Identifiers**: `USDT`, `XBT`, `XBTUSDT`, `XXBT`, `ZUSD`

## Related Files

This file is located in `crates/adapters/kraken/test_data/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/adapters/kraken/test_data/http_asset_pairs.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:00.225405Z*
