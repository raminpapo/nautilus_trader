# Documentation: coverage.yml

## File Metadata

- **Path**: `.github/workflows/coverage.yml`
- **Size**: 2,340 bytes
- **Lines**: 77
- **Language**: YAML

## Original Source

```yaml
name: coverage

permissions: # Principle of least privilege
  contents: read
  actions: read

on:
  push:
    branches: [nightly]

jobs:
  build:
    runs-on: ubuntu-latest
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
          python-version: "3.12"

      - name: Install Nautilus CLI
        env:
          NAUTILUS_CLI_FORCE_SOURCE: ${{ github.ref == 'refs/heads/nightly' && '1' || '0' }}
        run: bash scripts/ci/install-nautilus-cli.sh

      - name: Init postgres schema
        run: nautilus database init --schema ${{ github.workspace }}/schema/sql
        env:
          POSTGRES_HOST: localhost
          POSTGRES_PORT: 5432
          POSTGRES_USERNAME: postgres
          POSTGRES_PASSWORD: pass
          POSTGRES_DATABASE: nautilus

      - name: Cached test data
        uses: ./.github/actions/common-test-data

      # TODO: Temporarily pause coverage due runner receiving shutdown signal (OOM/resources)
      # - name: Run tests with coverage
      #   run: bash scripts/test-coverage.sh

      # - name: Upload coverage report
      #   uses: codecov/codecov-action@v4
      #   with:
      #     # fail_ci_if_error: true  # leave commented until flakiness improves
      #     token: ${{ secrets.CODECOV_TOKEN }}
      #     verbose: true

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a YAML configuration file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 22


**Identifiers**: `CLI`, `CODECOV_TOKEN`, `Cached`, `Checkout`, `Common`, `Init`, `Install`, `NAUTILUS_CLI_FORCE_SOURCE`, `Nautilus`, `OOM`, `POSTGRES_DATABASE`, `POSTGRES_DB`, `POSTGRES_HOST`, `POSTGRES_PASSWORD`, `POSTGRES_PORT`, `POSTGRES_USER`, `POSTGRES_USERNAME`, `Principle`, `Run`, `TODO`, `Temporarily`, `Upload`

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

⚠️ **Security**: This file may handle sensitive data. Ensure proper encryption and access controls.

⚠️ **Security**: This file may perform database operations. Use parameterized queries to prevent SQL injection.

---
*Generated on 2025-11-18T21:54:58.822816Z*
