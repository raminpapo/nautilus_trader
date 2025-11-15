# Documentation: `tests/unit_tests/persistence/conftest.py`
**Generated:** 2025-11-15T19:40:09.409760Z
**File Size:** 2309 bytes
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

- **Path:** `tests/unit_tests/persistence/conftest.py`
- **Size:** 2,309 bytes
- **Lines:** 61
- **Extension:** `.py`
- **Type:** text
- **Imports:** 8
- **Functions:** 3

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

import pytest

from nautilus_trader import TEST_DATA_DIR
from nautilus_trader.adapters.betfair.parsing.core import betting_instruments_from_file
from nautilus_trader.adapters.betfair.parsing.core import parse_betfair_file
from nautilus_trader.model.currencies import GBP
from nautilus_trader.model.objects import Money
from nautilus_trader.persistence.catalog.parquet import ParquetDataCatalog
from nautilus_trader.test_kit.mocks.data import setup_catalog


@pytest.fixture(name="catalog_memory")
def fixture_catalog_memory(tmp_path) -> ParquetDataCatalog:
    return setup_catalog(protocol="memory", path=tmp_path / "catalog_memory")


@pytest.fixture(name="catalog")
def fixture_catalog(tmp_path) -> ParquetDataCatalog:
    return setup_catalog(protocol="file", path=tmp_path / "catalog_file")


@pytest.fixture(name="catalog_betfair")
def fixture_catalog_betfair(catalog: ParquetDataCatalog) -> ParquetDataCatalog:
    filename = TEST_DATA_DIR / "betfair" / "1-166564490.bz2"

    # Write betting instruments
    instruments = betting_instruments_from_file(
        filename,
        currency="GBP",
        ts_event=0,
        ts_init=0,
        min_notional=Money(1, GBP),
    )
    catalog.write_data(instruments)

    # Write data
    data = list(
        parse_betfair_file(
            filename,
            currency="GBP",
            min_notional=Money(1, GBP),
        ),
    )
    catalog.write_data(data)

    return catalog
```


---

## Overview

This file is located at `tests/unit_tests/persistence/conftest.py` within the repository.

**Functions defined:** fixture_catalog_memory, fixture_catalog, fixture_catalog_betfair

**Import statements:** 8


---

## Detailed Analysis

### Functions

#### `fixture_catalog_memory(tmp_path)`


#### `fixture_catalog(tmp_path)`


#### `fixture_catalog_betfair(catalog: ParquetDataCatalog)`


### Imports

- `import pytest`
- `from nautilus_trader import TEST_DATA_DIR`
- `from nautilus_trader.adapters.betfair.parsing.core import betting_instruments_from_file`
- `from nautilus_trader.adapters.betfair.parsing.core import parse_betfair_file`
- `from nautilus_trader.model.currencies import GBP`
- `from nautilus_trader.model.objects import Money`
- `from nautilus_trader.persistence.catalog.parquet import ParquetDataCatalog`
- `from nautilus_trader.test_kit.mocks.data import setup_catalog`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.persistence.conftest import fixture_catalog_memory
```


---

## Related Files

This file imports from the following modules:

- `import pytest`
- `from nautilus_trader import TEST_DATA_DIR`
- `from nautilus_trader.adapters.betfair.parsing.core import betting_instruments_from_file`
- `from nautilus_trader.adapters.betfair.parsing.core import parse_betfair_file`
- `from nautilus_trader.model.currencies import GBP`
- `from nautilus_trader.model.objects import Money`
- `from nautilus_trader.persistence.catalog.parquet import ParquetDataCatalog`
- `from nautilus_trader.test_kit.mocks.data import setup_catalog`

**Directory:** `tests/unit_tests/persistence`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


