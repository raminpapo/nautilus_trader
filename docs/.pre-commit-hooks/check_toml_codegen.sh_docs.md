# Documentation: `.pre-commit-hooks/check_toml_codegen.sh`
**Generated:** 2025-11-15T19:40:00.233241Z
**File Size:** 260 bytes
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

- **Path:** `.pre-commit-hooks/check_toml_codegen.sh`
- **Size:** 260 bytes
- **Lines:** 13
- **Extension:** `.sh`
- **Type:** text

---

## Source Code

```bash
#!/usr/bin/env bash

# Check for "codegen-backend" in TOML files
EXIT_CODE=0

for file in "$@"; do
  if grep -q "codegen-backend" "$file"; then
    echo "ERROR: $file contains the forbidden keyword 'codegen-backend'"
    EXIT_CODE=1
  fi
done

exit $EXIT_CODE
```


---

## Overview

This file is located at `.pre-commit-hooks/check_toml_codegen.sh` within the repository.


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


