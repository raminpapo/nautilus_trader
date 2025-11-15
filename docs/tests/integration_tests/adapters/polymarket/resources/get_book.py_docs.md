# Documentation: `tests/integration_tests/adapters/polymarket/resources/get_book.py`
**Generated:** 2025-11-15T19:40:07.889097Z
**File Size:** 1359 bytes
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

- **Path:** `tests/integration_tests/adapters/polymarket/resources/get_book.py`
- **Size:** 1,359 bytes
- **Lines:** 34
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
    print("Requesting book")
    client = get_polymarket_http_client()
    token_id = 23360939988679364027624185518382759743328544433592111535569478055890815567848
    response = client.get_order_book(token_id)

    data = msgspec.json.encode(response)
    Path("http_responses/book.json").write_bytes(data)


if __name__ == "__main__":
    main()
```


---

## Overview

This file is located at `tests/integration_tests/adapters/polymarket/resources/get_book.py` within the repository.

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
from tests.integration_tests.adapters.polymarket.resources.get_book import main
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

**Security:** This file may contain sensitive patterns: token. Ensure proper handling of secrets.

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


