# Documentation: `nautilus_trader/backtest/models/__init__.py`
**Generated:** 2025-11-15T19:40:04.579668Z
**File Size:** 2804 bytes
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

- **Path:** `nautilus_trader/backtest/models/__init__.py`
- **Size:** 2,804 bytes
- **Lines:** 60
- **Extension:** `.py`
- **Type:** text
- **Imports:** 20

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

from nautilus_trader.accounting.margin_models import LeveragedMarginModel
from nautilus_trader.accounting.margin_models import MarginModel
from nautilus_trader.accounting.margin_models import StandardMarginModel
from nautilus_trader.backtest.models.aggregator import SpreadQuoteAggregator
from nautilus_trader.backtest.models.fee import FeeModel
from nautilus_trader.backtest.models.fee import FixedFeeModel
from nautilus_trader.backtest.models.fee import MakerTakerFeeModel
from nautilus_trader.backtest.models.fee import PerContractFeeModel
from nautilus_trader.backtest.models.fill import BestPriceFillModel
from nautilus_trader.backtest.models.fill import CompetitionAwareFillModel
from nautilus_trader.backtest.models.fill import FillModel
from nautilus_trader.backtest.models.fill import LimitOrderPartialFillModel
from nautilus_trader.backtest.models.fill import MarketHoursFillModel
from nautilus_trader.backtest.models.fill import OneTickSlippageFillModel
from nautilus_trader.backtest.models.fill import ProbabilisticFillModel
from nautilus_trader.backtest.models.fill import SizeAwareFillModel
from nautilus_trader.backtest.models.fill import ThreeTierFillModel
from nautilus_trader.backtest.models.fill import TwoTierFillModel
from nautilus_trader.backtest.models.fill import VolumeSensitiveFillModel
from nautilus_trader.backtest.models.latency import LatencyModel


__all__ = [
    "BestPriceFillModel",
    "CompetitionAwareFillModel",
    "FeeModel",
    "FillModel",
    "FixedFeeModel",
    "LatencyModel",
    "LeveragedMarginModel",
    "LimitOrderPartialFillModel",
    "MakerTakerFeeModel",
    "MarginModel",
    "MarginModel",
    "MarketHoursFillModel",
    "OneTickSlippageFillModel",
    "PerContractFeeModel",
    "ProbabilisticFillModel",
    "SizeAwareFillModel",
    "SpreadQuoteAggregator",
    "StandardMarginModel",
    "ThreeTierFillModel",
    "TwoTierFillModel",
    "VolumeSensitiveFillModel",
]
```


---

## Overview

This file is located at `nautilus_trader/backtest/models/__init__.py` within the repository.

This is a Python package initialization file that may expose package contents or execute initialization code.

**Import statements:** 20


---

## Detailed Analysis

### Imports

- `from nautilus_trader.accounting.margin_models import LeveragedMarginModel`
- `from nautilus_trader.accounting.margin_models import MarginModel`
- `from nautilus_trader.accounting.margin_models import StandardMarginModel`
- `from nautilus_trader.backtest.models.aggregator import SpreadQuoteAggregator`
- `from nautilus_trader.backtest.models.fee import FeeModel`
- `from nautilus_trader.backtest.models.fee import FixedFeeModel`
- `from nautilus_trader.backtest.models.fee import MakerTakerFeeModel`
- `from nautilus_trader.backtest.models.fee import PerContractFeeModel`
- `from nautilus_trader.backtest.models.fill import BestPriceFillModel`
- `from nautilus_trader.backtest.models.fill import CompetitionAwareFillModel`
- `from nautilus_trader.backtest.models.fill import FillModel`
- `from nautilus_trader.backtest.models.fill import LimitOrderPartialFillModel`
- `from nautilus_trader.backtest.models.fill import MarketHoursFillModel`
- `from nautilus_trader.backtest.models.fill import OneTickSlippageFillModel`
- `from nautilus_trader.backtest.models.fill import ProbabilisticFillModel`
- `from nautilus_trader.backtest.models.fill import SizeAwareFillModel`
- `from nautilus_trader.backtest.models.fill import ThreeTierFillModel`
- `from nautilus_trader.backtest.models.fill import TwoTierFillModel`
- `from nautilus_trader.backtest.models.fill import VolumeSensitiveFillModel`
- `from nautilus_trader.backtest.models.latency import LatencyModel`


---

## Usage Examples

### Importing

```python
import nautilus_trader.backtest.models.__init__
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.accounting.margin_models import LeveragedMarginModel`
- `from nautilus_trader.accounting.margin_models import MarginModel`
- `from nautilus_trader.accounting.margin_models import StandardMarginModel`
- `from nautilus_trader.backtest.models.aggregator import SpreadQuoteAggregator`
- `from nautilus_trader.backtest.models.fee import FeeModel`
- `from nautilus_trader.backtest.models.fee import FixedFeeModel`
- `from nautilus_trader.backtest.models.fee import MakerTakerFeeModel`
- `from nautilus_trader.backtest.models.fee import PerContractFeeModel`
- `from nautilus_trader.backtest.models.fill import BestPriceFillModel`
- `from nautilus_trader.backtest.models.fill import CompetitionAwareFillModel`

*... and 10 more*

**Directory:** `nautilus_trader/backtest/models`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


