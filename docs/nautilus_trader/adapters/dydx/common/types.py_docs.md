# Documentation: types.py

## File Metadata

- **Path**: `nautilus_trader/adapters/dydx/common/types.py`
- **Size**: 2,502 bytes
- **Lines**: 84
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

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`DYDXOraclePrice`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 8


**Classs**: `DYDXOraclePrice`
**Imports**: `__future__`, `decimal`, `nautilus_trader.core`, `nautilus_trader.model.custom`, `nautilus_trader.model.identifiers`, `pyarrow`, `typing`

## Related Files

This file is located in `nautilus_trader/adapters/dydx/common/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.714005Z*
