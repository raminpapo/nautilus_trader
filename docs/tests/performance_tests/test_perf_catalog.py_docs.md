# Documentation: test_perf_catalog.py

## File Metadata

- **Path**: `tests/performance_tests/test_perf_catalog.py`
- **Size**: 4,256 bytes
- **Lines**: 128
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 6 function(s).

## Detailed Walkthrough

### Functions
- **`test_write_quote_ticks()`**: Function defined in this file
- **`test_load_quote_ticks()`**: Function defined in this file
- **`test_write_trade_ticks()`**: Function defined in this file
- **`test_load_trade_ticks()`**: Function defined in this file
- **`test_load_single_stream()`**: Function defined in this file
- **`test_load_multi_stream_catalog_v2()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 12


**Functions**: `test_load_multi_stream_catalog_v2`, `test_load_quote_ticks`, `test_load_single_stream`, `test_load_trade_ticks`, `test_write_quote_ticks`, `test_write_trade_ticks`
**Imports**: `nautilus_trader`, `nautilus_trader.core.nautilus_pyo3`, `nautilus_trader.model.data`, `nautilus_trader.test_kit.mocks.data`, `os`, `pytest`

## Related Files

This file is located in `tests/performance_tests/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/performance_tests/test_perf_catalog.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:07.300640Z*
