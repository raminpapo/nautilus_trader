# Documentation: `nautilus_trader/__init__.py`
**Generated:** 2025-11-15T19:40:03.973912Z
**File Size:** 1569 bytes
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

- **Path:** `nautilus_trader/__init__.py`
- **Size:** 1,569 bytes
- **Lines:** 33
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3

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
NautilusTrader (http://nautilustrader.io) is an open-source, high-performance, production-grade
algorithmic trading platform, providing quantitative traders with the ability to backtest
portfolios of automated trading strategies on historical data with an event-driven engine,
and also deploy those same strategies live, with no code changes.
"""

from pathlib import Path
from typing import Final

from nautilus_trader.core import nautilus_pyo3


__version__ = nautilus_pyo3.NAUTILUS_VERSION

PACKAGE_ROOT: Final[Path] = Path(__file__).resolve().parent.parent
TEST_DATA_DIR: Final[Path] = PACKAGE_ROOT / "tests" / "test_data"

NAUTILUS_USER_AGENT: Final[str] = nautilus_pyo3.NAUTILUS_USER_AGENT
```


---

## Overview

This file is located at `nautilus_trader/__init__.py` within the repository.

This is a Python package initialization file that may expose package contents or execute initialization code.

**Import statements:** 3


---

## Detailed Analysis

### Imports

- `from pathlib import Path`
- `from typing import Final`
- `from nautilus_trader.core import nautilus_pyo3`


---

## Usage Examples

### Importing

```python
import nautilus_trader.__init__
```


---

## Related Files

This file imports from the following modules:

- `from pathlib import Path`
- `from typing import Final`
- `from nautilus_trader.core import nautilus_pyo3`

**Directory:** `nautilus_trader`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


