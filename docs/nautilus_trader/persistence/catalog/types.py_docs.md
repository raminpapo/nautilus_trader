# Documentation: `nautilus_trader/persistence/catalog/types.py`
**Generated:** 2025-11-15T19:40:05.251154Z
**File Size:** 1334 bytes
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

- **Path:** `nautilus_trader/persistence/catalog/types.py`
- **Size:** 1,334 bytes
- **Lines:** 34
- **Extension:** `.py`
- **Type:** text
- **Imports:** 5
- **Classes:** 1

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

from __future__ import annotations

from dataclasses import dataclass

from nautilus_trader.core.data import Data
from nautilus_trader.model.identifiers import ClientId
from nautilus_trader.model.instruments import Instrument


@dataclass(frozen=True)
class CatalogDataResult:
    """
    Represents a catalog data query result.
    """

    data_cls: type
    data: list[Data]
    instruments: list[Instrument] | None = None
    client_id: ClientId | None = None
```


---

## Overview

This file is located at `nautilus_trader/persistence/catalog/types.py` within the repository.

**Classes defined:** CatalogDataResult

**Import statements:** 5


---

## Detailed Analysis

### Classes

#### `CatalogDataResult`


### Imports

- `from __future__ import annotations`
- `from dataclasses import dataclass`
- `from nautilus_trader.core.data import Data`
- `from nautilus_trader.model.identifiers import ClientId`
- `from nautilus_trader.model.instruments import Instrument`


---

## Usage Examples

### Importing

```python
from nautilus_trader.persistence.catalog.types import CatalogDataResult
```


---

## Related Files

This file imports from the following modules:

- `from __future__ import annotations`
- `from dataclasses import dataclass`
- `from nautilus_trader.core.data import Data`
- `from nautilus_trader.model.identifiers import ClientId`
- `from nautilus_trader.model.instruments import Instrument`

**Directory:** `nautilus_trader/persistence/catalog`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


