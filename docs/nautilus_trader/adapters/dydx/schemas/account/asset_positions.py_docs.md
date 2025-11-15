# Documentation: `nautilus_trader/adapters/dydx/schemas/account/asset_positions.py`
**Generated:** 2025-11-15T19:40:04.306752Z
**File Size:** 1227 bytes
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

- **Path:** `nautilus_trader/adapters/dydx/schemas/account/asset_positions.py`
- **Size:** 1,227 bytes
- **Lines:** 30
- **Extension:** `.py`
- **Type:** text
- **Imports:** 2
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
"""
Define the schemas for the GetAssetPositions endpoint.
"""


import msgspec

from nautilus_trader.adapters.dydx.schemas.account.address import DYDXAssetPosition


class DYDXAssetPositionsResponse(msgspec.Struct, forbid_unknown_fields=False):
    """
    Define the schema for the asset positions response.
    """

    positions: list[DYDXAssetPosition]
```


---

## Overview

This file is located at `nautilus_trader/adapters/dydx/schemas/account/asset_positions.py` within the repository.

**Classes defined:** DYDXAssetPositionsResponse

**Import statements:** 2


---

## Detailed Analysis

### Classes

#### `DYDXAssetPositionsResponse`

**Inherits from:** msgspec.Struct, forbid_unknown_fields=False


### Imports

- `import msgspec`
- `from nautilus_trader.adapters.dydx.schemas.account.address import DYDXAssetPosition`


---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters.dydx.schemas.account.asset_positions import DYDXAssetPositionsResponse
```


---

## Related Files

This file imports from the following modules:

- `import msgspec`
- `from nautilus_trader.adapters.dydx.schemas.account.address import DYDXAssetPosition`

**Directory:** `nautilus_trader/adapters/dydx/schemas/account`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


