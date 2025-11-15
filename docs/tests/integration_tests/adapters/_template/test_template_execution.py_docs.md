# Documentation: `tests/integration_tests/adapters/_template/test_template_execution.py`
**Generated:** 2025-11-15T19:40:05.563419Z
**File Size:** 1907 bytes
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

- **Path:** `tests/integration_tests/adapters/_template/test_template_execution.py`
- **Size:** 1,907 bytes
- **Lines:** 58
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3
- **Functions:** 8

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

from nautilus_trader.adapters._template.execution import TemplateLiveExecutionClient
from nautilus_trader.live.execution_client import LiveExecutionClient


pytestmark = pytest.mark.skip(reason="template")


@pytest.fixture()
def execution_client() -> LiveExecutionClient:
    return TemplateLiveExecutionClient()  # type: ignore


def test_connect(execution_client: LiveExecutionClient):
    execution_client.connect()
    assert execution_client.is_connected


def test_disconnect(execution_client: LiveExecutionClient):
    execution_client.connect()
    execution_client.disconnect()
    assert not execution_client.is_connected


def test_submit_order(execution_client: LiveExecutionClient):
    pass


def test_submit_bracket_order(execution_client: LiveExecutionClient):
    pass


def test_modify_order(execution_client: LiveExecutionClient):
    pass


def test_cancel_order(execution_client: LiveExecutionClient):
    pass


def test_generate_order_status_report(execution_client: LiveExecutionClient):
    pass
```


---

## Overview

This file is located at `tests/integration_tests/adapters/_template/test_template_execution.py` within the repository.

**Functions defined:** execution_client, test_connect, test_disconnect, test_submit_order, test_submit_bracket_order, test_modify_order, test_cancel_order, test_generate_order_status_report

**Import statements:** 3


---

## Detailed Analysis

### Functions

#### `execution_client()`


#### `test_connect(execution_client: LiveExecutionClient)`


#### `test_disconnect(execution_client: LiveExecutionClient)`


#### `test_submit_order(execution_client: LiveExecutionClient)`


#### `test_submit_bracket_order(execution_client: LiveExecutionClient)`


#### `test_modify_order(execution_client: LiveExecutionClient)`


#### `test_cancel_order(execution_client: LiveExecutionClient)`


#### `test_generate_order_status_report(execution_client: LiveExecutionClient)`


### Imports

- `import pytest`
- `from nautilus_trader.adapters._template.execution import TemplateLiveExecutionClient`
- `from nautilus_trader.live.execution_client import LiveExecutionClient`


---

## Usage Examples

### Importing

```python
from tests.integration_tests.adapters._template.test_template_execution import execution_client
```


---

## Related Files

This file imports from the following modules:

- `import pytest`
- `from nautilus_trader.adapters._template.execution import TemplateLiveExecutionClient`
- `from nautilus_trader.live.execution_client import LiveExecutionClient`

**Directory:** `tests/integration_tests/adapters/_template`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


