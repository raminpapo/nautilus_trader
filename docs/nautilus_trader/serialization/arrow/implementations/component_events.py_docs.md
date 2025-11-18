# Documentation: component_events.py

## File Metadata

- **Path**: `nautilus_trader/serialization/arrow/implementations/component_events.py`
- **Size**: 1,695 bytes
- **Lines**: 39
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

import msgspec
import pyarrow as pa

from nautilus_trader.common.messages import ComponentStateChanged
from nautilus_trader.common.messages import TradingStateChanged
from nautilus_trader.serialization.arrow.schema import NAUTILUS_ARROW_SCHEMA


def serialize(event: ComponentStateChanged | TradingStateChanged) -> pa.RecordBatch:
    data = event.to_dict(event)
    data["config"] = msgspec.json.encode(data["config"])
    return pa.RecordBatch.from_pylist([data], schema=NAUTILUS_ARROW_SCHEMA[type(event)])


def deserialize(cls):
    def inner(batch: pa.RecordBatch) -> list[ComponentStateChanged | TradingStateChanged]:
        def parse(data):
            data["config"] = msgspec.json.decode(data["config"])
            return data

        return [cls.from_dict(parse(d)) for d in batch.to_pylist()]

    return inner

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 2 function(s).

## Detailed Walkthrough

### Functions
- **`serialize()`**: Function defined in this file
- **`deserialize()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 6


**Functions**: `deserialize`, `serialize`
**Imports**: `msgspec`, `nautilus_trader.common.messages`, `nautilus_trader.serialization.arrow.schema`, `pyarrow`

## Related Files

This file is located in `nautilus_trader/serialization/arrow/implementations/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

Tests for this file may be located in:
- `tests/` directory in the same folder
- Corresponding test module in the project

Run the full test suite to verify functionality.

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:05.917854Z*
