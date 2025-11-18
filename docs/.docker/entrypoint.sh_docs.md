# Documentation: entrypoint.sh

## File Metadata

- **Path**: `.docker/entrypoint.sh`
- **Size**: 1,218 bytes
- **Lines**: 36
- **Language**: Shell

## Original Source

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

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 20


**Identifiers**: `Container`, `Development`, `DockerfileUbuntu`, `Environment`, `Example`, `Install`, `Nautilus`, `PYO3_PYTHON`, `PyO3`, `Python`, `Run`, `Rust`, `Setting`, `Starting`, `TTY`, `Test`, `Trader`, `Use`, `Working`, `You`

## Related Files

This file is located in `.docker/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

Tests for this file may be located in:
- `tests/` directory in the same folder
- Corresponding test module in the project

Run the full test suite to verify functionality.

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:58.790122Z*
