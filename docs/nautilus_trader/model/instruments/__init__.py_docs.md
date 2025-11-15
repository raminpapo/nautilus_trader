# Documentation: `nautilus_trader/model/instruments/__init__.py`
**Generated:** 2025-11-15T19:40:05.095635Z
**File Size:** 2573 bytes
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

- **Path:** `nautilus_trader/model/instruments/__init__.py`
- **Size:** 2,573 bytes
- **Lines:** 57
- **Extension:** `.py`
- **Type:** text
- **Imports:** 17

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
"""
Defines tradable asset/contract instruments with specific properties dependent on the
asset class and instrument class.
"""

from nautilus_trader.model.instruments.base import Instrument
from nautilus_trader.model.instruments.base import instruments_from_pyo3
from nautilus_trader.model.instruments.betting import BettingInstrument
from nautilus_trader.model.instruments.binary_option import BinaryOption
from nautilus_trader.model.instruments.cfd import Cfd
from nautilus_trader.model.instruments.commodity import Commodity
from nautilus_trader.model.instruments.crypto_future import CryptoFuture
from nautilus_trader.model.instruments.crypto_option import CryptoOption
from nautilus_trader.model.instruments.crypto_perpetual import CryptoPerpetual
from nautilus_trader.model.instruments.currency_pair import CurrencyPair
from nautilus_trader.model.instruments.equity import Equity
from nautilus_trader.model.instruments.futures_contract import FuturesContract
from nautilus_trader.model.instruments.futures_spread import FuturesSpread
from nautilus_trader.model.instruments.index import IndexInstrument
from nautilus_trader.model.instruments.option_contract import OptionContract
from nautilus_trader.model.instruments.option_spread import OptionSpread
from nautilus_trader.model.instruments.synthetic import SyntheticInstrument


__all__ = [
    "BettingInstrument",
    "BinaryOption",
    "Cfd",
    "Commodity",
    "CryptoFuture",
    "CryptoOption",
    "CryptoPerpetual",
    "CurrencyPair",
    "Equity",
    "FuturesContract",
    "FuturesSpread",
    "IndexInstrument",
    "Instrument",
    "OptionContract",
    "OptionSpread",
    "SyntheticInstrument",
    "instruments_from_pyo3",
]
```


---

## Overview

This file is located at `nautilus_trader/model/instruments/__init__.py` within the repository.

This is a Python package initialization file that may expose package contents or execute initialization code.

**Import statements:** 17


---

## Detailed Analysis

### Imports

- `from nautilus_trader.model.instruments.base import Instrument`
- `from nautilus_trader.model.instruments.base import instruments_from_pyo3`
- `from nautilus_trader.model.instruments.betting import BettingInstrument`
- `from nautilus_trader.model.instruments.binary_option import BinaryOption`
- `from nautilus_trader.model.instruments.cfd import Cfd`
- `from nautilus_trader.model.instruments.commodity import Commodity`
- `from nautilus_trader.model.instruments.crypto_future import CryptoFuture`
- `from nautilus_trader.model.instruments.crypto_option import CryptoOption`
- `from nautilus_trader.model.instruments.crypto_perpetual import CryptoPerpetual`
- `from nautilus_trader.model.instruments.currency_pair import CurrencyPair`
- `from nautilus_trader.model.instruments.equity import Equity`
- `from nautilus_trader.model.instruments.futures_contract import FuturesContract`
- `from nautilus_trader.model.instruments.futures_spread import FuturesSpread`
- `from nautilus_trader.model.instruments.index import IndexInstrument`
- `from nautilus_trader.model.instruments.option_contract import OptionContract`
- `from nautilus_trader.model.instruments.option_spread import OptionSpread`
- `from nautilus_trader.model.instruments.synthetic import SyntheticInstrument`


---

## Usage Examples

### Importing

```python
import nautilus_trader.model.instruments.__init__
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.model.instruments.base import Instrument`
- `from nautilus_trader.model.instruments.base import instruments_from_pyo3`
- `from nautilus_trader.model.instruments.betting import BettingInstrument`
- `from nautilus_trader.model.instruments.binary_option import BinaryOption`
- `from nautilus_trader.model.instruments.cfd import Cfd`
- `from nautilus_trader.model.instruments.commodity import Commodity`
- `from nautilus_trader.model.instruments.crypto_future import CryptoFuture`
- `from nautilus_trader.model.instruments.crypto_option import CryptoOption`
- `from nautilus_trader.model.instruments.crypto_perpetual import CryptoPerpetual`
- `from nautilus_trader.model.instruments.currency_pair import CurrencyPair`

*... and 7 more*

**Directory:** `nautilus_trader/model/instruments`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


