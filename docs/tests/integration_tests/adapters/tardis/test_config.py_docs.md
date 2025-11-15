# Documentation: `tests/integration_tests/adapters/tardis/test_config.py`
**Generated:** 2025-11-15T19:40:07.979418Z
**File Size:** 2483 bytes
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

- **Path:** `tests/integration_tests/adapters/tardis/test_config.py`
- **Size:** 2,483 bytes
- **Lines:** 78
- **Extension:** `.py`
- **Type:** text
- **Imports:** 2
- **Functions:** 4

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

import pkgutil

from nautilus_trader.core import nautilus_pyo3


def test_tardis_config_replay_options():
    # Arrange
    data = pkgutil.get_data(
        "tests.integration_tests.adapters.tardis.resources",
        "replay_options.json",
    )
    assert data

    # Act
    options = nautilus_pyo3.ReplayNormalizedRequestOptions.from_json(data)

    # Assert
    assert isinstance(options, nautilus_pyo3.ReplayNormalizedRequestOptions)


def test_tardis_config_replay_options_array():
    # Arrange
    data = pkgutil.get_data(
        "tests.integration_tests.adapters.tardis.resources",
        "replay_options_array.json",
    )
    assert data

    # Act
    options = nautilus_pyo3.ReplayNormalizedRequestOptions.from_json_array(data)

    # Assert
    assert isinstance(options[0], nautilus_pyo3.ReplayNormalizedRequestOptions)


def test_tardis_config_stream_options():
    # Arrange
    data = pkgutil.get_data(
        "tests.integration_tests.adapters.tardis.resources",
        "stream_options.json",
    )
    assert data

    # Act
    options = nautilus_pyo3.StreamNormalizedRequestOptions.from_json(data)

    # Assert
    assert isinstance(options, nautilus_pyo3.StreamNormalizedRequestOptions)


def test_tardis_config_stream_options_array():
    # Arrange
    data = pkgutil.get_data(
        "tests.integration_tests.adapters.tardis.resources",
        "stream_options_array.json",
    )
    assert data

    # Act
    options = nautilus_pyo3.StreamNormalizedRequestOptions.from_json_array(data)

    # Assert
    assert isinstance(options[0], nautilus_pyo3.StreamNormalizedRequestOptions)
```


---

## Overview

This file is located at `tests/integration_tests/adapters/tardis/test_config.py` within the repository.

**Functions defined:** test_tardis_config_replay_options, test_tardis_config_replay_options_array, test_tardis_config_stream_options, test_tardis_config_stream_options_array

**Import statements:** 2


---

## Detailed Analysis

### Functions

#### `test_tardis_config_replay_options()`


#### `test_tardis_config_replay_options_array()`


#### `test_tardis_config_stream_options()`


#### `test_tardis_config_stream_options_array()`


### Imports

- `import pkgutil`
- `from nautilus_trader.core import nautilus_pyo3`


---

## Usage Examples

### Importing

```python
from tests.integration_tests.adapters.tardis.test_config import test_tardis_config_replay_options
```


---

## Related Files

This file imports from the following modules:

- `import pkgutil`
- `from nautilus_trader.core import nautilus_pyo3`

**Directory:** `tests/integration_tests/adapters/tardis`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


