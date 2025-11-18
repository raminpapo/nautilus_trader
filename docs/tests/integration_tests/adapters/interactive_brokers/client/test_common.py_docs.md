# Documentation: test_common.py

## File Metadata

- **Path**: `tests/integration_tests/adapters/interactive_brokers/client/test_common.py`
- **Size**: 4,842 bytes
- **Lines**: 190
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

import asyncio
from unittest.mock import Mock

import pytest

from nautilus_trader.adapters.interactive_brokers.client.common import Base
from nautilus_trader.adapters.interactive_brokers.client.common import Requests
from nautilus_trader.adapters.interactive_brokers.client.common import Subscriptions


class ConcreteBase(Base):
    def get(self, req_id=None, name=None):
        return "mocked get response"


@pytest.fixture
def base():
    return ConcreteBase()


@pytest.fixture
def subscriptions():
    return Subscriptions()


@pytest.fixture
def requests():
    return Requests()


@pytest.fixture
def mock_handle():
    return Mock()


@pytest.fixture
def mock_cancel():
    return Mock()


def test_add_req_id(base, mock_handle, mock_cancel):
    # Arrange

    # Act
    base.add_req_id(1, "test_name", mock_handle, mock_cancel)

    # Assert
    assert 1 in base._req_id_to_name
    assert 1 in base._req_id_to_handle
    assert 1 in base._req_id_to_cancel


def test_remove_req_id_existing(base, mock_handle, mock_cancel):
    # Arrange
    base.add_req_id(1, "test_name", mock_handle, mock_cancel)

    # Act
    base.remove_req_id(1)

    # Assert
    assert 1 not in base._req_id_to_name
    assert 1 not in base._req_id_to_handle
    assert 1 not in base._req_id_to_cancel


def test_remove_req_id_non_existing(base):
    base.remove_req_id(999)  # Removing a non-existing req_id should not raise an error


def test_remove_by_req_id(base, mock_handle, mock_cancel):
    # Arrange
    base.add_req_id(1, "test_name", mock_handle, mock_cancel)

    # Act
    base.remove(req_id=1)

    # Assert
    assert 1 not in base._req_id_to_name


def test_remove_by_name(base, mock_handle, mock_cancel):
    # Arrange
    base.add_req_id(1, "test_name", mock_handle, mock_cancel)

    # Act
    base.remove(name="test_name")

    # Assert
    assert 1 not in base._req_id_to_name


def test_add_subscription(subscriptions, mock_handle, mock_cancel):
    # Arrange

    # Act
    subscription = subscriptions.add(1, "test", mock_handle, mock_cancel)

    # Assert
    assert subscription.req_id == 1
    assert subscription.name == "test"
    assert subscription.handle == mock_handle
    assert subscription.cancel == mock_cancel
    assert subscription.last is None


def test_remove_subscription_by_req_id(subscriptions, mock_handle, mock_cancel):
    # Arrange
    subscriptions.add(1, "test", mock_handle, mock_cancel)

    # Act
    subscriptions.remove(req_id=1)

    # Assert
    assert subscriptions.get(req_id=1) is None


def test_remove_subscription_by_name(subscriptions, mock_handle, mock_cancel):
    # Arrange
    subscriptions.add(1, "test", mock_handle, mock_cancel)

    # Act
    subscriptions.remove(name="test")

    # Assert
    assert subscriptions.get(name="test") is None


def test_update_last(subscriptions, mock_handle, mock_cancel):
    # Arrange
    subscriptions.add(1, "test", mock_handle, mock_cancel)

    # Act
    subscriptions.update_last(1, "updated")

    # Assert
    assert subscriptions.get(req_id=1).last == "updated"


def test_add_request(requests, mock_handle, mock_cancel):
    # Arrange

    # Act
    requests.add(1, "test", mock_handle, mock_cancel)
    request = requests.get(req_id=1)

    # Assert
    assert request.req_id == 1
    assert request.name == "test"
    assert request.handle == mock_handle
    assert request.cancel == mock_cancel
    assert isinstance(request.future, asyncio.Future)
    assert request.result == []


def test_remove_request_by_req_id(requests, mock_handle, mock_cancel):
    # Arrange
    requests.add(1, "test", mock_handle, mock_cancel)

    # Act
    requests.remove(req_id=1)

    # Assert
    assert requests.get(req_id=1) is None


def test_remove_request_by_name(requests, mock_handle, mock_cancel):
    # Arrange
    requests.add(1, "test", mock_handle, mock_cancel)

    # Act
    requests.remove(name="test")

    # Assert
    assert requests.get(name="test") is None

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 17 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`base()`**: Function defined in this file
- **`subscriptions()`**: Function defined in this file
- **`requests()`**: Function defined in this file
- **`mock_handle()`**: Function defined in this file
- **`mock_cancel()`**: Function defined in this file
- **`test_add_req_id()`**: Function defined in this file
- **`test_remove_req_id_existing()`**: Function defined in this file
- **`test_remove_req_id_non_existing()`**: Function defined in this file
- **`test_remove_by_req_id()`**: Function defined in this file
- **`test_remove_by_name()`**: Function defined in this file
- **`test_add_subscription()`**: Function defined in this file
- **`test_remove_subscription_by_req_id()`**: Function defined in this file
- **`test_remove_subscription_by_name()`**: Function defined in this file
- **`test_update_last()`**: Function defined in this file
- **`test_add_request()`**: Function defined in this file
- **`test_remove_request_by_req_id()`**: Function defined in this file
- **`test_remove_request_by_name()`**: Function defined in this file

### Classes
- **`ConcreteBase`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 22


**Classs**: `ConcreteBase`
**Functions**: `base`, `mock_cancel`, `mock_handle`, `requests`, `subscriptions`, `test_add_req_id`, `test_add_request`, `test_add_subscription`, `test_remove_by_name`, `test_remove_by_req_id`, `test_remove_req_id_existing`, `test_remove_req_id_non_existing`, `test_remove_request_by_name`, `test_remove_request_by_req_id`, `test_remove_subscription_by_name`, `test_remove_subscription_by_req_id`, `test_update_last`
**Imports**: `asyncio`, `nautilus_trader.adapters.interactive_brokers.client.common`, `pytest`, `unittest.mock`

## Related Files

This file is located in `tests/integration_tests/adapters/interactive_brokers/client/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/interactive_brokers/client/test_common.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.876947Z*
