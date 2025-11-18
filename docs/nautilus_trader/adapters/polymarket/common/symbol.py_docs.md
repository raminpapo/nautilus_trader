# Documentation: symbol.py

## File Metadata

- **Path**: `nautilus_trader/adapters/polymarket/common/symbol.py`
- **Size**: 1,915 bytes
- **Lines**: 42
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

from nautilus_trader.adapters.polymarket.common.constants import POLYMARKET_VENUE
from nautilus_trader.model.identifiers import InstrumentId


def get_polymarket_instrument_id(condition_id: str, token_id: str | int) -> InstrumentId:
    return InstrumentId.from_str(f"{condition_id}-{token_id}.{POLYMARKET_VENUE}")


def get_polymarket_condition_id(instrument_id: InstrumentId) -> str:
    parts = instrument_id.symbol.value.split("-")
    if len(parts) != 2 or not parts[0]:
        raise ValueError(
            f"Invalid Polymarket instrument ID format: expected "
            f"'{{condition_id}}-{{token_id}}', was '{instrument_id.symbol.value}'",
        )
    return parts[0]


def get_polymarket_token_id(instrument_id: InstrumentId) -> str:
    parts = instrument_id.symbol.value.split("-")
    if len(parts) != 2 or not parts[1]:
        raise ValueError(
            f"Invalid Polymarket instrument ID format: expected "
            f"'{{condition_id}}-{{token_id}}', was '{instrument_id.symbol.value}'",
        )
    return parts[1]

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 3 function(s).

## Detailed Walkthrough

### Functions
- **`get_polymarket_instrument_id()`**: Function defined in this file
- **`get_polymarket_condition_id()`**: Function defined in this file
- **`get_polymarket_token_id()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 5


**Functions**: `get_polymarket_condition_id`, `get_polymarket_instrument_id`, `get_polymarket_token_id`
**Imports**: `nautilus_trader.adapters.polymarket.common.constants`, `nautilus_trader.model.identifiers`

## Related Files

This file is located in `nautilus_trader/adapters/polymarket/common/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.939576Z*
