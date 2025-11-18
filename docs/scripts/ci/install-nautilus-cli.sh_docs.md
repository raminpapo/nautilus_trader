# Documentation: install-nautilus-cli.sh

## File Metadata

- **Path**: `scripts/ci/install-nautilus-cli.sh`
- **Size**: 1,163 bytes
- **Lines**: 30
- **Language**: Shell

## Original Source

```bash
#!/usr/bin/env bash
set -euo pipefail

# Install Nautilus CLI from prebuilt tarball with retries.
# Falls back to building from source if needed.
# Set NAUTILUS_CLI_FORCE_SOURCE=1 to always build from source (e.g., on nightly branch).

BIN_DIR="${BIN_DIR:-"$HOME/.local/bin"}"
export PATH="$BIN_DIR:$PATH"

INSTALL_URL="https://packages.nautechsystems.io/cli/nautilus-cli/install.sh"

# Check if forced to build from source
if [ "${NAUTILUS_CLI_FORCE_SOURCE:-0}" = "1" ]; then
  echo "Building Nautilus CLI from source (NAUTILUS_CLI_FORCE_SOURCE=1)..."
  cargo install -q --path crates/cli --bin nautilus --locked --force --root "$HOME/.local"
else
  echo "Installing Nautilus CLI to $BIN_DIR..."
  if ! curl -fL --connect-timeout 10 --retry 5 --retry-delay 2 --retry-max-time 60 --retry-all-errors "$INSTALL_URL" | bash -s -- -b "$BIN_DIR"; then
    if command -v nautilus > /dev/null 2>&1; then
      echo "Installer exit ignored (known cleanup trap bug)"
    else
      echo "Prebuilt install failed; building CLI from source..."
      cargo install -q --path crates/cli --bin nautilus --locked --force --root "$HOME/.local"
    fi
  fi
fi

nautilus --version

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 15


**Identifiers**: `BIN_DIR`, `Building`, `CLI`, `Check`, `Falls`, `HOME`, `INSTALL_URL`, `Install`, `Installer`, `Installing`, `NAUTILUS_CLI_FORCE_SOURCE`, `Nautilus`, `PATH`, `Prebuilt`, `Set`

## Related Files

This file is located in `scripts/ci/`. Related files may include:
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
*Generated on 2025-11-18T21:55:06.137372Z*
