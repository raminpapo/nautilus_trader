# Documentation: action.yml

## File Metadata

- **Path**: `.github/actions/upload-artifact-wheel/action.yml`
- **Size**: 1,362 bytes
- **Lines**: 38
- **Language**: YAML

## Original Source

```yaml
name: Upload wheel artifact to GitHub Actions
description: Upload wheel artifact to GitHub Actions

runs:
  using: "composite"
  steps:
    - name: Set release output
      shell: bash
      if:
        github.event_name == 'push' && (github.ref_name == 'develop' || github.ref_name ==
        'nightly' || github.ref_name == 'master' || github.ref_name == 'test-ci')
      id: vars
      run: |
        if [ ! -d "./dist" ]; then
          echo "Error: dist directory not found"
          exit 1
        fi

        ASSET_PATH=$(find ./dist -name "nautilus_trader-*.whl" -type f | xargs ls -t 2>/dev/null | head -n 1)

        if [ -z "$ASSET_PATH" ]; then
          echo "Error: No nautilus_trader wheel files found in dist directory"
          exit 1
        fi

        echo "ASSET_NAME=$(basename "$ASSET_PATH")" >> $GITHUB_ENV

    - name: Upload wheel artifact
      if:
        github.event_name == 'push' && (github.ref_name == 'develop' || github.ref_name ==
        'nightly' || github.ref_name == 'master' || github.ref_name == 'test-ci')
      # https://github.com/actions/upload-artifact
      # Use wildcard to flatten dist/ prefix: path before first wildcard is stripped
      uses: actions/upload-artifact@330a01c490aca151604b8cf639adc76d48f6c5d4 # v5.0.0
      with:
        name: ${{ env.ASSET_NAME }}
        path: dist/nautilus_trader-*.whl

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a YAML configuration file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 9


**Identifiers**: `ASSET_NAME`, `ASSET_PATH`, `Actions`, `Error`, `GITHUB_ENV`, `GitHub`, `Set`, `Upload`, `Use`

## Related Files

This file is located in `.github/actions/upload-artifact-wheel/`. Related files may include:
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
*Generated on 2025-11-18T21:54:58.808873Z*
