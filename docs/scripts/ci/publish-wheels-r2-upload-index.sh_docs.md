# Documentation: publish-wheels-r2-upload-index.sh

## File Metadata

- **Path**: `scripts/ci/publish-wheels-r2-upload-index.sh`
- **Size**: 675 bytes
- **Lines**: 24
- **Language**: Shell

## Original Source

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

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 5


**Identifiers**: `CLOUDFLARE_R2_BUCKET_NAME`, `CLOUDFLARE_R2_PREFIX`, `CLOUDFLARE_R2_URL`, `Failed`, `Successfully`

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
*Generated on 2025-11-18T21:55:06.148616Z*
