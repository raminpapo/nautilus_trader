# Documentation: deny.toml

## File Metadata

- **Path**: `deny.toml`
- **Size**: 4,771 bytes
- **Lines**: 129
- **Language**: TOML

## Original Source

```toml
# cargo-deny configuration
# https://embarkstudios.github.io/cargo-deny/

# =============================================================================
# Dependency Graph Configuration
# =============================================================================
[graph]
all-features = false
no-default-features = false

[output]
feature-depth = 1

# =============================================================================
# Security Advisories
# =============================================================================
[advisories]
# Ignored advisories (use sparingly - document the reason)
ignore = [
  # paste is unmaintained but pulled in transitively via alloy (blockchain dependencies)
  # TODO: Monitor https://github.com/alloy-rs/alloy for migration to pastey or alternative
  { id = "RUSTSEC-2024-0436", reason = "paste crate is unmaintained but a transitive dependency via alloy" },

  # fast-float has soundness issues and is unmaintained, pulled in via hypersync-client
  # hypersync-client is optional (feature flag), so advisory only applies when feature is enabled
  # TODO: Monitor https://github.com/enviodev/hypersync-client-rust for polars upgrade
  # Consider migrating to fast-float2 fork once hypersync-client updates
  { id = "RUSTSEC-2024-0379", reason = "fast-float is transitive via hypersync-client→polars-arrow (optional dependency)" },
  { id = "RUSTSEC-2025-0003", reason = "fast-float is transitive via hypersync-client→polars-arrow (optional dependency)" },

  # unic-* crates are unmaintained, pulled in via pyo3-stub-gen→rustpython-parser
  # This is dev-time only for generating .pyi stub files, not a runtime security risk
  # TODO: Monitor https://github.com/Jij-Inc/pyo3-stub-gen for migration away from rustpython-parser
  { id = "RUSTSEC-2025-0075", reason = "unic-char-range unmaintained, transitive via pyo3-stub-gen (dev tool only)" },
  { id = "RUSTSEC-2025-0080", reason = "unic-ucd-ident unmaintained, transitive via pyo3-stub-gen (dev tool only)" },
  { id = "RUSTSEC-2025-0081", reason = "unic-char-property unmaintained, transitive via pyo3-stub-gen (dev tool only)" },
  { id = "RUSTSEC-2025-0090", reason = "unic-emoji-char unmaintained, transitive via pyo3-stub-gen (dev tool only)" },
  { id = "RUSTSEC-2025-0098", reason = "unic-ucd-version unmaintained, transitive via pyo3-stub-gen (dev tool only)" },
  { id = "RUSTSEC-2025-0100", reason = "unic-common unmaintained, transitive via pyo3-stub-gen (dev tool only)" },
]

# =============================================================================
# License Configuration
# =============================================================================
[licenses]
# Licenses compatible with LGPL-3.0
allow = [
  "MIT",
  "Apache-2.0",
  "Apache-2.0 WITH LLVM-exception",
  "BSD-2-Clause",
  "BSD-2-Clause-Patent",
  "BSD-3-Clause",
  "BSL-1.0",
  "ISC",
  "MPL-2.0",
  "CC0-1.0",
  "CDLA-Permissive-2.0",
  "Zlib",
  "Unicode-DFS-2016",
  "Unicode-3.0",
  "0BSD",
  "LGPL-3.0",
  "LGPL-3.0-only",
  "LGPL-3.0-or-later",
  "OpenSSL",
  "Unlicense",
]

confidence-threshold = 0.8

# Clarify licenses for crates with missing/incorrect license metadata
[[licenses.clarify]]
name = "implied-vol"
version = "*"
expression = "MIT"
license-files = [{ path = "LICENSE", hash = 0xb0803f0e }]

[licenses.private]
# Ignore workspace crates that aren't published
# Note: All workspace crates in this project are LGPL-3.0 (project license)
# If adding workspace crates with different licenses, set this to false
ignore = true
registries = []

# =============================================================================
# Banned/Duplicate Crates
# =============================================================================
[bans]
# Warn on multiple versions of the same crate
# TODO: Currently 35 duplicate warnings - schedule cleanup then change to "deny"
# Common duplicates: base64, darling, hashbrown, getrandom, rand
multiple-versions = "warn"

# Deny wildcard version requirements (*)
# Prevents uncontrolled version drift and supply-chain attacks
wildcards = "deny"

highlight = "all"

workspace-default-features = "allow"
external-default-features = "allow"

# Explicitly allowed crates (use with care)
allow = []

# Explicitly denied crates
deny = []

# Skip certain crates during duplicate detection
skip = []
skip-tree = []

# =============================================================================
# Dependency Sources
# =============================================================================
[sources]
# Only allow dependencies from crates.io
unknown-registry = "deny"
unknown-git = "deny"

allow-registry = ["https://github.com/rust-lang/crates.io-index"]
allow-git = []

[sources.allow-org]
github = []
gitlab = []
bitbucket = []

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a TOML configuration file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 35


**Keys**: `all-features`, `allow`, `allow-git`, `allow-registry`, `bitbucket`, `confidence-threshold`, `deny`, `expression`, `external-default-features`, `feature-depth`, `github`, `gitlab`, `highlight`, `ignore`, `license-files`, `multiple-versions`, `name`, `no-default-features`, `registries`, `skip`, `skip-tree`, `unknown-git`, `unknown-registry`, `version`, `wildcards`, `workspace-default-features`
**Sections**: `[licenses.clarify`, `advisories`, `bans`, `graph`, `licenses`, `licenses.private`, `output`, `sources`, `sources.allow-org`

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
*Generated on 2025-11-18T21:55:04.200222Z*
