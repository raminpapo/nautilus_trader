# Documentation: config.py

## File Metadata

- **Path**: `nautilus_trader/persistence/config.py`
- **Size**: 4,206 bytes
- **Lines**: 111
- **Language**: Python

## Original Source

```python
# -------------------------------------------------------------------------------------------------
#  Copyright (C) 2015-2025 Nautech Systems Pty Ltd. All rights reserved.
#  https://nautechsystems.io
#
#  Licensed under the GNU Lesser General Public License Version 3.0 (the "License");
#  You may not use this file except in compliance with the License.
#  You may obtain a copy of the License at https://www.gnu.org/licenses/lgpl-3.0.en.html
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# -------------------------------------------------------------------------------------------------

from __future__ import annotations

from datetime import time

import fsspec
import pandas as pd

from nautilus_trader.common.config import NautilusConfig
from nautilus_trader.persistence.writer import RotationMode


class StreamingConfig(NautilusConfig, frozen=True):
    """
    Configuration for streaming live or backtest runs to the catalog in feather format.

    Parameters
    ----------
    catalog_path : str
        The path to the data catalog.
    fs_protocol : str, optional
        The `fsspec` filesystem protocol for the catalog.
    fs_storage_options : dict, optional
        The `fsspec` storage options.
    fs_rust_storage_options : dict, optional
        The `fsspec` storage options for the Rust backend.
    flush_interval_ms : int, optional
        The flush interval (milliseconds) for writing chunks.
    replace_existing: bool, default False
        If any existing feather files should be replaced.
    include_types : list[type], optional
        A list of Arrow serializable types to write.
        If this is specified then **only** the included types will be written.
    rotation_mode : RotationMode, default RotationMode.NO_ROTATION
        The mode for file rotation.
    max_file_size : int, default 1GB
        The maximum file size in bytes before rotation (for SIZE mode).
    rotation_interval : pd.Timedelta, optional
        The time interval for file rotation (for INTERVAL mode and SCHEDULED_DATES mode).
    rotation_time : time, default 00:00
        The time of day for file rotation (for SCHEDULED_DATES mode).
    rotation_timezone : str, default 'UTC'
        The timezone for rotation calculations (for SCHEDULED_DATES mode).

    """

    catalog_path: str
    fs_protocol: str | None = None
    fs_storage_options: dict | None = None
    fs_rust_storage_options: dict | None = None
    flush_interval_ms: int | None = None
    replace_existing: bool = False
    include_types: list[type] | None = None
    rotation_mode: RotationMode = RotationMode.NO_ROTATION
    max_file_size: int = 1024 * 1024 * 1024  # 1GB
    rotation_interval: pd.Timedelta | None = None
    rotation_time: time = time(0, 0, 0, 0)
    rotation_timezone: str = "UTC"

    @property
    def fs(self):
        return fsspec.filesystem(protocol=self.fs_protocol, **(self.fs_storage_options or {}))

    def as_catalog(self):
        from nautilus_trader.persistence.catalog.parquet import ParquetDataCatalog

        return ParquetDataCatalog(
            path=self.catalog_path,
            fs_protocol=self.fs_protocol,
            fs_storage_options=self.fs_storage_options,
            fs_rust_storage_options=self.fs_rust_storage_options,
        )


class DataCatalogConfig(NautilusConfig, frozen=True):
    """
    Configuration for a data catalog.

    Parameters
    ----------
    path : str
        The path to the data catalog.
    fs_protocol : str, optional
        The fsspec file system protocol for the data catalog.
    fs_storage_options : dict, optional
        The fsspec storage options for the data catalog.
    fs_rust_storage_options : dict, optional
        The fsspec storage options for the Rust backend.

    """

    path: str
    fs_protocol: str | None = None
    fs_storage_options: dict | None = None
    fs_rust_storage_options: dict | None = None
    name: str | None = None

```

## High-Level Overview

This file is part of the NautilusTrader repository. 2 class(es).

## Detailed Walkthrough


### Classes
- **`StreamingConfig`**: Class defined in this file
- **`DataCatalogConfig`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 8


**Classs**: `DataCatalogConfig`, `StreamingConfig`
**Imports**: `__future__`, `datetime`, `fsspec`, `nautilus_trader.common.config`, `nautilus_trader.persistence.writer`, `pandas`

## Related Files

This file is located in `nautilus_trader/persistence/`. Related files may include:
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
*Generated on 2025-11-18T21:55:05.863928Z*
