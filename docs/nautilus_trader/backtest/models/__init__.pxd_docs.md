# Documentation: __init__.pxd

## File Metadata

- **Path**: `nautilus_trader/backtest/models/__init__.pxd`
- **Size**: 1,398 bytes
- **Lines**: 24
- **Language**: Unknown

## Original Source

```
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

from nautilus_trader.accounting.margin_models cimport MarginModel
from nautilus_trader.backtest.models.aggregator cimport SpreadQuoteAggregator
from nautilus_trader.backtest.models.fee cimport FeeModel
from nautilus_trader.backtest.models.fee cimport FixedFeeModel
from nautilus_trader.backtest.models.fee cimport MakerTakerFeeModel
from nautilus_trader.backtest.models.fee cimport PerContractFeeModel
from nautilus_trader.backtest.models.fill cimport FillModel
from nautilus_trader.backtest.models.latency cimport LatencyModel

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 30


**Identifiers**: `ANY`, `All`, `BASIS`, `CONDITIONS`, `Copyright`, `FeeModel`, `FillModel`, `FixedFeeModel`, `GNU`, `General`, `KIND`, `LatencyModel`, `Lesser`, `License`, `Licensed`, `Ltd`, `MakerTakerFeeModel`, `MarginModel`, `Nautech`, `PerContractFeeModel`, `Pty`, `Public`, `See`, `SpreadQuoteAggregator`, `Systems`, `Unless`, `Version`, `WARRANTIES`, `WITHOUT`, `You`

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
pytest nautilus_trader/backtest/models/__init__.pxd

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:05.083932Z*
