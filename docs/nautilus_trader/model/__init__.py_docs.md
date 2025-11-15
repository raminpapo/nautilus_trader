# Documentation: `nautilus_trader/model/__init__.py`
**Generated:** 2025-11-15T19:40:05.019014Z
**File Size:** 4967 bytes
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

- **Path:** `nautilus_trader/model/__init__.py`
- **Size:** 4,967 bytes
- **Lines:** 134
- **Extension:** `.py`
- **Type:** text
- **Imports:** 42
- **Functions:** 1

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
"""
The `model` subpackage defines a rich trading domain model.

The domain model is agnostic of any system design, seeking to represent the logic and
state transitions of trading in a generic way. Many system implementations could be
built around this domain model.

"""

from decimal import ROUND_HALF_UP
from decimal import Decimal

from nautilus_trader.core import nautilus_pyo3
from nautilus_trader.model.book import BookLevel
from nautilus_trader.model.book import OrderBook
from nautilus_trader.model.data import Bar
from nautilus_trader.model.data import BarSpecification
from nautilus_trader.model.data import BarType
from nautilus_trader.model.data import BookOrder
from nautilus_trader.model.data import CustomData
from nautilus_trader.model.data import DataType
from nautilus_trader.model.data import FundingRateUpdate
from nautilus_trader.model.data import InstrumentClose
from nautilus_trader.model.data import InstrumentStatus
from nautilus_trader.model.data import MarkPriceUpdate
from nautilus_trader.model.data import OrderBookDelta
from nautilus_trader.model.data import OrderBookDeltas
from nautilus_trader.model.data import OrderBookDepth10
from nautilus_trader.model.data import QuoteTick
from nautilus_trader.model.data import TradeTick
from nautilus_trader.model.identifiers import AccountId
from nautilus_trader.model.identifiers import ClientId
from nautilus_trader.model.identifiers import ClientOrderId
from nautilus_trader.model.identifiers import ComponentId
from nautilus_trader.model.identifiers import ExecAlgorithmId
from nautilus_trader.model.identifiers import InstrumentId
from nautilus_trader.model.identifiers import OrderListId
from nautilus_trader.model.identifiers import PositionId
from nautilus_trader.model.identifiers import StrategyId
from nautilus_trader.model.identifiers import Symbol
from nautilus_trader.model.identifiers import TradeId
from nautilus_trader.model.identifiers import TraderId
from nautilus_trader.model.identifiers import Venue
from nautilus_trader.model.identifiers import VenueOrderId
from nautilus_trader.model.objects import FIXED_PRECISION
from nautilus_trader.model.objects import AccountBalance
from nautilus_trader.model.objects import Currency
from nautilus_trader.model.objects import MarginBalance
from nautilus_trader.model.objects import Money
from nautilus_trader.model.objects import Price
from nautilus_trader.model.objects import Quantity
from nautilus_trader.model.position import Position


# Defines all order book data types (capable of updating an L2_MBP and L3_MBO book)
BOOK_DATA_TYPES: set[type] = {
    OrderBookDelta,
    OrderBookDeltas,
    OrderBookDepth10,
}

NAUTILUS_PYO3_DATA_TYPES: tuple[type, ...] = (
    nautilus_pyo3.OrderBookDelta,
    nautilus_pyo3.OrderBookDepth10,
    nautilus_pyo3.QuoteTick,
    nautilus_pyo3.TradeTick,
    nautilus_pyo3.Bar,
)


# Convert the given value into the raw integer representation based on the given precision
# and currently compiled precision mode (128-bit for HIGH_PRECISION or 64-bit).
def convert_to_raw_int(value, precision: int) -> int:
    # Use Decimal for exact decimal arithmetic to avoid platform-specific
    # floating-point rounding differences.
    decimal_value = Decimal(str(value))
    quantized = decimal_value.quantize(Decimal(10) ** -precision, rounding=ROUND_HALF_UP)
    return int(quantized * (10**FIXED_PRECISION))


__all__ = [
    "AccountBalance",
    "AccountId",
    "Bar",
    "BarSpecification",
    "BarType",
    "BookLevel",
    "BookOrder",
    "ClientId",
    "ClientOrderId",
    "ComponentId",
    "Currency",
    "CustomData",
    "DataType",
    "ExecAlgorithmId",
    "FundingRateUpdate",
    "InstrumentClose",
    "InstrumentId",
    "InstrumentStatus",
    "MarginBalance",
    "MarkPriceUpdate",
    "Money",
    "OrderBook",
    "OrderBookDelta",
    "OrderBookDeltas",
    "OrderBookDepth10",
    "OrderListId",
    "Position",
    "PositionId",
    "Price",
    "Quantity",
    "QuoteTick",
    "StrategyId",
    "Symbol",
    "TradeId",
    "TradeTick",
    "TraderId",
    "Venue",
    "VenueOrderId",
]
```


---

## Overview

This file is located at `nautilus_trader/model/__init__.py` within the repository.

This is a Python package initialization file that may expose package contents or execute initialization code.

**Functions defined:** convert_to_raw_int

**Import statements:** 42


---

## Detailed Analysis

### Functions

#### `convert_to_raw_int(value, precision: int)`


### Imports

- `from decimal import ROUND_HALF_UP`
- `from decimal import Decimal`
- `from nautilus_trader.core import nautilus_pyo3`
- `from nautilus_trader.model.book import BookLevel`
- `from nautilus_trader.model.book import OrderBook`
- `from nautilus_trader.model.data import Bar`
- `from nautilus_trader.model.data import BarSpecification`
- `from nautilus_trader.model.data import BarType`
- `from nautilus_trader.model.data import BookOrder`
- `from nautilus_trader.model.data import CustomData`
- `from nautilus_trader.model.data import DataType`
- `from nautilus_trader.model.data import FundingRateUpdate`
- `from nautilus_trader.model.data import InstrumentClose`
- `from nautilus_trader.model.data import InstrumentStatus`
- `from nautilus_trader.model.data import MarkPriceUpdate`
- `from nautilus_trader.model.data import OrderBookDelta`
- `from nautilus_trader.model.data import OrderBookDeltas`
- `from nautilus_trader.model.data import OrderBookDepth10`
- `from nautilus_trader.model.data import QuoteTick`
- `from nautilus_trader.model.data import TradeTick`
- `from nautilus_trader.model.identifiers import AccountId`
- `from nautilus_trader.model.identifiers import ClientId`
- `from nautilus_trader.model.identifiers import ClientOrderId`
- `from nautilus_trader.model.identifiers import ComponentId`
- `from nautilus_trader.model.identifiers import ExecAlgorithmId`
- `from nautilus_trader.model.identifiers import InstrumentId`
- `from nautilus_trader.model.identifiers import OrderListId`
- `from nautilus_trader.model.identifiers import PositionId`
- `from nautilus_trader.model.identifiers import StrategyId`
- `from nautilus_trader.model.identifiers import Symbol`

*... and 12 more imports*


---

## Usage Examples

### Importing

```python
from nautilus_trader.model.__init__ import convert_to_raw_int
```


---

## Related Files

This file imports from the following modules:

- `from decimal import ROUND_HALF_UP`
- `from decimal import Decimal`
- `from nautilus_trader.core import nautilus_pyo3`
- `from nautilus_trader.model.book import BookLevel`
- `from nautilus_trader.model.book import OrderBook`
- `from nautilus_trader.model.data import Bar`
- `from nautilus_trader.model.data import BarSpecification`
- `from nautilus_trader.model.data import BarType`
- `from nautilus_trader.model.data import BookOrder`
- `from nautilus_trader.model.data import CustomData`

*... and 32 more*

**Directory:** `nautilus_trader/model`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


