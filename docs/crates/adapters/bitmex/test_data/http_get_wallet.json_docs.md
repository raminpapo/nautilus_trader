# Documentation: http_get_wallet.json

## File Metadata

- **Path**: `crates/adapters/bitmex/test_data/http_get_wallet.json`
- **Size**: 789 bytes
- **Lines**: 29
- **Language**: JSON

## Original Source

```json
[
    {
        "account": 1234567,
        "currency": "XBt",
        "prevDeposited": 0,
        "prevWithdrawn": 0,
        "prevTransferIn": 0,
        "prevTransferOut": 0,
        "prevAmount": 1000000000,
        "prevTimestamp": "2024-11-24T00:00:00.000Z",
        "deltaDeposited": 0,
        "deltaWithdrawn": 0,
        "deltaTransferIn": 0,
        "deltaTransferOut": 0,
        "deltaAmount": 123456,
        "deposited": 0,
        "withdrawn": 0,
        "transferIn": 0,
        "transferOut": 0,
        "amount": 1000123456,
        "pendingCredit": 0,
        "pendingDebit": 0,
        "confirmedDebit": 0,
        "timestamp": "2024-11-25T10:35:00.000Z",
        "addr": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
        "script": "",
        "withdrawalLock": []
    }
]
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
pytest crates/adapters/bitmex/test_data/http_get_wallet.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.109683Z*
