# Documentation: uuid.pyx

## File Metadata

- **Path**: `nautilus_trader/core/uuid.pyx`
- **Size**: 3,383 bytes
- **Lines**: 107
- **Language**: Unknown

## Original Source

```
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

import uuid

from nautilus_trader.core.correctness cimport Condition
from nautilus_trader.core.rust.core cimport UUID4_t
from nautilus_trader.core.rust.core cimport uuid4_eq
from nautilus_trader.core.rust.core cimport uuid4_from_cstr
from nautilus_trader.core.rust.core cimport uuid4_hash
from nautilus_trader.core.rust.core cimport uuid4_new
from nautilus_trader.core.rust.core cimport uuid4_to_cstr
from nautilus_trader.core.string cimport cstr_to_pystr
from nautilus_trader.core.string cimport pystr_to_cstr


cdef class UUID4:
    """
    Represents a Universally Unique Identifier (UUID)
    version 4 based on a 128-bit label as specified in RFC 4122.

    References
    ----------
    https://en.wikipedia.org/wiki/Universally_unique_identifier
    """

    def __init__(self):
        self._mem = uuid4_new()

    def __getstate__(self):
        return self.to_str()

    def __setstate__(self, state):
        self._mem = uuid4_from_cstr(pystr_to_cstr(state))

    def __eq__(self, UUID4 other) -> bool:
        if other is None:
            return False
        return uuid4_eq(&self._mem, &other._mem)

    def __hash__(self) -> int:
        return uuid4_hash(&self._mem)

    def __str__(self) -> str:
        return self.to_str()

    def __repr__(self) -> str:
        return f"{type(self).__name__}('{self}')"

    cdef str to_str(self):
        return cstr_to_pystr(uuid4_to_cstr(&self._mem), False)

    @property
    def value(self) -> str:
        return self.to_str()

    @staticmethod
    cdef UUID4 from_mem_c(UUID4_t mem):
        cdef UUID4 uuid4 = UUID4.__new__(UUID4)
        uuid4._mem = mem
        return uuid4

    @staticmethod
    cdef UUID4 from_str_c(str value):
        Condition.valid_string(value, "value")
        uuid_obj = uuid.UUID(value)
        Condition.is_true(uuid_obj.version == 4, "UUID value is not version 4")
        Condition.is_true(uuid_obj.variant == uuid.RFC_4122, "UUID value is not RFC 4122")

        cdef UUID4 uuid4 = UUID4.__new__(UUID4)
        uuid4._mem = uuid4_from_cstr(pystr_to_cstr(value))
        return uuid4

    @staticmethod
    def from_str(str value) -> UUID4:
        """
        Create a new UUID4 from the given string value.

        Parameters
        ----------
        value : str
            The UUID value.

        Returns
        -------
        UUID4

        Raises
        ------
        ValueError
            If `value` is not a valid UUID version 4 RFC 4122 string.

        """
        return UUID4.from_str_c(value)

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 42


**Identifiers**: `ANY`, `All`, `BASIS`, `CONDITIONS`, `Condition`, `Copyright`, `Create`, `False`, `GNU`, `General`, `Identifier`, `KIND`, `Lesser`, `License`, `Licensed`, `Ltd`, `Nautech`, `None`, `Parameters`, `Pty`, `Public`, `RFC`, `RFC_4122`, `Raises`, `References`, `Represents`, `Returns`, `See`, `Systems`, `The` *(+12 more)*

## Related Files

This file is located in `nautilus_trader/core/`. Related files may include:
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
*Generated on 2025-11-18T21:55:05.368740Z*
