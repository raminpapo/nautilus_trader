# Documentation: `nautilus_trader/backtest/execution_client.pyx`
**Generated:** 2025-11-15T19:40:04.577417Z
**File Size:** 5630 bytes
**Extension:** .pyx
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

- **Path:** `nautilus_trader/backtest/execution_client.pyx`
- **Size:** 5,630 bytes
- **Lines:** 148
- **Extension:** `.pyx`
- **Type:** text
- **Imports:** 2
- **Functions:** 1

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

from nautilus_trader.accounting.factory import AccountFactory
from nautilus_trader.common.config import NautilusConfig

from nautilus_trader.backtest.engine cimport SimulatedExchange
from nautilus_trader.cache.cache cimport Cache
from nautilus_trader.common.component cimport MessageBus
from nautilus_trader.common.component cimport TestClock
from nautilus_trader.core.correctness cimport Condition
from nautilus_trader.core.rust.model cimport AccountType
from nautilus_trader.execution.client cimport ExecutionClient
from nautilus_trader.execution.messages cimport BatchCancelOrders
from nautilus_trader.execution.messages cimport CancelAllOrders
from nautilus_trader.execution.messages cimport CancelOrder
from nautilus_trader.execution.messages cimport ModifyOrder
from nautilus_trader.execution.messages cimport SubmitOrder
from nautilus_trader.execution.messages cimport SubmitOrderList
from nautilus_trader.model.identifiers cimport AccountId
from nautilus_trader.model.identifiers cimport ClientId
from nautilus_trader.model.identifiers cimport Venue
from nautilus_trader.model.orders.base cimport Order


cdef class BacktestExecClient(ExecutionClient):
    """
    Provides an execution client for the `BacktestEngine`.

    Parameters
    ----------
    exchange : SimulatedExchange
        The simulated exchange for the backtest.
    msgbus : MessageBus
        The message bus for the client.
    cache : Cache
        The cache for the client.
    clock : TestClock
        The clock for the client.
    routing : bool
        If multi-venue routing is enabled for the client.
    frozen_account : bool
        If the backtest run account is frozen.
    allow_cash_borrowing : bool
        If cash accounts should allow borrowing (negative balances).
    """

    def __init__(
        self,
        SimulatedExchange exchange not None,
        MessageBus msgbus not None,
        Cache cache not None,
        TestClock clock not None,
        bint routing=False,
        bint frozen_account=False,
        bint allow_cash_borrowing=False,
    ) -> None:
        super().__init__(
            client_id=ClientId(exchange.id.value),
            venue=Venue(exchange.id.value),
            oms_type=exchange.oms_type,
            account_type=exchange.account_type,
            base_currency=exchange.base_currency,
            msgbus=msgbus,
            cache=cache,
            clock=clock,
        )

        self._set_account_id(AccountId(f"{exchange.id.value}-001"))

        if not frozen_account:
            AccountFactory.register_calculated_account(exchange.id.value)

        if exchange.account_type == AccountType.CASH and allow_cash_borrowing:
            AccountFactory.register_cash_borrowing(exchange.id.value)

        self._exchange = exchange
        self.is_connected = False

    cpdef void _start(self):
        self._log.info(f"Connecting...")
        self.is_connected = True
        self._log.info(f"Connected")

    cpdef void _stop(self):
        self._log.info(f"Disconnecting...")
        self.is_connected = False
        self._log.info(f"Disconnected")

# -- COMMAND HANDLERS -----------------------------------------------------------------------------

    cpdef void submit_order(self, SubmitOrder command):
        Condition.is_true(self.is_connected, "not connected")

        self.generate_order_submitted(
            strategy_id=command.strategy_id,
            instrument_id=command.instrument_id,
            client_order_id=command.order.client_order_id,
            ts_event=self._clock.timestamp_ns(),
        )

        self._exchange.send(command)

    cpdef void submit_order_list(self, SubmitOrderList command):
        Condition.is_true(self.is_connected, "not connected")

        cdef Order order
        for order in command.order_list.orders:
            self.generate_order_submitted(
                strategy_id=order.strategy_id,
                instrument_id=order.instrument_id,
                client_order_id=order.client_order_id,
                ts_event=self._clock.timestamp_ns(),
            )

        self._exchange.send(command)

    cpdef void modify_order(self, ModifyOrder command):
        Condition.is_true(self.is_connected, "not connected")

        self._exchange.send(command)

    cpdef void cancel_order(self, CancelOrder command):
        Condition.is_true(self.is_connected, "not connected")

        self._exchange.send(command)

    cpdef void cancel_all_orders(self, CancelAllOrders command):
        Condition.is_true(self.is_connected, "not connected")

        self._exchange.send(command)

    cpdef void batch_cancel_orders(self, BatchCancelOrders command):
        Condition.is_true(self.is_connected, "not connected")

        self._exchange.send(command)
```


---

## Overview

This file is located at `nautilus_trader/backtest/execution_client.pyx` within the repository.

**Functions defined:** __init__

**Import statements:** 2


---

## Detailed Analysis

### Functions

#### `__init__(
        self,
        SimulatedExchange exchange not None,
        MessageBus msgbus not None,
        Cache cache not None,
        TestClock clock not None,
        bint routing=False,
        bint frozen_account=False,
        bint allow_cash_borrowing=False,
    )`


### Imports

- `from nautilus_trader.accounting.factory import AccountFactory`
- `from nautilus_trader.common.config import NautilusConfig`


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.accounting.factory import AccountFactory`
- `from nautilus_trader.common.config import NautilusConfig`

**Directory:** `nautilus_trader/backtest`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


