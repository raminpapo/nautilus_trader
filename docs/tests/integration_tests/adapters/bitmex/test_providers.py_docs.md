# Documentation: `tests/integration_tests/adapters/bitmex/test_providers.py`
**Generated:** 2025-11-15T19:40:07.718007Z
**File Size:** 3950 bytes
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

- **Path:** `tests/integration_tests/adapters/bitmex/test_providers.py`
- **Size:** 3,950 bytes
- **Lines:** 102
- **Extension:** `.py`
- **Type:** text
- **Imports:** 14
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

from decimal import Decimal
from unittest.mock import AsyncMock
from unittest.mock import MagicMock

import pytest

from nautilus_trader.adapters.bitmex.constants import BITMEX_VENUE
from nautilus_trader.adapters.bitmex.providers import BitmexInstrumentProvider
from nautilus_trader.core import nautilus_pyo3
from nautilus_trader.model.currencies import BTC
from nautilus_trader.model.currencies import USD
from nautilus_trader.model.identifiers import InstrumentId
from nautilus_trader.model.identifiers import Symbol
from nautilus_trader.model.instruments import CryptoPerpetual
from nautilus_trader.model.objects import Price
from nautilus_trader.model.objects import Quantity


def _create_perpetual(symbol: str) -> CryptoPerpetual:
    instrument_id = InstrumentId(Symbol(symbol), BITMEX_VENUE)
    return CryptoPerpetual(
        instrument_id=instrument_id,
        raw_symbol=Symbol(symbol),
        base_currency=BTC,
        quote_currency=USD,
        settlement_currency=BTC,
        is_inverse=True,
        price_precision=1,
        price_increment=Price.from_str("0.5"),
        size_precision=0,
        size_increment=Quantity.from_int(1),
        margin_init=Decimal("0.01"),
        margin_maint=Decimal("0.005"),
        maker_fee=Decimal("-0.00025"),
        taker_fee=Decimal("0.00075"),
        ts_event=0,
        ts_init=0,
    )


@pytest.mark.asyncio
async def test_load_all_async_populates_provider(monkeypatch, instrument):
    # Arrange
    mock_http_client = MagicMock(spec=nautilus_pyo3.BitmexHttpClient)
    pyo3_instruments = [MagicMock(name="py_instrument")]
    mock_http_client.request_instruments = AsyncMock(return_value=pyo3_instruments)

    provider = BitmexInstrumentProvider(mock_http_client)

    monkeypatch.setattr(
        "nautilus_trader.adapters.bitmex.providers.instruments_from_pyo3",
        lambda _values: [instrument],
    )

    # Act
    await provider.load_all_async()

    # Assert
    mock_http_client.request_instruments.assert_awaited_once_with(True)
    assert provider.instruments_pyo3() == pyo3_instruments
    assert provider.get_all().get(instrument.id) is instrument


@pytest.mark.asyncio
async def test_load_ids_async_filters_results(monkeypatch, instrument):
    # Arrange
    mock_http_client = MagicMock(spec=nautilus_pyo3.BitmexHttpClient)
    pyo3_instruments = [MagicMock(name="py_a"), MagicMock(name="py_b")]
    mock_http_client.request_instruments = AsyncMock(return_value=pyo3_instruments)

    provider = BitmexInstrumentProvider(mock_http_client)

    other_instrument = _create_perpetual("ETHUSD")

    monkeypatch.setattr(
        "nautilus_trader.adapters.bitmex.providers.instruments_from_pyo3",
        lambda _values: [instrument, other_instrument],
    )

    # Act
    await provider.load_ids_async([instrument.id])

    # Assert
    mock_http_client.request_instruments.assert_awaited_once_with(True)
    assert provider.get_all().get(instrument.id) is instrument
    assert provider.get_all().get(other_instrument.id) is None
    assert provider.instruments_pyo3() == pyo3_instruments
```


---

## Overview

This file is located at `tests/integration_tests/adapters/bitmex/test_providers.py` within the repository.

**Functions defined:** _create_perpetual

**Import statements:** 14


---

## Detailed Analysis

### Functions

#### `_create_perpetual(symbol: str)`


### Imports

- `from decimal import Decimal`
- `from unittest.mock import AsyncMock`
- `from unittest.mock import MagicMock`
- `import pytest`
- `from nautilus_trader.adapters.bitmex.constants import BITMEX_VENUE`
- `from nautilus_trader.adapters.bitmex.providers import BitmexInstrumentProvider`
- `from nautilus_trader.core import nautilus_pyo3`
- `from nautilus_trader.model.currencies import BTC`
- `from nautilus_trader.model.currencies import USD`
- `from nautilus_trader.model.identifiers import InstrumentId`
- `from nautilus_trader.model.identifiers import Symbol`
- `from nautilus_trader.model.instruments import CryptoPerpetual`
- `from nautilus_trader.model.objects import Price`
- `from nautilus_trader.model.objects import Quantity`


---

## Usage Examples

### Importing

```python
from tests.integration_tests.adapters.bitmex.test_providers import _create_perpetual
```


---

## Related Files

This file imports from the following modules:

- `from decimal import Decimal`
- `from unittest.mock import AsyncMock`
- `from unittest.mock import MagicMock`
- `import pytest`
- `from nautilus_trader.adapters.bitmex.constants import BITMEX_VENUE`
- `from nautilus_trader.adapters.bitmex.providers import BitmexInstrumentProvider`
- `from nautilus_trader.core import nautilus_pyo3`
- `from nautilus_trader.model.currencies import BTC`
- `from nautilus_trader.model.currencies import USD`
- `from nautilus_trader.model.identifiers import InstrumentId`

*... and 4 more*

**Directory:** `tests/integration_tests/adapters/bitmex`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


