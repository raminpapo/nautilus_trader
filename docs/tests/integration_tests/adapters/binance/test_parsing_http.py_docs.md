# Documentation: `tests/integration_tests/adapters/binance/test_parsing_http.py`
**Generated:** 2025-11-15T19:40:07.703975Z
**File Size:** 3311 bytes
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

- **Path:** `tests/integration_tests/adapters/binance/test_parsing_http.py`
- **Size:** 3,311 bytes
- **Lines:** 81
- **Extension:** `.py`
- **Type:** text
- **Imports:** 7
- **Classes:** 1
- **Functions:** 2

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

import pkgutil

import msgspec

from nautilus_trader.adapters.binance.common.schemas.market import BinanceDepth
from nautilus_trader.adapters.binance.futures.schemas.account import BinanceFuturesSymbolConfig
from nautilus_trader.model.objects import Price
from nautilus_trader.model.objects import Quantity
from nautilus_trader.test_kit.providers import TestInstrumentProvider


ETHUSDT = TestInstrumentProvider.ethusdt_binance()


class TestBinanceHttpParsing:
    def test_parse_book_snapshot(self):
        # Arrange
        raw = pkgutil.get_data(
            package="tests.integration_tests.adapters.binance.resources.http_responses",
            resource="http_spot_market_depth.json",
        )
        assert raw
        decoder = msgspec.json.Decoder(BinanceDepth)

        # Act
        data = decoder.decode(raw)
        result = data.parse_to_order_book_snapshot(
            instrument_id=ETHUSDT.id,
            ts_init=2,
        )

        # Assert
        assert result.is_snapshot
        assert result.instrument_id == ETHUSDT.id
        assert len(result.deltas) == 21
        assert result.deltas[1].order.price == Price.from_str("60650.00")  # <-- Top bid
        assert result.deltas[1].order.size == Quantity.from_str("0.00213")  # <-- Top bid
        assert result.deltas[11].order.price == Price.from_str("60650.01")  # <-- Top ask
        assert result.deltas[11].order.size == Quantity.from_str("0.61982")  # <-- Top ask
        assert result.sequence == 14527958487
        assert result.ts_init == 2

    def test_parse_futures_symbol_config(self):
        # Arrange
        raw = pkgutil.get_data(
            package="tests.integration_tests.adapters.binance.resources.http_responses",
            resource="http_futures_account_symbol_config.json",
        )
        assert raw
        decoder = msgspec.json.Decoder(list[BinanceFuturesSymbolConfig])

        # Act
        data = decoder.decode(raw)

        # Assert
        assert len(data) == 2
        assert data[0].symbol == "ETHUSDT"
        assert data[0].marginType == "CROSSED"
        assert data[0].isAutoAddMargin is False
        assert data[0].leverage == 20
        assert data[0].maxNotionalValue == "1000000"
        assert data[1].symbol == "BTCUSDT"
        assert data[1].marginType == "ISOLATED"
        assert data[1].isAutoAddMargin is True
        assert data[1].leverage == 25
        assert data[1].maxNotionalValue == "2000000"
```


---

## Overview

This file is located at `tests/integration_tests/adapters/binance/test_parsing_http.py` within the repository.

**Classes defined:** TestBinanceHttpParsing

**Functions defined:** test_parse_book_snapshot, test_parse_futures_symbol_config

**Import statements:** 7


---

## Detailed Analysis

### Classes

#### `TestBinanceHttpParsing`


### Functions

#### `test_parse_book_snapshot(self)`


#### `test_parse_futures_symbol_config(self)`


### Imports

- `import pkgutil`
- `import msgspec`
- `from nautilus_trader.adapters.binance.common.schemas.market import BinanceDepth`
- `from nautilus_trader.adapters.binance.futures.schemas.account import BinanceFuturesSymbolConfig`
- `from nautilus_trader.model.objects import Price`
- `from nautilus_trader.model.objects import Quantity`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`


---

## Usage Examples

### Importing

```python
from tests.integration_tests.adapters.binance.test_parsing_http import TestBinanceHttpParsing
```


---

## Related Files

This file imports from the following modules:

- `import pkgutil`
- `import msgspec`
- `from nautilus_trader.adapters.binance.common.schemas.market import BinanceDepth`
- `from nautilus_trader.adapters.binance.futures.schemas.account import BinanceFuturesSymbolConfig`
- `from nautilus_trader.model.objects import Price`
- `from nautilus_trader.model.objects import Quantity`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`

**Directory:** `tests/integration_tests/adapters/binance`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


