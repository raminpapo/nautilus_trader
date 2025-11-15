# Documentation: `nautilus_trader/accounting/manager.pxd`
**Generated:** 2025-11-15T19:40:04.001354Z
**File Size:** 2616 bytes
**Extension:** .pxd
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

- **Path:** `nautilus_trader/accounting/manager.pxd`
- **Size:** 2,616 bytes
- **Lines:** 44
- **Extension:** `.pxd`
- **Type:** text

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

from libc.stdint cimport uint64_t

from nautilus_trader.accounting.accounts.base cimport Account
from nautilus_trader.accounting.accounts.cash cimport CashAccount
from nautilus_trader.accounting.accounts.margin cimport MarginAccount
from nautilus_trader.cache.base cimport CacheFacade
from nautilus_trader.common.component cimport Clock
from nautilus_trader.common.component cimport Logger
from nautilus_trader.core.rust.model cimport OrderSide
from nautilus_trader.model.events.account cimport AccountState
from nautilus_trader.model.events.order cimport OrderFilled
from nautilus_trader.model.instruments.base cimport Instrument
from nautilus_trader.model.objects cimport Money


cdef class AccountsManager:
    cdef Clock _clock
    cdef Logger _log
    cdef CacheFacade _cache

    cpdef AccountState generate_account_state(self, Account account, uint64_t ts_event)
    cpdef void update_balances(self, Account account, Instrument instrument, OrderFilled fill)
    cpdef bint update_orders(self, Account account, Instrument instrument, list orders_open, uint64_t ts_event)
    cpdef bint update_positions(self, MarginAccount account, Instrument instrument, list positions_open, uint64_t ts_event)
    cdef bint _update_balance_locked(self, CashAccount account, Instrument instrument, list orders_open, uint64_t ts_event)
    cdef bint _update_margin_init(self, MarginAccount account, Instrument instrument, list orders_open, uint64_t ts_event)
    cdef bint _update_balance_single_currency(self, Account account, OrderFilled fill, Money pnl)
    cdef bint _update_balance_multi_currency(self, Account account, OrderFilled fill, list pnls)
    cdef object _calculate_xrate_to_base(self, Account account, Instrument instrument, OrderSide side)
```


---

## Overview

This file is located at `nautilus_trader/accounting/manager.pxd` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `nautilus_trader/accounting`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


