# Documentation: parsing.py

## File Metadata

- **Path**: `nautilus_trader/adapters/dydx/common/parsing.py`
- **Size**: 1,372 bytes
- **Lines**: 30
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
Define common methods for parsing messages from dYdX.
"""

from nautilus_trader.adapters.dydx.common.enums import DYDXCandlesResolution
from nautilus_trader.adapters.dydx.common.enums import DYDXEnumParser
from nautilus_trader.model.data import BarType


def get_interval_from_bar_type(bar_type: BarType) -> DYDXCandlesResolution:
    """
    Convert a nautilus bar type to a dYdX candles resolution enum.
    """
    enum_parser = DYDXEnumParser()
    return enum_parser.parse_dydx_kline(bar_type)

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`get_interval_from_bar_type()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Functions**: `get_interval_from_bar_type`
**Imports**: `nautilus_trader.adapters.dydx.common.enums`, `nautilus_trader.model.data`

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
*Generated on 2025-11-18T21:55:04.711495Z*
