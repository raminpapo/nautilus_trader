# Documentation: package-version.sh

## File Metadata

- **Path**: `scripts/package-version.sh`
- **Size**: 1,574 bytes
- **Lines**: 55
- **Language**: Shell

## Original Source

```bash
#!/usr/bin/env bash
set -euo pipefail

# Resolve pyproject.toml relative to this script's location
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYPROJECT_FILE="${SCRIPT_DIR}/../pyproject.toml"

# Check that pyproject.toml exists
if [[ ! -f "$PYPROJECT_FILE" ]]; then
  echo "Error: pyproject.toml not found at $PYPROJECT_FILE" >&2
  exit 1
fi

# Detect available Python interpreter (honor PYTHON env var, then probe common names)
detect_python() {
  if [[ -n "${PYTHON:-}" ]] && command -v "$PYTHON" &> /dev/null; then
    echo "$PYTHON"
  elif command -v python3 &> /dev/null; then
    echo "python3"
  elif command -v python &> /dev/null; then
    echo "python"
  elif command -v py &> /dev/null; then
    # Windows py launcher
    echo "py -3"
  else
    return 1
  fi
}

# Try to parse using Python's `tomllib` (Python 3.11+) if available
PYTHON_CMD=$(detect_python 2> /dev/null) || PYTHON_CMD=""

if [[ -n "$PYTHON_CMD" ]] && $PYTHON_CMD -c "import tomllib" &> /dev/null; then
  VERSION=$($PYTHON_CMD -c "
import tomllib
with open('$PYPROJECT_FILE', 'rb') as f:
    data = tomllib.load(f)
print(data['project']['version'])
" | tr -d '\n\r ')
else
  # Fallback: grep & sed one-liner (works without Python)
  VERSION=$(grep -E '^version\s*=' "$PYPROJECT_FILE" |
    sed -E 's/^version\s*=\s*\"([^\"]*)\".*/\1/' |
    tr -d '\n\r ')
fi

# Validate that we got a version
if [[ -z "$VERSION" ]]; then
  echo "Error: Could not extract version from $PYPROJECT_FILE" >&2
  exit 1
fi

# Output version (without trailing newline for consistency)
echo -n "$VERSION"

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 17


**Identifiers**: `BASH_SOURCE`, `Check`, `Could`, `Detect`, `Error`, `Fallback`, `Output`, `PYPROJECT_FILE`, `PYTHON`, `PYTHON_CMD`, `Python`, `Resolve`, `SCRIPT_DIR`, `Try`, `VERSION`, `Validate`, `Windows`

## Related Files

This file is located in `scripts/`. Related files may include:
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
*Generated on 2025-11-18T21:55:06.161040Z*
