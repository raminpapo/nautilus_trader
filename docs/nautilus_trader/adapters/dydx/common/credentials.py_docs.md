# Documentation: credentials.py

## File Metadata

- **Path**: `nautilus_trader/adapters/dydx/common/credentials.py`
- **Size**: 1,436 bytes
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
Read the authentication secrets from environment variables.
"""

from nautilus_trader.adapters.env import get_env_key


def get_wallet_address(is_testnet: bool) -> str:
    """
    Return the wallet address for dYdX.
    """
    if is_testnet:
        return get_env_key("DYDX_TESTNET_WALLET_ADDRESS")

    return get_env_key("DYDX_WALLET_ADDRESS")


def get_mnemonic(is_testnet: bool) -> str:
    """
    Return the wallet mnemonic for dYdX.
    """
    if is_testnet:
        return get_env_key("DYDX_TESTNET_MNEMONIC")

    return get_env_key("DYDX_MNEMONIC")

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 2 function(s).

## Detailed Walkthrough

### Functions
- **`get_wallet_address()`**: Function defined in this file
- **`get_mnemonic()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Functions**: `get_mnemonic`, `get_wallet_address`
**Imports**: `nautilus_trader.adapters.env`

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
*Generated on 2025-11-18T21:55:04.708062Z*
