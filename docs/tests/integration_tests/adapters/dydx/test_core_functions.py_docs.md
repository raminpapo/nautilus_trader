# Documentation: test_core_functions.py

## File Metadata

- **Path**: `tests/integration_tests/adapters/dydx/test_core_functions.py`
- **Size**: 3,324 bytes
- **Lines**: 109
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
Unit tests for core functions.
"""

import os

import pytest

from nautilus_trader.adapters.dydx.common.constants import DYDX_VENUE
from nautilus_trader.adapters.dydx.common.credentials import get_mnemonic
from nautilus_trader.adapters.dydx.common.credentials import get_wallet_address
from nautilus_trader.adapters.dydx.common.symbol import DYDXSymbol
from nautilus_trader.model.identifiers import InstrumentId
from nautilus_trader.model.identifiers import Symbol


def test_format_symbol() -> None:
    """
    Test the DYDXSymbol class.
    """
    # Arrange
    symbol = "eth-usdt-perp"

    # Act
    result = DYDXSymbol(symbol)

    # Assert
    assert result == "ETH-USDT"
    assert result.raw_symbol == "ETH-USDT"
    assert result.to_instrument_id() == InstrumentId(Symbol("ETH-USDT-PERP"), DYDX_VENUE)


@pytest.mark.parametrize(
    ("environment_variable", "is_testnet"),
    [
        ("DYDX_TESTNET_WALLET_ADDRESS", True),
        ("DYDX_WALLET_ADDRESS", False),
    ],
)
def test_wallet_address(environment_variable: str, is_testnet: bool) -> None:
    """
    Test retrieving the wallet address from environment variables.
    """
    os.environ[environment_variable] = "test_mnemonic"
    assert get_wallet_address(is_testnet=is_testnet) == "test_mnemonic"

    del os.environ[environment_variable]


@pytest.mark.parametrize(
    "is_testnet",
    [
        (True),
        (False),
    ],
)
def test_wallet_address_not_set(is_testnet: bool) -> None:
    """
    Test an exception is thrown when the environment variable is not set.
    """
    with pytest.raises(RuntimeError):
        get_wallet_address(is_testnet=is_testnet)


@pytest.mark.parametrize(
    ("environment_variable", "is_testnet"),
    [
        ("DYDX_TESTNET_MNEMONIC", True),
        ("DYDX_MNEMONIC", False),
    ],
)
def test_credentials(environment_variable: str, is_testnet: bool) -> None:
    """
    Test retrieving the credentials from environment variables.
    """
    os.environ[environment_variable] = "test_mnemonic"
    assert get_mnemonic(is_testnet=is_testnet) == "test_mnemonic"

    del os.environ[environment_variable]


@pytest.mark.parametrize(
    "is_testnet",
    [
        (True),
        (False),
    ],
)
def test_credentials_not_set(is_testnet: bool) -> None:
    """
    Test an exception is thrown when the environment variable is not set..
    """
    with pytest.raises(RuntimeError):
        get_mnemonic(is_testnet=is_testnet)

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 5 function(s).

## Detailed Walkthrough

### Functions
- **`test_format_symbol()`**: Function defined in this file
- **`test_wallet_address()`**: Function defined in this file
- **`test_wallet_address_not_set()`**: Function defined in this file
- **`test_credentials()`**: Function defined in this file
- **`test_credentials_not_set()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 11


**Functions**: `test_credentials`, `test_credentials_not_set`, `test_format_symbol`, `test_wallet_address`, `test_wallet_address_not_set`
**Imports**: `nautilus_trader.adapters.dydx.common.constants`, `nautilus_trader.adapters.dydx.common.credentials`, `nautilus_trader.adapters.dydx.common.symbol`, `nautilus_trader.model.identifiers`, `os`, `pytest`

## Related Files

This file is located in `tests/integration_tests/adapters/dydx/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/dydx/test_core_functions.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.835038Z*
