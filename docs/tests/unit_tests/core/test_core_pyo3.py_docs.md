# Documentation: test_core_pyo3.py

## File Metadata

- **Path**: `tests/unit_tests/core/test_core_pyo3.py`
- **Size**: 2,088 bytes
- **Lines**: 54
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

import pytest

from nautilus_trader.core import nautilus_pyo3


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        # PascalCase
        ["SomePascalCase", "some_pascal_case"],
        ["AnotherExample", "another_example"],
        # camelCase
        ["someCamelCase", "some_camel_case"],
        ["yetAnotherExample", "yet_another_example"],
        # kebab-case
        ["some-kebab-case", "some_kebab_case"],
        ["dashed-word-example", "dashed_word_example"],
        # snake_case
        ["already_snake_case", "already_snake_case"],
        ["no_change_needed", "no_change_needed"],
        # UPPER_CASE
        ["UPPER_CASE_EXAMPLE", "upper_case_example"],
        ["ANOTHER_UPPER_CASE", "another_upper_case"],
        # Mixed Cases
        ["MiXeD_CaseExample", "mi_xe_d_case_example"],
        ["Another-OneHere", "another_one_here"],
        # Use case
        ["BSPOrderBookDelta", "bsp_order_book_delta"],
        ["OrderBookDelta", "order_book_delta"],
        ["TradeTick", "trade_tick"],
    ],
)
def test_convert_to_snake_case(input: str, expected: str) -> None:
    # Arrange, Act
    result = nautilus_pyo3.convert_to_snake_case(input)

    # Assert
    assert result == expected

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`test_convert_to_snake_case()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Functions**: `test_convert_to_snake_case`
**Imports**: `nautilus_trader.core`, `pytest`

## Related Files

This file is located in `tests/unit_tests/core/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/unit_tests/core/test_core_pyo3.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:11.305936Z*
