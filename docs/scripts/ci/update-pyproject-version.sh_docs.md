# Documentation: update-pyproject-version.sh

## File Metadata

- **Path**: `scripts/ci/update-pyproject-version.sh`
- **Size**: 1,082 bytes
- **Lines**: 35
- **Language**: Shell

## Original Source

```bash
#!/usr/bin/env bash
set -euo pipefail

current_version=$(grep '^version = ' pyproject.toml | cut -d '"' -f2)
if [[ -z "$current_version" ]]; then
  echo "Error: Failed to extract version from pyproject.toml" >&2
  exit 1
fi

branch_name="${GITHUB_REF_NAME}" # Get the branch name
echo "Branch name: ${branch_name}"
base_version=$(echo "$current_version" | sed -E 's/(\.dev[0-9]{8}\+[0-9]+|a[0-9]{8})$//')

suffix=""
if [[ "$branch_name" == "develop" ]]; then
  # Develop branch: use dev versioning with build number
  suffix=".dev$(date +%Y%m%d)+${GITHUB_RUN_NUMBER}"
elif [[ "$branch_name" == "nightly" ]]; then
  # Nightly branch: use alpha versioning
  suffix="a$(date +%Y%m%d)"
else
  echo "Not modifying version"
fi

if [[ -n "$suffix" && "$current_version" != *"$suffix"* ]]; then
  new_version="${base_version}${suffix}"
  if sed -i.bak "s/^version = \".*\"/version = \"${new_version}\"/" pyproject.toml; then
    echo "Version updated to ${new_version}"
    rm -f pyproject.toml.bak
  else
    echo "Error: Failed to update version in pyproject.toml" >&2
    exit 1
  fi
fi

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 10


**Identifiers**: `Branch`, `Develop`, `Error`, `Failed`, `GITHUB_REF_NAME`, `GITHUB_RUN_NUMBER`, `Get`, `Nightly`, `Not`, `Version`

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
*Generated on 2025-11-18T21:55:06.152628Z*
