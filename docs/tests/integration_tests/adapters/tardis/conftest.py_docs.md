# Documentation: `tests/integration_tests/adapters/tardis/conftest.py`
**Generated:** 2025-11-15T19:40:07.962846Z
**File Size:** 1687 bytes
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

- **Path:** `tests/integration_tests/adapters/tardis/conftest.py`
- **Size:** 1,687 bytes
- **Lines:** 64
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3
- **Functions:** 6

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

from pathlib import Path

import pytest

from nautilus_trader import PACKAGE_ROOT


def get_test_data_path(file_name: str) -> Path:
    """
    Get path to test data file in the tardis test data directory.
    """
    path = (
        PACKAGE_ROOT
        / "crates"
        / "adapters"
        / "tardis"
        / "src"
        / "tests"
        / "data"
        / "csv"
        / file_name
    )
    assert path.exists(), f"Test data file not found: {path}"
    return path


@pytest.fixture()
def instrument_provider():
    pass  # Not applicable


@pytest.fixture()
def data_client():
    pass  # Not applicable


@pytest.fixture()
def exec_client():
    pass  # Not applicable


@pytest.fixture()
def instrument():
    pass  # Not applicable


@pytest.fixture()
def account_state():
    pass  # Not applicable
```


---

## Overview

This file is located at `tests/integration_tests/adapters/tardis/conftest.py` within the repository.

**Functions defined:** get_test_data_path, instrument_provider, data_client, exec_client, instrument, account_state

**Import statements:** 3


---

## Detailed Analysis

### Functions

#### `get_test_data_path(file_name: str)`


#### `instrument_provider()`


#### `data_client()`


#### `exec_client()`


#### `instrument()`


#### `account_state()`


### Imports

- `from pathlib import Path`
- `import pytest`
- `from nautilus_trader import PACKAGE_ROOT`


---

## Usage Examples

### Importing

```python
from tests.integration_tests.adapters.tardis.conftest import get_test_data_path
```


---

## Related Files

This file imports from the following modules:

- `from pathlib import Path`
- `import pytest`
- `from nautilus_trader import PACKAGE_ROOT`

**Directory:** `tests/integration_tests/adapters/tardis`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


