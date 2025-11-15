# Documentation: `tests/integration_tests/adapters/polymarket/test_symbol.py`
**Generated:** 2025-11-15T19:40:07.953266Z
**File Size:** 4393 bytes
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

- **Path:** `tests/integration_tests/adapters/polymarket/test_symbol.py`
- **Size:** 4,393 bytes
- **Lines:** 87
- **Extension:** `.py`
- **Type:** text
- **Imports:** 6
- **Classes:** 1
- **Functions:** 9

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

import pytest

from nautilus_trader.adapters.polymarket.common.constants import POLYMARKET_VENUE
from nautilus_trader.adapters.polymarket.common.symbol import get_polymarket_condition_id
from nautilus_trader.adapters.polymarket.common.symbol import get_polymarket_instrument_id
from nautilus_trader.adapters.polymarket.common.symbol import get_polymarket_token_id
from nautilus_trader.model.identifiers import InstrumentId


class TestPolymarketSymbol:
    def test_get_polymarket_instrument_id(self):
        condition_id = "0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917"
        token_id = "21742633143463906290569050155826241533067272736897614950488156847949938836455"

        result = get_polymarket_instrument_id(condition_id, token_id)

        expected = InstrumentId.from_str(f"{condition_id}-{token_id}.{POLYMARKET_VENUE}")
        assert result == expected

    def test_get_polymarket_condition_id_valid(self):
        condition_id = "0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917"
        token_id = "21742633143463906290569050155826241533067272736897614950488156847949938836455"
        instrument_id = get_polymarket_instrument_id(condition_id, token_id)

        result = get_polymarket_condition_id(instrument_id)

        assert result == condition_id

    def test_get_polymarket_token_id_valid(self):
        condition_id = "0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917"
        token_id = "21742633143463906290569050155826241533067272736897614950488156847949938836455"
        instrument_id = get_polymarket_instrument_id(condition_id, token_id)

        result = get_polymarket_token_id(instrument_id)

        assert result == token_id

    def test_get_polymarket_condition_id_no_dash_raises_error(self):
        instrument_id = InstrumentId.from_str(f"invalid_no_dash.{POLYMARKET_VENUE}")

        with pytest.raises(ValueError, match="Invalid Polymarket instrument ID format"):
            get_polymarket_condition_id(instrument_id)

    def test_get_polymarket_token_id_no_dash_raises_error(self):
        instrument_id = InstrumentId.from_str(f"invalid_no_dash.{POLYMARKET_VENUE}")

        with pytest.raises(ValueError, match="Invalid Polymarket instrument ID format"):
            get_polymarket_token_id(instrument_id)

    def test_get_polymarket_condition_id_too_many_dashes_raises_error(self):
        instrument_id = InstrumentId.from_str(f"too-many-dashes.{POLYMARKET_VENUE}")

        with pytest.raises(ValueError, match="Invalid Polymarket instrument ID format"):
            get_polymarket_condition_id(instrument_id)

    def test_get_polymarket_token_id_too_many_dashes_raises_error(self):
        instrument_id = InstrumentId.from_str(f"too-many-dashes.{POLYMARKET_VENUE}")

        with pytest.raises(ValueError, match="Invalid Polymarket instrument ID format"):
            get_polymarket_token_id(instrument_id)

    def test_get_polymarket_condition_id_missing_condition_raises_error(self):
        instrument_id = InstrumentId.from_str(f"-token_id.{POLYMARKET_VENUE}")

        with pytest.raises(ValueError, match="Invalid Polymarket instrument ID format"):
            get_polymarket_condition_id(instrument_id)

    def test_get_polymarket_token_id_missing_token_raises_error(self):
        instrument_id = InstrumentId.from_str(f"condition_id-.{POLYMARKET_VENUE}")

        with pytest.raises(ValueError, match="Invalid Polymarket instrument ID format"):
            get_polymarket_token_id(instrument_id)
```


---

## Overview

This file is located at `tests/integration_tests/adapters/polymarket/test_symbol.py` within the repository.

**Classes defined:** TestPolymarketSymbol

**Functions defined:** test_get_polymarket_instrument_id, test_get_polymarket_condition_id_valid, test_get_polymarket_token_id_valid, test_get_polymarket_condition_id_no_dash_raises_error, test_get_polymarket_token_id_no_dash_raises_error, test_get_polymarket_condition_id_too_many_dashes_raises_error, test_get_polymarket_token_id_too_many_dashes_raises_error, test_get_polymarket_condition_id_missing_condition_raises_error, test_get_polymarket_token_id_missing_token_raises_error

**Import statements:** 6


---

## Detailed Analysis

### Classes

#### `TestPolymarketSymbol`


### Functions

#### `test_get_polymarket_instrument_id(self)`


#### `test_get_polymarket_condition_id_valid(self)`


#### `test_get_polymarket_token_id_valid(self)`


#### `test_get_polymarket_condition_id_no_dash_raises_error(self)`


#### `test_get_polymarket_token_id_no_dash_raises_error(self)`


#### `test_get_polymarket_condition_id_too_many_dashes_raises_error(self)`


#### `test_get_polymarket_token_id_too_many_dashes_raises_error(self)`


#### `test_get_polymarket_condition_id_missing_condition_raises_error(self)`


#### `test_get_polymarket_token_id_missing_token_raises_error(self)`


### Imports

- `import pytest`
- `from nautilus_trader.adapters.polymarket.common.constants import POLYMARKET_VENUE`
- `from nautilus_trader.adapters.polymarket.common.symbol import get_polymarket_condition_id`
- `from nautilus_trader.adapters.polymarket.common.symbol import get_polymarket_instrument_id`
- `from nautilus_trader.adapters.polymarket.common.symbol import get_polymarket_token_id`
- `from nautilus_trader.model.identifiers import InstrumentId`


---

## Usage Examples

### Importing

```python
from tests.integration_tests.adapters.polymarket.test_symbol import TestPolymarketSymbol
```


---

## Related Files

This file imports from the following modules:

- `import pytest`
- `from nautilus_trader.adapters.polymarket.common.constants import POLYMARKET_VENUE`
- `from nautilus_trader.adapters.polymarket.common.symbol import get_polymarket_condition_id`
- `from nautilus_trader.adapters.polymarket.common.symbol import get_polymarket_instrument_id`
- `from nautilus_trader.adapters.polymarket.common.symbol import get_polymarket_token_id`
- `from nautilus_trader.model.identifiers import InstrumentId`

**Directory:** `tests/integration_tests/adapters/polymarket`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: token. Ensure proper handling of secrets.

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


