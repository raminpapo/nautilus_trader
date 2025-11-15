# Documentation: `nautilus_trader/serialization/arrow/implementations/order_events.py`
**Generated:** 2025-11-15T19:40:05.306549Z
**File Size:** 2527 bytes
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

- **Path:** `nautilus_trader/serialization/arrow/implementations/order_events.py`
- **Size:** 2,527 bytes
- **Lines:** 52
- **Extension:** `.py`
- **Type:** text
- **Imports:** 5
- **Functions:** 4

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

import msgspec
import pyarrow as pa

from nautilus_trader.model.events import OrderFilled
from nautilus_trader.model.events import OrderInitialized
from nautilus_trader.serialization.arrow.schema import NAUTILUS_ARROW_SCHEMA


def serialize(event: OrderInitialized | OrderFilled) -> pa.RecordBatch:
    data = event.to_dict(event)
    if isinstance(event, OrderInitialized):
        data["options"] = msgspec.json.encode(data["options"])
        data["linked_order_ids"] = msgspec.json.encode(data["linked_order_ids"])
        data["exec_algorithm_params"] = msgspec.json.encode(data["exec_algorithm_params"])
        data["tags"] = msgspec.json.encode(data["tags"])
    elif isinstance(event, OrderFilled):
        data["info"] = msgspec.json.encode(data["info"])
    return pa.RecordBatch.from_pylist([data], schema=NAUTILUS_ARROW_SCHEMA[type(event)])


def deserialize(cls):
    def inner(batch: pa.RecordBatch) -> OrderInitialized | OrderFilled:
        def parse(data):
            if cls == OrderInitialized:
                data["options"] = msgspec.json.decode(data["options"])
                data["linked_order_ids"] = msgspec.json.decode(data["linked_order_ids"])
                data["exec_algorithm_params"] = msgspec.json.decode(data["exec_algorithm_params"])
                data["tags"] = msgspec.json.decode(data["tags"])
            elif cls == OrderFilled:
                data["info"] = msgspec.json.decode(data["info"])
            else:
                raise RuntimeError("Unsupported order event type for deserialization")
            return data

        return [cls.from_dict(parse(d)) for d in batch.to_pylist()]

    return inner
```


---

## Overview

This file is located at `nautilus_trader/serialization/arrow/implementations/order_events.py` within the repository.

**Functions defined:** serialize, deserialize, inner, parse

**Import statements:** 5


---

## Detailed Analysis

### Functions

#### `serialize(event: OrderInitialized | OrderFilled)`


#### `deserialize(cls)`


#### `inner(batch: pa.RecordBatch)`


#### `parse(data)`


### Imports

- `import msgspec`
- `import pyarrow as pa`
- `from nautilus_trader.model.events import OrderFilled`
- `from nautilus_trader.model.events import OrderInitialized`
- `from nautilus_trader.serialization.arrow.schema import NAUTILUS_ARROW_SCHEMA`


---

## Usage Examples

### Importing

```python
from nautilus_trader.serialization.arrow.implementations.order_events import serialize
```


---

## Related Files

This file imports from the following modules:

- `import msgspec`
- `import pyarrow as pa`
- `from nautilus_trader.model.events import OrderFilled`
- `from nautilus_trader.model.events import OrderInitialized`
- `from nautilus_trader.serialization.arrow.schema import NAUTILUS_ARROW_SCHEMA`

**Directory:** `nautilus_trader/serialization/arrow/implementations`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


