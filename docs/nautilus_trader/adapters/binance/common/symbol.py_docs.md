# Documentation: symbol.py

## File Metadata

- **Path**: `nautilus_trader/adapters/binance/common/symbol.py`
- **Size**: 2,570 bytes
- **Lines**: 70
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

import json

from nautilus_trader.adapters.binance.common.enums import BinanceAccountType
from nautilus_trader.core.correctness import PyCondition


################################################################################
# HTTP responses
################################################################################


class BinanceSymbol(str):
    """
    Binance compatible symbol.
    """

    def __new__(cls, symbol: str) -> BinanceSymbol:  # noqa: PYI034
        PyCondition.valid_string(symbol, "symbol")

        # Format the string on construction to be Binance compatible
        return super().__new__(
            cls,
            symbol.upper().replace(" ", "").replace("/", "").replace("-PERP", ""),
        )

    def parse_as_nautilus(self, account_type: BinanceAccountType) -> str:
        if account_type.is_spot_or_margin:
            return str(self)

        # Parse Futures symbol
        if self[-1].isdigit():
            return str(self)  # Deliverable
        if self.endswith("_PERP"):
            return str(self).replace("_", "-")
        else:
            return str(self) + "-PERP"


class BinanceSymbols(str):
    """
    Binance compatible list of symbols.
    """

    def __new__(cls, symbols: list[str]) -> BinanceSymbols:  # noqa: PYI034
        PyCondition.not_empty(symbols, "symbols")

        binance_symbols: list[BinanceSymbol] = [BinanceSymbol(symbol) for symbol in symbols]
        return super().__new__(cls, json.dumps(binance_symbols).replace(" ", ""))

    def parse_str_to_list(self) -> list[BinanceSymbol]:
        binance_symbols: list[BinanceSymbol] = json.loads(self)
        return binance_symbols

```

## High-Level Overview

This file is part of the NautilusTrader repository. 2 class(es).

## Detailed Walkthrough


### Classes
- **`BinanceSymbol`**: Class defined in this file
- **`BinanceSymbols`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 6


**Classs**: `BinanceSymbol`, `BinanceSymbols`
**Imports**: `__future__`, `json`, `nautilus_trader.adapters.binance.common.enums`, `nautilus_trader.core.correctness`

## Related Files

This file is located in `nautilus_trader/adapters/binance/common/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.510741Z*
