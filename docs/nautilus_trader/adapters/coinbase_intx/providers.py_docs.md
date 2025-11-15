# Documentation: `nautilus_trader/adapters/coinbase_intx/providers.py`
**Generated:** 2025-11-15T19:40:04.212608Z
**File Size:** 3428 bytes
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

- **Path:** `nautilus_trader/adapters/coinbase_intx/providers.py`
- **Size:** 3,428 bytes
- **Lines:** 86
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

from typing import Any

from nautilus_trader.common.providers import InstrumentProvider
from nautilus_trader.config import InstrumentProviderConfig
from nautilus_trader.core import nautilus_pyo3
from nautilus_trader.core.correctness import PyCondition
from nautilus_trader.model.identifiers import InstrumentId
from nautilus_trader.model.instruments import instruments_from_pyo3


class CoinbaseIntxInstrumentProvider(InstrumentProvider):
    """
    Provides Nautilus instrument definitions from Coinbase International.

    Parameters
    ----------
    client : CoinbaseIntxHttpClient
        The Coinbase International HTTP client.
    config : InstrumentProviderConfig, optional
        The instrument provider configuration, by default None.

    """

    def __init__(
        self,
        client: nautilus_pyo3.CoinbaseIntxHttpClient,
        config: InstrumentProviderConfig | None = None,
    ) -> None:
        super().__init__(config=config)
        self._client = client
        self._log_warnings = config.log_warnings if config else True

        self._instruments_pyo3: list[nautilus_pyo3.Instrument] = []

    def instruments_pyo3(self) -> list[Any]:
        return self._instruments_pyo3

    async def load_all_async(self, filters: dict | None = None) -> None:
        pyo3_instruments = await self._client.request_instruments()
        self._instruments_pyo3 = pyo3_instruments

        instruments = instruments_from_pyo3(pyo3_instruments)
        for instrument in instruments:
            self.add(instrument=instrument)

    async def load_ids_async(
        self,
        instrument_ids: list[InstrumentId],
        filters: dict | None = None,
    ) -> None:
        if not instrument_ids:
            self._log.warning("No instrument IDs given for loading")
            return

        pyo3_instruments = await self._client.request_instruments()
        self._instruments_pyo3 = pyo3_instruments

        instruments = instruments_from_pyo3(pyo3_instruments)
        for instrument in instruments:
            self.add(instrument=instrument)

            instruments = instruments_from_pyo3(pyo3_instruments)

            for instrument in instruments:
                if instrument.id not in instrument_ids:
                    continue  # Filter instrument ID
                self.add(instrument=instrument)

    async def load_async(self, instrument_id: InstrumentId, filters: dict | None = None) -> None:
        PyCondition.not_none(instrument_id, "instrument_id")
        await self.load_ids_async([instrument_id], filters)
```


---

## Overview

This file is located at `nautilus_trader/adapters/coinbase_intx/providers.py` within the repository.

**Classes defined:** CoinbaseIntxInstrumentProvider

**Functions defined:** __init__, instruments_pyo3

**Import statements:** 7


---

## Detailed Analysis

### Classes

#### `CoinbaseIntxInstrumentProvider`

**Inherits from:** InstrumentProvider


### Functions

#### `__init__(
        self,
        client: nautilus_pyo3.CoinbaseIntxHttpClient,
        config: InstrumentProviderConfig | None = None,
    )`


#### `instruments_pyo3(self)`


### Imports

- `from typing import Any`
- `from nautilus_trader.common.providers import InstrumentProvider`
- `from nautilus_trader.config import InstrumentProviderConfig`
- `from nautilus_trader.core import nautilus_pyo3`
- `from nautilus_trader.core.correctness import PyCondition`
- `from nautilus_trader.model.identifiers import InstrumentId`
- `from nautilus_trader.model.instruments import instruments_from_pyo3`


---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters.coinbase_intx.providers import CoinbaseIntxInstrumentProvider
```


---

## Related Files

This file imports from the following modules:

- `from typing import Any`
- `from nautilus_trader.common.providers import InstrumentProvider`
- `from nautilus_trader.config import InstrumentProviderConfig`
- `from nautilus_trader.core import nautilus_pyo3`
- `from nautilus_trader.core.correctness import PyCondition`
- `from nautilus_trader.model.identifiers import InstrumentId`
- `from nautilus_trader.model.instruments import instruments_from_pyo3`

**Directory:** `nautilus_trader/adapters/coinbase_intx`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


