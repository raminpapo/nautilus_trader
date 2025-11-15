# Documentation: `nautilus_trader/adapters/_template/providers.py`
**Generated:** 2025-11-15T19:40:04.015215Z
**File Size:** 2592 bytes
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

- **Path:** `nautilus_trader/adapters/_template/providers.py`
- **Size:** 2,592 bytes
- **Lines:** 61
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

from nautilus_trader.common.providers import InstrumentProvider
from nautilus_trader.model.identifiers import InstrumentId


# The 'pragma: no cover' comment excludes a method from test coverage.
# https://coverage.readthedocs.io/en/coverage-4.3.3/excluding.html
# The reason for their use is to reduce redundant/needless tests which simply
# assert that a `NotImplementedError` is raised when calling abstract methods.
# These tests are expensive to maintain (as they must be kept in line with any
# refactorings), and offer little to no benefit in return. The intention
# is for all method implementations to be fully covered by tests.

# *** THESE PRAGMA: NO COVER COMMENTS MUST BE REMOVED IN ANY IMPLEMENTATION. ***


class TemplateInstrumentProvider(InstrumentProvider):
    """
    An example template of an ``InstrumentProvider`` showing the minimal methods which
    must be implemented for an integration to be complete.
    """

    async def load_all_async(
        self,
        filters: dict | None = None,
    ) -> None:
        raise NotImplementedError(
            "method `load_all_async` must be implemented in the subclass",
        )  # pragma: no cover

    async def load_ids_async(
        self,
        instrument_ids: list[InstrumentId],
        filters: dict | None = None,
    ) -> None:
        raise NotImplementedError(
            "method `load_ids_async` must be implemented in the subclass",
        )  # pragma: no cover

    async def load_async(
        self,
        instrument_id: InstrumentId,
        filters: dict | None = None,
    ) -> None:
        raise NotImplementedError(
            "method `load_async` must be implemented in the subclass",
        )  # pragma: no cover
```


---

## Overview

This file is located at `nautilus_trader/adapters/_template/providers.py` within the repository.

**Classes defined:** TemplateInstrumentProvider

**Import statements:** 2


---

## Detailed Analysis

### Classes

#### `TemplateInstrumentProvider`

**Inherits from:** InstrumentProvider


### Imports

- `from nautilus_trader.common.providers import InstrumentProvider`
- `from nautilus_trader.model.identifiers import InstrumentId`


---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters._template.providers import TemplateInstrumentProvider
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.common.providers import InstrumentProvider`
- `from nautilus_trader.model.identifiers import InstrumentId`

**Directory:** `nautilus_trader/adapters/_template`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


