# Documentation: test_writing.py

## File Metadata

- **Path**: `tests/unit_tests/persistence/test_writing.py`
- **Size**: 1,928 bytes
- **Lines**: 54
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`test_legacy_deltas_to_record_batch_reader()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 5


**Functions**: `test_legacy_deltas_to_record_batch_reader`
**Imports**: `io`, `nautilus_trader.core`, `nautilus_trader.model.data`, `pyarrow`

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
pytest tests/unit_tests/persistence/test_writing.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:11.721326Z*
