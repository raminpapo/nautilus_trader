# Documentation: osv-scanner.toml

## File Metadata

- **Path**: `osv-scanner.toml`
- **Size**: 2,056 bytes
- **Lines**: 58
- **Language**: TOML

## Original Source

```toml
# OSV-Scanner configuration
# https://google.github.io/osv-scanner/configuration/

# =============================================================================
# Ignored Vulnerabilities
# =============================================================================
# Ignored advisories that are already tracked/accepted in deny.toml or have
# no available fixes. These are acknowledged risks with documented reasons.

[[IgnoredVulns]]
id = "RUSTSEC-2024-0436"
reason = "paste crate is unmaintained but a transitive dependency via alloy"

[[IgnoredVulns]]
id = "RUSTSEC-2024-0379"
reason = "fast-float is transitive via hypersync-client→polars-arrow (optional dependency)"

[[IgnoredVulns]]
id = "RUSTSEC-2025-0003"
reason = "fast-float is transitive via hypersync-client→polars-arrow (optional dependency)"

[[IgnoredVulns]]
id = "RUSTSEC-2024-0388"
reason = "derivative crate is unmaintained, transitive dependency with no available fix"

[[IgnoredVulns]]
id = "RUSTSEC-2023-0071"
reason = "rsa timing sidechannel (Marvin Attack), no fix available, low risk for use case"

[[IgnoredVulns]]
id = "RUSTSEC-2025-0075"
reason = "unic-char-range unmaintained, transitive via pyo3-stub-gen (dev tool only)"

[[IgnoredVulns]]
id = "RUSTSEC-2025-0080"
reason = "unic-ucd-ident unmaintained, transitive via pyo3-stub-gen (dev tool only)"

[[IgnoredVulns]]
id = "RUSTSEC-2025-0081"
reason = "unic-char-property unmaintained, transitive via pyo3-stub-gen (dev tool only)"

[[IgnoredVulns]]
id = "RUSTSEC-2025-0090"
reason = "unic-emoji-char unmaintained, transitive via pyo3-stub-gen (dev tool only)"

[[IgnoredVulns]]
id = "RUSTSEC-2025-0098"
reason = "unic-ucd-version unmaintained, transitive via pyo3-stub-gen (dev tool only)"

[[IgnoredVulns]]
id = "RUSTSEC-2025-0100"
reason = "unic-common unmaintained, transitive via pyo3-stub-gen (dev tool only)"

# Python dependencies
[[IgnoredVulns]]
id = "GHSA-wj6h-64fc-37mp"
reason = "ecdsa Minerva timing attack on P-256, maintainers consider sidechannel attacks out of scope, only affects optional dYdX adapter"

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a TOML configuration file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 3


**Keys**: `id`, `reason`
**Sections**: `[IgnoredVulns`

## Related Files

This file is located in `./`. Related files may include:
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
*Generated on 2025-11-18T21:55:06.038953Z*
