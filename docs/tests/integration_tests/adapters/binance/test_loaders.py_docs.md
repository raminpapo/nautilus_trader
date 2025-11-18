# Documentation: test_loaders.py

## File Metadata

- **Path**: `tests/integration_tests/adapters/binance/test_loaders.py`
- **Size**: 1,875 bytes
- **Lines**: 42
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

from nautilus_trader import TEST_DATA_DIR
from nautilus_trader.adapters.binance.loaders import BinanceOrderBookDeltaDataLoader
from nautilus_trader.model.enums import BookAction
from nautilus_trader.model.enums import OrderSide
from nautilus_trader.model.enums import RecordFlag
from nautilus_trader.persistence.wranglers import OrderBookDeltaDataWrangler
from nautilus_trader.test_kit.providers import TestInstrumentProvider


def test_load_binance_deltas() -> None:
    # Arrange
    instrument = TestInstrumentProvider.btcusdt_binance()
    data_path = TEST_DATA_DIR / "binance" / "btcusdt-depth-snap.csv"
    df = BinanceOrderBookDeltaDataLoader.load(data_path)

    wrangler = OrderBookDeltaDataWrangler(instrument)

    # Act
    deltas = wrangler.process(df)

    # Assert
    assert len(deltas) == 101
    assert deltas[0].action == BookAction.CLEAR
    assert deltas[1].action == BookAction.ADD
    assert deltas[1].order.side == OrderSide.BUY
    assert deltas[1].flags == RecordFlag.F_SNAPSHOT

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`test_load_binance_deltas()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 6


**Functions**: `test_load_binance_deltas`
**Imports**: `nautilus_trader`, `nautilus_trader.adapters.binance.loaders`, `nautilus_trader.model.enums`, `nautilus_trader.persistence.wranglers`, `nautilus_trader.test_kit.providers`

## Related Files

This file is located in `tests/integration_tests/adapters/binance/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/binance/test_loaders.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.769584Z*
