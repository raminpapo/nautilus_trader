# Documentation: retry.txt

## File Metadata

- **Path**: `crates/network/proptest-regressions/retry.txt`
- **Size**: 902 bytes
- **Lines**: 12
- **Language**: Unknown

## Original Source

```
# Seeds for failure cases proptest has generated in the past. It is
# automatically read and these particular cases re-run before any
# novel cases are generated.
#
# It is recommended to check this file in to source control so that
# everyone who runs the test benefits from these saved cases.
cc 92d6a183a29ef3cdbb304d0947dcd49f0f61c6fbd0ef6684fdabd86e86127e19 # shrinks to jitter_ms = 0, base_delay_ms = 50
cc f166544819b7c556ff78a632cc61ab0b3ad23eb8ad5df8bfa06846dd42c2328f # shrinks to max_elapsed_ms = 37, delay_per_retry = 5, max_retries = 3
cc 955dbfd4e07a55762de27ec05e0bb9449e8478c5d028617d3a42953b157fda88 # shrinks to max_elapsed_ms = 19, delay_per_retry = 32
cc 1f7b6a390f6dd8a928732a1eaac3acc04ed6be8da7e0df9b9e396358f7f31758 # shrinks to jitter_ms = 0, base_delay_ms = 28
cc 756838c4ec902a43e02f41f9ca0d9c2be51cdc19b38550a873f65337874bfc5a # shrinks to jitter_ms = 5, base_delay_ms = 27

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 1


**Identifiers**: `Seeds`

## Related Files

This file is located in `crates/network/proptest-regressions/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/network/proptest-regressions/retry.txt

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:03.332035Z*
