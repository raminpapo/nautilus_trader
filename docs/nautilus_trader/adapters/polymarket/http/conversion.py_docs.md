# Documentation: conversion.py

## File Metadata

- **Path**: `nautilus_trader/adapters/polymarket/http/conversion.py`
- **Size**: 1,554 bytes
- **Lines**: 35
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

from py_clob_client.clob_types import OrderType

from nautilus_trader.model.enums import TimeInForce
from nautilus_trader.model.enums import time_in_force_to_str


def convert_tif_to_polymarket_order_type(time_in_force) -> str:
    match time_in_force:
        case TimeInForce.GTC:
            return OrderType.GTC
        case TimeInForce.GTD:
            return OrderType.GTD
        case TimeInForce.FOK:
            return OrderType.FOK
        case TimeInForce.IOC:
            return OrderType.FAK
        case _:
            time_in_force_str = time_in_force_to_str(time_in_force)
            raise ValueError(f"invalid `TimeInForce` for conversion, was {time_in_force_str}")

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`convert_tif_to_polymarket_order_type()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Functions**: `convert_tif_to_polymarket_order_type`
**Imports**: `nautilus_trader.model.enums`, `py_clob_client.clob_types`

## Related Files

This file is located in `nautilus_trader/adapters/polymarket/http/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.960984Z*
