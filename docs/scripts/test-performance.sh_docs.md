# Documentation: test-performance.sh

## File Metadata

- **Path**: `scripts/test-performance.sh`
- **Size**: 129 bytes
- **Lines**: 5
- **Language**: Shell

## Original Source

```bash
#!/bin/bash

uv sync --all-groups --all-extras
uv run --no-sync pytest tests/performance_tests --benchmark-disable-gc --codspeed

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 0

*No keywords extracted*

## Related Files

This file is located in `scripts/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest scripts/test-performance.sh

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.168916Z*
