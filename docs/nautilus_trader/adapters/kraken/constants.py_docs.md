# Documentation: `nautilus_trader/adapters/kraken/constants.py`
**Generated:** 2025-11-15T19:40:04.406289Z
**File Size:** 1131 bytes
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

- **Path:** `nautilus_trader/adapters/kraken/constants.py`
- **Size:** 1,131 bytes
- **Lines:** 24
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

from typing import Final

from nautilus_trader.model.identifiers import ClientId
from nautilus_trader.model.identifiers import Venue


KRAKEN: Final[str] = "KRAKEN"
KRAKEN_VENUE: Final[Venue] = Venue(KRAKEN)
KRAKEN_CLIENT_ID: Final[ClientId] = ClientId(KRAKEN)
```


---

## Overview

This file is located at `nautilus_trader/adapters/kraken/constants.py` within the repository.

**Import statements:** 3


---

## Detailed Analysis

### Imports

- `from typing import Final`
- `from nautilus_trader.model.identifiers import ClientId`
- `from nautilus_trader.model.identifiers import Venue`


---

## Usage Examples

### Importing

```python
import nautilus_trader.adapters.kraken.constants
```


---

## Related Files

This file imports from the following modules:

- `from typing import Final`
- `from nautilus_trader.model.identifiers import ClientId`
- `from nautilus_trader.model.identifiers import Venue`

**Directory:** `nautilus_trader/adapters/kraken`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


