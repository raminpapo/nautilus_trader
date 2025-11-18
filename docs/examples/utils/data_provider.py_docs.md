# Documentation: data_provider.py

## File Metadata

- **Path**: `examples/utils/data_provider.py`
- **Size**: 2,611 bytes
- **Lines**: 62
- **Language**: Python

## Original Source

```python
#!/usr/bin/env python3
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

from nautilus_trader import TEST_DATA_DIR
from nautilus_trader.model.data import Bar
from nautilus_trader.model.data import BarType
from nautilus_trader.persistence.wranglers import BarDataWrangler
from nautilus_trader.test_kit.providers import TestInstrumentProvider


def prepare_demo_data_eurusd_futures_1min():
    # Define exchange name
    VENUE_NAME = "XCME"

    # Instrument definition for EURUSD futures (March 2024)
    EURUSD_INSTRUMENT = TestInstrumentProvider.eurusd_future(
        expiry_year=2024,
        expiry_month=3,
        venue_name=VENUE_NAME,
    )

    # CSV file containing 1-minute bars instrument data above
    csv_file_path = rf"{TEST_DATA_DIR}/xcme/6EH4.{VENUE_NAME}_1min_bars_20240101_20240131.csv.gz"

    # Load raw data from CSV file and restructure them into required format for BarDataWrangler
    df = pd.read_csv(csv_file_path, header=0, index_col=False)
    df = df.reindex(columns=["timestamp_utc", "open", "high", "low", "close", "volume"])
    df["timestamp_utc"] = pd.to_datetime(df["timestamp_utc"], format="%Y-%m-%d %H:%M:%S")
    df = df.rename(columns={"timestamp_utc": "timestamp"})
    df = df.set_index("timestamp")

    # Define bar type
    EURUSD_1MIN_BARTYPE = BarType.from_str(f"{EURUSD_INSTRUMENT.id}-1-MINUTE-LAST-EXTERNAL")

    # Convert DataFrame rows into Bar objects
    wrangler = BarDataWrangler(EURUSD_1MIN_BARTYPE, EURUSD_INSTRUMENT)
    bars_list: list[Bar] = wrangler.process(df)

    # Collect and return all prepared data
    prepared_data = {
        "venue_name": VENUE_NAME,
        "instrument": EURUSD_INSTRUMENT,
        "bar_type": EURUSD_1MIN_BARTYPE,
        "bars_list": bars_list,
    }
    return prepared_data

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`prepare_demo_data_eurusd_futures_1min()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 6


**Functions**: `prepare_demo_data_eurusd_futures_1min`
**Imports**: `nautilus_trader`, `nautilus_trader.model.data`, `nautilus_trader.persistence.wranglers`, `nautilus_trader.test_kit.providers`, `pandas`

## Related Files

This file is located in `examples/utils/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.397595Z*
