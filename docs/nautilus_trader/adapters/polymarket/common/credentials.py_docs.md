# Documentation: `nautilus_trader/adapters/polymarket/common/credentials.py`
**Generated:** 2025-11-15T19:40:04.440673Z
**File Size:** 1482 bytes
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

- **Path:** `nautilus_trader/adapters/polymarket/common/credentials.py`
- **Size:** 1,482 bytes
- **Lines:** 44
- **Extension:** `.py`
- **Type:** text
- **Imports:** 2
- **Classes:** 1
- **Functions:** 5

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


---

## Overview

This file is located at `nautilus_trader/adapters/polymarket/common/credentials.py` within the repository.

**Classes defined:** PolymarketWebSocketAuth

**Functions defined:** get_polymarket_api_key, get_polymarket_api_secret, get_polymarket_passphrase, get_polymarket_private_key, get_polymarket_funder

**Import statements:** 2


---

## Detailed Analysis

### Classes

#### `PolymarketWebSocketAuth`

**Inherits from:** msgspec.Struct, frozen=True


### Functions

#### `get_polymarket_api_key()`


#### `get_polymarket_api_secret()`


#### `get_polymarket_passphrase()`


#### `get_polymarket_private_key()`


#### `get_polymarket_funder()`


### Imports

- `import msgspec`
- `from nautilus_trader.adapters.env import get_env_key`


---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters.polymarket.common.credentials import PolymarketWebSocketAuth
```


---

## Related Files

This file imports from the following modules:

- `import msgspec`
- `from nautilus_trader.adapters.env import get_env_key`

**Directory:** `nautilus_trader/adapters/polymarket/common`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: secret, api_key, private_key, auth. Ensure proper handling of secrets.


