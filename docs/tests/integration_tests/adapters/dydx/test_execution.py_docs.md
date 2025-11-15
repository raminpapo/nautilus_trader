# Documentation: `tests/integration_tests/adapters/dydx/test_execution.py`
**Generated:** 2025-11-15T19:40:07.757588Z
**File Size:** 4010 bytes
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

- **Path:** `tests/integration_tests/adapters/dydx/test_execution.py`
- **Size:** 4,010 bytes
- **Lines:** 125
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3
- **Functions:** 7

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
# -------------------------------------------------------------------------------------------------"""Unit tests for the execution engine of dYdX."""
"""
Unit tests for the dYdX execution engine.
"""


import pytest

from nautilus_trader.adapters.dydx.execution import ClientOrderIdHelper
from nautilus_trader.model.identifiers import ClientOrderId


@pytest.fixture
def client_order_id_helper(cache):
    """
    Create a stub ClientOrderIdHelper.
    """
    return ClientOrderIdHelper(cache=cache)


@pytest.mark.parametrize("order_string", ["839ca109-f2c8-46b5-88f2-345eeeb01058", str(12345)])
def test_generate_client_order_id_int_uuid(client_order_id_helper, order_string) -> None:
    """
    Test the generate_client_order_id_int method with a UUID4.
    """
    # Prepare
    client_order_id = ClientOrderId(order_string)

    # Act
    result = client_order_id_helper.generate_client_order_id_int(client_order_id)

    # Assert
    assert isinstance(result, int)


def test_generate_client_order_id_int_with_int(client_order_id_helper) -> None:
    """
    Test the generate_client_order_id_int method with an integer.
    """
    # Prepare
    expected_result = 12345
    client_order_id = ClientOrderId(str(expected_result))

    # Act
    result = client_order_id_helper.generate_client_order_id_int(client_order_id)

    # Assert
    assert result == expected_result


def test_retrieve_from_cache(client_order_id_helper) -> None:
    """
    Test the generate_client_order_id_int method with an integer.
    """
    # Prepare
    client_order_id_int = 12345
    expected_result = ClientOrderId(str(client_order_id_int))
    client_order_id_helper.generate_client_order_id_int(expected_result)

    # Act
    result = client_order_id_helper.get_client_order_id(client_order_id_int)

    # Assert
    assert result.value == expected_result.value
    assert result == expected_result


def test_retrieve_from_empty_cache(client_order_id_helper) -> None:
    """
    Test the generate_client_order_id_int method with an integer.
    """
    # Prepare
    client_order_id_int = 12345
    expected_result = ClientOrderId(str(client_order_id_int))

    # Act
    result = client_order_id_helper.get_client_order_id(client_order_id_int)

    # Assert
    assert result.value == expected_result.value
    assert result == expected_result


def test_retrieve_client_order_id_integer_from_cache(client_order_id_helper) -> None:
    """
    Test the generate_client_order_id_int method with an integer.
    """
    # Prepare
    expected_result = 12345
    client_order_id = ClientOrderId(str(expected_result))
    client_order_id_helper.generate_client_order_id_int(client_order_id)

    # Act
    result = client_order_id_helper.get_client_order_id_int(client_order_id)

    # Assert
    assert result == expected_result


def test_retrieve_client_order_id_integer_from_empty_cache(client_order_id_helper) -> None:
    """
    Test the generate_client_order_id_int method with an integer.
    """
    # Prepare
    expected_result = 12345
    client_order_id = ClientOrderId(str(expected_result))

    # Act
    result = client_order_id_helper.get_client_order_id_int(client_order_id)

    # Assert
    assert result == expected_result
```


---

## Overview

This file is located at `tests/integration_tests/adapters/dydx/test_execution.py` within the repository.

**Functions defined:** client_order_id_helper, test_generate_client_order_id_int_uuid, test_generate_client_order_id_int_with_int, test_retrieve_from_cache, test_retrieve_from_empty_cache, test_retrieve_client_order_id_integer_from_cache, test_retrieve_client_order_id_integer_from_empty_cache

**Import statements:** 3


---

## Detailed Analysis

### Functions

#### `client_order_id_helper(cache)`


#### `test_generate_client_order_id_int_uuid(client_order_id_helper, order_string)`


#### `test_generate_client_order_id_int_with_int(client_order_id_helper)`


#### `test_retrieve_from_cache(client_order_id_helper)`


#### `test_retrieve_from_empty_cache(client_order_id_helper)`


#### `test_retrieve_client_order_id_integer_from_cache(client_order_id_helper)`


#### `test_retrieve_client_order_id_integer_from_empty_cache(client_order_id_helper)`


### Imports

- `import pytest`
- `from nautilus_trader.adapters.dydx.execution import ClientOrderIdHelper`
- `from nautilus_trader.model.identifiers import ClientOrderId`


---

## Usage Examples

### Importing

```python
from tests.integration_tests.adapters.dydx.test_execution import client_order_id_helper
```


---

## Related Files

This file imports from the following modules:

- `import pytest`
- `from nautilus_trader.adapters.dydx.execution import ClientOrderIdHelper`
- `from nautilus_trader.model.identifiers import ClientOrderId`

**Directory:** `tests/integration_tests/adapters/dydx`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


