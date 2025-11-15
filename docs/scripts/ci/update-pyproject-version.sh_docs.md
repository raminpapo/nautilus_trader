# Documentation: `scripts/ci/update-pyproject-version.sh`
**Generated:** 2025-11-15T19:40:05.515516Z
**File Size:** 1082 bytes
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

- **Path:** `scripts/ci/update-pyproject-version.sh`
- **Size:** 1,082 bytes
- **Lines:** 34
- **Extension:** `.sh`
- **Type:** text

---

## Source Code

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


---

## Overview

This file is located at `scripts/ci/update-pyproject-version.sh` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `scripts/ci`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


