# Documentation: DockerfileUbuntu

## File Metadata

- **Path**: `.docker/DockerfileUbuntu`
- **Size**: 1,913 bytes
- **Lines**: 70
- **Language**: Unknown

## Original Source

```
# Dockerfile to reproduce locally an environment similar to what is run on the github runner
#
# From nautilus project's root folder:
#
# Build the image:
# docker build -f .docker/DockerfileUbuntu -t nautilus-dev .
#
# Run interactively with local directory mounted:
# docker run --rm -itv "$(pwd)":/workspace nautilus-dev bash
#
# Or run the default entrypoint:
# docker run --rm -itv "$(pwd)":/workspace nautilus-dev
#
# Remove the image
# docker image rm nautilus-dev

FROM ubuntu:22.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV BUILD_MODE=release
ENV RUST_BACKTRACE=1
ENV CARGO_INCREMENTAL=0
ENV CC="clang"
ENV CXX="clang++"

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    clang \
    git \
    pkg-config \
    make \
    capnproto \
    libcapnp-dev \
    gcc-aarch64-linux-gnu \
    && rm -rf /var/lib/apt/lists/*

# Install Rust
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --default-toolchain stable
ENV PATH="/root/.cargo/bin:${PATH}"

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.cargo/bin:/root/.local/bin:${PATH}"

# Install Python 3.13
RUN uv python install

# Set working directory
WORKDIR /workspace

# Copy only necessary files for dependency setup
# The actual source code will be mounted as a volume
COPY ../scripts/rust-toolchain.sh scripts/
COPY ../Cargo.toml Cargo.lock pyproject.toml rust-toolchain.toml ./

# Set up Rust toolchain based on project requirements
RUN bash scripts/rust-toolchain.sh > /tmp/toolchain.txt && \
    TOOLCHAIN=$(cat /tmp/toolchain.txt) && \
    rustup toolchain install $TOOLCHAIN && \
    rustup default $TOOLCHAIN && \
    rustup component add clippy rustfmt

# Copy and set up entrypoint script for interactive development
COPY .docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 27


**Identifiers**: `BUILD_MODE`, `Build`, `CARGO_INCREMENTAL`, `COPY`, `CXX`, `Cargo`, `Copy`, `DEBIAN_FRONTEND`, `Dockerfile`, `DockerfileUbuntu`, `ENTRYPOINT`, `ENV`, `FROM`, `From`, `Install`, `LsSf`, `PATH`, `Python`, `RUN`, `RUST_BACKTRACE`, `Remove`, `Run`, `Rust`, `Set`, `TOOLCHAIN`, `The`, `WORKDIR`

## Related Files

This file is located in `.docker/`. Related files may include:
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
*Generated on 2025-11-18T21:54:58.788136Z*
