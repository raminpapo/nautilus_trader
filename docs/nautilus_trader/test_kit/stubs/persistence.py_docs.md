# Documentation: persistence.py

## File Metadata

- **Path**: `nautilus_trader/test_kit/stubs/persistence.py`
- **Size**: 3,626 bytes
- **Lines**: 94
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

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`TestPersistenceStubs`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 8


**Classs**: `TestPersistenceStubs`
**Imports**: `nautilus_trader`, `nautilus_trader.core.datetime`, `nautilus_trader.model.objects`, `nautilus_trader.serialization.arrow.serializer`, `nautilus_trader.test_kit.mocks.data`, `nautilus_trader.trading.filters`, `pandas`

## Related Files

This file is located in `nautilus_trader/test_kit/stubs/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest nautilus_trader/test_kit/stubs/persistence.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.016276Z*
