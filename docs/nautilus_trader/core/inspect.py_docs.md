# Documentation: `nautilus_trader/core/inspect.py`
**Generated:** 2025-11-15T19:40:04.762180Z
**File Size:** 2722 bytes
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

- **Path:** `nautilus_trader/core/inspect.py`
- **Size:** 2,722 bytes
- **Lines:** 76
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3
- **Functions:** 2

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

import gc
import sys
from typing import Any


def is_nautilus_class(cls: type) -> bool:
    """
    Determine whether a class is a builtin nautilus type.
    """
    if cls.__module__.startswith("nautilus_trader.core.nautilus_pyo3.model"):
        return True
    if cls.__module__.startswith("nautilus_trader.model.greeks"):
        return False
    if cls.__module__.startswith("nautilus_trader.model"):
        return True
    if cls.__module__.startswith("nautilus_trader.common"):
        # Custom user signals return False, everything else returns True
        return not cls.__name__.startswith("Signal")
    if cls.__module__.startswith("nautilus_trader.test_kit"):
        return False
    return bool(any(base.__module__.startswith("nautilus_trader.model") for base in cls.__bases__))


def get_size_of(obj: Any) -> int:
    """
    Return the bytes size in memory of the given object.

    Parameters
    ----------
    obj : object
        The object to analyze.

    Returns
    -------
    int

    """
    marked: set = {id(obj)}
    obj_q = [obj]
    size = 0

    while obj_q:
        size += sum(map(sys.getsizeof, obj_q))

        # Lookup all the object referred to by the object in obj_q.
        # See: https://docs.python.org/3.7/library/gc.html#gc.get_referents
        all_refs = [(id(o), o) for o in gc.get_referents(*obj_q)]

        # Filter object that are already marked.
        # Using dict notation will prevent repeated objects.
        new_ref = {
            o_id: o for o_id, o in all_refs if o_id not in marked and not isinstance(o, type)
        }

        # The new obj_q will be the ones that were not marked,
        # and we will update marked with their ids so we will
        # not traverse them again.
        obj_q = new_ref.values()  # type: ignore
        marked.update(new_ref.keys())

    return size
```


---

## Overview

This file is located at `nautilus_trader/core/inspect.py` within the repository.

**Functions defined:** is_nautilus_class, get_size_of

**Import statements:** 3


---

## Detailed Analysis

### Functions

#### `is_nautilus_class(cls: type)`


#### `get_size_of(obj: Any)`


### Imports

- `import gc`
- `import sys`
- `from typing import Any`


---

## Usage Examples

### Importing

```python
from nautilus_trader.core.inspect import is_nautilus_class
```


---

## Related Files

This file imports from the following modules:

- `import gc`
- `import sys`
- `from typing import Any`

**Directory:** `nautilus_trader/core`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


