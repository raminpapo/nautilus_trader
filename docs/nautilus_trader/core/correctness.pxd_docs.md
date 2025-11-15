# Documentation: `nautilus_trader/core/correctness.pxd`
**Generated:** 2025-11-15T19:40:04.716104Z
**File Size:** 3625 bytes
**Extension:** .pxd
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

- **Path:** `nautilus_trader/core/correctness.pxd`
- **Size:** 3,625 bytes
- **Lines:** 150
- **Extension:** `.pxd`
- **Type:** text

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


cdef inline Exception make_exception(ex_default, ex_type, str msg):
    if type(ex_type) is type(Exception):
        return ex_type(msg)
    else:
        return ex_default(msg)


cdef class Condition:

    @staticmethod
    cdef void is_true(bint predicate, str fail_msg, ex_type=*)

    @staticmethod
    cdef void is_false(bint predicate, str fail_msg, ex_type=*)

    @staticmethod
    cdef void none(object argument, str param, ex_type=*)

    @staticmethod
    cdef void not_none(object argument, str param, ex_type=*)

    @staticmethod
    cdef void type(
        object argument,
        object expected,
        str param,
        ex_type=*,
    )

    @staticmethod
    cdef void type_or_none(
        object argument,
        object expected,
        str param,
        ex_type=*,
    )

    @staticmethod
    cdef void callable(object argument, str param, ex_type=*)

    @staticmethod
    cdef void callable_or_none(object argument, str param, ex_type=*)

    @staticmethod
    cdef void equal(
        object argument1,
        object argument2,
        str param1,
        str param2,
        ex_type=*,
    )

    @staticmethod
    cdef void not_equal(
        object argument1,
        object argument2,
        str param1,
        str param2,
        ex_type=*,
    )

    @staticmethod
    cdef void list_type(
        list argument,
        type expected_type,
        str param,
        ex_type=*,
    )

    @staticmethod
    cdef void dict_types(
        dict argument,
        type key_type,
        type value_type,
        str param,
        ex_type=*,
    )

    @staticmethod
    cdef void is_in(
        object element,
        object collection,
        str param1,
        str param2,
        ex_type=*,
    )

    @staticmethod
    cdef void not_in(
        object element,
        object collection,
        str param1,
        str param2,
        ex_type=*,
    )

    @staticmethod
    cdef void empty(object collection, str param, ex_type=*)

    @staticmethod
    cdef void not_empty(object collection, str param, ex_type=*)

    @staticmethod
    cdef void positive(double value, str param, ex_type=*)

    @staticmethod
    cdef void positive_int(value: int, str param, ex_type=*)

    @staticmethod
    cdef void not_negative(double value, str param, ex_type=*)

    @staticmethod
    cdef void not_negative_int(value: int, str param, ex_type=*)

    @staticmethod
    cdef void in_range(
        double value,
        double start,
        double end,
        str param,
        ex_type=*,
    )

    @staticmethod
    cdef void in_range_int(
        value,
        start,
        end,
        str param,
        ex_type=*,
    )

    @staticmethod
    cdef void valid_string(str argument, str param, ex_type=*)
```


---

## Overview

This file is located at `nautilus_trader/core/correctness.pxd` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `nautilus_trader/core`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


