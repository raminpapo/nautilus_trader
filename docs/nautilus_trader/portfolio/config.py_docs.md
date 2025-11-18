# Documentation: config.py

## File Metadata

- **Path**: `nautilus_trader/portfolio/config.py`
- **Size**: 2,758 bytes
- **Lines**: 58
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

from __future__ import annotations

from nautilus_trader.common.config import NautilusConfig
from nautilus_trader.common.config import PositiveInt


class PortfolioConfig(NautilusConfig, frozen=True):
    """
    Configuration for ``Portfolio`` instances.

    Parameters
    ----------
    use_mark_prices : bool, default False
        The type of prices used for P&L and net exposure calculations.
        If False (default), uses quote prices if available; otherwise, last trade prices
        (or falls back to bar prices if `bar_updates` is True).
        If True, uses mark prices.
    use_mark_xrates : bool, default False
        The type of exchange rates used for P&L and net exposure calculations.
        If False (default), uses quote prices.
        If True, uses mark prices.
    bar_updates : bool, default True
        If external bar prices should be considered for calculations.
    convert_to_account_base_currency : bool, default True
        If calculations should be converted into each account's base currency.
        This setting is only effective for accounts with a specified base currency.
    min_account_state_logging_interval_ms : PositiveInt, optional
        The minimum interval (milliseconds) between logging account state events for the same account.
        When set, account state updates will only be logged if this much time has passed since the last log.
        Useful for HFT deployments to prevent excessive logging when account states change rapidly.
        Default is None (no throttling).
    debug : bool, default False
        If debug mode is active (will provide extra debug logging).

    """

    use_mark_prices: bool = False
    use_mark_xrates: bool = False
    bar_updates: bool = True
    convert_to_account_base_currency: bool = True
    min_account_state_logging_interval_ms: PositiveInt | None = None
    debug: bool = False

```

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`PortfolioConfig`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Classs**: `PortfolioConfig`
**Imports**: `__future__`, `nautilus_trader.common.config`

## Related Files

This file is located in `nautilus_trader/portfolio/`. Related files may include:
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
*Generated on 2025-11-18T21:55:05.884913Z*
