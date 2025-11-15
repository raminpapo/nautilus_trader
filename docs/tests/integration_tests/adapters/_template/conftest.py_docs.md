# Documentation: `tests/integration_tests/adapters/_template/conftest.py`
**Generated:** 2025-11-15T19:40:05.560800Z
**File Size:** 1681 bytes
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

- **Path:** `tests/integration_tests/adapters/_template/conftest.py`
- **Size:** 1,681 bytes
- **Lines:** 44
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

from nautilus_trader.model.events import AccountState
from nautilus_trader.model.identifiers import Venue


@pytest.fixture()
def venue() -> Venue:
    raise NotImplementedError("`venue` needs to be implemented in adapter `conftest.py`")


@pytest.fixture()
def data_client():
    raise NotImplementedError("`data_client` needs to be implemented in adapter `conftest.py`")


@pytest.fixture()
def exec_client():
    raise NotImplementedError("`exec_client` needs to be implemented in adapter `conftest.py`")


@pytest.fixture()
def instrument():
    raise NotImplementedError("`instrument` needs to be implemented in adapter `conftest.py`")


@pytest.fixture()
def account_state() -> AccountState:
    raise NotImplementedError("`account_state` needs to be implemented in adapter `conftest.py`")
```


---

## Overview

This file is located at `tests/integration_tests/adapters/_template/conftest.py` within the repository.

**Functions defined:** venue, data_client, exec_client, instrument, account_state

**Import statements:** 3


---

## Detailed Analysis

### Functions

#### `venue()`


#### `data_client()`


#### `exec_client()`


#### `instrument()`


#### `account_state()`


### Imports

- `import pytest`
- `from nautilus_trader.model.events import AccountState`
- `from nautilus_trader.model.identifiers import Venue`


---

## Usage Examples

### Importing

```python
from tests.integration_tests.adapters._template.conftest import venue
```


---

## Related Files

This file imports from the following modules:

- `import pytest`
- `from nautilus_trader.model.events import AccountState`
- `from nautilus_trader.model.identifiers import Venue`

**Directory:** `tests/integration_tests/adapters/_template`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


