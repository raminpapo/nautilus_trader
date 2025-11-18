# Documentation: __init__.py

## File Metadata

- **Path**: `nautilus_trader/model/instruments/__init__.py`
- **Size**: 2,573 bytes
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

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 16


**Imports**: `nautilus_trader.model.instruments.base`, `nautilus_trader.model.instruments.betting`, `nautilus_trader.model.instruments.binary_option`, `nautilus_trader.model.instruments.cfd`, `nautilus_trader.model.instruments.commodity`, `nautilus_trader.model.instruments.crypto_future`, `nautilus_trader.model.instruments.crypto_option`, `nautilus_trader.model.instruments.crypto_perpetual`, `nautilus_trader.model.instruments.currency_pair`, `nautilus_trader.model.instruments.equity`, `nautilus_trader.model.instruments.futures_contract`, `nautilus_trader.model.instruments.futures_spread`, `nautilus_trader.model.instruments.index`, `nautilus_trader.model.instruments.option_contract`, `nautilus_trader.model.instruments.option_spread`, `nautilus_trader.model.instruments.synthetic`

## Related Files

This file is located in `nautilus_trader/model/instruments/`. Related files may include:
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
*Generated on 2025-11-18T21:55:05.693380Z*
