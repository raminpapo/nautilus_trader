# Documentation: publish-wheels-delete-artifacts.sh

## File Metadata

- **Path**: `scripts/ci/publish-wheels-delete-artifacts.sh`
- **Size**: 1,631 bytes
- **Lines**: 55
- **Language**: Shell

## Original Source

```bash
#!/usr/bin/env bash
set -euo pipefail

echo "Fetching artifacts for the current run"

response=$(curl -sS --retry 5 --retry-delay 2 --retry-all-errors --connect-timeout 5 --max-time 60 \
  -H "Authorization: Bearer ${GITHUB_TOKEN}" \
  -H "Accept: application/vnd.github+json" \
  "https://api.github.com/repos/${GITHUB_REPOSITORY}/actions/runs/${GITHUB_RUN_ID}/artifacts")

# Extract artifact IDs
ids=$(echo "$response" | jq -r '.artifacts[].id // empty')
if [[ -z "$ids" ]]; then
  echo "No artifact IDs found for the current run"
  exit 0
fi

echo "Artifact IDs to delete: $ids"

# Delete artifacts
for id in $ids; do
  echo "Deleting artifact ID $id"
  attempts=0
  while true; do
    attempts=$((attempts + 1))
    status=$(curl -sS --connect-timeout 5 --max-time 60 -o /dev/null -w "%{http_code}" -X DELETE \
      -H "Authorization: Bearer ${GITHUB_TOKEN}" \
      -H "Accept: application/vnd.github+json" \
      "https://api.github.com/repos/${GITHUB_REPOSITORY}/actions/artifacts/$id")

    if [ "$status" -eq 204 ]; then
      echo "Successfully deleted artifact ID $id"
      break
    fi

    # 404 means already gone – treat as success
    if [ "$status" -eq 404 ]; then
      echo "Artifact ID $id already deleted (404)"
      break
    fi

    # Retry on 5xx up to 5 attempts; fail on persistent 4xx
    if [ "$status" -ge 500 ] && [ $attempts -lt 5 ]; then
      echo "Delete failed for $id (HTTP $status), retrying ($attempts/5)..."
      sleep $((2 ** attempts))
      continue
    fi

    echo "Failed to delete artifact ID $id (HTTP $status)"
    exit 1
  done
done

echo "Artifact deletion process completed"

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 17


**Identifiers**: `Accept`, `Artifact`, `Authorization`, `Bearer`, `DELETE`, `Delete`, `Deleting`, `Extract`, `Failed`, `Fetching`, `GITHUB_REPOSITORY`, `GITHUB_RUN_ID`, `GITHUB_TOKEN`, `HTTP`, `IDs`, `Retry`, `Successfully`

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
*Generated on 2025-11-18T21:55:06.144435Z*
