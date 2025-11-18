# Documentation: action.yml

## File Metadata

- **Path**: `.github/actions/publish-wheels/action.yml`
- **Size**: 1,889 bytes
- **Lines**: 64
- **Language**: YAML

## Original Source

```yaml
name: Publish wheels (R2)
description: Publish wheels to Cloudflare R2

runs:
  using: "composite"
  steps:
    - name: Configure AWS CLI for Cloudflare R2
      shell: bash
      run: |
        set -euo pipefail
        echo "Configuring AWS CLI for Cloudflare R2..."

        # AWS CLI v2 is pre-installed on GitHub runners
        aws --version

        # Configure credentials for Cloudflare R2
        mkdir -p ~/.aws
        {
          echo "[default]"
          echo "aws_access_key_id=${AWS_ACCESS_KEY_ID}"
          echo "aws_secret_access_key=${AWS_SECRET_ACCESS_KEY}"
        } > ~/.aws/credentials

        {
          echo "[default]"
          echo "region=${CLOUDFLARE_R2_REGION:-auto}"
          echo "output=json"
          echo "s3 ="
          echo "    signature_version = s3v4"
          echo "    addressing_style = path"
          echo "    payload_signing_enabled = false"
          echo "    use_accelerate_endpoint = false"
          echo "    use_dualstack_endpoint = false"
          echo "    use_fips_endpoint = false"
        } > ~/.aws/config

        # Disable metadata lookups to avoid network to IMDS by default
        export AWS_EC2_METADATA_DISABLED=true

    - name: Upload new wheels to Cloudflare R2
      shell: bash
      run: |
        bash ./scripts/ci/publish-wheels-r2-upload-new-wheels.sh

    - name: Remove old wheels from Cloudflare R2
      shell: bash
      run: |
        bash ./scripts/ci/publish-wheels-r2-remove-old-wheels.sh

    - name: Generate index.html
      shell: bash
      run: |
        bash ./scripts/ci/publish-wheels-generate-index.sh

    - name: Upload index.html to Cloudflare R2
      shell: bash
      run: |
        bash ./scripts/ci/publish-wheels-r2-upload-index.sh

    - name: Verify uploaded files in Cloudflare R2
      shell: bash
      run: |
        bash ./scripts/ci/publish-wheels-r2-verify-files.sh

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a YAML configuration file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 17


**Identifiers**: `AWS`, `AWS_ACCESS_KEY_ID`, `AWS_EC2_METADATA_DISABLED`, `AWS_SECRET_ACCESS_KEY`, `CLI`, `CLOUDFLARE_R2_REGION`, `Cloudflare`, `Configure`, `Configuring`, `Disable`, `Generate`, `GitHub`, `IMDS`, `Publish`, `Remove`, `Upload`, `Verify`

## Related Files

This file is located in `.github/actions/publish-wheels/`. Related files may include:
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
*Generated on 2025-11-18T21:54:58.807728Z*
