# Documentation: config.py

## File Metadata

- **Path**: `nautilus_trader/adapters/sandbox/config.py`
- **Size**: 3,314 bytes
- **Lines**: 76
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

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`SandboxExecutionClientConfig`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Classs**: `SandboxExecutionClientConfig`
**Imports**: `decimal`, `nautilus_trader.config`

## Related Files

This file is located in `nautilus_trader/adapters/sandbox/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

Tests for this file may be located in:
- `tests/` directory in the same folder
- Corresponding test module in the project

Run the full test suite to verify functionality.

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:04.990411Z*
