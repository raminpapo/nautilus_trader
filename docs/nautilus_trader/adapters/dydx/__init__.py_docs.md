# Documentation: `nautilus_trader/adapters/dydx/__init__.py`
**Generated:** 2025-11-15T19:40:04.237133Z
**File Size:** 2512 bytes
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

- **Path:** `nautilus_trader/adapters/dydx/__init__.py`
- **Size:** 2,512 bytes
- **Lines:** 53
- **Extension:** `.py`
- **Type:** text
- **Imports:** 12

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
The dYdX cryptocurrency decentralized exchange integration adapter.

This subpackage provides instrument provider, data and execution client configurations,
factories, and common constants/functions for connecting to and interacting with the
dYdX API.

For convenience, the most commonly used symbols are re-exported at the subpackage's
top level, so downstream code can simply import from ``nautilus_trader.adapters.dydx``.

"""
from nautilus_trader.adapters.dydx.common.common import DYDXOrderTags
from nautilus_trader.adapters.dydx.common.constants import DYDX
from nautilus_trader.adapters.dydx.common.constants import DYDX_CLIENT_ID
from nautilus_trader.adapters.dydx.common.constants import DYDX_VENUE
from nautilus_trader.adapters.dydx.config import DYDXDataClientConfig
from nautilus_trader.adapters.dydx.config import DYDXExecClientConfig
from nautilus_trader.adapters.dydx.factories import DYDXLiveDataClientFactory
from nautilus_trader.adapters.dydx.factories import DYDXLiveExecClientFactory
from nautilus_trader.adapters.dydx.factories import get_dydx_grcp_client
from nautilus_trader.adapters.dydx.factories import get_dydx_http_client
from nautilus_trader.adapters.dydx.factories import get_dydx_instrument_provider
from nautilus_trader.adapters.dydx.providers import DYDXInstrumentProvider


__all__ = [
    "DYDX",
    "DYDX_CLIENT_ID",
    "DYDX_VENUE",
    "DYDXDataClientConfig",
    "DYDXExecClientConfig",
    "DYDXInstrumentProvider",
    "DYDXLiveDataClientFactory",
    "DYDXLiveExecClientFactory",
    "DYDXOrderTags",
    "get_dydx_grcp_client",
    "get_dydx_http_client",
    "get_dydx_instrument_provider",
]
```


---

## Overview

This file is located at `nautilus_trader/adapters/dydx/__init__.py` within the repository.

This is a Python package initialization file that may expose package contents or execute initialization code.

**Import statements:** 12


---

## Detailed Analysis

### Imports

- `from nautilus_trader.adapters.dydx.common.common import DYDXOrderTags`
- `from nautilus_trader.adapters.dydx.common.constants import DYDX`
- `from nautilus_trader.adapters.dydx.common.constants import DYDX_CLIENT_ID`
- `from nautilus_trader.adapters.dydx.common.constants import DYDX_VENUE`
- `from nautilus_trader.adapters.dydx.config import DYDXDataClientConfig`
- `from nautilus_trader.adapters.dydx.config import DYDXExecClientConfig`
- `from nautilus_trader.adapters.dydx.factories import DYDXLiveDataClientFactory`
- `from nautilus_trader.adapters.dydx.factories import DYDXLiveExecClientFactory`
- `from nautilus_trader.adapters.dydx.factories import get_dydx_grcp_client`
- `from nautilus_trader.adapters.dydx.factories import get_dydx_http_client`
- `from nautilus_trader.adapters.dydx.factories import get_dydx_instrument_provider`
- `from nautilus_trader.adapters.dydx.providers import DYDXInstrumentProvider`


---

## Usage Examples

### Importing

```python
import nautilus_trader.adapters.dydx.__init__
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.adapters.dydx.common.common import DYDXOrderTags`
- `from nautilus_trader.adapters.dydx.common.constants import DYDX`
- `from nautilus_trader.adapters.dydx.common.constants import DYDX_CLIENT_ID`
- `from nautilus_trader.adapters.dydx.common.constants import DYDX_VENUE`
- `from nautilus_trader.adapters.dydx.config import DYDXDataClientConfig`
- `from nautilus_trader.adapters.dydx.config import DYDXExecClientConfig`
- `from nautilus_trader.adapters.dydx.factories import DYDXLiveDataClientFactory`
- `from nautilus_trader.adapters.dydx.factories import DYDXLiveExecClientFactory`
- `from nautilus_trader.adapters.dydx.factories import get_dydx_grcp_client`
- `from nautilus_trader.adapters.dydx.factories import get_dydx_http_client`

*... and 2 more*

**Directory:** `nautilus_trader/adapters/dydx`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


