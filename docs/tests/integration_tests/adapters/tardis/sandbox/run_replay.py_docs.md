# Documentation: run_replay.py

## File Metadata

- **Path**: `tests/integration_tests/adapters/tardis/sandbox/run_replay.py`
- **Size**: 2,147 bytes
- **Lines**: 63
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
"""
Utility script to launch a local Tardis-Machine replay from Python.

The location of the example JSON configuration file changed when the Rust
crates were moved out of the Python package directory in April-2025.  The
script now references the new path directly (``crates/adapters/tardis/bin``).

To start a server first run (example):

    docker run -p 8000:8000 -p 8001:8001 \
        -e "TM_API_KEY=YOUR_API_KEY" \
        -d tardisdev/tardis-machine

Then execute this file:

    python tests/integration_tests/adapters/tardis/sandbox/run_replay.py

Export ``RUST_LOG=debug`` if you want verbose logging from the Rust side.

"""

from __future__ import annotations

import asyncio
from pathlib import Path

from nautilus_trader import PACKAGE_ROOT
from nautilus_trader.core import nautilus_pyo3


async def run() -> None:
    config_filepath: Path = (
        PACKAGE_ROOT  # project root
        / "crates"
        / "adapters"
        / "tardis"
        / "bin"
        / "example_config.json"
    ).resolve()

    if not config_filepath.is_file():
        raise FileNotFoundError(f"Unable to locate example_config.json at {config_filepath}")

    await nautilus_pyo3.run_tardis_machine_replay(str(config_filepath))


if __name__ == "__main__":
    asyncio.run(run())

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 5


**Imports**: `__future__`, `asyncio`, `nautilus_trader`, `nautilus_trader.core`, `pathlib`

## Related Files

This file is located in `tests/integration_tests/adapters/tardis/sandbox/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/tardis/sandbox/run_replay.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:07.209724Z*
