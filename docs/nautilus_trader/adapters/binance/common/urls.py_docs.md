# Documentation: `nautilus_trader/adapters/binance/common/urls.py`
**Generated:** 2025-11-15T19:40:04.070802Z
**File Size:** 3461 bytes
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

- **Path:** `nautilus_trader/adapters/binance/common/urls.py`
- **Size:** 3,461 bytes
- **Lines:** 75
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

from nautilus_trader.adapters.binance.common.enums import BinanceAccountType


def get_http_base_url(account_type: BinanceAccountType, is_testnet: bool, is_us: bool) -> str:
    # Testnet base URLs
    if is_testnet:
        if account_type.is_spot_or_margin:
            return "https://testnet.binance.vision"
        elif (
            account_type == BinanceAccountType.USDT_FUTURES
            or account_type == BinanceAccountType.COIN_FUTURES
        ):
            return "https://testnet.binancefuture.com"
        else:
            raise RuntimeError(  # pragma: no cover (design-time error)
                f"invalid `BinanceAccountType`, was {account_type}",  # pragma: no cover
            )

    # Live base URLs
    top_level_domain: str = "us" if is_us else "com"
    if account_type.is_spot:
        return f"https://api.binance.{top_level_domain}"
    elif account_type.is_margin:
        return f"https://sapi.binance.{top_level_domain}"
    elif account_type == BinanceAccountType.USDT_FUTURES:
        return f"https://fapi.binance.{top_level_domain}"
    elif account_type == BinanceAccountType.COIN_FUTURES:
        return f"https://dapi.binance.{top_level_domain}"
    else:
        raise RuntimeError(  # pragma: no cover (design-time error)
            f"invalid `BinanceAccountType`, was {account_type}",  # pragma: no cover
        )


def get_ws_base_url(account_type: BinanceAccountType, is_testnet: bool, is_us: bool) -> str:
    # Testnet base URLs
    if is_testnet:
        if account_type.is_spot_or_margin:
            return "wss://stream.testnet.binance.vision"
        elif account_type == BinanceAccountType.USDT_FUTURES:
            return "wss://stream.binancefuture.com"
        elif account_type == BinanceAccountType.COIN_FUTURES:
            raise ValueError("no testnet for COIN-M futures")
        else:
            raise RuntimeError(  # pragma: no cover (design-time error)
                f"invalid `BinanceAccountType`, was {account_type}",  # pragma: no cover
            )

    # Live base URLs
    top_level_domain: str = "us" if is_us else "com"
    if account_type.is_spot_or_margin:
        return f"wss://stream.binance.{top_level_domain}:9443"
    elif account_type == BinanceAccountType.USDT_FUTURES:
        return f"wss://fstream.binance.{top_level_domain}"
    elif account_type == BinanceAccountType.COIN_FUTURES:
        return f"wss://dstream.binance.{top_level_domain}"
    else:
        raise RuntimeError(
            f"invalid `BinanceAccountType`, was {account_type}",
        )  # pragma: no cover (design-time error)
```


---

## Overview

This file is located at `nautilus_trader/adapters/binance/common/urls.py` within the repository.

**Functions defined:** get_http_base_url, get_ws_base_url

**Import statements:** 1


---

## Detailed Analysis

### Functions

#### `get_http_base_url(account_type: BinanceAccountType, is_testnet: bool, is_us: bool)`


#### `get_ws_base_url(account_type: BinanceAccountType, is_testnet: bool, is_us: bool)`


### Imports

- `from nautilus_trader.adapters.binance.common.enums import BinanceAccountType`


---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters.binance.common.urls import get_http_base_url
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.adapters.binance.common.enums import BinanceAccountType`

**Directory:** `nautilus_trader/adapters/binance/common`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


