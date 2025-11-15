# Documentation: `.docker/entrypoint.sh`
**Generated:** 2025-11-15T19:40:00.217766Z
**File Size:** 1218 bytes
**Extension:** .sh
**Type:** text

---

## Table of Contents

1. [File Metadata](#file-metadata)
2. [Source Code](#source-code)
3. [Overview](#overview)
4. [Detailed Analysis](#detailed-analysis)
5. [Usage Examples](#usage-examples)
6. [Related Files](#related-files)
7. [Notes](#notes)

---

## File Metadata

- **Path:** `.docker/entrypoint.sh`
- **Size:** 1,218 bytes
- **Lines:** 35
- **Extension:** `.sh`
- **Type:** text

---

## Source Code

```bash
#!/bin/bash
# entrypoint script for DockerfileUbuntu

echo "=== Nautilus Trader Development Environment ==="
echo "Rust version: $(rustc --version)"
echo "UV version: $(uv --version)"
echo "Working directory: $(pwd)"
echo

echo "=== Setting PyO3 environment ==="
export PYO3_PYTHON=/workspace/.venv/bin/python3
echo "PYO3_PYTHON: $PYO3_PYTHON"
echo

echo "=== Development environment ready! ==="
echo "You can now run for example:"
echo "  make install-debug                                            # Install nautilus in debug mode"
echo "  make cargo-test                                               # Test Rust code"
echo "  make pytest                                                   # Run Python tests"
echo "  uv run python -c \"import nautilus_trader.backtest.engine;\"    # Run a Python instruction"
echo

# If no command is provided, check if we have a TTY and start appropriate shell
if [ $# -eq 0 ]; then
  if [ -t 0 ]; then
    echo "Starting interactive shell..."
    exec bash
  else
    echo "No TTY detected. Use docker run -it for interactive mode."
    echo "Container ready for commands. Example:"
    echo "  docker run --rm -itv \"\$(pwd)\":/workspace nautilus-dev"
  fi
else
  exec "$@"
fi
```


---

## Overview

This file is located at `.docker/entrypoint.sh` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `.docker`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


