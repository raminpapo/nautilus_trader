# Documentation: `nautilus_trader/indicators/base.pyx`
**Generated:** 2025-11-15T19:40:04.950497Z
**File Size:** 3029 bytes
**Extension:** .pyx
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

- **Path:** `nautilus_trader/indicators/base.pyx`
- **Size:** 3,029 bytes
- **Lines:** 78
- **Extension:** `.pyx`
- **Type:** text
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

from nautilus_trader.model.data cimport Bar
from nautilus_trader.model.data cimport QuoteTick
from nautilus_trader.model.data cimport TradeTick


cdef class Indicator:
    """
    The base class for all indicators.

    Parameters
    ----------
    params : list
        The initialization parameters for the indicator.

    Warnings
    --------
    This class should not be used directly, but through a concrete subclass.
    """

    def __init__(self, list params not None):
        self._params = params.copy()

        self.name = type(self).__name__
        self.has_inputs = False
        self.initialized = False

    def __repr__(self) -> str:
        return f"{self.name}({self._params_str()})"

    cdef str _params_str(self):
        return str(self._params)[1:-1].replace("'", '') if self._params else ''

    cpdef void handle_quote_tick(self, QuoteTick tick):
        """Abstract method (implement in subclass)."""
        raise NotImplementedError(f"Cannot handle {repr(tick)}: method `handle_quote_tick` not implemented in subclass")  # pragma: no cover

    cpdef void handle_trade_tick(self, TradeTick tick):
        """Abstract method (implement in subclass)."""
        raise NotImplementedError(f"Cannot handle {repr(tick)}: method `handle_trade_tick` not implemented in subclass")  # pragma: no cover

    cpdef void handle_bar(self, Bar bar):
        """Abstract method (implement in subclass)."""
        raise NotImplementedError(f"Cannot handle {repr(bar)}: method `handle_bar` not implemented in subclass")  # pragma: no cover

    cpdef void reset(self):
        """
        Reset the indicator.

        All stateful fields are reset to their initial value.
        """
        self._reset()
        self.has_inputs = False
        self.initialized = False

    cpdef void _set_has_inputs(self, bint setting):
        self.has_inputs = setting

    cpdef void _set_initialized(self, bint setting):
        self.initialized = setting

    cpdef void _reset(self):
        """Abstract method (implement in subclass)."""
        raise NotImplementedError("method `_reset` must be implemented in the subclass")  # pragma: no cover
```


---

## Overview

This file is located at `nautilus_trader/indicators/base.pyx` within the repository.

**Functions defined:** __init__, __repr__


---

## Detailed Analysis

### Functions

#### `__init__(self, list params not None)`


#### `__repr__(self)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `nautilus_trader/indicators`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


