# Documentation: `tests/unit_tests/analysis/test_statistics_expectancy.py`
**Generated:** 2025-11-15T19:40:08.910885Z
**File Size:** 2351 bytes
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

- **Path:** `tests/unit_tests/analysis/test_statistics_expectancy.py`
- **Size:** 2,351 bytes
- **Lines:** 75
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3
- **Classes:** 1
- **Functions:** 5

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

import pandas as pd
from numpy import float64

from nautilus_trader.analysis import Expectancy


class TestExpectancyPortfolioStatistic:
    def test_name_returns_expected_returns_expected(self):
        # Arrange
        stat = Expectancy()

        # Act
        result = stat.name

        # Assert
        assert result == "Expectancy"

    def test_calculate_given_empty_series_returns_zero(self):
        # Arrange
        stat = Expectancy()
        data = pd.Series(dtype=float64)

        # Act
        result = stat.calculate_from_realized_pnls(data)

        # Assert
        assert result == 0.0

    def test_calculate_given_insufficient_data_returns_zero(self):
        # Arrange
        stat = Expectancy()
        data = pd.Series([0.0, 0.0], dtype=float64)

        # Act
        result = stat.calculate_from_realized_pnls(data)

        # Assert
        assert result == 0.0

    def test_calculate_given_one_winner_one_loser_returns_zero(self):
        # Arrange
        stat = Expectancy()
        data = pd.Series([1.0, -1.0], dtype=float64)

        # Act
        result = stat.calculate_from_realized_pnls(data)

        # Assert
        assert result == 0.0

    def test_calculate_given_mix_of_pnls_returns_expected(self):
        # Arrange
        stat = Expectancy()
        data = pd.Series([2.0, 1.5, 1.0, 0.5, -1.0], dtype=float64)

        # Act
        result = stat.calculate_from_realized_pnls(data)

        # Assert
        assert result == 0.8
```


---

## Overview

This file is located at `tests/unit_tests/analysis/test_statistics_expectancy.py` within the repository.

**Classes defined:** TestExpectancyPortfolioStatistic

**Functions defined:** test_name_returns_expected_returns_expected, test_calculate_given_empty_series_returns_zero, test_calculate_given_insufficient_data_returns_zero, test_calculate_given_one_winner_one_loser_returns_zero, test_calculate_given_mix_of_pnls_returns_expected

**Import statements:** 3


---

## Detailed Analysis

### Classes

#### `TestExpectancyPortfolioStatistic`


### Functions

#### `test_name_returns_expected_returns_expected(self)`


#### `test_calculate_given_empty_series_returns_zero(self)`


#### `test_calculate_given_insufficient_data_returns_zero(self)`


#### `test_calculate_given_one_winner_one_loser_returns_zero(self)`


#### `test_calculate_given_mix_of_pnls_returns_expected(self)`


### Imports

- `import pandas as pd`
- `from numpy import float64`
- `from nautilus_trader.analysis import Expectancy`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.analysis.test_statistics_expectancy import TestExpectancyPortfolioStatistic
```


---

## Related Files

This file imports from the following modules:

- `import pandas as pd`
- `from numpy import float64`
- `from nautilus_trader.analysis import Expectancy`

**Directory:** `tests/unit_tests/analysis`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


