# Documentation: `tests/unit_tests/msgbus/test_subscription.py`
**Generated:** 2025-11-15T19:40:09.407494Z
**File Size:** 3607 bytes
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

- **Path:** `tests/unit_tests/msgbus/test_subscription.py`
- **Size:** 3,607 bytes
- **Lines:** 99
- **Extension:** `.py`
- **Type:** text
- **Imports:** 1
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

from nautilus_trader.common.component import Subscription


def test_comparisons_returns_expected():
    # Arrange
    subscriber = []
    subscription1 = Subscription(topic="*", handler=subscriber.append, priority=0)
    subscription2 = Subscription(topic="*", handler=subscriber.append, priority=1)

    # Act, Assert
    assert subscription1 == subscription2
    assert subscription1 < subscription2
    assert subscription1 <= subscription2
    assert subscription2 > subscription1
    assert subscription2 >= subscription1


def test_equality_when_equal_returns_true():
    # Arrange
    subscriber = []
    subscription1 = Subscription(topic="*", handler=subscriber.append, priority=1)
    subscription2 = Subscription(topic="*", handler=subscriber.append, priority=2)

    # Act, Assert
    assert subscription1 == subscription2


def test_equality_when_not_equal_returns_false():
    # Arrange
    subscriber = []
    subscription1 = Subscription(topic="*", handler=subscriber.append, priority=1)
    subscription2 = Subscription(topic="something", handler=subscriber.append, priority=2)

    # Act, Assert
    assert subscription1 != subscription2


def test_reverse_sorting_list_of_subscribers_returns_expected_ordered_list():
    # Arrange
    subscriber = []
    subscription1 = Subscription(topic="*", handler=subscriber.append)
    subscription2 = Subscription(topic="*", handler=subscriber.append, priority=5)
    subscription3 = Subscription(topic="*", handler=subscriber.append, priority=2)
    subscription4 = Subscription(topic="*", handler=subscriber.append, priority=10)

    # Act
    sorted_list = sorted([subscription1, subscription2, subscription3, subscription4], reverse=True)

    # Assert
    assert sorted_list == [subscription4, subscription2, subscription3, subscription1]
    assert sorted_list[0] == subscription4
    assert sorted_list[1] == subscription2
    assert sorted_list[2] == subscription3
    assert sorted_list[3] == subscription1


def test_subscription_for_all():
    # Arrange
    subscriber = []
    handler_str = str(subscriber.append)

    # Act
    subscription = Subscription(topic="*", handler=subscriber.append)

    # Assert
    assert str(subscription).startswith(f"Subscription(topic=*, handler={handler_str}, priority=0)")


def test_str_repr():
    # Arrange
    subscriber = []
    handler_str = str(subscriber.append)

    # Act
    subscription = Subscription(topic="system_status", handler=subscriber.append)

    # Assert
    assert (
        str(subscription) == f"Subscription(topic=system_status, handler={handler_str}, priority=0)"
    )
    assert (
        repr(subscription)
        == f"Subscription(topic=system_status, handler={handler_str}, priority=0)"
    )
```


---

## Overview

This file is located at `tests/unit_tests/msgbus/test_subscription.py` within the repository.

**Functions defined:** test_comparisons_returns_expected, test_equality_when_equal_returns_true, test_equality_when_not_equal_returns_false, test_reverse_sorting_list_of_subscribers_returns_expected_ordered_list, test_subscription_for_all, test_str_repr

**Import statements:** 1


---

## Detailed Analysis

### Functions

#### `test_comparisons_returns_expected()`


#### `test_equality_when_equal_returns_true()`


#### `test_equality_when_not_equal_returns_false()`


#### `test_reverse_sorting_list_of_subscribers_returns_expected_ordered_list()`


#### `test_subscription_for_all()`


#### `test_str_repr()`


### Imports

- `from nautilus_trader.common.component import Subscription`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.msgbus.test_subscription import test_comparisons_returns_expected
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.common.component import Subscription`

**Directory:** `tests/unit_tests/msgbus`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


