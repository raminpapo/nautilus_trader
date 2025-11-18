# Documentation: download.py

## File Metadata

- **Path**: `nautilus_trader/adapters/tardis/download.py`
- **Size**: 1,848 bytes
- **Lines**: 50
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

import os
from urllib.parse import urlparse

from nautilus_trader.core.nautilus_pyo3.network import http_download


def download_file(url: str):
    print(f"Checking file for {url}")
    path = url_to_path(url)
    print(f"Generated path: {path}")

    if os.path.exists(path):
        return path

    print(f"Downloading from {url}")
    headers = {"Authorization": f"Bearer {os.environ['TM_API_KEY']}"}
    http_download(url, path, headers=headers, timeout_secs=60)
    return path


def url_to_path(url: str) -> str:
    parsed_url = urlparse(url)
    path_components = [x for x in parsed_url.path.split("/") if x]

    exchange = path_components[1]
    data_type = path_components[2]
    year = path_components[3]
    month = path_components[4]
    day = path_components[5]
    filename = path_components[6]

    local_path = f"~/Downloads/tardis/{exchange}/{data_type}/{year}/{month}/{day}/{filename}"
    local_path = os.path.expanduser(local_path)
    return local_path

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 2 function(s).

## Detailed Walkthrough

### Functions
- **`download_file()`**: Function defined in this file
- **`url_to_path()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 5


**Functions**: `download_file`, `url_to_path`
**Imports**: `nautilus_trader.core.nautilus_pyo3.network`, `os`, `urllib.parse`

## Related Files

This file is located in `nautilus_trader/adapters/tardis/`. Related files may include:
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
*Generated on 2025-11-18T21:55:05.004303Z*
