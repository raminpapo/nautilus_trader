# Documentation: `tests/unit_tests/analysis/test_statistics_returns_avg_loss.py`
**Generated:** 2025-11-15T19:40:08.919312Z
**File Size:** 2254 bytes
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

- **Path:** `tests/unit_tests/analysis/test_statistics_returns_avg_loss.py`
- **Size:** 2,254 bytes
- **Lines:** 65
- **Extension:** `.py`
- **Type:** text
- **Imports:** 4
- **Classes:** 1
- **Functions:** 4

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

from nautilus_trader.analysis import ReturnsAverageLoss
from tests.unit_tests.analysis.conftest import convert_series_to_dict


class TestReturnsAverageLossPortfolioStatistic:
    def test_name_returns_expected_returns_expected(self):
        # Arrange
        stat = ReturnsAverageLoss()

        # Act
        result = stat.name

        # Assert
        assert result == "Average Loss (Return)"

    def test_calculate_given_empty_series_returns_nan(self):
        # Arrange
        stat = ReturnsAverageLoss()
        data = pd.Series([], dtype=float64)

        # Act
        result = stat.calculate_from_returns(convert_series_to_dict(data))

        # Assert
        assert pd.isna(result)

    def test_calculate_given_mix_of_pnls1_returns_expected(self):
        # Arrange
        stat = ReturnsAverageLoss()
        data = pd.Series([1.0, -1.0], dtype=float64)

        # Act
        result = stat.calculate_from_returns(convert_series_to_dict(data))

        # Assert
        assert result == -1.0

    def test_calculate_given_mix_of_pnls2_returns_expected(self):
        # Arrange
        stat = ReturnsAverageLoss()
        data = pd.Series([2.0, 2.0, 1.0, -1.0, -2.0], dtype=float64)

        # Act
        result = stat.calculate_from_returns(convert_series_to_dict(data))

        # Assert
        assert result == -1.5
```


---

## Overview

This file is located at `tests/unit_tests/analysis/test_statistics_returns_avg_loss.py` within the repository.

**Classes defined:** TestReturnsAverageLossPortfolioStatistic

**Functions defined:** test_name_returns_expected_returns_expected, test_calculate_given_empty_series_returns_nan, test_calculate_given_mix_of_pnls1_returns_expected, test_calculate_given_mix_of_pnls2_returns_expected

**Import statements:** 4


---

## Detailed Analysis

### Classes

#### `TestReturnsAverageLossPortfolioStatistic`


### Functions

#### `test_name_returns_expected_returns_expected(self)`


#### `test_calculate_given_empty_series_returns_nan(self)`


#### `test_calculate_given_mix_of_pnls1_returns_expected(self)`


#### `test_calculate_given_mix_of_pnls2_returns_expected(self)`


### Imports

- `import pandas as pd`
- `from numpy import float64`
- `from nautilus_trader.analysis import ReturnsAverageLoss`
- `from tests.unit_tests.analysis.conftest import convert_series_to_dict`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.analysis.test_statistics_returns_avg_loss import TestReturnsAverageLossPortfolioStatistic
```


---

## Related Files

This file imports from the following modules:

- `import pandas as pd`
- `from numpy import float64`
- `from nautilus_trader.analysis import ReturnsAverageLoss`
- `from tests.unit_tests.analysis.conftest import convert_series_to_dict`

**Directory:** `tests/unit_tests/analysis`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


