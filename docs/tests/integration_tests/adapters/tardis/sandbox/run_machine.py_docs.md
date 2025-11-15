# Documentation: `tests/integration_tests/adapters/tardis/sandbox/run_machine.py`
**Generated:** 2025-11-15T19:40:07.973486Z
**File Size:** 1869 bytes
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

- **Path:** `tests/integration_tests/adapters/tardis/sandbox/run_machine.py`
- **Size:** 1,869 bytes
- **Lines:** 52
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3

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

import asyncio
import json

import aiohttp


# Example taken from https://docs.tardis.dev/api/tardis-machine
# Run the following to start the tardis-machine server:
# docker run -p 8000:8000 -p 8001:8001 -e "TM_API_KEY=YOUR_API_KEY" -d tardisdev/tardis-machine


async def run():
    WS_REPLAY_URL = "ws://localhost:8001/ws-replay"
    URL = f"{WS_REPLAY_URL}?exchange=bitmex&from=2019-10-01&to=2019-10-02"

    async with aiohttp.ClientSession() as session, session.ws_connect(URL) as websocket:

        await websocket.send_str(
            json.dumps(
                {
                    "op": "subscribe",
                    "args": [
                        "trade:XBTUSD",
                        "trade:ETHUSD",
                        "orderBookL2:XBTUSD",
                        "orderBookL2:ETHUSD",
                    ],
                },
            ),
        )

        async for msg in websocket:
            print(msg.data)


if __name__ == "__main__":
    asyncio.run(run())
```


---

## Overview

This file is located at `tests/integration_tests/adapters/tardis/sandbox/run_machine.py` within the repository.

**Import statements:** 3


---

## Detailed Analysis

### Imports

- `import asyncio`
- `import json`
- `import aiohttp`


---

## Usage Examples

### Importing

```python
import tests.integration_tests.adapters.tardis.sandbox.run_machine
```


---

## Related Files

This file imports from the following modules:

- `import asyncio`
- `import json`
- `import aiohttp`

**Directory:** `tests/integration_tests/adapters/tardis/sandbox`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: api_key, session. Ensure proper handling of secrets.

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


