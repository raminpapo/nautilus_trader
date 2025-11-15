# Documentation: `scripts/ci/publish-wheels-r2-verify-files.sh`
**Generated:** 2025-11-15T19:40:05.514462Z
**File Size:** 1079 bytes
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

- **Path:** `scripts/ci/publish-wheels-r2-verify-files.sh`
- **Size:** 1,079 bytes
- **Lines:** 38
- **Extension:** `.sh`
- **Type:** text

---

## Source Code

```bash
#!/usr/bin/env bash
set -euo pipefail

echo "Verifying uploaded files in Cloudflare R2..."

ok=false
for i in {1..5}; do
  if aws s3 ls "s3://${CLOUDFLARE_R2_BUCKET_NAME}/${CLOUDFLARE_R2_PREFIX:-simple/nautilus-trader}/" \
    --endpoint-url="${CLOUDFLARE_R2_URL}" --cli-connect-timeout 10 --cli-read-timeout 60; then
    ok=true
    break
  else
    echo "Failed to list files in R2 bucket, retrying ($i/5)..."
    sleep $((2 ** i))
  fi
done
if [ "$ok" = false ]; then
  echo "Error: Could not list files in R2 bucket after retries"
  exit 1
fi

# Verify index.html exists
ok_index=false
for i in {1..5}; do
  if aws s3 ls "s3://${CLOUDFLARE_R2_BUCKET_NAME}/${CLOUDFLARE_R2_PREFIX:-simple/nautilus-trader}/index.html" \
    --endpoint-url="${CLOUDFLARE_R2_URL}" --cli-connect-timeout 10 --cli-read-timeout 60; then
    ok_index=true
    break
  else
    echo "index.html not found yet, retrying ($i/5)..."
    sleep $((2 ** i))
  fi
done
if [ "$ok_index" = false ]; then
  echo "Error: index.html not found in R2 bucket after retries"
  exit 1
fi
echo "Verification completed"
```


---

## Overview

This file is located at `scripts/ci/publish-wheels-r2-verify-files.sh` within the repository.


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


