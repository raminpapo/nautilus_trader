# Documentation: http_order_book.json

## File Metadata

- **Path**: `crates/adapters/kraken/test_data/http_order_book.json`
- **Size**: 1,475 bytes
- **Lines**: 62
- **Language**: JSON

## Original Source

```json
{
    "error": [],
    "result": {
        "XBTUSDT": {
            "asks": [
                [
                    "105944.30000",
                    "0.136",
                    1762820248
                ],
                [
                    "105946.90000",
                    "0.095",
                    1762820191
                ],
                [
                    "105955.80000",
                    "0.003",
                    1762820244
                ],
                [
                    "105955.90000",
                    "0.103",
                    1762820247
                ],
                [
                    "105963.60000",
                    "0.024",
                    1762820248
                ]
            ],
            "bids": [
                [
                    "105944.20000",
                    "0.002",
                    1762820233
                ],
                [
                    "105935.40000",
                    "0.024",
                    1762820244
                ],
                [
                    "105918.80000",
                    "0.095",
                    1762820249
                ],
                [
                    "105916.80000",
                    "0.016",
                    1762820249
                ],
                [
                    "105916.70000",
                    "0.005",
                    1762820248
                ]
            ]
        }
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 1


**Identifiers**: `XBTUSDT`

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
pytest crates/adapters/kraken/test_data/http_order_book.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:00.247396Z*
