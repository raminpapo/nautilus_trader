# Documentation: `nautilus_trader/adapters/polymarket/scripts/create_api_key.py`
**Generated:** 2025-11-15T19:40:04.484393Z
**File Size:** 1243 bytes
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

- **Path:** `nautilus_trader/adapters/polymarket/scripts/create_api_key.py`
- **Size:** 1,243 bytes
- **Lines:** 32
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3

---

## Source Code

```python
#!/usr/bin/env python3
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

import os

from py_clob_client.client import ClobClient
from py_clob_client.constants import POLYGON


client = ClobClient(
    "https://clob.polymarket.com",
    chain_id=POLYGON,
    signature_type=0,
    key=os.environ["POLYMARKET_PK"],
    funder=os.environ["POLYMARKET_FUNDER"],
)

response = client.create_or_derive_api_creds()
print(response)
```


---

## Overview

This file is located at `nautilus_trader/adapters/polymarket/scripts/create_api_key.py` within the repository.

**Import statements:** 3


---

## Detailed Analysis

### Imports

- `import os`
- `from py_clob_client.client import ClobClient`
- `from py_clob_client.constants import POLYGON`


---

## Usage Examples

### Importing

```python
import nautilus_trader.adapters.polymarket.scripts.create_api_key
```


---

## Related Files

This file imports from the following modules:

- `import os`
- `from py_clob_client.client import ClobClient`
- `from py_clob_client.constants import POLYGON`

**Directory:** `nautilus_trader/adapters/polymarket/scripts`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


