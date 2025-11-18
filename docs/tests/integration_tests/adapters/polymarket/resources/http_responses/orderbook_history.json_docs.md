# Documentation: orderbook_history.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/polymarket/resources/http_responses/orderbook_history.json`
- **Size**: 1,815 bytes
- **Lines**: 58
- **Language**: JSON

## Original Source

```json
{
  "snapshots": [
    {
      "timestamp": 1729000000000,
      "hash": "0xabc123",
      "market": "0x4319532e181605cb15b1bd677759a3bc7f7394b2fdf145195b700eeaedfd5221",
      "asset_id": "60487116984468020978247225474488676749601001829886755968952521846780452448915",
      "bids": [
        {"price": "0.51", "size": "100.5"},
        {"price": "0.50", "size": "250.0"},
        {"price": "0.49", "size": "500.25"}
      ],
      "asks": [
        {"price": "0.52", "size": "150.75"},
        {"price": "0.53", "size": "300.0"},
        {"price": "0.54", "size": "450.5"}
      ]
    },
    {
      "timestamp": 1729000060000,
      "hash": "0xdef456",
      "market": "0x4319532e181605cb15b1bd677759a3bc7f7394b2fdf145195b700eeaedfd5221",
      "asset_id": "60487116984468020978247225474488676749601001829886755968952521846780452448915",
      "bids": [
        {"price": "0.52", "size": "120.0"},
        {"price": "0.51", "size": "280.5"},
        {"price": "0.50", "size": "520.0"}
      ],
      "asks": [
        {"price": "0.53", "size": "140.25"},
        {"price": "0.54", "size": "290.0"},
        {"price": "0.55", "size": "480.75"}
      ]
    },
    {
      "timestamp": 1729000120000,
      "hash": "0x789abc",
      "market": "0x4319532e181605cb15b1bd677759a3bc7f7394b2fdf145195b700eeaedfd5221",
      "asset_id": "60487116984468020978247225474488676749601001829886755968952521846780452448915",
      "bids": [
        {"price": "0.53", "size": "110.5"},
        {"price": "0.52", "size": "260.0"},
        {"price": "0.51", "size": "510.25"}
      ],
      "asks": [
        {"price": "0.54", "size": "130.0"},
        {"price": "0.55", "size": "270.5"},
        {"price": "0.56", "size": "460.0"}
      ]
    }
  ],
  "pagination": {
    "count": 3,
    "limit": 500,
    "has_more": false
  }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 0

*No keywords extracted*

## Related Files

This file is located in `tests/integration_tests/adapters/polymarket/resources/http_responses/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/polymarket/resources/http_responses/orderbook_history.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:07.132680Z*
