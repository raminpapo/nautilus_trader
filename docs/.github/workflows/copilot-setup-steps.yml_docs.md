# Documentation: copilot-setup-steps.yml

## File Metadata

- **Path**: `.github/workflows/copilot-setup-steps.yml`
- **Size**: 1,568 bytes
- **Lines**: 55
- **Language**: YAML

## Original Source

```yaml
name: "Copilot Setup Steps"

on:
  workflow_dispatch:

jobs:
  copilot-setup-steps:
    permissions:
      contents: read
    defaults:
      run:
        shell: bash
    runs-on: ubuntu-22.04
    timeout-minutes: 59
    env:
      BUILD_MODE: debug
      RUST_BACKTRACE: 1
      COPILOT_AGENT_FIREWALL_ALLOW_LIST:
        "crates.io,index.crates.io,static.crates.io,doc.rust-lang.org,docs.rs,datasets.tardis.dev"
    services:
      redis:
        image: public.ecr.aws/docker/library/redis:7.4.5-alpine3.21
        ports:
          - 6379:6379
        options: >-
          --health-cmd "redis-cli ping"
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
      postgres:
        image: public.ecr.aws/docker/library/postgres:16.4-alpine
        env:
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: pass
          POSTGRES_DB: nautilus
        ports:
          - 5432:5432
        options: --health-cmd pg_isready --health-interval 10s --health-timeout 5s --health-retries 5
    steps:
      # https://github.com/step-security/harden-runner
      - uses: step-security/harden-runner@f4a75cfd619ee5ce8d5b864b0d183aff3c69b55a # v2.13.1
        with:
          egress-policy: audit

      - name: Checkout repository
        # https://github.com/actions/checkout
        uses: actions/checkout@08c6903cd8c0fde910a37f88322edcfb5dd907a8 # v5.0.0
        with:
          persist-credentials: false

      - name: Common setup
        uses: ./.github/actions/common-setup
        with:
          python-version: "3.13"

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a YAML configuration file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 11


**Identifiers**: `BUILD_MODE`, `COPILOT_AGENT_FIREWALL_ALLOW_LIST`, `Checkout`, `Common`, `Copilot`, `POSTGRES_DB`, `POSTGRES_PASSWORD`, `POSTGRES_USER`, `RUST_BACKTRACE`, `Setup`, `Steps`

## Related Files

This file is located in `.github/workflows/`. Related files may include:
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
*Generated on 2025-11-18T21:54:58.821314Z*
