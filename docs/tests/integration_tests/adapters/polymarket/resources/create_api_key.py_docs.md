# Documentation: create_api_key.py

## File Metadata

- **Path**: `tests/integration_tests/adapters/polymarket/resources/create_api_key.py`
- **Size**: 1,202 bytes
- **Lines**: 29
- **Language**: Python

## Original Source

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

import os

from py_clob_client.client import ClobClient
from py_clob_client.constants import POLYGON


def create_polymarket_api_key():
    host = "https://clob.polymarket.com"
    key = os.environ["POLYMARKET_PK"]
    chain_id = POLYGON
    client = ClobClient(host, key=key, chain_id=chain_id)

    print(client.create_api_key())

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`create_polymarket_api_key()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 4


**Functions**: `create_polymarket_api_key`
**Imports**: `os`, `py_clob_client.client`, `py_clob_client.constants`

## Related Files

This file is located in `tests/integration_tests/adapters/polymarket/resources/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/polymarket/resources/create_api_key.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:07.087091Z*
