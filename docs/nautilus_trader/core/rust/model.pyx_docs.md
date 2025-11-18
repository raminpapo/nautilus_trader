# Documentation: model.pyx

## File Metadata

- **Path**: `nautilus_trader/core/rust/model.pyx`
- **Size**: 2,704 bytes
- **Lines**: 42
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

# Allows importing as Python enum from other modules

from nautilus_trader.core.rust.model cimport AccountType  # type: ignore
from nautilus_trader.core.rust.model cimport AggregationSource  # type: ignore
from nautilus_trader.core.rust.model cimport AggressorSide  # type: ignore
from nautilus_trader.core.rust.model cimport AssetClass  # type: ignore
from nautilus_trader.core.rust.model cimport BookAction  # type: ignore
from nautilus_trader.core.rust.model cimport BookType  # type: ignore
from nautilus_trader.core.rust.model cimport ContingencyType  # type: ignore
from nautilus_trader.core.rust.model cimport CurrencyType  # type: ignore
from nautilus_trader.core.rust.model cimport InstrumentClass  # type: ignore
from nautilus_trader.core.rust.model cimport InstrumentCloseType  # type: ignore
from nautilus_trader.core.rust.model cimport LiquiditySide  # type: ignore
from nautilus_trader.core.rust.model cimport MarketStatus  # type: ignore
from nautilus_trader.core.rust.model cimport MarketStatusAction  # type: ignore
from nautilus_trader.core.rust.model cimport OmsType  # type: ignore
from nautilus_trader.core.rust.model cimport OptionKind  # type: ignore
from nautilus_trader.core.rust.model cimport OrderSide  # type: ignore
from nautilus_trader.core.rust.model cimport OrderStatus  # type: ignore
from nautilus_trader.core.rust.model cimport OrderType  # type: ignore
from nautilus_trader.core.rust.model cimport PositionSide  # type: ignore
from nautilus_trader.core.rust.model cimport PriceType  # type: ignore
from nautilus_trader.core.rust.model cimport TimeInForce  # type: ignore
from nautilus_trader.core.rust.model cimport TradingState  # type: ignore
from nautilus_trader.core.rust.model cimport TrailingOffsetType  # type: ignore
from nautilus_trader.core.rust.model cimport TriggerType  # type: ignore

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 48


**Identifiers**: `ANY`, `AccountType`, `AggregationSource`, `AggressorSide`, `All`, `Allows`, `AssetClass`, `BASIS`, `BookAction`, `BookType`, `CONDITIONS`, `ContingencyType`, `Copyright`, `CurrencyType`, `GNU`, `General`, `InstrumentClass`, `InstrumentCloseType`, `KIND`, `Lesser`, `License`, `Licensed`, `LiquiditySide`, `Ltd`, `MarketStatus`, `MarketStatusAction`, `Nautech`, `OmsType`, `OptionKind`, `OrderSide` *(+18 more)*

## Related Files

This file is located in `nautilus_trader/core/rust/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

Tests for this file may be located in:
- `tests/` directory in the same folder
- Corresponding test module in the project

Run the full test suite to verify functionality.

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:05.359627Z*
