# Documentation: test_inspect.py

## File Metadata

- **Path**: `tests/unit_tests/core/test_inspect.py`
- **Size**: 1,755 bytes
- **Lines**: 41
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

import pandas as pd
import pytest

from nautilus_trader.adapters.betfair.data_types import BetfairStartingPrice
from nautilus_trader.adapters.betfair.data_types import BetfairTicker
from nautilus_trader.core.inspect import is_nautilus_class
from nautilus_trader.model.data import OrderBookDelta
from nautilus_trader.model.data import TradeTick
from nautilus_trader.model.events import OrderAccepted


@pytest.mark.parametrize(
    ("cls", "is_nautilus"),
    [
        (OrderBookDelta, True),
        (TradeTick, True),
        (OrderAccepted, True),
        (BetfairStartingPrice, False),  # BetfairStartingPrice is an adapter specific type
        (BetfairTicker, False),  # BetfairTicker is an adapter specific type
        (pd.DataFrame, False),
    ],
)
def test_is_nautilus_class(cls, is_nautilus):
    # Arrange, Act, Assert
    assert is_nautilus_class(cls=cls) is is_nautilus

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`test_is_nautilus_class()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 7


**Functions**: `test_is_nautilus_class`
**Imports**: `nautilus_trader.adapters.betfair.data_types`, `nautilus_trader.core.inspect`, `nautilus_trader.model.data`, `nautilus_trader.model.events`, `pandas`, `pytest`

## Related Files

This file is located in `tests/unit_tests/core/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/unit_tests/core/test_inspect.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:11.314498Z*
