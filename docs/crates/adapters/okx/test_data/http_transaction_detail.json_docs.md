# Documentation: http_transaction_detail.json

## File Metadata

- **Path**: `crates/adapters/okx/test_data/http_transaction_detail.json`
- **Size**: 293 bytes
- **Lines**: 16
- **Language**: JSON

## Original Source

```json
{
  "instType": "SPOT",
  "instId": "BTC-USDT",
  "tradeId": "123456789",
  "ordId": "987654321",
  "clOrdId": "client_123",
  "billId": "bill_456",
  "fillPx": "42000.5",
  "fillSz": "0.001",
  "side": "buy",
  "execType": "T",
  "feeCcy": "USDT",
  "fee": "0.042",
  "ts": "1625097600000"
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 3


**Identifiers**: `BTC`, `SPOT`, `USDT`

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
pytest crates/adapters/okx/test_data/http_transaction_detail.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:00.566911Z*
