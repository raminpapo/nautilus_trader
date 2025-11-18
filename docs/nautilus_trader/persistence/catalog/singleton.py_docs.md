# Documentation: singleton.py

## File Metadata

- **Path**: `nautilus_trader/persistence/catalog/singleton.py`
- **Size**: 2,073 bytes
- **Lines**: 60
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

from __future__ import annotations

import inspect
from typing import Any


class Singleton(type):
    """
    The base class to ensure a singleton.
    """

    def __init__(cls, name, bases, dict_like):
        super().__init__(name, bases, dict_like)
        cls._instances = {}

    def __call__(cls, *args, **kw):
        full_kwargs = resolve_kwargs(cls.__init__, None, *args, **kw)
        if full_kwargs == {"self": None, "args": (), "kwargs": {}}:
            full_kwargs = {}
        full_kwargs.pop("self", None)
        key = tuple(full_kwargs.items())
        if key not in cls._instances:
            cls._instances[key] = super().__call__(*args, **kw)
        return cls._instances[key]


def clear_singleton_instances(cls: type) -> None:
    assert isinstance(cls, Singleton)
    cls._instances = {}


def resolve_kwargs(func, *args, **kwargs):
    kw = inspect.getcallargs(func, *args, **kwargs)
    return {k: check_value(v) for k, v in kw.items()}


def check_value(v: Any) -> Any:
    if isinstance(v, dict):
        return freeze_dict(dict_like=v)
    return v


def freeze_dict(dict_like: dict) -> tuple:
    return tuple(sorted((k, check_value(v)) for k, v in dict_like.items()))

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 4 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`clear_singleton_instances()`**: Function defined in this file
- **`resolve_kwargs()`**: Function defined in this file
- **`check_value()`**: Function defined in this file
- **`freeze_dict()`**: Function defined in this file

### Classes
- **`Singleton`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 8


**Classs**: `Singleton`
**Functions**: `check_value`, `clear_singleton_instances`, `freeze_dict`, `resolve_kwargs`
**Imports**: `__future__`, `inspect`, `typing`

## Related Files

This file is located in `nautilus_trader/persistence/catalog/`. Related files may include:
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
*Generated on 2025-11-18T21:55:05.861539Z*
