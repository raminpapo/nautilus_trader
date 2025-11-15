# Documentation: `nautilus_trader/adapters/tardis/download.py`
**Generated:** 2025-11-15T19:40:04.506280Z
**File Size:** 1848 bytes
**Extension:** .py
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

- **Path:** `nautilus_trader/adapters/tardis/download.py`
- **Size:** 1,848 bytes
- **Lines:** 49
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3
- **Functions:** 2

---

## Source Code

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


---

## Overview

This file is located at `nautilus_trader/adapters/tardis/download.py` within the repository.

**Functions defined:** download_file, url_to_path

**Import statements:** 3


---

## Detailed Analysis

### Functions

#### `download_file(url: str)`


#### `url_to_path(url: str)`


### Imports

- `import os`
- `from urllib.parse import urlparse`
- `from nautilus_trader.core.nautilus_pyo3.network import http_download`


---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters.tardis.download import download_file
```


---

## Related Files

This file imports from the following modules:

- `import os`
- `from urllib.parse import urlparse`
- `from nautilus_trader.core.nautilus_pyo3.network import http_download`

**Directory:** `nautilus_trader/adapters/tardis`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: api_key, auth. Ensure proper handling of secrets.


