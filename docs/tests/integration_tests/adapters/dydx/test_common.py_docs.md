# Documentation: `tests/integration_tests/adapters/dydx/test_common.py`
**Generated:** 2025-11-15T19:40:07.751823Z
**File Size:** 2312 bytes
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

- **Path:** `tests/integration_tests/adapters/dydx/test_common.py`
- **Size:** 2,312 bytes
- **Lines:** 67
- **Extension:** `.py`
- **Type:** text
- **Imports:** 2
- **Functions:** 3

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
"""
Unit tests for the common module.
"""

from nautilus_trader.adapters.dydx.common.common import DYDXOrderTags
from nautilus_trader.model.objects import Price


def test_serialize_tags() -> None:
    """
    Test the DYDXOrderTags serialization to string.
    """
    # Arrange
    tags = DYDXOrderTags()
    expected_result = (
        'DYDXOrderTags:{"is_short_term_order":true,"num_blocks_open":20,"market_order_price":null}'
    )

    # Act
    result = tags.value

    # Assert
    assert result == expected_result


def test_serialize_tags_with_price() -> None:
    """
    Test the DYDXOrderTags serialization to string when setting a market order Price.
    """
    # Arrange
    tags = DYDXOrderTags(market_order_price=Price.from_int(100_000))
    expected_result = 'DYDXOrderTags:{"is_short_term_order":true,"num_blocks_open":20,"market_order_price":"100000"}'

    # Act
    result = tags.value

    # Assert
    assert result == expected_result


def test_parsing_string() -> None:
    """
    Test the DYDXOrderTags serialization to string when setting a market order Price.
    """
    # Arrange
    expected_result = DYDXOrderTags(market_order_price=Price.from_int(100_000))
    tag_string = 'DYDXOrderTags:{"is_short_term_order":true,"num_blocks_open":20,"market_order_price":"100000"}'

    # Act
    result = DYDXOrderTags.parse(tag_string.replace("DYDXOrderTags:", ""))

    # Assert
    assert result == expected_result
```


---

## Overview

This file is located at `tests/integration_tests/adapters/dydx/test_common.py` within the repository.

**Functions defined:** test_serialize_tags, test_serialize_tags_with_price, test_parsing_string

**Import statements:** 2


---

## Detailed Analysis

### Functions

#### `test_serialize_tags()`


#### `test_serialize_tags_with_price()`


#### `test_parsing_string()`


### Imports

- `from nautilus_trader.adapters.dydx.common.common import DYDXOrderTags`
- `from nautilus_trader.model.objects import Price`


---

## Usage Examples

### Importing

```python
from tests.integration_tests.adapters.dydx.test_common import test_serialize_tags
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.adapters.dydx.common.common import DYDXOrderTags`
- `from nautilus_trader.model.objects import Price`

**Directory:** `tests/integration_tests/adapters/dydx`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


