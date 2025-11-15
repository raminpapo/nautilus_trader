# Documentation: `nautilus_trader/adapters/dydx/common/credentials.py`
**Generated:** 2025-11-15T19:40:04.241136Z
**File Size:** 1436 bytes
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

- **Path:** `nautilus_trader/adapters/dydx/common/credentials.py`
- **Size:** 1,436 bytes
- **Lines:** 39
- **Extension:** `.py`
- **Type:** text
- **Imports:** 1
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


---

## Overview

This file is located at `nautilus_trader/adapters/dydx/common/credentials.py` within the repository.

**Functions defined:** get_wallet_address, get_mnemonic

**Import statements:** 1


---

## Detailed Analysis

### Functions

#### `get_wallet_address(is_testnet: bool)`


#### `get_mnemonic(is_testnet: bool)`


### Imports

- `from nautilus_trader.adapters.env import get_env_key`


---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters.dydx.common.credentials import get_wallet_address
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.adapters.env import get_env_key`

**Directory:** `nautilus_trader/adapters/dydx/common`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: secret, auth. Ensure proper handling of secrets.


