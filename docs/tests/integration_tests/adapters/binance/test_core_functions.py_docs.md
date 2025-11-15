# Documentation: `tests/integration_tests/adapters/binance/test_core_functions.py`
**Generated:** 2025-11-15T19:40:07.683065Z
**File Size:** 3649 bytes
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

- **Path:** `tests/integration_tests/adapters/binance/test_core_functions.py`
- **Size:** 3,649 bytes
- **Lines:** 98
- **Extension:** `.py`
- **Type:** text
- **Imports:** 4
- **Classes:** 1
- **Functions:** 6

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

import pytest

from nautilus_trader.adapters.binance.common.enums import BinanceAccountType
from nautilus_trader.adapters.binance.common.symbol import BinanceSymbol
from nautilus_trader.adapters.binance.common.symbol import BinanceSymbols


class TestBinanceCoreFunctions:
    def test_format_symbol(self):
        # Arrange
        symbol = "ethusdt-perp"

        # Act
        result = BinanceSymbol(symbol)

        # Assert
        assert result == "ETHUSDT"

    def test_convert_symbols_list_to_json_array(self):
        # Arrange
        symbols = ["BTCUSDT", "ETHUSDT-PERP", " XRDUSDT"]

        # Act
        result = BinanceSymbols(symbols)

        # Assert
        assert result == '["BTCUSDT","ETHUSDT","XRDUSDT"]'

    @pytest.mark.parametrize(
        ("account_type", "expected"),
        [
            [BinanceAccountType.SPOT, True],
            [BinanceAccountType.MARGIN, False],
            [BinanceAccountType.ISOLATED_MARGIN, False],
            [BinanceAccountType.USDT_FUTURES, False],
            [BinanceAccountType.COIN_FUTURES, False],
        ],
    )
    def test_binance_account_type_is_spot(self, account_type, expected):
        # Arrange, Act, Assert
        assert account_type.is_spot == expected

    @pytest.mark.parametrize(
        ("account_type", "expected"),
        [
            [BinanceAccountType.SPOT, False],
            [BinanceAccountType.MARGIN, True],
            [BinanceAccountType.ISOLATED_MARGIN, True],
            [BinanceAccountType.USDT_FUTURES, False],
            [BinanceAccountType.COIN_FUTURES, False],
        ],
    )
    def test_binance_account_type_is_margin(self, account_type, expected):
        # Arrange, Act, Assert
        assert account_type.is_margin == expected

    @pytest.mark.parametrize(
        ("account_type", "expected"),
        [
            [BinanceAccountType.SPOT, True],
            [BinanceAccountType.MARGIN, True],
            [BinanceAccountType.ISOLATED_MARGIN, True],
            [BinanceAccountType.USDT_FUTURES, False],
            [BinanceAccountType.COIN_FUTURES, False],
        ],
    )
    def test_binance_account_type_is_spot_or_margin(self, account_type, expected):
        # Arrange, Act, Assert
        assert account_type.is_spot_or_margin == expected

    @pytest.mark.parametrize(
        ("account_type", "expected"),
        [
            [BinanceAccountType.SPOT, False],
            [BinanceAccountType.MARGIN, False],
            [BinanceAccountType.ISOLATED_MARGIN, False],
            [BinanceAccountType.USDT_FUTURES, True],
            [BinanceAccountType.COIN_FUTURES, True],
        ],
    )
    def test_binance_account_type_is_futures(self, account_type, expected):
        # Arrange, Act, Assert
        assert account_type.is_futures == expected
```


---

## Overview

This file is located at `tests/integration_tests/adapters/binance/test_core_functions.py` within the repository.

**Classes defined:** TestBinanceCoreFunctions

**Functions defined:** test_format_symbol, test_convert_symbols_list_to_json_array, test_binance_account_type_is_spot, test_binance_account_type_is_margin, test_binance_account_type_is_spot_or_margin, test_binance_account_type_is_futures

**Import statements:** 4


---

## Detailed Analysis

### Classes

#### `TestBinanceCoreFunctions`


### Functions

#### `test_format_symbol(self)`


#### `test_convert_symbols_list_to_json_array(self)`


#### `test_binance_account_type_is_spot(self, account_type, expected)`


#### `test_binance_account_type_is_margin(self, account_type, expected)`


#### `test_binance_account_type_is_spot_or_margin(self, account_type, expected)`


#### `test_binance_account_type_is_futures(self, account_type, expected)`


### Imports

- `import pytest`
- `from nautilus_trader.adapters.binance.common.enums import BinanceAccountType`
- `from nautilus_trader.adapters.binance.common.symbol import BinanceSymbol`
- `from nautilus_trader.adapters.binance.common.symbol import BinanceSymbols`


---

## Usage Examples

### Importing

```python
from tests.integration_tests.adapters.binance.test_core_functions import TestBinanceCoreFunctions
```


---

## Related Files

This file imports from the following modules:

- `import pytest`
- `from nautilus_trader.adapters.binance.common.enums import BinanceAccountType`
- `from nautilus_trader.adapters.binance.common.symbol import BinanceSymbol`
- `from nautilus_trader.adapters.binance.common.symbol import BinanceSymbols`

**Directory:** `tests/integration_tests/adapters/binance`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


