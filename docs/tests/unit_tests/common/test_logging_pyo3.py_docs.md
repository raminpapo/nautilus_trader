# Documentation: test_logging_pyo3.py

## File Metadata

- **Path**: `tests/unit_tests/common/test_logging_pyo3.py`
- **Size**: 2,175 bytes
- **Lines**: 68
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

from nautilus_trader.common.component import is_logging_pyo3
from nautilus_trader.common.component import set_logging_pyo3
from nautilus_trader.core import nautilus_pyo3


@pytest.mark.parametrize(
    "invalid_level",
    [
        "INVALID",
        "DEBG",
        "WARNINGG",
        "FOO",
        "",
    ],
)
def test_init_logging_invalid_component_level_raises(invalid_level):
    with pytest.raises(Exception, match="Invalid log level string"):
        nautilus_pyo3.init_logging(
            trader_id=nautilus_pyo3.TraderId("TESTER-001"),
            instance_id=nautilus_pyo3.UUID4(),
            level_stdout=nautilus_pyo3.LogLevel.INFO,
            component_levels={"MyStrategy": invalid_level},
        )


def test_set_logging_pyo3_flag():
    initial = is_logging_pyo3()

    set_logging_pyo3(True)
    after_set = is_logging_pyo3()
    set_logging_pyo3(False)
    after_reset = is_logging_pyo3()

    assert after_set is True
    assert after_reset is False

    set_logging_pyo3(initial)


def test_logging_pyo3_flag_can_toggle_between_modes():
    set_logging_pyo3(True)
    assert is_logging_pyo3() is True

    set_logging_pyo3(False)
    assert is_logging_pyo3() is False

    set_logging_pyo3(True)
    assert is_logging_pyo3() is True

    set_logging_pyo3(False)

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 3 function(s).

## Detailed Walkthrough

### Functions
- **`test_init_logging_invalid_component_level_raises()`**: Function defined in this file
- **`test_set_logging_pyo3_flag()`**: Function defined in this file
- **`test_logging_pyo3_flag_can_toggle_between_modes()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 6


**Functions**: `test_init_logging_invalid_component_level_raises`, `test_logging_pyo3_flag_can_toggle_between_modes`, `test_set_logging_pyo3_flag`
**Imports**: `nautilus_trader.common.component`, `nautilus_trader.core`, `pytest`

## Related Files

This file is located in `tests/unit_tests/common/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/unit_tests/common/test_logging_pyo3.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:11.278410Z*
