# Documentation: __init__.py

## File Metadata

- **Path**: `nautilus_trader/backtest/models/__init__.py`
- **Size**: 2,804 bytes
- **Lines**: 61
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

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 5


**Imports**: `nautilus_trader.accounting.margin_models`, `nautilus_trader.backtest.models.aggregator`, `nautilus_trader.backtest.models.fee`, `nautilus_trader.backtest.models.fill`, `nautilus_trader.backtest.models.latency`

## Related Files

This file is located in `nautilus_trader/backtest/models/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest nautilus_trader/backtest/models/__init__.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:05.085266Z*
