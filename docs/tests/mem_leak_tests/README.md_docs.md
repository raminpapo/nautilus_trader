# Documentation: README.md

## File Metadata

- **Path**: `tests/mem_leak_tests/README.md`
- **Size**: 666 bytes
- **Lines**: 26
- **Language**: Markdown

## Original Source

```markdown
# Performance tests

This subpackage provides a suite of performance tests, including scripts which can be run
to profile memory and thread resource usage.

Memory profiling is conducted using [memray](https://github.com/bloomberg/memray).
The package is not a development dependency because it doesn't currently support windows.

You can install the package via PyPI:

```bash
pip install memray
```

To profile using memray, first invoke the script using the memray CLI:

```bash
memray run --live-port 8100 --live-remote tests/mem_leak_tests/memray_backtest.py
```

Then from another shell, connect to the memray profiler dashboard:

```bash
memray live 8100
```

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a Markdown documentation file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 8


**Identifiers**: `CLI`, `Memory`, `Performance`, `PyPI`, `The`, `Then`, `This`, `You`

## Related Files

This file is located in `tests/mem_leak_tests/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/mem_leak_tests/README.md

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:07.261526Z*
