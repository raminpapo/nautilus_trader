# Documentation: ws_execution_cancel_reject.json

## File Metadata

- **Path**: `crates/adapters/bitmex/test_data/ws_execution_cancel_reject.json`
- **Size**: 371 bytes
- **Lines**: 13
- **Language**: JSON

## Original Source

```json
{
  "execID": "00000000-006d-1000-0000-001e7f5081ad",
  "orderID": "ece0a2cc-7729-4f4c-bc6c-65d7c723e75b",
  "account": 1667725,
  "execType": "CancelReject",
  "ordStatus": "Rejected",
  "workingIndicator": false,
  "ordRejReason": "Invalid orderID",
  "text": "Invalid orderID",
  "transactTime": "2025-09-05T05:38:28.001Z",
  "timestamp": "2025-09-05T05:38:28.001Z"
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 3


**Identifiers**: `CancelReject`, `Invalid`, `Rejected`

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
pytest crates/adapters/bitmex/test_data/ws_execution_cancel_reject.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.111940Z*
