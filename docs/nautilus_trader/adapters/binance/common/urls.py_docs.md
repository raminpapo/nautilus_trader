# Documentation: urls.py

## File Metadata

- **Path**: `nautilus_trader/adapters/binance/common/urls.py`
- **Size**: 3,461 bytes
- **Lines**: 76
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 2 function(s).

## Detailed Walkthrough

### Functions
- **`get_http_base_url()`**: Function defined in this file
- **`get_ws_base_url()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Functions**: `get_http_base_url`, `get_ws_base_url`
**Imports**: `nautilus_trader.adapters.binance.common.enums`

## Related Files

This file is located in `nautilus_trader/adapters/binance/common/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.514715Z*
