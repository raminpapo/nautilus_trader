# Documentation: test_core_functions.py

## File Metadata

- **Path**: `tests/integration_tests/adapters/binance/test_core_functions.py`
- **Size**: 3,649 bytes
- **Lines**: 99
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

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`TestBinanceCoreFunctions`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 4


**Classs**: `TestBinanceCoreFunctions`
**Imports**: `nautilus_trader.adapters.binance.common.enums`, `nautilus_trader.adapters.binance.common.symbol`, `pytest`

## Related Files

This file is located in `tests/integration_tests/adapters/binance/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/binance/test_core_functions.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.746041Z*
