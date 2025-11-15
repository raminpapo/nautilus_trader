# Documentation: `nautilus_trader/adapters/polymarket/scripts/active_markets.py`
**Generated:** 2025-11-15T19:40:04.483339Z
**File Size:** 2177 bytes
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

- **Path:** `nautilus_trader/adapters/polymarket/scripts/active_markets.py`
- **Size:** 2,177 bytes
- **Lines:** 64
- **Extension:** `.py`
- **Type:** text
- **Imports:** 4

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

import ast
import asyncio

import msgspec

from nautilus_trader.core.nautilus_pyo3 import HttpClient


async def main():
    params = {
        "active": "true",
        "closed": "false",
        "archived": "false",
        "limit": 5,
    }

    base_url = "https://gamma-api.polymarket.com/markets"

    client = HttpClient(timeout_secs=30)
    resp = await client.get(base_url, params=params)
    data = msgspec.json.decode(resp.body)

    for market in data:
        slug = market.get("slug", "")
        active = market.get("active", False)
        condition_id = market.get("conditionId", "N/A")
        clob_token_ids = market.get("clobTokenIds", "[]")

        if isinstance(clob_token_ids, str):
            try:
                clob_token_ids = ast.literal_eval(clob_token_ids)
            except Exception:
                clob_token_ids = []

        if not isinstance(clob_token_ids, list):
            clob_token_ids = []

        token_ids = ", ".join(clob_token_ids) if clob_token_ids else "N/A"

        print(f"Slug: {slug}")
        print(f"Active: {active}")
        print(f"Condition ID: {condition_id}")
        print(f"Token IDs: {token_ids}")
        print(f"Link: https://polymarket.com/event/{slug}\n")


if __name__ == "__main__":
    asyncio.run(main())
```


---

## Overview

This file is located at `nautilus_trader/adapters/polymarket/scripts/active_markets.py` within the repository.

**Import statements:** 4


---

## Detailed Analysis

### Imports

- `import ast`
- `import asyncio`
- `import msgspec`
- `from nautilus_trader.core.nautilus_pyo3 import HttpClient`


---

## Usage Examples

### Importing

```python
import nautilus_trader.adapters.polymarket.scripts.active_markets
```


---

## Related Files

This file imports from the following modules:

- `import ast`
- `import asyncio`
- `import msgspec`
- `from nautilus_trader.core.nautilus_pyo3 import HttpClient`

**Directory:** `nautilus_trader/adapters/polymarket/scripts`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: token. Ensure proper handling of secrets.


