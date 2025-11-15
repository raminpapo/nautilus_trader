# Documentation: `nautilus_trader/serialization/arrow/implementations/component_commands.py`
**Generated:** 2025-11-15T19:40:05.301865Z
**File Size:** 1437 bytes
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

- **Path:** `nautilus_trader/serialization/arrow/implementations/component_commands.py`
- **Size:** 1,437 bytes
- **Lines:** 34
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3
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

import pyarrow as pa

from nautilus_trader.common.messages import ShutdownSystem
from nautilus_trader.serialization.arrow.schema import NAUTILUS_ARROW_SCHEMA


def serialize(command: ShutdownSystem) -> pa.RecordBatch:
    data = command.to_dict(command)
    return pa.RecordBatch.from_pylist([data], schema=NAUTILUS_ARROW_SCHEMA[type(command)])


def deserialize(cls):
    def inner(batch: pa.RecordBatch) -> list[ShutdownSystem]:
        def parse(data):
            return data

        return [cls.from_dict(parse(d)) for d in batch.to_pylist()]

    return inner
```


---

## Overview

This file is located at `nautilus_trader/serialization/arrow/implementations/component_commands.py` within the repository.

**Functions defined:** serialize, deserialize, inner, parse

**Import statements:** 3


---

## Detailed Analysis

### Functions

#### `serialize(command: ShutdownSystem)`


#### `deserialize(cls)`


#### `inner(batch: pa.RecordBatch)`


#### `parse(data)`


### Imports

- `import pyarrow as pa`
- `from nautilus_trader.common.messages import ShutdownSystem`
- `from nautilus_trader.serialization.arrow.schema import NAUTILUS_ARROW_SCHEMA`


---

## Usage Examples

### Importing

```python
from nautilus_trader.serialization.arrow.implementations.component_commands import serialize
```


---

## Related Files

This file imports from the following modules:

- `import pyarrow as pa`
- `from nautilus_trader.common.messages import ShutdownSystem`
- `from nautilus_trader.serialization.arrow.schema import NAUTILUS_ARROW_SCHEMA`

**Directory:** `nautilus_trader/serialization/arrow/implementations`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


