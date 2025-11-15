# Documentation: `tests/unit_tests/model/instruments/test_futures_spread_pyo3.py`
**Generated:** 2025-11-15T19:40:09.280207Z
**File Size:** 3140 bytes
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

- **Path:** `tests/unit_tests/model/instruments/test_futures_spread_pyo3.py`
- **Size:** 3,140 bytes
- **Lines:** 82
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3
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

from nautilus_trader.core import nautilus_pyo3
from nautilus_trader.model.instruments import FuturesSpread
from nautilus_trader.test_kit.rust.instruments_pyo3 import TestInstrumentProviderPyo3


_ES_FUTURES_SPREAD = TestInstrumentProviderPyo3.futures_spread_es()


def test_equality():
    item_1 = TestInstrumentProviderPyo3.futures_spread_es()
    item_2 = TestInstrumentProviderPyo3.futures_spread_es()
    assert item_1 == item_2


def test_hash():
    assert hash(_ES_FUTURES_SPREAD) == hash(_ES_FUTURES_SPREAD)


def test_to_dict():
    result = _ES_FUTURES_SPREAD.to_dict()
    assert nautilus_pyo3.FuturesSpread.from_dict(result) == _ES_FUTURES_SPREAD
    assert result == {
        "type": "FuturesSpread",
        "id": "ESM4-ESU4.GLBX",
        "raw_symbol": "ESM4-ESU4",
        "asset_class": "INDEX",
        "underlying": "ES",
        "strategy_type": "EQ",
        "activation_ns": 1655818200000000000,
        "expiration_ns": 1718976600000000000,
        "currency": "USD",
        "price_precision": 2,
        "price_increment": "0.01",
        "size_increment": "1",
        "size_precision": 0,
        "multiplier": "1",
        "lot_size": "1",
        "max_price": None,
        "max_quantity": None,
        "min_price": None,
        "min_quantity": "1",
        "margin_init": "0",
        "margin_maint": "0",
        "maker_fee": "0",
        "taker_fee": "0",
        "info": {},
        "ts_event": 0,
        "ts_init": 0,
        "exchange": "XCME",
    }


def test_legacy_futures_contract_from_pyo3():
    future = FuturesSpread.from_pyo3(_ES_FUTURES_SPREAD)

    assert future.id.value == "ESM4-ESU4.GLBX"


def test_pyo3_cython_conversion():
    futures_spread_pyo3 = TestInstrumentProviderPyo3.futures_spread_es()
    futures_spread_pyo3_dict = futures_spread_pyo3.to_dict()
    futures_spread_cython = FuturesSpread.from_pyo3(futures_spread_pyo3)
    futures_spread_cython_dict = FuturesSpread.to_dict(futures_spread_cython)
    del futures_spread_cython_dict["tick_scheme_name"]  # TODO: Under development
    futures_spread_pyo3_back = nautilus_pyo3.FuturesSpread.from_dict(futures_spread_cython_dict)
    assert futures_spread_pyo3_dict == futures_spread_cython_dict
    assert futures_spread_pyo3 == futures_spread_pyo3_back
```


---

## Overview

This file is located at `tests/unit_tests/model/instruments/test_futures_spread_pyo3.py` within the repository.

**Functions defined:** test_equality, test_hash, test_to_dict, test_legacy_futures_contract_from_pyo3, test_pyo3_cython_conversion

**Import statements:** 3


---

## Detailed Analysis

### Functions

#### `test_equality()`


#### `test_hash()`


#### `test_to_dict()`


#### `test_legacy_futures_contract_from_pyo3()`


#### `test_pyo3_cython_conversion()`


### Imports

- `from nautilus_trader.core import nautilus_pyo3`
- `from nautilus_trader.model.instruments import FuturesSpread`
- `from nautilus_trader.test_kit.rust.instruments_pyo3 import TestInstrumentProviderPyo3`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.model.instruments.test_futures_spread_pyo3 import test_equality
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.core import nautilus_pyo3`
- `from nautilus_trader.model.instruments import FuturesSpread`
- `from nautilus_trader.test_kit.rust.instruments_pyo3 import TestInstrumentProviderPyo3`

**Directory:** `tests/unit_tests/model/instruments`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


