# Documentation: `tests/integration_tests/adapters/_template/test_template_data.py`
**Generated:** 2025-11-15T19:40:05.562190Z
**File Size:** 1600 bytes
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

- **Path:** `tests/integration_tests/adapters/_template/test_template_data.py`
- **Size:** 1,600 bytes
- **Lines:** 46
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3
- **Functions:** 5

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

import pytest

from nautilus_trader.adapters._template.data import TemplateLiveMarketDataClient
from nautilus_trader.live.data_client import LiveMarketDataClient


pytestmark = pytest.mark.skip(reason="template")


@pytest.fixture()
def data_client() -> LiveMarketDataClient:
    return TemplateLiveMarketDataClient()  # type: ignore


def test_connect(data_client: LiveMarketDataClient):
    data_client.connect()
    assert data_client.is_connected


def test_disconnect(data_client: LiveMarketDataClient):
    data_client.connect()
    data_client.disconnect()
    assert not data_client.is_connected


def test_reset(data_client: LiveMarketDataClient):
    pass


def test_dispose(data_client: LiveMarketDataClient):
    pass
```


---

## Overview

This file is located at `tests/integration_tests/adapters/_template/test_template_data.py` within the repository.

**Functions defined:** data_client, test_connect, test_disconnect, test_reset, test_dispose

**Import statements:** 3


---

## Detailed Analysis

### Functions

#### `data_client()`


#### `test_connect(data_client: LiveMarketDataClient)`


#### `test_disconnect(data_client: LiveMarketDataClient)`


#### `test_reset(data_client: LiveMarketDataClient)`


#### `test_dispose(data_client: LiveMarketDataClient)`


### Imports

- `import pytest`
- `from nautilus_trader.adapters._template.data import TemplateLiveMarketDataClient`
- `from nautilus_trader.live.data_client import LiveMarketDataClient`


---

## Usage Examples

### Importing

```python
from tests.integration_tests.adapters._template.test_template_data import data_client
```


---

## Related Files

This file imports from the following modules:

- `import pytest`
- `from nautilus_trader.adapters._template.data import TemplateLiveMarketDataClient`
- `from nautilus_trader.live.data_client import LiveMarketDataClient`

**Directory:** `tests/integration_tests/adapters/_template`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


