# Documentation: test_rvi.py

## File Metadata

- **Path**: `tests/unit_tests/indicators/test_rvi.py`
- **Size**: 3,811 bytes
- **Lines**: 112
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

from nautilus_trader.indicators import RelativeVolatilityIndex
from nautilus_trader.test_kit.providers import TestInstrumentProvider
from nautilus_trader.test_kit.stubs.data import TestDataStubs


AUDUSD_SIM = TestInstrumentProvider.default_fx_ccy("AUD/USD")


class TestRelativeVolatilityIndex:
    def setup(self):
        # Fixture Setup
        self.rvi = RelativeVolatilityIndex(10)

    def test_name_returns_expected_string(self):
        # Arrange, Act, Assert
        assert self.rvi.name == "RelativeVolatilityIndex"

    def test_str_repr_returns_expected_string(self):
        # Arrange, Act, Assert
        assert str(self.rvi) == "RelativeVolatilityIndex(10, 100.0, EXPONENTIAL)"
        assert repr(self.rvi) == "RelativeVolatilityIndex(10, 100.0, EXPONENTIAL)"

    def test_period_returns_expected_value(self):
        # Arrange, Act, Assert
        assert self.rvi.period == 10

    def test_initialized_without_inputs_returns_false(self):
        # Arrange, Act, Assert
        assert self.rvi.initialized is False

    def test_initialized_with_required_inputs_returns_true(self):
        # Arrange
        for i in range(20):
            self.rvi.update_raw(i)

        # Act, Assert
        assert self.rvi.initialized is True

    def test_handle_bar_updates_indicator(self):
        # Arrange
        indicator = RelativeVolatilityIndex(10)

        bar = TestDataStubs.bar_5decimal()

        # Act
        indicator.handle_bar(bar)

        # Assert
        assert indicator.has_inputs
        assert indicator.value == 0

    def test_value_with_one_input_returns_expected_value(self):
        # Arrange, Act
        self.rvi.update_raw(1.00000)

        # Assert
        assert self.rvi.value == 0

    def test_value_with_all_higher_inputs_returns_expected_value(self):
        # Arrange, Act
        self.rvi.update_raw(109.93)
        self.rvi.update_raw(110.0)
        self.rvi.update_raw(109.77)
        self.rvi.update_raw(109.96)
        self.rvi.update_raw(110.29)
        self.rvi.update_raw(110.53)
        self.rvi.update_raw(110.27)
        self.rvi.update_raw(110.21)
        self.rvi.update_raw(110.06)
        self.rvi.update_raw(110.19)
        self.rvi.update_raw(109.83)
        self.rvi.update_raw(109.9)
        self.rvi.update_raw(110.0)
        self.rvi.update_raw(110.03)
        self.rvi.update_raw(110.13)
        self.rvi.update_raw(109.95)
        self.rvi.update_raw(109.75)
        self.rvi.update_raw(110.15)
        self.rvi.update_raw(109.9)
        self.rvi.update_raw(110.04)

        # Assert
        assert self.rvi.value == 67.2446018137445

    def test_reset_successfully_returns_indicator_to_fresh_state(self):
        # Arrange
        self.rvi.update_raw(1.00020)
        self.rvi.update_raw(1.00030)
        self.rvi.update_raw(1.00050)

        # Act
        self.rvi.reset()

        # Assert
        assert not self.rvi.initialized
        assert self.rvi.value == 0

```

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`TestRelativeVolatilityIndex`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 4


**Classs**: `TestRelativeVolatilityIndex`
**Imports**: `nautilus_trader.indicators`, `nautilus_trader.test_kit.providers`, `nautilus_trader.test_kit.stubs.data`

## Related Files

This file is located in `tests/unit_tests/indicators/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/unit_tests/indicators/test_rvi.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:11.446219Z*
