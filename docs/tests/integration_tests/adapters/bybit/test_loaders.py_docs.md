# Documentation: `tests/integration_tests/adapters/bybit/test_loaders.py`
**Generated:** 2025-11-15T19:40:07.729388Z
**File Size:** 1977 bytes
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

- **Path:** `tests/integration_tests/adapters/bybit/test_loaders.py`
- **Size:** 1,977 bytes
- **Lines:** 43
- **Extension:** `.py`
- **Type:** text
- **Imports:** 7
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

from nautilus_trader import TEST_DATA_DIR
from nautilus_trader.adapters.bybit.loaders import BybitOrderBookDeltaDataLoader
from nautilus_trader.model.enums import BookAction
from nautilus_trader.model.enums import OrderSide
from nautilus_trader.model.enums import RecordFlag
from nautilus_trader.persistence.wranglers import OrderBookDeltaDataWrangler
from nautilus_trader.test_kit.providers import TestInstrumentProvider


def test_load_bybit_deltas() -> None:
    # Arrange
    instrument = TestInstrumentProvider.xrpusdt_linear_bybit()
    data_path = TEST_DATA_DIR / "bybit" / "xrpusdt-ob500.data.zip"
    df = BybitOrderBookDeltaDataLoader.load(data_path)

    wrangler = OrderBookDeltaDataWrangler(instrument)

    # Act
    deltas = wrangler.process(df)

    # Assert
    assert len(deltas) == 3968
    assert deltas[0].action == BookAction.CLEAR
    assert deltas[1].action == BookAction.ADD
    assert deltas[1].order.side == OrderSide.SELL
    assert deltas[1].flags == RecordFlag.F_SNAPSHOT
    assert deltas[1002].action == BookAction.UPDATE
    assert deltas[1235].order.side == OrderSide.SELL
```


---

## Overview

This file is located at `tests/integration_tests/adapters/bybit/test_loaders.py` within the repository.

**Functions defined:** test_load_bybit_deltas

**Import statements:** 7


---

## Detailed Analysis

### Functions

#### `test_load_bybit_deltas()`


### Imports

- `from nautilus_trader import TEST_DATA_DIR`
- `from nautilus_trader.adapters.bybit.loaders import BybitOrderBookDeltaDataLoader`
- `from nautilus_trader.model.enums import BookAction`
- `from nautilus_trader.model.enums import OrderSide`
- `from nautilus_trader.model.enums import RecordFlag`
- `from nautilus_trader.persistence.wranglers import OrderBookDeltaDataWrangler`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`


---

## Usage Examples

### Importing

```python
from tests.integration_tests.adapters.bybit.test_loaders import test_load_bybit_deltas
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader import TEST_DATA_DIR`
- `from nautilus_trader.adapters.bybit.loaders import BybitOrderBookDeltaDataLoader`
- `from nautilus_trader.model.enums import BookAction`
- `from nautilus_trader.model.enums import OrderSide`
- `from nautilus_trader.model.enums import RecordFlag`
- `from nautilus_trader.persistence.wranglers import OrderBookDeltaDataWrangler`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`

**Directory:** `tests/integration_tests/adapters/bybit`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


