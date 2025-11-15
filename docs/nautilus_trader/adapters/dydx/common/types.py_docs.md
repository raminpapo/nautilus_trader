# Documentation: `nautilus_trader/adapters/dydx/common/types.py`
**Generated:** 2025-11-15T19:40:04.246696Z
**File Size:** 2502 bytes
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

- **Path:** `nautilus_trader/adapters/dydx/common/types.py`
- **Size:** 2,502 bytes
- **Lines:** 83
- **Extension:** `.py`
- **Type:** text
- **Imports:** 7
- **Classes:** 1
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

from __future__ import annotations

from decimal import Decimal
from typing import Any

import pyarrow as pa

from nautilus_trader.core import Data
from nautilus_trader.model.custom import customdataclass
from nautilus_trader.model.identifiers import InstrumentId


@customdataclass
class DYDXOraclePrice(Data):
    """
    Represents an oracle price.
    """

    instrument_id: InstrumentId
    price: Decimal

    _schema = pa.schema(
        {
            "instrument_id": pa.string(),
            "price": pa.string(),
            "ts_event": pa.int64(),
            "ts_init": pa.int64(),
        },
        metadata={"type": "DYDXOraclePrice"},
    )

    def to_dict(self, to_arrow=False) -> dict[str, Any]:
        """
        Return a dictionary representation of this object.

        Returns
        -------
        dict[str, Any]

        """
        return {
            "instrument_id": self.instrument_id.value,
            "price": str(self.price),
            "ts_event": self.ts_event,
            "ts_init": self.ts_init,
        }

    @staticmethod
    def from_dict(values: dict[str, Any]) -> DYDXOraclePrice:
        """
        Return a DYDXOraclePrice parsed from the given values.

        Parameters
        ----------
        values : dict[str, Any]
            The values for initialization.

        Returns
        -------
        DYDXOraclePrice

        """
        return DYDXOraclePrice(
            instrument_id=InstrumentId.from_str(values["instrument_id"]),
            price=Decimal(values["price"]),
            ts_event=values["ts_event"],
            ts_init=values["ts_init"],
        )
```


---

## Overview

This file is located at `nautilus_trader/adapters/dydx/common/types.py` within the repository.

**Classes defined:** DYDXOraclePrice

**Functions defined:** to_dict, from_dict

**Import statements:** 7


---

## Detailed Analysis

### Classes

#### `DYDXOraclePrice`

**Inherits from:** Data


### Functions

#### `to_dict(self, to_arrow=False)`


#### `from_dict(values: dict[str, Any])`


### Imports

- `from __future__ import annotations`
- `from decimal import Decimal`
- `from typing import Any`
- `import pyarrow as pa`
- `from nautilus_trader.core import Data`
- `from nautilus_trader.model.custom import customdataclass`
- `from nautilus_trader.model.identifiers import InstrumentId`


---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters.dydx.common.types import DYDXOraclePrice
```


---

## Related Files

This file imports from the following modules:

- `from __future__ import annotations`
- `from decimal import Decimal`
- `from typing import Any`
- `import pyarrow as pa`
- `from nautilus_trader.core import Data`
- `from nautilus_trader.model.custom import customdataclass`
- `from nautilus_trader.model.identifiers import InstrumentId`

**Directory:** `nautilus_trader/adapters/dydx/common`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


