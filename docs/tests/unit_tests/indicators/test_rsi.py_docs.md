# Documentation: test_rsi.py

## File Metadata

- **Path**: `tests/unit_tests/indicators/test_rsi.py`
- **Size**: 5,063 bytes
- **Lines**: 154
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

from nautilus_trader.indicators import RelativeStrengthIndex
from nautilus_trader.test_kit.providers import TestInstrumentProvider
from nautilus_trader.test_kit.stubs.data import TestDataStubs


AUDUSD_SIM = TestInstrumentProvider.default_fx_ccy("AUD/USD")


class TestRelativeStrengthIndex:
    def setup(self):
        # Fixture Setup
        self.rsi = RelativeStrengthIndex(10)

    def test_name_returns_expected_string(self):
        # Arrange, Act, Assert
        assert self.rsi.name == "RelativeStrengthIndex"

    def test_str_repr_returns_expected_string(self):
        # Arrange, Act, Assert
        assert str(self.rsi) == "RelativeStrengthIndex(10, EXPONENTIAL)"
        assert repr(self.rsi) == "RelativeStrengthIndex(10, EXPONENTIAL)"

    def test_period_returns_expected_value(self):
        # Arrange, Act, Assert
        assert self.rsi.period == 10

    def test_initialized_without_inputs_returns_false(self):
        # Arrange, Act, Assert
        assert self.rsi.initialized is False

    def test_initialized_with_required_inputs_returns_true(self):
        # Arrange
        self.rsi.update_raw(1.00000)
        self.rsi.update_raw(2.00000)
        self.rsi.update_raw(3.00000)
        self.rsi.update_raw(4.00000)
        self.rsi.update_raw(5.00000)
        self.rsi.update_raw(6.00000)
        self.rsi.update_raw(7.00000)
        self.rsi.update_raw(8.00000)
        self.rsi.update_raw(9.00000)
        self.rsi.update_raw(10.00000)

        # Act, Assert
        assert self.rsi.initialized is True

    def test_handle_bar_updates_indicator(self):
        # Arrange
        indicator = RelativeStrengthIndex(10)

        bar = TestDataStubs.bar_5decimal()

        # Act
        indicator.handle_bar(bar)

        # Assert
        assert indicator.has_inputs
        assert indicator.value == 1.0

    def test_value_with_one_input_returns_expected_value(self):
        # Arrange
        self.rsi.update_raw(1.00000)

        # Act, Assert
        assert self.rsi.value == 1

    def test_value_with_all_higher_inputs_returns_expected_value(self):
        # Arrange
        self.rsi.update_raw(1.00000)
        self.rsi.update_raw(2.00000)
        self.rsi.update_raw(3.00000)
        self.rsi.update_raw(4.00000)

        # Act, Assert
        assert self.rsi.value == 1

    def test_value_with_all_lower_inputs_returns_expected_value(self):
        # Arrange
        self.rsi.update_raw(3.00000)
        self.rsi.update_raw(2.00000)
        self.rsi.update_raw(1.00000)
        self.rsi.update_raw(0.50000)

        # Act, Assert
        assert self.rsi.value == 0

    def test_value_with_various_inputs_returns_expected_value(self):
        # Arrange
        self.rsi.update_raw(3.00000)
        self.rsi.update_raw(2.00000)
        self.rsi.update_raw(5.00000)
        self.rsi.update_raw(6.00000)
        self.rsi.update_raw(7.00000)
        self.rsi.update_raw(6.00000)

        # Act, Assert
        assert self.rsi.value == 0.6837363325825265

    def test_value_at_returns_expected_value(self):
        # Arrange
        self.rsi.update_raw(3.00000)
        self.rsi.update_raw(2.00000)
        self.rsi.update_raw(5.00000)
        self.rsi.update_raw(6.00000)
        self.rsi.update_raw(7.00000)
        self.rsi.update_raw(6.00000)
        self.rsi.update_raw(6.00000)
        self.rsi.update_raw(7.00000)

        # Act, Assert
        assert self.rsi.value == 0.7615344667662725

    def test_min_value_as_first(self):
        # Arrange
        self.rsi.update_raw(1.00000)
        self.rsi.update_raw(2.00000)
        self.rsi.update_raw(3.00000)
        self.rsi.update_raw(4.00000)
        self.rsi.update_raw(5.00000)
        self.rsi.update_raw(6.00000)
        self.rsi.update_raw(7.00000)
        self.rsi.update_raw(2.00000)

        # Act, Assert
        assert self.rsi.value == 0.38650828748031707

    def test_reset_successfully_returns_indicator_to_fresh_state(self):
        # Arrange
        self.rsi.update_raw(1.00020)
        self.rsi.update_raw(1.00030)
        self.rsi.update_raw(1.00050)

        # Act
        self.rsi.reset()

        # Assert
        assert not self.rsi.initialized
        assert self.rsi.value == 0

```

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`TestRelativeStrengthIndex`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 4


**Classs**: `TestRelativeStrengthIndex`
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
pytest tests/unit_tests/indicators/test_rsi.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:11.444895Z*
