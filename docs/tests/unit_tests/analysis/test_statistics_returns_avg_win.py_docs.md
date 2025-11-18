# Documentation: test_statistics_returns_avg_win.py

## File Metadata

- **Path**: `tests/unit_tests/analysis/test_statistics_returns_avg_win.py`
- **Size**: 2,260 bytes
- **Lines**: 66
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

import pandas as pd
from numpy import float64

from nautilus_trader.analysis import ReturnsAverageWin
from tests.unit_tests.analysis.conftest import convert_series_to_dict


class TestReturnsAverageWinPortfolioStatistic:
    def test_name_returns_expected_returns_expected(self):
        # Arrange
        stat = ReturnsAverageWin()

        # Act
        result = stat.name

        # Assert
        assert result == "Average Win (Return)"

    def test_calculate_given_empty_series_returns_nan(self):
        # Arrange
        stat = ReturnsAverageWin()
        data = pd.Series([], dtype=float64)

        # Act
        result = stat.calculate_from_returns(convert_series_to_dict(data))

        # Assert
        assert pd.isna(result)

    def test_calculate_given_mix_of_pnls1_returns_expected(self):
        # Arrange
        stat = ReturnsAverageWin()
        data = pd.Series([1.0, -1.0], dtype=float64)

        # Act
        result = stat.calculate_from_returns(convert_series_to_dict(data))

        # Assert
        assert result == 1.0

    def test_calculate_given_mix_of_pnls2_returns_expected(self):
        # Arrange
        stat = ReturnsAverageWin()
        data = pd.Series([2.0, 2.0, 1.0, -1.0, -2.0], dtype=float64)

        # Act
        result = stat.calculate_from_returns(convert_series_to_dict(data))

        # Assert
        assert result == 1.6666666666666667

```

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`TestReturnsAverageWinPortfolioStatistic`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 5


**Classs**: `TestReturnsAverageWinPortfolioStatistic`
**Imports**: `nautilus_trader.analysis`, `numpy`, `pandas`, `tests.unit_tests.analysis.conftest`

## Related Files

This file is located in `tests/unit_tests/analysis/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/unit_tests/analysis/test_statistics_returns_avg_win.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:11.132829Z*
