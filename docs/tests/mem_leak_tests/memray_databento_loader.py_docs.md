# Documentation: `tests/mem_leak_tests/memray_databento_loader.py`
**Generated:** 2025-11-15T19:40:08.022487Z
**File Size:** 1591 bytes
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

- **Path:** `tests/mem_leak_tests/memray_databento_loader.py`
- **Size:** 1,591 bytes
- **Lines:** 34
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3

---

## Source Code

```python
#!/usr/bin/env python3
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

from nautilus_trader.adapters.databento.loaders import DatabentoDataLoader
from nautilus_trader.model.identifiers import InstrumentId
from tests.integration_tests.adapters.databento.test_loaders import DATABENTO_TEST_DATA_DIR


if __name__ == "__main__":
    loader = DatabentoDataLoader()
    path = DATABENTO_TEST_DATA_DIR / "temp" / "tsla-xnas-20240107-20240206.trades.dbn.zst"
    instrument_id = InstrumentId.from_str("TSLA.XNAS")

    count = 0
    total_runs = 128
    while count < total_runs:
        count += 1
        print(f"Run: {count}/{total_runs}")

        data = loader.from_dbn_file(path, instrument_id=instrument_id, as_legacy_cython=True)
        assert len(data) == 6_885_435
```


---

## Overview

This file is located at `tests/mem_leak_tests/memray_databento_loader.py` within the repository.

**Import statements:** 3


---

## Detailed Analysis

### Imports

- `from nautilus_trader.adapters.databento.loaders import DatabentoDataLoader`
- `from nautilus_trader.model.identifiers import InstrumentId`
- `from tests.integration_tests.adapters.databento.test_loaders import DATABENTO_TEST_DATA_DIR`


---

## Usage Examples

### Importing

```python
import tests.mem_leak_tests.memray_databento_loader
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.adapters.databento.loaders import DatabentoDataLoader`
- `from nautilus_trader.model.identifiers import InstrumentId`
- `from tests.integration_tests.adapters.databento.test_loaders import DATABENTO_TEST_DATA_DIR`

**Directory:** `tests/mem_leak_tests`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


