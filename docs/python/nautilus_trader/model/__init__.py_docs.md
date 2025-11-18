# Documentation: __init__.py

## File Metadata

- **Path**: `python/nautilus_trader/model/__init__.py`
- **Size**: 2,178 bytes
- **Lines**: 59
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

from nautilus_trader._libnautilus.model import *  # noqa: F403 (undefined-local-with-import-star)


try:  # pragma: no cover - optional extension may be absent
    from nautilus_trader._libnautilus.blockchain import Blockchain as _Blockchain
    from nautilus_trader._libnautilus.blockchain import Chain as _Chain
    from nautilus_trader._libnautilus.blockchain import Dex as _Dex  # type: ignore[attr-defined]
    from nautilus_trader._libnautilus.blockchain import DexType as _DexType
except ImportError:

    class _Blockchain:  # type: ignore[too-many-ancestors]
        ...

    class _Chain:  # type: ignore[too-many-ancestors]
        ...

    class _Dex:  # type: ignore[too-many-ancestors]
        ...

    class _DexType:  # type: ignore[too-many-ancestors]
        ...

else:
    Blockchain = _Blockchain
    Chain = _Chain
    Dex = _Dex
    DexType = _DexType


def _reassign_module_names() -> None:
    for _name, _obj in list(globals().items()):
        module = getattr(_obj, "__module__", "")
        if module.startswith("nautilus_trader.core.nautilus_pyo3.model"):
            try:
                _obj.__module__ = __name__
            except (AttributeError, TypeError):
                continue


_reassign_module_names()
del _reassign_module_names

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`_reassign_module_names()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Functions**: `_reassign_module_names`
**Imports**: `__future__`, `nautilus_trader._libnautilus.model`

## Related Files

This file is located in `python/nautilus_trader/model/`. Related files may include:
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
*Generated on 2025-11-18T21:55:06.082399Z*
