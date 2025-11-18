# Documentation: test_status_pyo3.py

## File Metadata

- **Path**: `tests/unit_tests/model/test_status_pyo3.py`
- **Size**: 1,624 bytes
- **Lines**: 38
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

from nautilus_trader.core.nautilus_pyo3 import InstrumentId
from nautilus_trader.core.nautilus_pyo3 import InstrumentStatus
from nautilus_trader.core.nautilus_pyo3 import MarketStatusAction


def test_instrument_status():
    # Arrange
    update = InstrumentStatus(
        instrument_id=InstrumentId.from_str("MSFT.XNAS"),
        action=MarketStatusAction.TRADING,
        ts_event=0,
        ts_init=0,
        reason=None,
        trading_event=None,
        is_trading=True,
        is_quoting=True,
        is_short_sell_restricted=False,
    )

    # Act, Assert
    assert InstrumentStatus.from_dict(InstrumentStatus.to_dict(update)) == update
    assert repr(update) == "InstrumentStatus(MSFT.XNAS,TRADING,0,0)"  # TODO: Improve repr from Rust

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`test_instrument_status()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 2


**Functions**: `test_instrument_status`
**Imports**: `nautilus_trader.core.nautilus_pyo3`

## Related Files

This file is located in `tests/unit_tests/model/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/unit_tests/model/test_status_pyo3.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:11.679098Z*
