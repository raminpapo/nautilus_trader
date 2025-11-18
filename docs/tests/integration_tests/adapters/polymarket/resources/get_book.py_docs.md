# Documentation: get_book.py

## File Metadata

- **Path**: `tests/integration_tests/adapters/polymarket/resources/get_book.py`
- **Size**: 1,359 bytes
- **Lines**: 35
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`main()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 4


**Functions**: `main`
**Imports**: `msgspec`, `nautilus_trader.adapters.polymarket.factories`, `pathlib`

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
pytest tests/integration_tests/adapters/polymarket/resources/get_book.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:07.088366Z*
