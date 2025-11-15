# Documentation: `nautilus_trader/persistence/funcs.py`
**Generated:** 2025-11-15T19:40:05.253626Z
**File Size:** 3109 bytes
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

- **Path:** `nautilus_trader/persistence/funcs.py`
- **Size:** 3,109 bytes
- **Lines:** 92
- **Extension:** `.py`
- **Type:** text
- **Imports:** 11
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

from nautilus_trader.core.inspect import is_nautilus_class
from nautilus_trader.core.nautilus_pyo3 import convert_to_snake_case
from nautilus_trader.model.data import Bar
from nautilus_trader.model.data import BarType
from nautilus_trader.model.data import MarkPriceUpdate
from nautilus_trader.model.data import OrderBookDelta
from nautilus_trader.model.data import OrderBookDepth10
from nautilus_trader.model.data import QuoteTick
from nautilus_trader.model.data import TradeTick
from nautilus_trader.model.identifiers import InstrumentId
from nautilus_trader.serialization.arrow.serializer import _ARROW_ENCODERS


CUSTOM_DATA_PREFIX = "custom_"


def class_to_filename(cls: type) -> str:
    """
    Convert the given class to a filename.
    """
    filename_mappings = {
        "OrderBookDelta": "OrderBookDeltas",
        "OrderBookDeltas": "OrderBookDeltas",
        "OrderBookDepth10": "OrderBookDepths",
    }
    name = f"{convert_to_snake_case(filename_mappings.get(cls.__name__, cls.__name__))}"

    if not is_nautilus_class(cls):
        name = f"{CUSTOM_DATA_PREFIX}{name}"

    return name


def filename_to_class(filename: str) -> type | None:
    """
    Convert the given filename back to a class.
    """
    builtin_filename_to_class = {
        "quote_tick": QuoteTick,
        "trade_tick": TradeTick,
        "bar": Bar,
        "order_book_deltas": OrderBookDelta,
        "order_book_depths": OrderBookDepth10,
        "mark_price_update": MarkPriceUpdate,
    }

    if filename in builtin_filename_to_class:
        return builtin_filename_to_class[filename]

    for data_cls in _ARROW_ENCODERS:
        if class_to_filename(data_cls) == filename:
            return data_cls

    return None


def urisafe_identifier(identifier: InstrumentId | BarType | str) -> str:
    """
    Convert an instrument_id into a valid URI for writing to a file path.
    """
    return str(identifier).replace("/", "")


def combine_filters(*filters):
    filters = tuple(x for x in filters if x is not None)

    if len(filters) == 0:
        return None
    elif len(filters) == 1:
        return filters[0]
    else:
        expr = filters[0]

        for f in filters[1:]:
            expr = expr & f

        return expr
```


---

## Overview

This file is located at `nautilus_trader/persistence/funcs.py` within the repository.

**Functions defined:** class_to_filename, filename_to_class, urisafe_identifier, combine_filters

**Import statements:** 11


---

## Detailed Analysis

### Functions

#### `class_to_filename(cls: type)`


#### `filename_to_class(filename: str)`


#### `urisafe_identifier(identifier: InstrumentId | BarType | str)`


#### `combine_filters(*filters)`


### Imports

- `from nautilus_trader.core.inspect import is_nautilus_class`
- `from nautilus_trader.core.nautilus_pyo3 import convert_to_snake_case`
- `from nautilus_trader.model.data import Bar`
- `from nautilus_trader.model.data import BarType`
- `from nautilus_trader.model.data import MarkPriceUpdate`
- `from nautilus_trader.model.data import OrderBookDelta`
- `from nautilus_trader.model.data import OrderBookDepth10`
- `from nautilus_trader.model.data import QuoteTick`
- `from nautilus_trader.model.data import TradeTick`
- `from nautilus_trader.model.identifiers import InstrumentId`
- `from nautilus_trader.serialization.arrow.serializer import _ARROW_ENCODERS`


---

## Usage Examples

### Importing

```python
from nautilus_trader.persistence.funcs import class_to_filename
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.core.inspect import is_nautilus_class`
- `from nautilus_trader.core.nautilus_pyo3 import convert_to_snake_case`
- `from nautilus_trader.model.data import Bar`
- `from nautilus_trader.model.data import BarType`
- `from nautilus_trader.model.data import MarkPriceUpdate`
- `from nautilus_trader.model.data import OrderBookDelta`
- `from nautilus_trader.model.data import OrderBookDepth10`
- `from nautilus_trader.model.data import QuoteTick`
- `from nautilus_trader.model.data import TradeTick`
- `from nautilus_trader.model.identifiers import InstrumentId`

*... and 1 more*

**Directory:** `nautilus_trader/persistence`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


