# Documentation: `scripts/ci/publish-cli-r2-verify.sh`
**Generated:** 2025-11-15T19:40:05.506556Z
**File Size:** 597 bytes
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

- **Path:** `scripts/ci/publish-cli-r2-verify.sh`
- **Size:** 597 bytes
- **Lines:** 15
- **Extension:** `.sh`
- **Type:** text

---

## Source Code

```bash
#!/usr/bin/env bash
set -euo pipefail

PREFIX=${CLOUDFLARE_R2_PREFIX:-cli/nautilus-cli}
BUCKET=${CLOUDFLARE_R2_BUCKET_NAME:?}
R2_URL=${CLOUDFLARE_R2_URL:?}

echo "Verifying contents at s3://${BUCKET}/${PREFIX}/latest/"
aws s3 ls "s3://${BUCKET}/${PREFIX}/latest/" --endpoint-url="$R2_URL" || true

echo "Checking installer presence (stable + latest)"
aws s3 ls "s3://${BUCKET}/${PREFIX}/install.sh" --endpoint-url="$R2_URL" || echo "install.sh (stable) not found"
aws s3 ls "s3://${BUCKET}/${PREFIX}/latest/install.sh" --endpoint-url="$R2_URL" || echo "install.sh (latest) not found"

echo "Done"
```


---

## Overview

This file is located at `scripts/ci/publish-cli-r2-verify.sh` within the repository.


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


