# Documentation: `nautilus_trader/adapters/bitmex/__init__.py`
**Generated:** 2025-11-15T19:40:04.164871Z
**File Size:** 2092 bytes
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

- **Path:** `nautilus_trader/adapters/bitmex/__init__.py`
- **Size:** 2,092 bytes
- **Lines:** 45
- **Extension:** `.py`
- **Type:** text
- **Imports:** 8

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
BitMEX cryptocurrency exchange integration adapter.

This subpackage provides an instrument provider, data and execution clients,
configurations, and constants for connecting to and interacting with BitMEX's API.

For convenience, the most commonly used symbols are re-exported at the
subpackage's top level, so downstream code can simply import from
``nautilus_trader.adapters.bitmex``.

"""
from nautilus_trader.adapters.bitmex.config import BitmexDataClientConfig
from nautilus_trader.adapters.bitmex.config import BitmexExecClientConfig
from nautilus_trader.adapters.bitmex.constants import BITMEX
from nautilus_trader.adapters.bitmex.constants import BITMEX_CLIENT_ID
from nautilus_trader.adapters.bitmex.constants import BITMEX_VENUE
from nautilus_trader.adapters.bitmex.factories import BitmexLiveDataClientFactory
from nautilus_trader.adapters.bitmex.factories import BitmexLiveExecClientFactory
from nautilus_trader.adapters.bitmex.providers import BitmexInstrumentProvider


__all__ = [
    "BITMEX",
    "BITMEX_CLIENT_ID",
    "BITMEX_VENUE",
    "BitmexDataClientConfig",
    "BitmexExecClientConfig",
    "BitmexInstrumentProvider",
    "BitmexLiveDataClientFactory",
    "BitmexLiveExecClientFactory",
]
```


---

## Overview

This file is located at `nautilus_trader/adapters/bitmex/__init__.py` within the repository.

This is a Python package initialization file that may expose package contents or execute initialization code.

**Import statements:** 8


---

## Detailed Analysis

### Imports

- `from nautilus_trader.adapters.bitmex.config import BitmexDataClientConfig`
- `from nautilus_trader.adapters.bitmex.config import BitmexExecClientConfig`
- `from nautilus_trader.adapters.bitmex.constants import BITMEX`
- `from nautilus_trader.adapters.bitmex.constants import BITMEX_CLIENT_ID`
- `from nautilus_trader.adapters.bitmex.constants import BITMEX_VENUE`
- `from nautilus_trader.adapters.bitmex.factories import BitmexLiveDataClientFactory`
- `from nautilus_trader.adapters.bitmex.factories import BitmexLiveExecClientFactory`
- `from nautilus_trader.adapters.bitmex.providers import BitmexInstrumentProvider`


---

## Usage Examples

### Importing

```python
import nautilus_trader.adapters.bitmex.__init__
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.adapters.bitmex.config import BitmexDataClientConfig`
- `from nautilus_trader.adapters.bitmex.config import BitmexExecClientConfig`
- `from nautilus_trader.adapters.bitmex.constants import BITMEX`
- `from nautilus_trader.adapters.bitmex.constants import BITMEX_CLIENT_ID`
- `from nautilus_trader.adapters.bitmex.constants import BITMEX_VENUE`
- `from nautilus_trader.adapters.bitmex.factories import BitmexLiveDataClientFactory`
- `from nautilus_trader.adapters.bitmex.factories import BitmexLiveExecClientFactory`
- `from nautilus_trader.adapters.bitmex.providers import BitmexInstrumentProvider`

**Directory:** `nautilus_trader/adapters/bitmex`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


