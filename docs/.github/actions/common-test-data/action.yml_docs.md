# Documentation: action.yml

## File Metadata

- **Path**: `.github/actions/common-test-data/action.yml`
- **Size**: 938 bytes
- **Lines**: 25
- **Language**: YAML

## Original Source

```yaml
name: common-test-data
description: Common test data caching

runs:
  using: "composite"
  steps:
    - name: Restore test data from cache
      id: cached-testdata-large
      # https://github.com/actions/cache/tree/main/restore
      uses: actions/cache/restore@0057852bfaa89a56745cba8c7296529d2fc39830 # v4.3.0
      with:
        path: tests/test_data/large
        key: large-files-${{ hashFiles('tests/test_data/large/checksums.json') }}
        restore-keys: large-files-
        enableCrossOsArchive: true

    - name: Save test data to cache
      if: ${{ always() && steps.cached-testdata-large.outputs.cache-hit != 'true' }}
      # https://github.com/actions/cache/tree/main/save
      uses: actions/cache/save@0057852bfaa89a56745cba8c7296529d2fc39830 # v4.3.0
      with:
        path: tests/test_data/large
        key: large-files-${{ hashFiles('tests/test_data/large/checksums.json') }}
        enableCrossOsArchive: true

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a YAML configuration file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 3


**Identifiers**: `Common`, `Restore`, `Save`

## Related Files

This file is located in `.github/actions/common-test-data/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest .github/actions/common-test-data/action.yml

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:58.805342Z*
