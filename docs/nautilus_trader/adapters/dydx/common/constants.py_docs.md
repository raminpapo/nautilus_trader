# Documentation: constants.py

## File Metadata

- **Path**: `nautilus_trader/adapters/dydx/common/constants.py`
- **Size**: 1,434 bytes
- **Lines**: 40
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
Define constants used in the dYdX adapter.
"""

from typing import Final

from nautilus_trader.model.identifiers import ClientId
from nautilus_trader.model.identifiers import Venue


DYDX: Final[str] = "DYDX"
DYDX_VENUE: Final[Venue] = Venue(DYDX)
DYDX_CLIENT_ID: Final[ClientId] = ClientId(DYDX)

FEE_SCALING: Final[int] = 1_000_000
DEFAULT_CURRENCY: Final[str] = "USDC"

CURRENCY_MAP: Final[dict[str, str]] = {
    "USD": "USDC",
}

ACCOUNT_SEQUENCE_MISMATCH_ERROR_CODE = 32
DYDX_RETRY_ERRORS_GRPC: Final[list[int]] = [
    32,  # Account sequence mismatch
]

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 2


**Imports**: `nautilus_trader.model.identifiers`, `typing`

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
*Generated on 2025-11-18T21:55:04.706285Z*
