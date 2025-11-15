# Documentation: `nautilus_trader/core/data.pyx`
**Generated:** 2025-11-15T19:40:04.722859Z
**File Size:** 2799 bytes
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

- **Path:** `nautilus_trader/core/data.pyx`
- **Size:** 2,799 bytes
- **Lines:** 91
- **Extension:** `.pyx`
- **Type:** text
- **Imports:** 1
- **Functions:** 4

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

import cython


@cython.auto_pickle(False)
cdef class Data:
    """
    The abstract base class for all data.

    Warnings
    --------
    This class should not be used directly, but through a concrete subclass.
    """

    @property
    def ts_event(self) -> int:
        """
        UNIX timestamp (nanoseconds) when the data event occurred.

        Returns
        -------
        int

        """
        raise NotImplementedError("abstract property must be implemented")

    @property
    def ts_init(self) -> int:
        """
        UNIX timestamp (nanoseconds) when the instance was created.

        Returns
        -------
        int

        """
        raise NotImplementedError("abstract property must be implemented")

    @classmethod
    def fully_qualified_name(cls) -> str:
        """
        Return the fully qualified name for the `Data` class.

        Returns
        -------
        str

        References
        ----------
        https://www.python.org/dev/peps/pep-3155/

        """
        return cls.__module__ + ':' + cls.__qualname__

    @classmethod
    def is_signal(cls, str name = "") -> bool:
        """
        Determine if the current class is a signal type, optionally checking for a specific signal name.

        Parameters
        ----------
        name : str, optional
            The specific signal name to check.
            If `name` not provided or if an empty string is passed, the method checks whether the
            class name indicates a general signal type.
            If `name` is provided, the method checks if the class name corresponds to that specific signal.

        Returns
        -------
        bool
            True if the class name matches the signal type or the specific signal name, otherwise False.

        """
        if name == "":
            return cls.__name__.startswith("Signal")

        return cls.__name__ == f"Signal{name.title()}"
```


---

## Overview

This file is located at `nautilus_trader/core/data.pyx` within the repository.

**Functions defined:** ts_event, ts_init, fully_qualified_name, is_signal

**Import statements:** 1


---

## Detailed Analysis

### Functions

#### `ts_event(self)`


#### `ts_init(self)`


#### `fully_qualified_name(cls)`


#### `is_signal(cls, str name = "")`


### Imports

- `import cython`


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

This file imports from the following modules:

- `import cython`

**Directory:** `nautilus_trader/core`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


