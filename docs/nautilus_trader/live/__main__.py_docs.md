# Documentation: `nautilus_trader/live/__main__.py`
**Generated:** 2025-11-15T19:40:04.978087Z
**File Size:** 1861 bytes
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

- **Path:** `nautilus_trader/live/__main__.py`
- **Size:** 1,861 bytes
- **Lines:** 49
- **Extension:** `.py`
- **Type:** text
- **Imports:** 5
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

import click
import fsspec
import msgspec

from nautilus_trader.config import TradingNodeConfig
from nautilus_trader.live.node import TradingNode


@click.command()
@click.option("--raw", help="A raw string config")
@click.option("--fsspec-url", help="A fsspec url to read config from")
@click.option("--start", default=True, help="Start the live node")
def main(
    raw: str | None = None,
    fsspec_url: str | None = None,
    start: bool = True,
) -> None:
    assert raw is not None or fsspec_url is not None, "Must pass one of `raw` or `fsspec_url`"
    if fsspec_url and raw is None:
        with fsspec.open(fsspec_url, "rb") as f:
            raw = f.read().decode()
    assert raw is not None  # Type checking
    config: TradingNodeConfig = msgspec.json.decode(raw, type=TradingNodeConfig)
    node = TradingNode(config=config)
    node.build()
    if start:
        try:
            node.run()
        finally:
            node.dispose()


if __name__ == "__main__":
    main()
```


---

## Overview

This file is located at `nautilus_trader/live/__main__.py` within the repository.

**Functions defined:** main

**Import statements:** 5


---

## Detailed Analysis

### Functions

#### `main(
    raw: str | None = None,
    fsspec_url: str | None = None,
    start: bool = True,
)`


### Imports

- `import click`
- `import fsspec`
- `import msgspec`
- `from nautilus_trader.config import TradingNodeConfig`
- `from nautilus_trader.live.node import TradingNode`


---

## Usage Examples

### Importing

```python
from nautilus_trader.live.__main__ import main
```


---

## Related Files

This file imports from the following modules:

- `import click`
- `import fsspec`
- `import msgspec`
- `from nautilus_trader.config import TradingNodeConfig`
- `from nautilus_trader.live.node import TradingNode`

**Directory:** `nautilus_trader/live`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


