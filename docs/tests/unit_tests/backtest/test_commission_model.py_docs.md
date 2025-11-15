# Documentation: `tests/unit_tests/backtest/test_commission_model.py`
**Generated:** 2025-11-15T19:40:08.939570Z
**File Size:** 4535 bytes
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

- **Path:** `tests/unit_tests/backtest/test_commission_model.py`
- **Size:** 4,535 bytes
- **Lines:** 145
- **Extension:** `.py`
- **Type:** text
- **Imports:** 11
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

import pytest

from nautilus_trader.backtest.models import FixedFeeModel
from nautilus_trader.backtest.models import MakerTakerFeeModel
from nautilus_trader.model.currencies import USD
from nautilus_trader.model.enums import OrderSide
from nautilus_trader.model.instruments import Instrument
from nautilus_trader.model.objects import Money
from nautilus_trader.model.objects import Price
from nautilus_trader.test_kit.providers import TestInstrumentProvider
from nautilus_trader.test_kit.stubs.events import TestEventStubs
from nautilus_trader.test_kit.stubs.execution import TestExecStubs


@pytest.fixture()
def instrument() -> Instrument:
    return TestInstrumentProvider.default_fx_ccy("EUR/USD")


@pytest.mark.parametrize("order_side", [OrderSide.BUY, OrderSide.SELL])
def test_fixed_commission_single_fill(instrument, order_side):
    # Arrange
    expected = Money(1, USD)
    fee_model = FixedFeeModel(expected)
    order = TestExecStubs.make_accepted_order(
        instrument=instrument,
        order_side=order_side,
    )

    # Act
    commission = fee_model.get_commission(
        order,
        instrument.make_qty(10),
        Price.from_str("1.1234"),
        instrument,
    )

    # Assert
    assert commission == expected


@pytest.mark.parametrize(
    "order_side, charge_commission_once, expected_first_fill, expected_next_fill",
    [
        [OrderSide.BUY, True, Money(1, USD), Money(0, USD)],
        [OrderSide.SELL, True, Money(1, USD), Money(0, USD)],
        [OrderSide.BUY, False, Money(1, USD), Money(1, USD)],
        [OrderSide.SELL, False, Money(1, USD), Money(1, USD)],
    ],
)
def test_fixed_commission_multiple_fills(
    instrument,
    order_side,
    charge_commission_once,
    expected_first_fill,
    expected_next_fill,
):
    # Arrange
    fee_model = FixedFeeModel(
        commission=expected_first_fill,
        charge_commission_once=charge_commission_once,
    )
    order = TestExecStubs.make_accepted_order(
        instrument=instrument,
        order_side=order_side,
    )

    # Act
    commission_first_fill = fee_model.get_commission(
        order,
        instrument.make_qty(10),
        Price.from_str("1.1234"),
        instrument,
    )
    fill = TestEventStubs.order_filled(order=order, instrument=instrument)
    order.apply(fill)
    commission_next_fill = fee_model.get_commission(
        order,
        instrument.make_qty(10),
        Price.from_str("1.1234"),
        instrument,
    )

    # Assert
    assert commission_first_fill == expected_first_fill
    assert commission_next_fill == expected_next_fill


def test_instrument_percent_commission_maker(instrument):
    # Arrange
    fee_model = MakerTakerFeeModel()
    order = TestExecStubs.make_filled_order(
        instrument=instrument,
        order_side=OrderSide.SELL,
    )
    expected = order.quantity * order.price * instrument.maker_fee

    # Act
    commission = fee_model.get_commission(
        order,
        order.quantity,
        order.price,
        instrument,
    )

    # Assert
    assert isinstance(commission, Money)
    assert commission.as_decimal() == expected


def test_instrument_percent_commission_taker(instrument):
    # Arrange
    fee_model = MakerTakerFeeModel()
    order = TestExecStubs.make_filled_order(
        instrument=instrument,
        order_side=OrderSide.SELL,
    )
    expected = order.quantity * order.price * instrument.taker_fee

    # Act
    commission = fee_model.get_commission(
        order,
        order.quantity,
        order.price,
        instrument,
    )

    # Assert
    assert isinstance(commission, Money)
    assert commission.as_decimal() == expected
```


---

## Overview

This file is located at `tests/unit_tests/backtest/test_commission_model.py` within the repository.

**Functions defined:** instrument, test_fixed_commission_single_fill, test_fixed_commission_multiple_fills, test_instrument_percent_commission_maker, test_instrument_percent_commission_taker

**Import statements:** 11


---

## Detailed Analysis

### Functions

#### `instrument()`


#### `test_fixed_commission_single_fill(instrument, order_side)`


#### `test_fixed_commission_multiple_fills(
    instrument,
    order_side,
    charge_commission_once,
    expected_first_fill,
    expected_next_fill,
)`


#### `test_instrument_percent_commission_maker(instrument)`


#### `test_instrument_percent_commission_taker(instrument)`


### Imports

- `import pytest`
- `from nautilus_trader.backtest.models import FixedFeeModel`
- `from nautilus_trader.backtest.models import MakerTakerFeeModel`
- `from nautilus_trader.model.currencies import USD`
- `from nautilus_trader.model.enums import OrderSide`
- `from nautilus_trader.model.instruments import Instrument`
- `from nautilus_trader.model.objects import Money`
- `from nautilus_trader.model.objects import Price`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`
- `from nautilus_trader.test_kit.stubs.events import TestEventStubs`
- `from nautilus_trader.test_kit.stubs.execution import TestExecStubs`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.backtest.test_commission_model import instrument
```


---

## Related Files

This file imports from the following modules:

- `import pytest`
- `from nautilus_trader.backtest.models import FixedFeeModel`
- `from nautilus_trader.backtest.models import MakerTakerFeeModel`
- `from nautilus_trader.model.currencies import USD`
- `from nautilus_trader.model.enums import OrderSide`
- `from nautilus_trader.model.instruments import Instrument`
- `from nautilus_trader.model.objects import Money`
- `from nautilus_trader.model.objects import Price`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`
- `from nautilus_trader.test_kit.stubs.events import TestEventStubs`

*... and 1 more*

**Directory:** `tests/unit_tests/backtest`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


