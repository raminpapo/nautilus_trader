# Documentation: `nautilus_trader/adapters/sandbox/config.py`
**Generated:** 2025-11-15T19:40:04.493947Z
**File Size:** 3314 bytes
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

- **Path:** `nautilus_trader/adapters/sandbox/config.py`
- **Size:** 3,314 bytes
- **Lines:** 75
- **Extension:** `.py`
- **Type:** text
- **Imports:** 2
- **Classes:** 1

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

from decimal import Decimal

from nautilus_trader.config import LiveExecClientConfig


class SandboxExecutionClientConfig(LiveExecClientConfig, frozen=True, kw_only=True):
    """
    Configuration for ``SandboxExecClient`` instances.

    Parameters
    ----------
    venue : str
        The venue to generate a sandbox execution client for.
    starting_balances : list[str]
        The starting balances for this sandbox venue.
    base_currency : str, optional
        The base currency for this venue.
    oms_type : str, default 'NETTING'
        The order management system type used by the exchange.
    account_type : str, default 'MARGIN'
        The account type for the client.
    default_leverage : decimal.Decimal, default Decimal(1)
        The account default leverage (for margin accounts).
    bar_execution : bool, default True
        If bars should be processed by the matching engine(s) (and move the market).
    trade_execution : bool, default False
        If trades should be processed by the matching engine(s) (and move the market).
    reject_stop_orders : bool, default True
        If stop orders are rejected on submission if trigger price is in the market.
    support_gtd_orders : bool, default True
        If orders with GTD time in force will be supported by the venue.
    support_contingent_orders : bool, default True
        If contingent orders will be supported/respected by the venue.
        If False, then it's expected the strategy will be managing any contingent orders.
    use_position_ids : bool, default True
        If venue position IDs will be generated on order fills.
    use_random_ids : bool, default False
        If all venue generated identifiers will be random UUID4's.
    use_reduce_only : bool, default True
        If the `reduce_only` execution instruction on orders will be honored.

    """

    venue: str
    starting_balances: list[str]
    base_currency: str | None = None
    oms_type: str = "NETTING"
    account_type: str = "MARGIN"
    default_leverage: Decimal = Decimal(1)
    leverages: dict[str, float] | None = None
    book_type: str = "L1_MBP"
    frozen_account: bool = False
    bar_execution: bool = True
    trade_execution: bool = False
    reject_stop_orders: bool = True
    support_gtd_orders: bool = True
    support_contingent_orders: bool = True
    use_position_ids: bool = True
    use_random_ids: bool = False
    use_reduce_only: bool = True
```


---

## Overview

This file is located at `nautilus_trader/adapters/sandbox/config.py` within the repository.

**Classes defined:** SandboxExecutionClientConfig

**Import statements:** 2


---

## Detailed Analysis

### Classes

#### `SandboxExecutionClientConfig`

**Inherits from:** LiveExecClientConfig, frozen=True, kw_only=True


### Imports

- `from decimal import Decimal`
- `from nautilus_trader.config import LiveExecClientConfig`


---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters.sandbox.config import SandboxExecutionClientConfig
```


---

## Related Files

This file imports from the following modules:

- `from decimal import Decimal`
- `from nautilus_trader.config import LiveExecClientConfig`

**Directory:** `nautilus_trader/adapters/sandbox`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


