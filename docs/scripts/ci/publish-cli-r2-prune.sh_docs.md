# Documentation: publish-cli-r2-prune.sh

## File Metadata

- **Path**: `scripts/ci/publish-cli-r2-prune.sh`
- **Size**: 2,237 bytes
- **Lines**: 76
- **Language**: Shell

## Original Source

```bash
#!/usr/bin/env bash
set -euo pipefail

echo "Pruning old CLI versions in Cloudflare R2..."

PREFIX=${CLOUDFLARE_R2_PREFIX:-cli/nautilus-cli}
BUCKET=${CLOUDFLARE_R2_BUCKET_NAME:?CLOUDFLARE_R2_BUCKET_NAME not set}
R2_URL=${CLOUDFLARE_R2_URL:?CLOUDFLARE_R2_URL not set}
BRANCH_NAME="${GITHUB_REF_NAME:-}"

KEEP_DEVELOP=1
KEEP_NIGHTLY=30

# Collect version directories (exclude 'latest')
mapfile -t dirs < <(aws s3 ls "s3://${BUCKET}/${PREFIX}/" --endpoint-url="$R2_URL" --cli-connect-timeout 10 --cli-read-timeout 60 | awk '/PRE/ {print $2}' | sed 's:/$::' | grep -v '^latest$' || true)

if [[ ${#dirs[@]} -eq 0 ]]; then
  echo "No version directories found; nothing to prune."
  exit 0
fi

# Sort lexicographically; dev/nightly names include date and generally increase
mapfile -t sorted < <(printf '%s\n' "${dirs[@]}" | sort)

keep=$KEEP_DEVELOP
if [[ "$BRANCH_NAME" == "nightly" ]]; then
  keep=$KEEP_NIGHTLY
fi

to_delete=()
if ((${#sorted[@]} > keep)); then
  count=$((${#sorted[@]} - keep))
  for ((i = 0; i < count; i++)); do
    to_delete+=("${sorted[$i]}")
  done
fi

if [[ ${#to_delete[@]} -eq 0 ]]; then
  echo "Nothing to prune; keeping last $keep versions."
  exit 0
fi

echo "Deleting ${#to_delete[@]} old version directories:"
printf '  %s\n' "${to_delete[@]}"

had_failures=false
for d in "${to_delete[@]}"; do
  echo "Removing s3://${BUCKET}/${PREFIX}/${d}/"
  success=false
  for i in {1..5}; do
    if aws s3 rm "s3://${BUCKET}/${PREFIX}/${d}/" --recursive --endpoint-url="$R2_URL" --cli-connect-timeout 10 --cli-read-timeout 60; then
      success=true
      break
    else
      echo "Delete failed for ${d}, retrying ($i/5)..."
      sleep $((2 ** i))
    fi
  done
  if [ "$success" = false ]; then
    # Accept concurrent deletion: treat as success if the directory is now empty
    if aws s3 ls "s3://${BUCKET}/${PREFIX}/${d}/" --recursive --endpoint-url="$R2_URL" --cli-connect-timeout 10 --cli-read-timeout 60 | grep -q .; then
      echo "Error: failed to delete ${d} after retries (still present)"
      had_failures=true
    else
      echo "${d} already gone (treated as success)"
    fi
  fi
done

if [ "$had_failures" = true ]; then
  echo "Prune completed with failures"
  exit 1
fi

echo "Prune complete"

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 23


**Identifiers**: `Accept`, `BRANCH_NAME`, `BUCKET`, `CLI`, `CLOUDFLARE_R2_BUCKET_NAME`, `CLOUDFLARE_R2_PREFIX`, `CLOUDFLARE_R2_URL`, `Cloudflare`, `Collect`, `Delete`, `Deleting`, `Error`, `GITHUB_REF_NAME`, `KEEP_DEVELOP`, `KEEP_NIGHTLY`, `Nothing`, `PRE`, `PREFIX`, `Prune`, `Pruning`, `R2_URL`, `Removing`, `Sort`

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
*Generated on 2025-11-18T21:55:06.140442Z*
