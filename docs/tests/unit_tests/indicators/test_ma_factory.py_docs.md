# Documentation: test_ma_factory.py

## File Metadata

- **Path**: `tests/unit_tests/indicators/test_ma_factory.py`
- **Size**: 3,378 bytes
- **Lines**: 84
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

from nautilus_trader.indicators import DoubleExponentialMovingAverage
from nautilus_trader.indicators import ExponentialMovingAverage
from nautilus_trader.indicators import HullMovingAverage
from nautilus_trader.indicators import MovingAverageFactory
from nautilus_trader.indicators import MovingAverageType
from nautilus_trader.indicators import SimpleMovingAverage
from nautilus_trader.indicators import VariableIndexDynamicAverage
from nautilus_trader.indicators import WeightedMovingAverage
from nautilus_trader.indicators import WilderMovingAverage
from nautilus_trader.test_kit.providers import TestInstrumentProvider


AUDUSD_SIM = TestInstrumentProvider.default_fx_ccy("AUD/USD")


class TestMaFactory:
    def test_simple_returns_expected_indicator(self):
        # Arrange, Act
        indicator = MovingAverageFactory.create(10, MovingAverageType.SIMPLE)

        # Assert
        assert isinstance(indicator, SimpleMovingAverage)

    def test_exponential_returns_expected_indicator(self):
        # Arrange, Act
        indicator = MovingAverageFactory.create(10, MovingAverageType.EXPONENTIAL)

        # Assert
        assert isinstance(indicator, ExponentialMovingAverage)

    def test_hull_returns_expected_indicator(self):
        # Arrange, Act
        indicator = MovingAverageFactory.create(10, MovingAverageType.HULL)

        # Assert
        assert isinstance(indicator, HullMovingAverage)

    def test_weighted_returns_expected_indicator(self):
        # Arrange, Act
        indicator = MovingAverageFactory.create(10, MovingAverageType.WEIGHTED)

        # Assert
        assert isinstance(indicator, WeightedMovingAverage)

    def test_wilde_returns_expected_indicator(self):
        # Arrange, Act
        indicator = MovingAverageFactory.create(10, MovingAverageType.WILDER)

        # Assert
        assert isinstance(indicator, WilderMovingAverage)

    def test_double_exponential_returns_expected_indicator(self):
        # Arrange, Act
        indicator = MovingAverageFactory.create(10, MovingAverageType.DOUBLE_EXPONENTIAL)

        # Assert
        assert isinstance(indicator, DoubleExponentialMovingAverage)

    def test_variable_index_dynamic_returns_expected_indicator(self):
        # Arrange, Act
        indicator = MovingAverageFactory.create(
            10,
            MovingAverageType.VARIABLE_INDEX_DYNAMIC,
            cmo_ma_type=MovingAverageType.SIMPLE,
        )

        # Assert
        assert isinstance(indicator, VariableIndexDynamicAverage)

```

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`TestMaFactory`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Classs**: `TestMaFactory`
**Imports**: `nautilus_trader.indicators`, `nautilus_trader.test_kit.providers`

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
pytest tests/unit_tests/indicators/test_ma_factory.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:11.436124Z*
