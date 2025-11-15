# Documentation: `osv-scanner.toml`
**Generated:** 2025-11-15T19:40:05.411092Z
**File Size:** 2060 bytes
**Extension:** .toml
**Type:** text

---

## Table of Contents

1. [File Metadata](#file-metadata)
2. [Source Code](#source-code)
3. [Overview](#overview)
4. [Detailed Analysis](#detailed-analysis)
5. [Usage Examples](#usage-examples)
6. [Related Files](#related-files)
7. [Notes](#notes)

---

## File Metadata

- **Path:** `osv-scanner.toml`
- **Size:** 2,060 bytes
- **Lines:** 57
- **Extension:** `.toml`
- **Type:** text

---

## Source Code

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


---

## Overview

This file is located at `osv-scanner.toml` within the repository.

This is a configuration file.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `.`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


