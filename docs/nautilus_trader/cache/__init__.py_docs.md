# Documentation: `nautilus_trader/cache/__init__.py`
**Generated:** 2025-11-15T19:40:04.607491Z
**File Size:** 1220 bytes
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

- **Path:** `nautilus_trader/cache/__init__.py`
- **Size:** 1,220 bytes
- **Lines:** 30
- **Extension:** `.py`
- **Type:** text
- **Imports:** 2

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
The `cache` subpackage provides common caching infrastructure.

A running Nautilus system generally uses a single centralized cache which can be
accessed by many components.

"""

from nautilus_trader.cache.cache import Cache
from nautilus_trader.cache.database import CacheDatabaseAdapter


__all__ = [
    "Cache",
    "CacheDatabaseAdapter",
]
```


---

## Overview

This file is located at `nautilus_trader/cache/__init__.py` within the repository.

This is a Python package initialization file that may expose package contents or execute initialization code.

**Import statements:** 2


---

## Detailed Analysis

### Imports

- `from nautilus_trader.cache.cache import Cache`
- `from nautilus_trader.cache.database import CacheDatabaseAdapter`


---

## Usage Examples

### Importing

```python
import nautilus_trader.cache.__init__
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.cache.cache import Cache`
- `from nautilus_trader.cache.database import CacheDatabaseAdapter`

**Directory:** `nautilus_trader/cache`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


