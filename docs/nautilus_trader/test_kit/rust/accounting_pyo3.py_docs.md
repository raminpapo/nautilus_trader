# Documentation: accounting_pyo3.py

## File Metadata

- **Path**: `nautilus_trader/test_kit/rust/accounting_pyo3.py`
- **Size**: 3,697 bytes
- **Lines**: 88
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

from nautilus_trader.core.nautilus_pyo3 import CashAccount
from nautilus_trader.core.nautilus_pyo3 import MarginAccount
from nautilus_trader.core.nautilus_pyo3 import OrderSide
from nautilus_trader.core.nautilus_pyo3 import Position
from nautilus_trader.core.nautilus_pyo3 import Price
from nautilus_trader.core.nautilus_pyo3 import Quantity
from nautilus_trader.test_kit.rust.events_pyo3 import TestEventsProviderPyo3
from nautilus_trader.test_kit.rust.identifiers_pyo3 import TestIdProviderPyo3
from nautilus_trader.test_kit.rust.instruments_pyo3 import TestInstrumentProviderPyo3
from nautilus_trader.test_kit.rust.orders_pyo3 import TestOrderProviderPyo3


class TestAccountingProviderPyo3:
    @staticmethod
    def margin_account() -> MarginAccount:
        return MarginAccount(
            event=TestEventsProviderPyo3.margin_account_state(),
            calculate_account_state=False,
        )

    @staticmethod
    def cash_account() -> CashAccount:
        return CashAccount(
            event=TestEventsProviderPyo3.cash_account_state(),
            calculate_account_state=False,
        )

    @staticmethod
    def cash_account_million_usd() -> CashAccount:
        return CashAccount(
            event=TestEventsProviderPyo3.cash_account_state_million_usd(),
            calculate_account_state=False,
        )

    @staticmethod
    def cash_account_multi() -> CashAccount:
        return CashAccount(
            event=TestEventsProviderPyo3.cash_account_state_multi(),
            calculate_account_state=False,
        )

    @staticmethod
    def long_position() -> Position:
        order = TestOrderProviderPyo3.market_order(
            instrument_id=TestIdProviderPyo3.audusd_id(),
            order_side=OrderSide.BUY,
            quantity=Quantity.from_int(100_000),
        )
        instrument = TestInstrumentProviderPyo3.audusd_sim()
        order_filled = TestEventsProviderPyo3.order_filled(
            instrument=instrument,
            order=order,
            position_id=TestIdProviderPyo3.position_id(),
            last_px=Price.from_str("1.00001"),
        )
        return Position(instrument=instrument, fill=order_filled)

    @staticmethod
    def short_position() -> Position:
        order = TestOrderProviderPyo3.market_order(
            instrument_id=TestIdProviderPyo3.audusd_id(),
            order_side=OrderSide.SELL,
            quantity=Quantity.from_int(100_000),
        )
        instrument = TestInstrumentProviderPyo3.audusd_sim()
        order_filled = TestEventsProviderPyo3.order_filled(
            instrument=instrument,
            order=order,
            position_id=TestIdProviderPyo3.position_id(),
            last_px=Price.from_str("1.00001"),
        )
        return Position(instrument=TestInstrumentProviderPyo3.audusd_sim(), fill=order_filled)

```

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`TestAccountingProviderPyo3`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 6


**Classs**: `TestAccountingProviderPyo3`
**Imports**: `nautilus_trader.core.nautilus_pyo3`, `nautilus_trader.test_kit.rust.events_pyo3`, `nautilus_trader.test_kit.rust.identifiers_pyo3`, `nautilus_trader.test_kit.rust.instruments_pyo3`, `nautilus_trader.test_kit.rust.orders_pyo3`

## Related Files

This file is located in `nautilus_trader/test_kit/rust/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest nautilus_trader/test_kit/rust/accounting_pyo3.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:05.979809Z*
