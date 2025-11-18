# Documentation: ws_books_update.json

## File Metadata

- **Path**: `crates/adapters/okx/test_data/ws_books_update.json`
- **Size**: 1,662 bytes
- **Lines**: 116
- **Language**: JSON

## Original Source

```json
{
  "arg": {
    "channel": "books",
    "instId": "BTC-USDT"
  },
  "action": "update",
  "data": [
    {
      "asks": [
        [
          "8476.98",
          "415",
          "0",
          "13"
        ],
        [
          "8477",
          "7",
          "0",
          "2"
        ],
        [
          "8477.34",
          "85",
          "0",
          "1"
        ],
        [
          "8477.56",
          "1",
          "0",
          "1"
        ],
        [
          "8505.84",
          "8",
          "0",
          "1"
        ],
        [
          "8506.37",
          "85",
          "0",
          "1"
        ],
        [
          "8506.49",
          "2",
          "0",
          "1"
        ],
        [
          "8506.96",
          "100",
          "0",
          "2"
        ]
      ],
      "bids": [
        [
          "8476.97",
          "256",
          "0",
          "12"
        ],
        [
          "8475.55",
          "101",
          "0",
          "1"
        ],
        [
          "8475.54",
          "100",
          "0",
          "1"
        ],
        [
          "8475.3",
          "1",
          "0",
          "1"
        ],
        [
          "8447.32",
          "6",
          "0",
          "1"
        ],
        [
          "8447.02",
          "246",
          "0",
          "1"
        ],
        [
          "8446.83",
          "24",
          "0",
          "1"
        ],
        [
          "8446",
          "95",
          "0",
          "3"
        ]
      ],
      "ts": "1597026383085",
      "checksum": -855196043,
      "prevSeqId": 123456,
      "seqId": 123457
    }
  ]
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 2


**Identifiers**: `BTC`, `USDT`

## Related Files

This file is located in `crates/adapters/okx/test_data/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/adapters/okx/test_data/ws_books_update.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:00.574509Z*
