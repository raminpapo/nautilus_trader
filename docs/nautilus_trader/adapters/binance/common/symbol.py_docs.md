# Documentation: `nautilus_trader/adapters/binance/common/symbol.py`
**Generated:** 2025-11-15T19:40:04.066725Z
**File Size:** 2570 bytes
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

- **Path:** `nautilus_trader/adapters/binance/common/symbol.py`
- **Size:** 2,570 bytes
- **Lines:** 69
- **Extension:** `.py`
- **Type:** text
- **Imports:** 4
- **Classes:** 2
- **Functions:** 4

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


---

## Overview

This file is located at `nautilus_trader/adapters/binance/common/symbol.py` within the repository.

**Classes defined:** BinanceSymbol, BinanceSymbols

**Functions defined:** __new__, parse_as_nautilus, __new__, parse_str_to_list

**Import statements:** 4


---

## Detailed Analysis

### Classes

#### `BinanceSymbol`

**Inherits from:** str


#### `BinanceSymbols`

**Inherits from:** str


### Functions

#### `__new__(cls, symbol: str)`


#### `parse_as_nautilus(self, account_type: BinanceAccountType)`


#### `__new__(cls, symbols: list[str])`


#### `parse_str_to_list(self)`


### Imports

- `from __future__ import annotations`
- `import json`
- `from nautilus_trader.adapters.binance.common.enums import BinanceAccountType`
- `from nautilus_trader.core.correctness import PyCondition`


---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters.binance.common.symbol import BinanceSymbol
```


---

## Related Files

This file imports from the following modules:

- `from __future__ import annotations`
- `import json`
- `from nautilus_trader.adapters.binance.common.enums import BinanceAccountType`
- `from nautilus_trader.core.correctness import PyCondition`

**Directory:** `nautilus_trader/adapters/binance/common`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


