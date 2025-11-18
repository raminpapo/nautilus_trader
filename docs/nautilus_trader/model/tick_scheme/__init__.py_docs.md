# Documentation: __init__.py

## File Metadata

- **Path**: `nautilus_trader/model/tick_scheme/__init__.py`
- **Size**: 1,889 bytes
- **Lines**: 41
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
"""
Defines a scheme for modeling the tick space for various instruments.
"""

from nautilus_trader.model.tick_scheme.base import get_tick_scheme
from nautilus_trader.model.tick_scheme.base import register_tick_scheme
from nautilus_trader.model.tick_scheme.implementations.fixed import FOREX_3DECIMAL_TICK_SCHEME
from nautilus_trader.model.tick_scheme.implementations.fixed import FOREX_5DECIMAL_TICK_SCHEME
from nautilus_trader.model.tick_scheme.implementations.fixed import FixedTickScheme
from nautilus_trader.model.tick_scheme.implementations.tiered import TOPIX100_TICK_SCHEME
from nautilus_trader.model.tick_scheme.implementations.tiered import TieredTickScheme


register_tick_scheme(TOPIX100_TICK_SCHEME)
register_tick_scheme(FOREX_3DECIMAL_TICK_SCHEME)
register_tick_scheme(FOREX_5DECIMAL_TICK_SCHEME)

__all__ = [
    "FOREX_3DECIMAL_TICK_SCHEME",
    "FOREX_5DECIMAL_TICK_SCHEME",
    "TOPIX100_TICK_SCHEME",
    "FixedTickScheme",
    "TieredTickScheme",
    "get_tick_scheme",
    "register_tick_scheme",
]

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 3


**Imports**: `nautilus_trader.model.tick_scheme.base`, `nautilus_trader.model.tick_scheme.implementations.fixed`, `nautilus_trader.model.tick_scheme.implementations.tiered`

## Related Files

This file is located in `nautilus_trader/model/tick_scheme/`. Related files may include:
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
*Generated on 2025-11-18T21:55:05.833672Z*
