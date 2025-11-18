# Documentation: position_reports.py

## File Metadata

- **Path**: `tests/integration_tests/adapters/okx/sandbox/position_reports.py`
- **Size**: 3,852 bytes
- **Lines**: 93
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
"""
Sandbox script for requesting position reports from OKX.

This script uses the same HTTP endpoint as the execution client uses for requesting
position status reports.

"""

import asyncio

from nautilus_trader.common.component import Logger
from nautilus_trader.common.component import init_logging
from nautilus_trader.common.enums import LogLevel
from nautilus_trader.core import nautilus_pyo3


async def main():
    # Setup logging (to see Rust logs run `export RUST_LOG=debug,h2=off`)
    nautilus_pyo3.init_tracing()
    _guard = init_logging(level_stdout=LogLevel.TRACE)
    logger = Logger("okx-sandbox")

    # Setup client: we must cache all instruments we intend on using for requests
    http_client = nautilus_pyo3.OKXHttpClient.from_env()

    # Instrument type must match the product type you want to query
    okx_account_id = nautilus_pyo3.AccountId("OKX-master")
    okx_instrument_type = nautilus_pyo3.OKXInstrumentType.MARGIN

    # Request instruments and cache them
    instruments = await http_client.request_instruments(okx_instrument_type)
    logger.info(f"Received {len(instruments)} instruments")

    for inst in instruments:
        http_client.cache_instrument(inst)

    logger.info("Cached instruments for HTTP client")

    # Request position reports for the instrument type
    position_reports = await http_client.request_position_status_reports(
        account_id=okx_account_id,
        instrument_type=okx_instrument_type,
    )
    logger.info(f"Received {len(position_reports)} position reports")

    # Display details of each position
    for i, report in enumerate(position_reports, 1):
        logger.info(f"Position {i}/{len(position_reports)}:")
        logger.info(f"  instrument_id: {report.instrument_id}")
        logger.info(f"  position_side: {report.position_side}")
        logger.info(f"  quantity: {report.quantity}")
        logger.info(f"  avg_px_open: {report.avg_px_open}")

    # You can also query for a specific instrument
    if instruments:
        specific_instrument_id = instruments[0].id
        logger.info(f"Requesting position for specific instrument: {specific_instrument_id}")

        # For MARGIN, we need to pass the instrument_type explicitly
        if okx_instrument_type == nautilus_pyo3.OKXInstrumentType.MARGIN:
            specific_position_reports = await http_client.request_position_status_reports(
                account_id=okx_account_id,
                instrument_id=specific_instrument_id,
                instrument_type=okx_instrument_type,
            )
        else:
            specific_position_reports = await http_client.request_position_status_reports(
                account_id=okx_account_id,
                instrument_id=specific_instrument_id,
            )
        logger.info(
            f"Received {len(specific_position_reports)} position reports for {specific_instrument_id}",
        )


if __name__ == "__main__":
    asyncio.run(main())

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 4


**Imports**: `asyncio`, `nautilus_trader.common.component`, `nautilus_trader.common.enums`, `nautilus_trader.core`

## Related Files

This file is located in `tests/integration_tests/adapters/okx/sandbox/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/okx/sandbox/position_reports.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:07.069319Z*
