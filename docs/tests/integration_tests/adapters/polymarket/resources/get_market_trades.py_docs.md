# Documentation: `tests/integration_tests/adapters/polymarket/resources/get_market_trades.py`
**Generated:** 2025-11-15T19:40:07.891203Z
**File Size:** 1420 bytes
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

- **Path:** `tests/integration_tests/adapters/polymarket/resources/get_market_trades.py`
- **Size:** 1,420 bytes
- **Lines:** 36
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3
- **Functions:** 1

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

from pathlib import Path

import msgspec

from nautilus_trader.adapters.polymarket.factories import get_polymarket_http_client


def main():
    print("Requesting trades")
    client = get_polymarket_http_client()

    # Trump Election 2024 Winner market
    condition_id = "0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917"
    response = client.get_market_trades_events(condition_id)

    data = msgspec.json.encode(response)
    Path("http_responses/market_trades.json").write_bytes(data)


if __name__ == "__main__":
    main()
```


---

## Overview

This file is located at `tests/integration_tests/adapters/polymarket/resources/get_market_trades.py` within the repository.

**Functions defined:** main

**Import statements:** 3


---

## Detailed Analysis

### Functions

#### `main()`


### Imports

- `from pathlib import Path`
- `import msgspec`
- `from nautilus_trader.adapters.polymarket.factories import get_polymarket_http_client`


---

## Usage Examples

### Importing

```python
from tests.integration_tests.adapters.polymarket.resources.get_market_trades import main
```


---

## Related Files

This file imports from the following modules:

- `from pathlib import Path`
- `import msgspec`
- `from nautilus_trader.adapters.polymarket.factories import get_polymarket_http_client`

**Directory:** `tests/integration_tests/adapters/polymarket/resources`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


