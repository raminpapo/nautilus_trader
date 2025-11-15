# Documentation: `tests/integration_tests/adapters/polymarket/resources/create_api_key.py`
**Generated:** 2025-11-15T19:40:07.888022Z
**File Size:** 1202 bytes
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

- **Path:** `tests/integration_tests/adapters/polymarket/resources/create_api_key.py`
- **Size:** 1,202 bytes
- **Lines:** 28
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3
- **Functions:** 1

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

from py_clob_client.client import ClobClient
from py_clob_client.constants import POLYGON


def create_polymarket_api_key():
    host = "https://clob.polymarket.com"
    key = os.environ["POLYMARKET_PK"]
    chain_id = POLYGON
    client = ClobClient(host, key=key, chain_id=chain_id)

    print(client.create_api_key())
```


---

## Overview

This file is located at `tests/integration_tests/adapters/polymarket/resources/create_api_key.py` within the repository.

**Functions defined:** create_polymarket_api_key

**Import statements:** 3


---

## Detailed Analysis

### Functions

#### `create_polymarket_api_key()`


### Imports

- `import os`
- `from py_clob_client.client import ClobClient`
- `from py_clob_client.constants import POLYGON`


---

## Usage Examples

### Importing

```python
from tests.integration_tests.adapters.polymarket.resources.create_api_key import create_polymarket_api_key
```


---

## Related Files

This file imports from the following modules:

- `import os`
- `from py_clob_client.client import ClobClient`
- `from py_clob_client.constants import POLYGON`

**Directory:** `tests/integration_tests/adapters/polymarket/resources`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: api_key. Ensure proper handling of secrets.

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


