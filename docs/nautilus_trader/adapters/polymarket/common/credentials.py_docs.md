# Documentation: credentials.py

## File Metadata

- **Path**: `nautilus_trader/adapters/polymarket/common/credentials.py`
- **Size**: 1,482 bytes
- **Lines**: 45
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

import msgspec

from nautilus_trader.adapters.env import get_env_key


def get_polymarket_api_key() -> str:
    return get_env_key("POLYMARKET_API_KEY")


def get_polymarket_api_secret() -> str:
    return get_env_key("POLYMARKET_API_SECRET")


def get_polymarket_passphrase() -> str:
    return get_env_key("POLYMARKET_PASSPHRASE")


def get_polymarket_private_key() -> str:
    return get_env_key("POLYMARKET_PK")


def get_polymarket_funder() -> str:
    return get_env_key("POLYMARKET_FUNDER")


class PolymarketWebSocketAuth(msgspec.Struct, frozen=True):
    apiKey: str
    secret: str
    passphrase: str

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 5 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`get_polymarket_api_key()`**: Function defined in this file
- **`get_polymarket_api_secret()`**: Function defined in this file
- **`get_polymarket_passphrase()`**: Function defined in this file
- **`get_polymarket_private_key()`**: Function defined in this file
- **`get_polymarket_funder()`**: Function defined in this file

### Classes
- **`PolymarketWebSocketAuth`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 8


**Classs**: `PolymarketWebSocketAuth`
**Functions**: `get_polymarket_api_key`, `get_polymarket_api_secret`, `get_polymarket_funder`, `get_polymarket_passphrase`, `get_polymarket_private_key`
**Imports**: `msgspec`, `nautilus_trader.adapters.env`

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

⚠️ **Security**: This file may handle sensitive data. Ensure proper encryption and access controls.

---
*Generated on 2025-11-18T21:55:04.930479Z*
