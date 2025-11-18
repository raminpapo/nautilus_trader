# Documentation: __init__.py

## File Metadata

- **Path**: `nautilus_trader/__init__.py`
- **Size**: 1,569 bytes
- **Lines**: 34
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

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 3


**Imports**: `nautilus_trader.core`, `pathlib`, `typing`

## Related Files

This file is located in `nautilus_trader/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.401658Z*
