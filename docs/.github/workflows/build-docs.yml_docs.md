# Documentation: build-docs.yml

## File Metadata

- **Path**: `.github/workflows/build-docs.yml`
- **Size**: 951 bytes
- **Lines**: 30
- **Language**: YAML

## Original Source

```yaml
name: build-docs

permissions: # Principle of least privilege
  contents: read
  actions: read

on:
  push:
    branches: [master, nightly]

jobs:
  build-docs:
    runs-on: ubuntu-latest
    steps:
      # https://github.com/step-security/harden-runner
      - uses: step-security/harden-runner@f4a75cfd619ee5ce8d5b864b0d183aff3c69b55a # v2.13.1
        with:
          egress-policy: audit

      - name: Fire event to nautilus_docs
        run: |
          curl -sS -L --retry 5 --retry-delay 2 --retry-all-errors --connect-timeout 5 --max-time 60 --fail-with-body \
            -X POST \
            -H "Accept: application/vnd.github+json" \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer ${{ secrets.REPOSITORY_ACCESS_TOKEN }}" \
            -H "X-GitHub-Api-Version: 2022-11-28" \
            https://api.github.com/repos/nautechsystems/nautilus_docs/dispatches \
            -d '{"event_type":"push"}'

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a YAML configuration file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 12


**Identifiers**: `Accept`, `Api`, `Authorization`, `Bearer`, `Content`, `Fire`, `GitHub`, `POST`, `Principle`, `REPOSITORY_ACCESS_TOKEN`, `Type`, `Version`

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
*Generated on 2025-11-18T21:54:58.811173Z*
