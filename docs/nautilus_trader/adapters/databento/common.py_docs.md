# Documentation: `nautilus_trader/adapters/databento/common.py`
**Generated:** 2025-11-15T19:40:04.216596Z
**File Size:** 3142 bytes
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

- **Path:** `nautilus_trader/adapters/databento/common.py`
- **Size:** 3,142 bytes
- **Lines:** 83
- **Extension:** `.py`
- **Type:** text
- **Imports:** 7
- **Functions:** 2

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

from nautilus_trader.adapters.databento.enums import DatabentoSchema
from nautilus_trader.core import nautilus_pyo3
from nautilus_trader.core.correctness import PyCondition
from nautilus_trader.model.data import BarType
from nautilus_trader.model.enums import BarAggregation
from nautilus_trader.model.enums import PriceType
from nautilus_trader.model.identifiers import InstrumentId


def instrument_id_to_pyo3(
    instrument_id: InstrumentId | nautilus_pyo3.InstrumentId,
) -> nautilus_pyo3.InstrumentId:
    if isinstance(instrument_id, nautilus_pyo3.InstrumentId):
        return instrument_id

    return nautilus_pyo3.InstrumentId.from_str(instrument_id.value)


def databento_schema_from_nautilus_bar_type(bar_type: BarType) -> DatabentoSchema:
    """
    Return the Databento bar aggregate schema string for the given Nautilus `bar_type`.

    Parameters
    ----------
    bar_type : BarType
        The bar type for the schema.

    Returns
    -------
    str

    Raises
    ------
    ValueError
        If any property of `bar_type` is invalid to map to a Databento schema.

    """
    PyCondition.is_true(bar_type.is_externally_aggregated(), "aggregation_source is not EXTERNAL")

    if not bar_type.spec.is_time_aggregated():
        raise ValueError(
            f"Invalid bar type '{bar_type}' (only time bars are aggregated by Databento).",
        )

    if bar_type.spec.price_type != PriceType.LAST:
        raise ValueError(
            f"Invalid bar type '{bar_type}' (only `LAST` price bars are aggregated by Databento).",
        )

    if bar_type.spec.step != 1:
        raise ValueError(
            f"Invalid bar type '{bar_type}' (only a step of 1 is supported by Databento).",
        )

    match bar_type.spec.aggregation:
        case BarAggregation.SECOND:
            return DatabentoSchema.OHLCV_1S
        case BarAggregation.MINUTE:
            return DatabentoSchema.OHLCV_1M
        case BarAggregation.HOUR:
            return DatabentoSchema.OHLCV_1H
        case BarAggregation.DAY:
            return DatabentoSchema.OHLCV_1D
        case _:
            raise ValueError(
                f"Invalid bar type '{bar_type}'. "
                "Use any of ['SECOND', 'MINUTE', 'HOUR', 'DAY'] time aggregations.",
            )
```


---

## Overview

This file is located at `nautilus_trader/adapters/databento/common.py` within the repository.

**Functions defined:** instrument_id_to_pyo3, databento_schema_from_nautilus_bar_type

**Import statements:** 7


---

## Detailed Analysis

### Functions

#### `instrument_id_to_pyo3(
    instrument_id: InstrumentId | nautilus_pyo3.InstrumentId,
)`


#### `databento_schema_from_nautilus_bar_type(bar_type: BarType)`


### Imports

- `from nautilus_trader.adapters.databento.enums import DatabentoSchema`
- `from nautilus_trader.core import nautilus_pyo3`
- `from nautilus_trader.core.correctness import PyCondition`
- `from nautilus_trader.model.data import BarType`
- `from nautilus_trader.model.enums import BarAggregation`
- `from nautilus_trader.model.enums import PriceType`
- `from nautilus_trader.model.identifiers import InstrumentId`


---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters.databento.common import instrument_id_to_pyo3
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.adapters.databento.enums import DatabentoSchema`
- `from nautilus_trader.core import nautilus_pyo3`
- `from nautilus_trader.core.correctness import PyCondition`
- `from nautilus_trader.model.data import BarType`
- `from nautilus_trader.model.enums import BarAggregation`
- `from nautilus_trader.model.enums import PriceType`
- `from nautilus_trader.model.identifiers import InstrumentId`

**Directory:** `nautilus_trader/adapters/databento`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


