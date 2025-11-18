# Documentation: test-coverage.sh

## File Metadata

- **Path**: `scripts/test-coverage.sh`
- **Size**: 1,007 bytes
- **Lines**: 36
- **Language**: Shell

## Original Source

```bash
#!/bin/bash
set -eo pipefail

# Function to update Cython version in pyproject.toml
update_cython_version() {
  local old_version="3.1.3"
  local new_version="3.0.11"

  # Create backup of original file
  cp pyproject.toml pyproject.toml.bak

  # Update all occurrences of the pinned Cython version (case-insensitive on "cython")
  # Example matches: "cython==3.1.3" or "Cython==3.1.3"
  if sed -i.tmp \
    -e "s/[cC]ython==${old_version}/cython==${new_version}/g" \
    pyproject.toml; then
    echo "Updated Cython version to ${new_version}"
    rm -f pyproject.toml.tmp
  else
    echo "Error: Failed to update Cython version in pyproject.toml" >&2
    mv pyproject.toml.bak pyproject.toml
    exit 1
  fi
}

# TODO: Temporarily change Cython version in pyproject.toml while we require v3.0.11 for coverage
update_cython_version
uv lock --no-upgrade

export PROFILE_MODE=true
uv sync --all-groups --all-extras
uv run --no-sync pytest \
  --cov-report=term \
  --cov-report=xml \
  --cov=nautilus_trader

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 11


**Identifiers**: `Create`, `Cython`, `Error`, `Example`, `Failed`, `Function`, `PROFILE_MODE`, `TODO`, `Temporarily`, `Update`, `Updated`

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
pytest scripts/test-coverage.sh

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.166962Z*
