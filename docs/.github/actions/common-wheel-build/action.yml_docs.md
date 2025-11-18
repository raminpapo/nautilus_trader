# Documentation: action.yml

## File Metadata

- **Path**: `.github/actions/common-wheel-build/action.yml`
- **Size**: 3,475 bytes
- **Lines**: 104
- **Language**: YAML

## Original Source

```yaml
name: common-wheel-build
description: Common wheel build and install

inputs:
  python-version:
    description: The Python version to setup
    required: true
  github_ref:
    description: The GitHub ref (branch name)
    required: true
    default: ${{ github.ref }}

runs:
  using: "composite"
  steps:
    - name: Debug github_ref
      shell: bash
      run: echo "Received github_ref:" "${INPUTS_GITHUB_REF}"
      env:
        INPUTS_GITHUB_REF: ${{ inputs.github_ref }}

    - name: Update version in pyproject.toml
      if: ${{ inputs.github_ref != 'refs/heads/master' }}
      shell: bash
      run: |
        bash ./scripts/ci/update-pyproject-version.sh

    - name: Generate updated lock file
      if: inputs.github_ref != 'refs/heads/master'
      shell: bash
      run: uv lock --no-upgrade

    - name: Build Python wheel (Linux x86_64)
      if: runner.os == 'Linux' && runner.arch != 'ARM64' && runner.arch != 'aarch64'
      shell: bash
      run: |
        uv build --wheel
        ls -lh dist/

    - name: Build Python wheel (Linux ARM64)
      if: runner.os == 'Linux' && (runner.arch == 'ARM64' || runner.arch == 'aarch64')
      shell: bash
      run: |
        echo "Building for Linux ARM64"

        PYTHON_LIB_DIR=$(python3 -c 'import sysconfig; print(sysconfig.get_config_var("LIBDIR"))')
        PYTHON_VERSION=$(python3 -c 'import platform; print(".".join(platform.python_version_tuple()[:2]))')

        export CARGO_BUILD_JOBS=1
        export LD_LIBRARY_PATH="/usr/lib/aarch64-linux-gnu:$PYTHON_LIB_DIR:$LD_LIBRARY_PATH"
        export LIBRARY_PATH="/usr/lib/aarch64-linux-gnu:$PYTHON_LIB_DIR:$LIBRARY_PATH"
        export PYO3_PYTHON=$(which "python${INPUTS_PYTHON_VERSION}")
        export RUSTFLAGS="-C link-arg=-L${PYTHON_LIB_DIR} -C link-arg=-lpython${PYTHON_VERSION}"

        echo "LD_LIBRARY_PATH: $LD_LIBRARY_PATH"
        echo "LIBRARY_PATH: $LIBRARY_PATH"
        echo "PYO3_PYTHON: $PYO3_PYTHON"
        echo "PYTHON_LIB_DIR: $PYTHON_LIB_DIR"
        echo "PYTHON_VERSION: $PYTHON_VERSION"
        echo "RUSTFLAGS: $RUSTFLAGS"

        uv build --wheel
        ls -lh dist/
      env:
        INPUTS_PYTHON_VERSION: ${{ inputs.python-version }}

    - name: Build Python wheel (Windows)
      if: runner.os == 'Windows'
      shell: bash
      run: |
        uv build --wheel
        ls -lh dist/

    - name: Build Python wheel (macOS)
      if: runner.os == 'macOS'
      shell: bash
      run: |
        export PATH="$pythonLocation/bin:$PATH"
        export PYO3_PYTHON=$(
          which "python${INPUTS_PYTHON_VERSION}" ||
          echo "$pythonLocation/bin/python${INPUTS_PYTHON_VERSION}"
        )
        export RUSTFLAGS="-C link-arg=-undefined -C link-arg=dynamic_lookup"

        PYTHON_LIB_DIR=$(dirname $(dirname $PYO3_PYTHON))/lib
        export LIBRARY_PATH="$pythonLocation/lib:$PYTHON_LIB_DIR:$LIBRARY_PATH"
        export LD_LIBRARY_PATH="$pythonLocation/lib:$PYTHON_LIB_DIR:$LD_LIBRARY_PATH"
        export DYLD_LIBRARY_PATH="$pythonLocation/lib:$PYTHON_LIB_DIR:$DYLD_LIBRARY_PATH"

        echo "PYO3_PYTHON: $PYO3_PYTHON"
        echo "PYTHON_LIB_DIR: $PYTHON_LIB_DIR"
        echo "RUSTFLAGS: $RUSTFLAGS"

        uv build --wheel
        ls -lh dist/
      env:
        INPUTS_PYTHON_VERSION: ${{ inputs.python-version }}

    - name: Install Python wheel
      shell: bash
      run: |
        uv sync --all-groups --all-extras --no-install-package nautilus_trader
        uv pip install dist/*.whl

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a YAML configuration file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 26


**Identifiers**: `ARM64`, `Build`, `Building`, `CARGO_BUILD_JOBS`, `Common`, `DYLD_LIBRARY_PATH`, `Debug`, `Generate`, `GitHub`, `INPUTS_GITHUB_REF`, `INPUTS_PYTHON_VERSION`, `Install`, `LD_LIBRARY_PATH`, `LIBDIR`, `LIBRARY_PATH`, `Linux`, `PATH`, `PYO3_PYTHON`, `PYTHON_LIB_DIR`, `PYTHON_VERSION`, `Python`, `RUSTFLAGS`, `Received`, `The`, `Update`, `Windows`

## Related Files

This file is located in `.github/actions/common-wheel-build/`. Related files may include:
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
*Generated on 2025-11-18T21:54:58.806545Z*
