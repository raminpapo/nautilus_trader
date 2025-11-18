# Documentation: conftest.py

## File Metadata

- **Path**: `tests/unit_tests/persistence/conftest.py`
- **Size**: 2,309 bytes
- **Lines**: 62
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 3 function(s).

## Detailed Walkthrough

### Functions
- **`fixture_catalog_memory()`**: Function defined in this file
- **`fixture_catalog()`**: Function defined in this file
- **`fixture_catalog_betfair()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 10


**Functions**: `fixture_catalog`, `fixture_catalog_betfair`, `fixture_catalog_memory`
**Imports**: `nautilus_trader`, `nautilus_trader.adapters.betfair.parsing.core`, `nautilus_trader.model.currencies`, `nautilus_trader.model.objects`, `nautilus_trader.persistence.catalog.parquet`, `nautilus_trader.test_kit.mocks.data`, `pytest`

## Related Files

This file is located in `tests/unit_tests/persistence/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/unit_tests/persistence/conftest.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:11.694698Z*
