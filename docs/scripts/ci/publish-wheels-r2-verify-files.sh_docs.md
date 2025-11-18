# Documentation: publish-wheels-r2-verify-files.sh

## File Metadata

- **Path**: `scripts/ci/publish-wheels-r2-verify-files.sh`
- **Size**: 1,079 bytes
- **Lines**: 39
- **Language**: Shell

## Original Source

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

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 10


**Identifiers**: `CLOUDFLARE_R2_BUCKET_NAME`, `CLOUDFLARE_R2_PREFIX`, `CLOUDFLARE_R2_URL`, `Cloudflare`, `Could`, `Error`, `Failed`, `Verification`, `Verify`, `Verifying`

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
*Generated on 2025-11-18T21:55:06.150933Z*
