# Documentation: `python/nautilus_trader/adapters/blockchain/__init__.py`
**Generated:** 2025-11-15T19:40:05.431165Z
**File Size:** 1412 bytes
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

- **Path:** `python/nautilus_trader/adapters/blockchain/__init__.py`
- **Size:** 1,412 bytes
- **Lines:** 32
- **Extension:** `.py`
- **Type:** text
- **Imports:** 2
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

from __future__ import annotations

from nautilus_trader._libnautilus.blockchain import *  # noqa: F403 (undefined-local-with-import-star)


def _reassign_module_names() -> None:
    for _name, _obj in list(globals().items()):
        module = getattr(_obj, "__module__", "")
        if module.startswith("nautilus_trader.core.nautilus_pyo3.blockchain"):
            try:
                _obj.__module__ = __name__
            except (AttributeError, TypeError):
                continue


_reassign_module_names()
del _reassign_module_names
```


---

## Overview

This file is located at `python/nautilus_trader/adapters/blockchain/__init__.py` within the repository.

This is a Python package initialization file that may expose package contents or execute initialization code.

**Functions defined:** _reassign_module_names

**Import statements:** 2


---

## Detailed Analysis

### Functions

#### `_reassign_module_names()`


### Imports

- `from __future__ import annotations`
- `from nautilus_trader._libnautilus.blockchain import *  # noqa: F403 (undefined-local-with-import-star)`


---

## Usage Examples

### Importing

```python
from python.nautilus_trader.adapters.blockchain.__init__ import _reassign_module_names
```


---

## Related Files

This file imports from the following modules:

- `from __future__ import annotations`
- `from nautilus_trader._libnautilus.blockchain import *  # noqa: F403 (undefined-local-with-import-star)`

**Directory:** `python/nautilus_trader/adapters/blockchain`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


