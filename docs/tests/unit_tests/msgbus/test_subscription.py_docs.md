# Documentation: test_subscription.py

## File Metadata

- **Path**: `tests/unit_tests/msgbus/test_subscription.py`
- **Size**: 3,607 bytes
- **Lines**: 100
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 6 function(s).

## Detailed Walkthrough

### Functions
- **`test_comparisons_returns_expected()`**: Function defined in this file
- **`test_equality_when_equal_returns_true()`**: Function defined in this file
- **`test_equality_when_not_equal_returns_false()`**: Function defined in this file
- **`test_reverse_sorting_list_of_subscribers_returns_expected_ordered_list()`**: Function defined in this file
- **`test_subscription_for_all()`**: Function defined in this file
- **`test_str_repr()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 7


**Functions**: `test_comparisons_returns_expected`, `test_equality_when_equal_returns_true`, `test_equality_when_not_equal_returns_false`, `test_reverse_sorting_list_of_subscribers_returns_expected_ordered_list`, `test_str_repr`, `test_subscription_for_all`
**Imports**: `nautilus_trader.common.component`

## Related Files

This file is located in `tests/unit_tests/msgbus/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/unit_tests/msgbus/test_subscription.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:11.692553Z*
