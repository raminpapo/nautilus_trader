# Documentation: account_funds.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/betfair/resources/requests/account_funds.json`
- **Size**: 414 bytes
- **Lines**: 17
- **Language**: JSON

## Original Source

```json
{
  "method": "POST",
  "url": "https://api.betfair.com/exchange/account/json-rpc/v1",
  "headers": {
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "content-type": "application/json",
    "X-Application": "app_key",
    "X-Authentication": "xxxsessionToken="
  },
  "json": {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "AccountAPING/v1.0/getAccountFunds",
    "params": {}
  }
}
```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 7


**Identifiers**: `Accept`, `AccountAPING`, `Application`, `Authentication`, `Connection`, `Encoding`, `POST`

## Related Files

This file is located in `tests/integration_tests/adapters/betfair/resources/requests/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/betfair/resources/requests/account_funds.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.200828Z*
