# Documentation: test_commission_model.py

## File Metadata

- **Path**: `tests/unit_tests/backtest/test_commission_model.py`
- **Size**: 4,541 bytes
- **Lines**: 146
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


@pytest.fixture
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
    ("order_side", "charge_commission_once", "expected_first_fill", "expected_next_fill"),
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 5 function(s).

## Detailed Walkthrough

### Functions
- **`instrument()`**: Function defined in this file
- **`test_fixed_commission_single_fill()`**: Function defined in this file
- **`test_fixed_commission_multiple_fills()`**: Function defined in this file
- **`test_instrument_percent_commission_maker()`**: Function defined in this file
- **`test_instrument_percent_commission_taker()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 14


**Functions**: `instrument`, `test_fixed_commission_multiple_fills`, `test_fixed_commission_single_fill`, `test_instrument_percent_commission_maker`, `test_instrument_percent_commission_taker`
**Imports**: `nautilus_trader.backtest.models`, `nautilus_trader.model.currencies`, `nautilus_trader.model.enums`, `nautilus_trader.model.instruments`, `nautilus_trader.model.objects`, `nautilus_trader.test_kit.providers`, `nautilus_trader.test_kit.stubs.events`, `nautilus_trader.test_kit.stubs.execution`, `pytest`

## Related Files

This file is located in `tests/unit_tests/backtest/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/unit_tests/backtest/test_commission_model.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:11.153930Z*
