# Documentation: `.docker/jupyterlab.dockerfile`
**Generated:** 2025-11-15T19:40:00.218494Z
**File Size:** 739 bytes
**Extension:** .dockerfile
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

- **Path:** `.docker/jupyterlab.dockerfile`
- **Size:** 739 bytes
- **Lines:** 23
- **Extension:** `.dockerfile`
- **Type:** text

---

## Source Code

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


---

## Overview

This file is located at `.docker/jupyterlab.dockerfile` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `.docker`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: password, token. Ensure proper handling of secrets.


