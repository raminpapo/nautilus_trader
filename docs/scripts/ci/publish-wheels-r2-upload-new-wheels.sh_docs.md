# Documentation: publish-wheels-r2-upload-new-wheels.sh

## File Metadata

- **Path**: `scripts/ci/publish-wheels-r2-upload-new-wheels.sh`
- **Size**: 1,458 bytes
- **Lines**: 61
- **Language**: Shell

## Original Source

```bash
#!/usr/bin/env bash
set -euo pipefail

echo "Uploading new wheels to Cloudflare R2..."

echo "dist/ contents:"
ls -la dist/
find dist/ -type f -name "nautilus_trader-*.whl" -ls

# Verify wheels exist
if ! find dist/ -type f -name "nautilus_trader-*.whl" -print -quit | grep -q .; then
  echo "ERROR: No wheels found in dist/"
  exit 1
fi

wheel_count=0
for file in dist/nautilus_trader-*.whl; do
  echo "File details for $file:"
  ls -l "$file"
  file "$file"

  if [ ! -f "$file" ]; then
    echo "Warning: '$file' is not a regular file, skipping"
    continue
  fi

  wheel_count=$((wheel_count + 1))
  echo "Found wheel: $file"
  echo "sha256:$(sha256sum "$file" | awk '{print $1}')"

  echo "Uploading $file..."
  set +e
  success=false
  for i in {1..5}; do
    aws s3 cp "$file" "s3://${CLOUDFLARE_R2_BUCKET_NAME}/${CLOUDFLARE_R2_PREFIX:-simple/nautilus-trader}/" \
      --endpoint-url="${CLOUDFLARE_R2_URL}" \
      --content-type "application/zip"
    status=$?
    if [ $status -eq 0 ]; then
      echo "Successfully uploaded $file"
      success=true
      break
    else
      echo "Upload failed for $file (exit=$status), retrying ($i/5)..."
      sleep $((2 ** i))
    fi
  done
  set -e
  if [ "$success" = false ]; then
    echo "Failed to upload $file after 5 attempts"
    exit 1
  fi
done

if [ "$wheel_count" -eq 0 ]; then
  echo "No wheel files found in dist directory"
  exit 1
fi

echo "Successfully uploaded $wheel_count wheel files"

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 13


**Identifiers**: `CLOUDFLARE_R2_BUCKET_NAME`, `CLOUDFLARE_R2_PREFIX`, `CLOUDFLARE_R2_URL`, `Cloudflare`, `ERROR`, `Failed`, `File`, `Found`, `Successfully`, `Upload`, `Uploading`, `Verify`, `Warning`

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
*Generated on 2025-11-18T21:55:06.149743Z*
