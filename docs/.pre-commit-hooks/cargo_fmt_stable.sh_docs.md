# Documentation: `.pre-commit-hooks/cargo_fmt_stable.sh`
**Generated:** 2025-11-15T19:40:00.224675Z
**File Size:** 600 bytes
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

- **Path:** `.pre-commit-hooks/cargo_fmt_stable.sh`
- **Size:** 600 bytes
- **Lines:** 27
- **Extension:** `.sh`
- **Type:** text

---

## Source Code

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


---

## Overview

This file is located at `.pre-commit-hooks/cargo_fmt_stable.sh` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `.pre-commit-hooks`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


