# Documentation: `tests/unit_tests/core/test_inspect.py`
**Generated:** 2025-11-15T19:40:09.082738Z
**File Size:** 1755 bytes
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

- **Path:** `tests/unit_tests/core/test_inspect.py`
- **Size:** 1,755 bytes
- **Lines:** 40
- **Extension:** `.py`
- **Type:** text
- **Imports:** 8
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


---

## Overview

This file is located at `tests/unit_tests/core/test_inspect.py` within the repository.

**Functions defined:** test_is_nautilus_class

**Import statements:** 8


---

## Detailed Analysis

### Functions

#### `test_is_nautilus_class(cls, is_nautilus)`


### Imports

- `import pandas as pd`
- `import pytest`
- `from nautilus_trader.adapters.betfair.data_types import BetfairStartingPrice`
- `from nautilus_trader.adapters.betfair.data_types import BetfairTicker`
- `from nautilus_trader.core.inspect import is_nautilus_class`
- `from nautilus_trader.model.data import OrderBookDelta`
- `from nautilus_trader.model.data import TradeTick`
- `from nautilus_trader.model.events import OrderAccepted`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.core.test_inspect import test_is_nautilus_class
```


---

## Related Files

This file imports from the following modules:

- `import pandas as pd`
- `import pytest`
- `from nautilus_trader.adapters.betfair.data_types import BetfairStartingPrice`
- `from nautilus_trader.adapters.betfair.data_types import BetfairTicker`
- `from nautilus_trader.core.inspect import is_nautilus_class`
- `from nautilus_trader.model.data import OrderBookDelta`
- `from nautilus_trader.model.data import TradeTick`
- `from nautilus_trader.model.events import OrderAccepted`

**Directory:** `tests/unit_tests/core`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


