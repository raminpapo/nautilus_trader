# Documentation: `nautilus_trader/adapters/databento/constants.py`
**Generated:** 2025-11-15T19:40:04.219144Z
**File Size:** 1214 bytes
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

- **Path:** `nautilus_trader/adapters/databento/constants.py`
- **Size:** 1,214 bytes
- **Lines:** 27
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3

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

from pathlib import Path
from typing import Final

from nautilus_trader.model.identifiers import ClientId


DATABENTO: Final[str] = "DATABENTO"
DATABENTO_CLIENT_ID: Final[ClientId] = ClientId(DATABENTO)

ALL_SYMBOLS: Final[str] = "ALL_SYMBOLS"

PUBLISHERS_FILEPATH: Final[Path] = (Path(__file__).resolve().parent / "publishers.json").resolve()
```


---

## Overview

This file is located at `nautilus_trader/adapters/databento/constants.py` within the repository.

**Import statements:** 3


---

## Detailed Analysis

### Imports

- `from pathlib import Path`
- `from typing import Final`
- `from nautilus_trader.model.identifiers import ClientId`


---

## Usage Examples

### Importing

```python
import nautilus_trader.adapters.databento.constants
```


---

## Related Files

This file imports from the following modules:

- `from pathlib import Path`
- `from typing import Final`
- `from nautilus_trader.model.identifiers import ClientId`

**Directory:** `nautilus_trader/adapters/databento`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


