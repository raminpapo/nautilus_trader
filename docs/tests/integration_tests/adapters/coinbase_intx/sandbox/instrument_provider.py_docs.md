# Documentation: instrument_provider.py

## File Metadata

- **Path**: `tests/integration_tests/adapters/coinbase_intx/sandbox/instrument_provider.py`
- **Size**: 1,917 bytes
- **Lines**: 48
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

import asyncio

from nautilus_trader.adapters.coinbase_intx.factories import get_coinbase_intx_http_client
from nautilus_trader.adapters.coinbase_intx.factories import get_coinbase_intx_instrument_provider
from nautilus_trader.common.component import init_logging
from nautilus_trader.common.config import InstrumentProviderConfig
from nautilus_trader.common.enums import LogLevel
from nautilus_trader.core import nautilus_pyo3


async def run():
    nautilus_pyo3.init_tracing()
    _guard = init_logging(level_stdout=LogLevel.TRACE)

    http_client = get_coinbase_intx_http_client()

    filters = {}

    # config = InstrumentProviderConfig(load_ids=frozenset(instrument_ids))
    config = InstrumentProviderConfig(load_all=True, filters=filters)
    provider = get_coinbase_intx_instrument_provider(http_client, config)

    await provider.initialize()

    for instrument in provider.list_all():
        print(repr(instrument))

    print(f"Loaded {len(provider.list_all())} instruments")


if __name__ == "__main__":
    asyncio.run(run())

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 6


**Imports**: `asyncio`, `nautilus_trader.adapters.coinbase_intx.factories`, `nautilus_trader.common.component`, `nautilus_trader.common.config`, `nautilus_trader.common.enums`, `nautilus_trader.core`

## Related Files

This file is located in `tests/integration_tests/adapters/coinbase_intx/sandbox/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/coinbase_intx/sandbox/instrument_provider.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.810880Z*
