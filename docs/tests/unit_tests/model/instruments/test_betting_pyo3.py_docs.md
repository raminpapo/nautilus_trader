# Documentation: `tests/unit_tests/model/instruments/test_betting_pyo3.py`
**Generated:** 2025-11-15T19:40:09.269551Z
**File Size:** 3302 bytes
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

- **Path:** `tests/unit_tests/model/instruments/test_betting_pyo3.py`
- **Size:** 3,302 bytes
- **Lines:** 85
- **Extension:** `.py`
- **Type:** text
- **Imports:** 2
- **Functions:** 3

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
from nautilus_trader.test_kit.rust.instruments_pyo3 import TestInstrumentProviderPyo3


_BETTING_INSTRUMENT = TestInstrumentProviderPyo3.betting_instrument()


def test_equality():
    item_1 = TestInstrumentProviderPyo3.betting_instrument()
    item_2 = TestInstrumentProviderPyo3.betting_instrument()
    assert item_1 == item_2


def test_hash():
    assert hash(_BETTING_INSTRUMENT) == hash(_BETTING_INSTRUMENT)


def test_to_dict():
    result = _BETTING_INSTRUMENT.to_dict()
    assert nautilus_pyo3.BettingInstrument.from_dict(result) == _BETTING_INSTRUMENT
    assert result == {
        "type": "BettingInstrument",
        "id": "1-123456789.BETFAIR",
        "raw_symbol": "1-123456789",
        "event_type_id": 6423,
        "event_type_name": "American Football",
        "competition_id": 12282733,
        "competition_name": "NFL",
        "event_id": 29678534,
        "event_name": "NFL",
        "event_country_code": "GB",
        "event_open_date": 1644276600000000000,
        "betting_type": "ODDS",
        "market_id": "1-123456789",
        "market_name": "AFC Conference Winner",
        "market_start_time": 1644276600000000000,
        "market_type": "SPECIAL",
        "selection_id": 50214,
        "selection_name": "Kansas City Chiefs",
        "selection_handicap": 0.0,
        "currency": "GBP",
        "price_precision": 2,
        "size_precision": 2,
        "price_increment": "0.01",
        "size_increment": "0.01",
        "max_quantity": None,
        "min_quantity": None,
        "max_notional": None,
        "min_notional": "1.00 GBP",
        "max_price": None,
        "min_price": None,
        "margin_init": "1",
        "margin_maint": "1",
        "maker_fee": "0",
        "taker_fee": "0",
        "ts_event": 0,
        "ts_init": 0,
        "info": {},
    }


# TODO: Not implemented
# def test_pyo3_cython_conversion():
#     binary_option_pyo3 = TestInstrumentProviderPyo3.binary_option()
#     binary_option_pyo3_dict = binary_option_pyo3.to_dict()
#     binary_option_cython = BinaryOption.from_pyo3(binary_option_pyo3)
#     binary_option_cython_dict = BinaryOption.to_dict(binary_option_cython)
#     binary_option_pyo3_back = nautilus_pyo3.BinaryOption.from_dict(binary_option_cython_dict)
#     assert binary_option_pyo3 == binary_option_pyo3_back
#     assert binary_option_pyo3_dict == binary_option_cython_dict
```


---

## Overview

This file is located at `tests/unit_tests/model/instruments/test_betting_pyo3.py` within the repository.

**Functions defined:** test_equality, test_hash, test_to_dict

**Import statements:** 2


---

## Detailed Analysis

### Functions

#### `test_equality()`


#### `test_hash()`


#### `test_to_dict()`


### Imports

- `from nautilus_trader.core import nautilus_pyo3`
- `from nautilus_trader.test_kit.rust.instruments_pyo3 import TestInstrumentProviderPyo3`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.model.instruments.test_betting_pyo3 import test_equality
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.core import nautilus_pyo3`
- `from nautilus_trader.test_kit.rust.instruments_pyo3 import TestInstrumentProviderPyo3`

**Directory:** `tests/unit_tests/model/instruments`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


