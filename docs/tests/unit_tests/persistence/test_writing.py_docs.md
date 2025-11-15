# Documentation: `tests/unit_tests/persistence/test_writing.py`
**Generated:** 2025-11-15T19:40:09.434784Z
**File Size:** 1928 bytes
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

- **Path:** `tests/unit_tests/persistence/test_writing.py`
- **Size:** 1,928 bytes
- **Lines:** 53
- **Extension:** `.py`
- **Type:** text
- **Imports:** 4
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

from io import BytesIO

import pyarrow as pa

from nautilus_trader.core import nautilus_pyo3
from nautilus_trader.model.data import OrderBookDelta


def test_legacy_deltas_to_record_batch_reader() -> None:
    # Arrange
    ticks = [
        OrderBookDelta.from_dict(
            {
                "type": "OrderBookDelta",
                "instrument_id": "1.166564490-237491-0.0.BETFAIR",
                "action": "CLEAR",
                "order": {
                    "side": "NO_ORDER_SIDE",
                    "price": "0",
                    "size": "0",
                    "order_id": 0,
                },
                "flags": 32,
                "sequence": 0,
                "ts_event": 1576840503572000000,
                "ts_init": 1576840503572000000,
            },
        ),
    ]

    # Act
    batch_bytes = nautilus_pyo3.pyobjects_to_arrow_record_batch_bytes(ticks)
    reader = pa.ipc.open_stream(BytesIO(batch_bytes))

    # Assert
    assert len(ticks) == 1
    assert len(reader.read_all()) == len(ticks)
    reader.close()
```


---

## Overview

This file is located at `tests/unit_tests/persistence/test_writing.py` within the repository.

**Functions defined:** test_legacy_deltas_to_record_batch_reader

**Import statements:** 4


---

## Detailed Analysis

### Functions

#### `test_legacy_deltas_to_record_batch_reader()`


### Imports

- `from io import BytesIO`
- `import pyarrow as pa`
- `from nautilus_trader.core import nautilus_pyo3`
- `from nautilus_trader.model.data import OrderBookDelta`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.persistence.test_writing import test_legacy_deltas_to_record_batch_reader
```


---

## Related Files

This file imports from the following modules:

- `from io import BytesIO`
- `import pyarrow as pa`
- `from nautilus_trader.core import nautilus_pyo3`
- `from nautilus_trader.model.data import OrderBookDelta`

**Directory:** `tests/unit_tests/persistence`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


