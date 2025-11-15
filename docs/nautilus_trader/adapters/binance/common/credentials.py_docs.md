# Documentation: `nautilus_trader/adapters/binance/common/credentials.py`
**Generated:** 2025-11-15T19:40:04.054537Z
**File Size:** 1654 bytes
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

- **Path:** `nautilus_trader/adapters/binance/common/credentials.py`
- **Size:** 1,654 bytes
- **Lines:** 37
- **Extension:** `.py`
- **Type:** text
- **Imports:** 2
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

from nautilus_trader.adapters.binance.common.enums import BinanceAccountType
from nautilus_trader.adapters.env import get_env_key


def get_api_key(account_type: BinanceAccountType, is_testnet: bool) -> str:
    if is_testnet:
        if account_type.is_spot_or_margin:
            return get_env_key("BINANCE_TESTNET_API_KEY")
        else:
            return get_env_key("BINANCE_FUTURES_TESTNET_API_KEY")

    return get_env_key("BINANCE_API_KEY")


def get_api_secret(account_type: BinanceAccountType, is_testnet: bool) -> str:
    if is_testnet:
        if account_type.is_spot_or_margin:
            return get_env_key("BINANCE_TESTNET_API_SECRET")
        else:
            return get_env_key("BINANCE_FUTURES_TESTNET_API_SECRET")

    return get_env_key("BINANCE_API_SECRET")
```


---

## Overview

This file is located at `nautilus_trader/adapters/binance/common/credentials.py` within the repository.

**Functions defined:** get_api_key, get_api_secret

**Import statements:** 2


---

## Detailed Analysis

### Functions

#### `get_api_key(account_type: BinanceAccountType, is_testnet: bool)`


#### `get_api_secret(account_type: BinanceAccountType, is_testnet: bool)`


### Imports

- `from nautilus_trader.adapters.binance.common.enums import BinanceAccountType`
- `from nautilus_trader.adapters.env import get_env_key`


---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters.binance.common.credentials import get_api_key
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.adapters.binance.common.enums import BinanceAccountType`
- `from nautilus_trader.adapters.env import get_env_key`

**Directory:** `nautilus_trader/adapters/binance/common`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: secret, api_key. Ensure proper handling of secrets.


