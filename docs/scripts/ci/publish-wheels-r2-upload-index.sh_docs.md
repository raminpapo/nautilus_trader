# Documentation: `scripts/ci/publish-wheels-r2-upload-index.sh`
**Generated:** 2025-11-15T19:40:05.512153Z
**File Size:** 675 bytes
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

- **Path:** `scripts/ci/publish-wheels-r2-upload-index.sh`
- **Size:** 675 bytes
- **Lines:** 23
- **Extension:** `.sh`
- **Type:** text

---

## Source Code

```bash
#!/usr/bin/env bash
set -euo pipefail

success=false
for i in {1..5}; do
  if aws s3 cp index.html "s3://${CLOUDFLARE_R2_BUCKET_NAME}/${CLOUDFLARE_R2_PREFIX:-simple/nautilus-trader}/index.html" \
    --endpoint-url="${CLOUDFLARE_R2_URL}" \
    --content-type "text/html; charset=utf-8" \
    --cache-control "no-cache, max-age=60, must-revalidate" \
    --cli-connect-timeout 10 --cli-read-timeout 60; then
    echo "Successfully uploaded index.html"
    success=true
    break
  else
    echo "Failed to upload index.html, retrying ($i/5)..."
    sleep $((2 ** i))
  fi
done

if [ "$success" = false ]; then
  echo "Failed to upload index.html after 5 attempts"
  exit 1
fi
```


---

## Overview

This file is located at `scripts/ci/publish-wheels-r2-upload-index.sh` within the repository.


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


