# Documentation: test_option_spread_pyo3.py

## File Metadata

- **Path**: `tests/unit_tests/model/instruments/test_option_spread_pyo3.py`
- **Size**: 3,101 bytes
- **Lines**: 83
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

from nautilus_trader.core import nautilus_pyo3
from nautilus_trader.model.instruments import OptionSpread
from nautilus_trader.test_kit.rust.instruments_pyo3 import TestInstrumentProviderPyo3


_OPTION_SPREAD = TestInstrumentProviderPyo3.option_spread()


def test_equality():
    item_1 = TestInstrumentProviderPyo3.option_spread()
    item_2 = TestInstrumentProviderPyo3.option_spread()
    assert item_1 == item_2


def test_hash():
    assert hash(_OPTION_SPREAD) == hash(_OPTION_SPREAD)


def test_to_dict():
    result = _OPTION_SPREAD.to_dict()
    assert nautilus_pyo3.OptionSpread.from_dict(result) == _OPTION_SPREAD
    assert result == {
        "type": "OptionSpread",
        "id": "UD:U$: GN 2534559.GLBX",
        "raw_symbol": "UD:U$: GN 2534559",
        "asset_class": "FX",
        "exchange": "XCME",
        "underlying": "SR3",
        "strategy_type": "GN",
        "activation_ns": 1699304047000000000,
        "expiration_ns": 1708729140000000000,
        "currency": "USDT",
        "price_precision": 2,
        "price_increment": "0.01",
        "size_increment": "1",
        "size_precision": 0,
        "multiplier": "1",
        "lot_size": "1",
        "max_quantity": None,
        "min_quantity": "1",
        "max_price": None,
        "min_price": None,
        "margin_init": "0",
        "margin_maint": "0",
        "maker_fee": "0",
        "taker_fee": "0",
        "info": {},
        "ts_event": 0,
        "ts_init": 0,
    }


def test_legacy_option_contract_from_pyo3():
    option = OptionSpread.from_pyo3(_OPTION_SPREAD)

    assert option.id.value == "UD:U$: GN 2534559.GLBX"


def test_pyo3_cython_conversion():
    option_spread_pyo3 = TestInstrumentProviderPyo3.option_spread()
    option_spread_pyo3_dict = option_spread_pyo3.to_dict()
    option_spread_cython = OptionSpread.from_pyo3(option_spread_pyo3)
    option_spread_cython_dict = OptionSpread.to_dict(option_spread_cython)
    del option_spread_cython_dict["tick_scheme_name"]  # TODO: Under development
    option_spread_pyo3_back = nautilus_pyo3.OptionSpread.from_dict(option_spread_cython_dict)
    assert option_spread_cython_dict == option_spread_pyo3_dict
    assert option_spread_pyo3 == option_spread_pyo3_back

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 5 function(s).

## Detailed Walkthrough

### Functions
- **`test_equality()`**: Function defined in this file
- **`test_hash()`**: Function defined in this file
- **`test_to_dict()`**: Function defined in this file
- **`test_legacy_option_contract_from_pyo3()`**: Function defined in this file
- **`test_pyo3_cython_conversion()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 8


**Functions**: `test_equality`, `test_hash`, `test_legacy_option_contract_from_pyo3`, `test_pyo3_cython_conversion`, `test_to_dict`
**Imports**: `nautilus_trader.core`, `nautilus_trader.model.instruments`, `nautilus_trader.test_kit.rust.instruments_pyo3`

## Related Files

This file is located in `tests/unit_tests/model/instruments/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/unit_tests/model/instruments/test_option_spread_pyo3.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:11.538422Z*
