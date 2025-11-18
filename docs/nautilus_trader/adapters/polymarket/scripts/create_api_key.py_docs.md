# Documentation: create_api_key.py

## File Metadata

- **Path**: `nautilus_trader/adapters/polymarket/scripts/create_api_key.py`
- **Size**: 1,243 bytes
- **Lines**: 33
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

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 3


**Imports**: `os`, `py_clob_client.client`, `py_clob_client.constants`

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

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:04.979713Z*
