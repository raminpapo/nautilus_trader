# Documentation: nextest.toml

## File Metadata

- **Path**: `.config/nextest.toml`
- **Size**: 437 bytes
- **Lines**: 19
- **Language**: TOML

## Original Source

```toml
[test-groups]
serial-tests = { max-threads = 1 }

[profile.default]
# Default settings

[[profile.default.overrides]]
filter = 'test(serial_tests)'
test-group = 'serial-tests'

[[profile.default.overrides]]
filter = 'test(test_order_book)'
slow-timeout = { period = "300s" }

# Websocket tests can be flaky due to timing on low-spec runners, give them extra retries
[[profile.default.overrides]]
filter = 'binary(websocket)'
retries = 3

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a TOML configuration file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 8


**Keys**: `filter`, `retries`, `serial-tests`, `slow-timeout`, `test-group`
**Sections**: `[profile.default.overrides`, `profile.default`, `test-groups`

## Related Files

This file is located in `.config/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest .config/nextest.toml

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:58.787006Z*
