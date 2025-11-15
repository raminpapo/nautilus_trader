# Documentation: `nautilus_trader/test_kit/stubs/persistence.py`
**Generated:** 2025-11-15T19:40:05.389364Z
**File Size:** 3626 bytes
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

- **Path:** `nautilus_trader/test_kit/stubs/persistence.py`
- **Size:** 3,626 bytes
- **Lines:** 93
- **Extension:** `.py`
- **Type:** text
- **Imports:** 8
- **Classes:** 1
- **Functions:** 6

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

from nautilus_trader import TEST_DATA_DIR
from nautilus_trader.core.datetime import maybe_dt_to_unix_nanos
from nautilus_trader.model.objects import Currency
from nautilus_trader.serialization.arrow.serializer import register_arrow
from nautilus_trader.test_kit.mocks.data import NewsEventData
from nautilus_trader.trading.filters import NewsImpact


class TestPersistenceStubs:
    @staticmethod
    def setup_news_event_persistence() -> None:
        import pyarrow as pa

        def _news_event_to_dict(self):
            return pa.RecordBatch.from_pylist(
                [
                    {
                        "name": self.name,
                        "impact": self.impact.name,
                        "currency": self.currency.code,
                        "ts_event": self.ts_event,
                        "ts_init": self.ts_init,
                    },
                ],
                schema=schema(),
            )

        def _news_event_from_dict(table: pa.Table):
            def parse(data):
                data.update(
                    {
                        "impact": getattr(NewsImpact, data["impact"]),
                        "currency": Currency.from_str(data["currency"]),
                    },
                )
                return data

            return [NewsEventData(**parse(d)) for d in table.to_pylist()]

        def schema():
            return pa.schema(
                {
                    "name": pa.string(),
                    "impact": pa.string(),
                    "currency": pa.string(),
                    "ts_event": pa.uint64(),
                    "ts_init": pa.uint64(),
                },
            )

        register_arrow(
            data_cls=NewsEventData,
            encoder=_news_event_to_dict,
            decoder=_news_event_from_dict,
            # partition_keys=("currency",),
            schema=schema(),
            # force=True,
        )

    @staticmethod
    def news_events() -> list[NewsEventData]:
        df = pd.read_csv(TEST_DATA_DIR / "news_events.csv")
        # Use only first 5000 rows for faster testing (vs original 86,985 rows)
        # This reduces test time from ~40s to ~2-3s while maintaining test validity
        df = df.head(5000)
        events = []
        for _, row in df.iterrows():
            data = NewsEventData(
                name=str(row["Name"]),
                impact=getattr(NewsImpact, row["Impact"]),
                currency=Currency.from_str(row["Currency"]),
                ts_event=maybe_dt_to_unix_nanos(pd.Timestamp(row["Start"])) or 0,
                ts_init=maybe_dt_to_unix_nanos(pd.Timestamp(row["Start"])) or 0,
            )
            events.append(data)
        return events
```


---

## Overview

This file is located at `nautilus_trader/test_kit/stubs/persistence.py` within the repository.

**Classes defined:** TestPersistenceStubs

**Functions defined:** setup_news_event_persistence, _news_event_to_dict, _news_event_from_dict, parse, schema, news_events

**Import statements:** 8


---

## Detailed Analysis

### Classes

#### `TestPersistenceStubs`


### Functions

#### `setup_news_event_persistence()`


#### `_news_event_to_dict(self)`


#### `_news_event_from_dict(table: pa.Table)`


#### `parse(data)`


#### `schema()`


#### `news_events()`


### Imports

- `import pandas as pd`
- `from nautilus_trader import TEST_DATA_DIR`
- `from nautilus_trader.core.datetime import maybe_dt_to_unix_nanos`
- `from nautilus_trader.model.objects import Currency`
- `from nautilus_trader.serialization.arrow.serializer import register_arrow`
- `from nautilus_trader.test_kit.mocks.data import NewsEventData`
- `from nautilus_trader.trading.filters import NewsImpact`
- `import pyarrow as pa`


---

## Usage Examples

### Importing

```python
from nautilus_trader.test_kit.stubs.persistence import TestPersistenceStubs
```


---

## Related Files

This file imports from the following modules:

- `import pandas as pd`
- `from nautilus_trader import TEST_DATA_DIR`
- `from nautilus_trader.core.datetime import maybe_dt_to_unix_nanos`
- `from nautilus_trader.model.objects import Currency`
- `from nautilus_trader.serialization.arrow.serializer import register_arrow`
- `from nautilus_trader.test_kit.mocks.data import NewsEventData`
- `from nautilus_trader.trading.filters import NewsImpact`
- `import pyarrow as pa`

**Directory:** `nautilus_trader/test_kit/stubs`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


