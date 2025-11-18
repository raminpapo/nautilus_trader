# Documentation: active_markets.py

## File Metadata

- **Path**: `nautilus_trader/adapters/polymarket/scripts/active_markets.py`
- **Size**: 2,177 bytes
- **Lines**: 65
- **Language**: Python

## Original Source

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

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 4


**Imports**: `ast`, `asyncio`, `msgspec`, `nautilus_trader.core.nautilus_pyo3`

## Related Files

This file is located in `nautilus_trader/adapters/polymarket/scripts/`. Related files may include:
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

⚠️ **Security**: This file may handle sensitive data. Ensure proper encryption and access controls.

---
*Generated on 2025-11-18T21:55:04.977862Z*
