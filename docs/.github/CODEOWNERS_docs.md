# Documentation: CODEOWNERS

## File Metadata

- **Path**: `.github/CODEOWNERS`
- **Size**: 4,309 bytes
- **Lines**: 84
- **Language**: Unknown

## Original Source

```
# =============================================================================
# NautilusTrader Code Owners
# =============================================================================
# These files require explicit review to prevent supply chain attacks,
# configuration errors, and unauthorized changes to critical infrastructure.
#
# More info: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners

# =============================================================================
# GitHub Actions & Workflows - HIGH SECURITY RISK
# =============================================================================
/.github/workflows/              @nautechsystems/core
/.github/actions/                @nautechsystems/core
/.github/dependabot.yml          @nautechsystems/core
/.github/CODEOWNERS              @nautechsystems/core

# =============================================================================
# Rust Build & Dependencies - SUPPLY CHAIN RISK
# =============================================================================
/Cargo.toml                      @nautechsystems/core
/Cargo.lock                      @nautechsystems/core
/crates/Cargo.toml               @nautechsystems/core
/crates/**/Cargo.toml            @nautechsystems/core
/.cargo/config.toml              @nautechsystems/core
/rust-toolchain.toml             @nautechsystems/core
/deny.toml                       @nautechsystems/core

# =============================================================================
# Python Build & Dependencies - SUPPLY CHAIN RISK
# =============================================================================
# Root Python project
/pyproject.toml                  @nautechsystems/core
/uv.lock                         @nautechsystems/core

# Python nautilus_trader v2 system
/python/pyproject.toml           @nautechsystems/core
/python/uv.lock                  @nautechsystems/core

# =============================================================================
# Build & CI Configuration
# =============================================================================
/Makefile                        @nautechsystems/core
/.config/nextest.toml            @nautechsystems/core

# =============================================================================
# Code Quality & Formatting Configuration
# =============================================================================
/.pre-commit-config.yaml         @nautechsystems/core
/.pre-commit-hooks/              @nautechsystems/core
/rustfmt.toml                    @nautechsystems/core
/clippy.toml                     @nautechsystems/core
/.taplo.toml                     @nautechsystems/core
/.markdownlint.jsonc             @nautechsystems/core
/.gitlint                        @nautechsystems/core
/.yamllint.yaml                  @nautechsystems/core

# =============================================================================
# Git Configuration
# =============================================================================
/.gitignore                      @nautechsystems/core
/.gitattributes                  @nautechsystems/core

# =============================================================================
# Container Build & Docker - SUPPLY CHAIN RISK
# =============================================================================
/.docker/                        @nautechsystems/core
/.dockerignore                   @nautechsystems/core

# =============================================================================
# Scripts - HIGH SECURITY RISK
# =============================================================================
/scripts/                        @nautechsystems/core

# =============================================================================
# Build Automation & Reporting
# =============================================================================
/build.py                        @nautechsystems/core
/.codecov.yml                    @nautechsystems/core

# =============================================================================
# Security & Documentation
# =============================================================================
/SECURITY.md                     @nautechsystems/core

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 32


**Identifiers**: `Actions`, `Automation`, `Build`, `CHAIN`, `CODEOWNERS`, `Cargo`, `Code`, `Configuration`, `Container`, `Dependencies`, `Docker`, `Documentation`, `Formatting`, `Git`, `GitHub`, `HIGH`, `Makefile`, `More`, `NautilusTrader`, `Owners`, `Python`, `Quality`, `RISK`, `Reporting`, `Root`, `Rust`, `SECURITY`, `SUPPLY`, `Scripts`, `Security` *(+2 more)*

## Related Files

This file is located in `.github/`. Related files may include:
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
*Generated on 2025-11-18T21:54:58.796710Z*
