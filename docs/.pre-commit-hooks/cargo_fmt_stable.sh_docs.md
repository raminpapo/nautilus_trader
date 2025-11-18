# Documentation: cargo_fmt_stable.sh

## File Metadata

- **Path**: `.pre-commit-hooks/cargo_fmt_stable.sh`
- **Size**: 600 bytes
- **Lines**: 28
- **Language**: Shell

## Original Source

```bash
#!/usr/bin/env bash
set -euo pipefail

# Run cargo fmt while forcing rustfmt to read an empty config
# to avoid nightly-only options in the repository rustfmt.toml.

tmpdir="$(mktemp -d)"
cleanup() { rm -rf "$tmpdir"; }
trap cleanup EXIT

# Create an empty rustfmt.toml in the temp directory
touch "$tmpdir/rustfmt.toml"

# Forward all args; ensure rustfmt-specific flags come after '--'
has_dd=false
for arg in "$@"; do
  if [[ "$arg" == "--" ]]; then
    has_dd=true
    break
  fi
done

if $has_dd; then
  cargo fmt "$@" --config-path "$tmpdir"
else
  cargo fmt "$@" -- --config-path "$tmpdir"
fi

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 4


**Identifiers**: `Create`, `EXIT`, `Forward`, `Run`

## Related Files

This file is located in `.pre-commit-hooks/`. Related files may include:
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
*Generated on 2025-11-18T21:54:58.839137Z*
