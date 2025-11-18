# Documentation: cert_login.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/betfair/resources/requests/cert_login.json`
- **Size**: 337 bytes
- **Lines**: 14
- **Language**: JSON

## Original Source

```json
{
  "data": {
    "password": "password",
    "username": "username"
  },
  "headers": {
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "X-Application": "app_key"
  },
  "method": "POST",
  "url": "https://identitysso-cert.betfair.com/api/certlogin"
}
```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 7


**Identifiers**: `Accept`, `Application`, `Connection`, `Content`, `Encoding`, `POST`, `Type`

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
pytest tests/integration_tests/adapters/betfair/resources/requests/cert_login.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

⚠️ **Security**: This file may handle sensitive data. Ensure proper encryption and access controls.

---
*Generated on 2025-11-18T21:55:06.211470Z*
