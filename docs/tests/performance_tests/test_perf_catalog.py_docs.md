# Documentation: `tests/performance_tests/test_perf_catalog.py`
**Generated:** 2025-11-15T19:40:08.038287Z
**File Size:** 4256 bytes
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

- **Path:** `tests/performance_tests/test_perf_catalog.py`
- **Size:** 4,256 bytes
- **Lines:** 127
- **Extension:** `.py`
- **Type:** text
- **Imports:** 9
- **Functions:** 12

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

import os

import pytest

from nautilus_trader import PACKAGE_ROOT
from nautilus_trader.core.nautilus_pyo3 import DataBackendSession
from nautilus_trader.core.nautilus_pyo3 import NautilusDataType
from nautilus_trader.model.data import capsule_to_list
from nautilus_trader.test_kit.mocks.data import load_catalog_with_stub_quote_ticks_audusd
from nautilus_trader.test_kit.mocks.data import load_catalog_with_stub_trade_ticks_ethusdt
from nautilus_trader.test_kit.mocks.data import setup_catalog


@pytest.mark.skip
@pytest.mark.benchmark(min_rounds=1)
def test_write_quote_ticks(benchmark, tmp_path) -> None:
    catalog = setup_catalog("file", path=tmp_path / "catalog")

    def run():
        load_catalog_with_stub_quote_ticks_audusd(catalog)
        quotes = catalog.quote_ticks()
        assert len(quotes) == 100_000

    benchmark(run)


@pytest.mark.skip
@pytest.mark.benchmark(min_rounds=1)
def test_load_quote_ticks(benchmark, tmp_path) -> None:
    catalog = setup_catalog("file", path=tmp_path / "catalog")
    load_catalog_with_stub_quote_ticks_audusd(catalog)

    def run():
        quotes = catalog.quote_ticks()
        assert len(quotes) == 100_000

    benchmark(run)


@pytest.mark.skip
@pytest.mark.benchmark(min_rounds=1)
def test_write_trade_ticks(benchmark, tmp_path) -> None:
    catalog = setup_catalog("file", path=tmp_path / "catalog")

    def run():
        load_catalog_with_stub_trade_ticks_ethusdt(catalog)
        trades = catalog.trade_ticks()
        assert len(trades) == 69_806

    benchmark(run)


@pytest.mark.skip
@pytest.mark.benchmark(min_rounds=1)
def test_load_trade_ticks(benchmark, tmp_path) -> None:
    catalog = setup_catalog("file", path=tmp_path / "catalog")
    load_catalog_with_stub_trade_ticks_ethusdt(catalog)

    def run():
        trades = catalog.trade_ticks()
        assert len(trades) == 69_806

    benchmark(run)


@pytest.mark.skip(reason="development_only")
def test_load_single_stream(benchmark) -> None:
    file_path = PACKAGE_ROOT / "bench_data" / "quotes_0005.parquet"
    session = DataBackendSession()
    session.add_file(
        NautilusDataType.QuoteTick,
        "quote_ticks",
        str(file_path),
    )

    def run(result):
        count = 0
        for chunk in result:
            count += len(capsule_to_list(chunk))

        assert count == 9_689_614

    benchmark(run)


@pytest.mark.skip(reason="development_only")
def test_load_multi_stream_catalog_v2(benchmark) -> None:
    dir_path = PACKAGE_ROOT / "bench_data" / "multi_stream_data/"

    session = DataBackendSession()

    for dirpath, _, filenames in os.walk(dir_path):
        for filename in filenames:
            if filename.endswith("parquet"):
                file_stem = os.path.splitext(filename)[0]
                if "quotes" in filename:
                    full_path = os.path.join(dirpath, filename)
                    session.add_file(NautilusDataType.QuoteTick, file_stem, full_path)
                elif "trades" in filename:
                    full_path = os.path.join(dirpath, filename)
                    session.add_file(NautilusDataType.TradeTick, file_stem, full_path)

    def run(result):
        count = 0
        for chunk in result:
            ticks = capsule_to_list(chunk)
            count += len(ticks)

        # Check total count is correct
        assert count == 72_536_038

    benchmark(run)
```


---

## Overview

This file is located at `tests/performance_tests/test_perf_catalog.py` within the repository.

**Functions defined:** test_write_quote_ticks, run, test_load_quote_ticks, run, test_write_trade_ticks, run, test_load_trade_ticks, run, test_load_single_stream, run and 2 more

**Import statements:** 9


---

## Detailed Analysis

### Functions

#### `test_write_quote_ticks(benchmark, tmp_path)`


#### `run()`


#### `test_load_quote_ticks(benchmark, tmp_path)`


#### `run()`


#### `test_write_trade_ticks(benchmark, tmp_path)`


#### `run()`


#### `test_load_trade_ticks(benchmark, tmp_path)`


#### `run()`


#### `test_load_single_stream(benchmark)`


#### `run(result)`


#### `test_load_multi_stream_catalog_v2(benchmark)`


#### `run(result)`


### Imports

- `import os`
- `import pytest`
- `from nautilus_trader import PACKAGE_ROOT`
- `from nautilus_trader.core.nautilus_pyo3 import DataBackendSession`
- `from nautilus_trader.core.nautilus_pyo3 import NautilusDataType`
- `from nautilus_trader.model.data import capsule_to_list`
- `from nautilus_trader.test_kit.mocks.data import load_catalog_with_stub_quote_ticks_audusd`
- `from nautilus_trader.test_kit.mocks.data import load_catalog_with_stub_trade_ticks_ethusdt`
- `from nautilus_trader.test_kit.mocks.data import setup_catalog`


---

## Usage Examples

### Importing

```python
from tests.performance_tests.test_perf_catalog import test_write_quote_ticks
```


---

## Related Files

This file imports from the following modules:

- `import os`
- `import pytest`
- `from nautilus_trader import PACKAGE_ROOT`
- `from nautilus_trader.core.nautilus_pyo3 import DataBackendSession`
- `from nautilus_trader.core.nautilus_pyo3 import NautilusDataType`
- `from nautilus_trader.model.data import capsule_to_list`
- `from nautilus_trader.test_kit.mocks.data import load_catalog_with_stub_quote_ticks_audusd`
- `from nautilus_trader.test_kit.mocks.data import load_catalog_with_stub_trade_ticks_ethusdt`
- `from nautilus_trader.test_kit.mocks.data import setup_catalog`

**Directory:** `tests/performance_tests`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: session. Ensure proper handling of secrets.

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


