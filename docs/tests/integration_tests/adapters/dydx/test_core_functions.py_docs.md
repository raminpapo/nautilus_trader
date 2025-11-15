# Documentation: `tests/integration_tests/adapters/dydx/test_core_functions.py`
**Generated:** 2025-11-15T19:40:07.753171Z
**File Size:** 3324 bytes
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

- **Path:** `tests/integration_tests/adapters/dydx/test_core_functions.py`
- **Size:** 3,324 bytes
- **Lines:** 108
- **Extension:** `.py`
- **Type:** text
- **Imports:** 8
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


---

## Overview

This file is located at `tests/integration_tests/adapters/dydx/test_core_functions.py` within the repository.

**Functions defined:** test_format_symbol, test_wallet_address, test_wallet_address_not_set, test_credentials, test_credentials_not_set

**Import statements:** 8


---

## Detailed Analysis

### Functions

#### `test_format_symbol()`


#### `test_wallet_address(environment_variable: str, is_testnet: bool)`


#### `test_wallet_address_not_set(is_testnet: bool)`


#### `test_credentials(environment_variable: str, is_testnet: bool)`


#### `test_credentials_not_set(is_testnet: bool)`


### Imports

- `import os`
- `import pytest`
- `from nautilus_trader.adapters.dydx.common.constants import DYDX_VENUE`
- `from nautilus_trader.adapters.dydx.common.credentials import get_mnemonic`
- `from nautilus_trader.adapters.dydx.common.credentials import get_wallet_address`
- `from nautilus_trader.adapters.dydx.common.symbol import DYDXSymbol`
- `from nautilus_trader.model.identifiers import InstrumentId`
- `from nautilus_trader.model.identifiers import Symbol`


---

## Usage Examples

### Importing

```python
from tests.integration_tests.adapters.dydx.test_core_functions import test_format_symbol
```


---

## Related Files

This file imports from the following modules:

- `import os`
- `import pytest`
- `from nautilus_trader.adapters.dydx.common.constants import DYDX_VENUE`
- `from nautilus_trader.adapters.dydx.common.credentials import get_mnemonic`
- `from nautilus_trader.adapters.dydx.common.credentials import get_wallet_address`
- `from nautilus_trader.adapters.dydx.common.symbol import DYDXSymbol`
- `from nautilus_trader.model.identifiers import InstrumentId`
- `from nautilus_trader.model.identifiers import Symbol`

**Directory:** `tests/integration_tests/adapters/dydx`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: credential. Ensure proper handling of secrets.

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


