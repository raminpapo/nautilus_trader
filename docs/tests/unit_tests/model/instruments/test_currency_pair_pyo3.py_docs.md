# Documentation: `tests/unit_tests/model/instruments/test_currency_pair_pyo3.py`
**Generated:** 2025-11-15T19:40:09.276545Z
**File Size:** 2837 bytes
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

- **Path:** `tests/unit_tests/model/instruments/test_currency_pair_pyo3.py`
- **Size:** 2,837 bytes
- **Lines:** 73
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3
- **Functions:** 4

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

from nautilus_trader.core import nautilus_pyo3
from nautilus_trader.model.instruments import CurrencyPair
from nautilus_trader.test_kit.rust.instruments_pyo3 import TestInstrumentProviderPyo3


_BTCUSDT = TestInstrumentProviderPyo3.btcusdt_binance()


def test_equality():
    item_1 = TestInstrumentProviderPyo3.btcusdt_binance()
    item_2 = TestInstrumentProviderPyo3.btcusdt_binance()
    assert item_1 == item_2


def test_hash():
    assert hash(_BTCUSDT) == hash(_BTCUSDT)


def test_to_dict():
    result = _BTCUSDT.to_dict()
    assert nautilus_pyo3.CurrencyPair.from_dict(result) == _BTCUSDT
    assert result == {
        "type": "CurrencyPair",
        "id": "BTCUSDT.BINANCE",
        "raw_symbol": "BTCUSDT",
        "base_currency": "BTC",
        "quote_currency": "USDT",
        "price_precision": 2,
        "size_precision": 6,
        "price_increment": "0.01",
        "size_increment": "0.000001",
        "multiplier": "1",
        "lot_size": None,
        "max_quantity": "9000",
        "min_quantity": "0.00001",
        "max_notional": None,
        "min_notional": None,
        "min_price": "0.01",
        "max_price": "1000000",
        "maker_fee": "0.001",
        "margin_init": "0.0500",
        "margin_maint": "0.0250",
        "taker_fee": "0.001",
        "info": {},
        "ts_event": 0,
        "ts_init": 0,
    }


def test_pyo3_cython_conversion():
    currency_pair_pyo3 = TestInstrumentProviderPyo3.btcusdt_binance()
    currency_pair_pyo3_dict = currency_pair_pyo3.to_dict()
    currency_pair_cython = CurrencyPair.from_pyo3(currency_pair_pyo3)
    currency_pair_cython_dict = CurrencyPair.to_dict(currency_pair_cython)
    del currency_pair_cython_dict["tick_scheme_name"]  # TODO: Under development
    currency_pair_pyo3_back = nautilus_pyo3.CurrencyPair.from_dict(currency_pair_cython_dict)
    assert currency_pair_cython_dict == currency_pair_pyo3_dict
    assert currency_pair_pyo3 == currency_pair_pyo3_back
```


---

## Overview

This file is located at `tests/unit_tests/model/instruments/test_currency_pair_pyo3.py` within the repository.

**Functions defined:** test_equality, test_hash, test_to_dict, test_pyo3_cython_conversion

**Import statements:** 3


---

## Detailed Analysis

### Functions

#### `test_equality()`


#### `test_hash()`


#### `test_to_dict()`


#### `test_pyo3_cython_conversion()`


### Imports

- `from nautilus_trader.core import nautilus_pyo3`
- `from nautilus_trader.model.instruments import CurrencyPair`
- `from nautilus_trader.test_kit.rust.instruments_pyo3 import TestInstrumentProviderPyo3`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.model.instruments.test_currency_pair_pyo3 import test_equality
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.core import nautilus_pyo3`
- `from nautilus_trader.model.instruments import CurrencyPair`
- `from nautilus_trader.test_kit.rust.instruments_pyo3 import TestInstrumentProviderPyo3`

**Directory:** `tests/unit_tests/model/instruments`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


