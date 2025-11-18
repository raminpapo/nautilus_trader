# Documentation: jupyterlab.dockerfile

## File Metadata

- **Path**: `.docker/jupyterlab.dockerfile`
- **Size**: 739 bytes
- **Lines**: 24
- **Language**: Unknown

## Original Source

```
ARG GIT_TAG=develop
FROM ghcr.io/nautechsystems/nautilus_trader:$GIT_TAG

COPY --from=ghcr.io/nautechsystems/nautilus_data:main /opt/pysetup/catalog /catalog
COPY docs/tutorials /opt/pysetup/tutorials

ENV PATH="/root/.local/bin:$PATH"

# Install build deps
RUN apt-get update && \
    apt-get install -y curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install UV
COPY uv-version ./
RUN UV_VERSION=$(cat uv-version) && curl -LsSf https://astral.sh/uv/$UV_VERSION/install.sh | sh

RUN uv pip install --system jupyterlab datafusion

ENV NAUTILUS_PATH="/"

CMD ["python", "-m", "jupyterlab", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root", "-NotebookApp.token=''", "--NotebookApp.password=''", "tutorials"]

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 13


**Identifiers**: `ARG`, `CMD`, `COPY`, `ENV`, `FROM`, `GIT_TAG`, `Install`, `LsSf`, `NAUTILUS_PATH`, `NotebookApp`, `PATH`, `RUN`, `UV_VERSION`

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

⚠️ **Security**: This file may handle sensitive data. Ensure proper encryption and access controls.

---
*Generated on 2025-11-18T21:54:58.791127Z*
