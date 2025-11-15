# Documentation: `tests/integration_tests/adapters/tardis/sandbox/run_replay.py`
**Generated:** 2025-11-15T19:40:07.974913Z
**File Size:** 2147 bytes
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

- **Path:** `tests/integration_tests/adapters/tardis/sandbox/run_replay.py`
- **Size:** 2,147 bytes
- **Lines:** 62
- **Extension:** `.py`
- **Type:** text
- **Imports:** 5

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


---

## Overview

This file is located at `tests/integration_tests/adapters/tardis/sandbox/run_replay.py` within the repository.

**Import statements:** 5


---

## Detailed Analysis

### Imports

- `from __future__ import annotations`
- `import asyncio`
- `from pathlib import Path`
- `from nautilus_trader import PACKAGE_ROOT`
- `from nautilus_trader.core import nautilus_pyo3`


---

## Usage Examples

### Importing

```python
import tests.integration_tests.adapters.tardis.sandbox.run_replay
```


---

## Related Files

This file imports from the following modules:

- `from __future__ import annotations`
- `import asyncio`
- `from pathlib import Path`
- `from nautilus_trader import PACKAGE_ROOT`
- `from nautilus_trader.core import nautilus_pyo3`

**Directory:** `tests/integration_tests/adapters/tardis/sandbox`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: api_key. Ensure proper handling of secrets.

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


