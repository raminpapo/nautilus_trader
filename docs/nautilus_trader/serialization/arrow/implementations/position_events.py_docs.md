# Documentation: position_events.py

## File Metadata

- **Path**: `nautilus_trader/serialization/arrow/implementations/position_events.py`
- **Size**: 5,928 bytes
- **Lines**: 151
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

import pyarrow as pa

from nautilus_trader.model.events import PositionChanged
from nautilus_trader.model.events import PositionClosed
from nautilus_trader.model.events import PositionEvent
from nautilus_trader.model.events import PositionOpened
from nautilus_trader.model.objects import Money


def try_float(x):
    if x == "None" or x is None:
        return None
    return float(x)


def serialize(event: PositionEvent):
    data = {k: v for k, v in event.to_dict(event).items() if k not in ("order_fill",)}
    caster = {
        "signed_qty": float,
        "quantity": float,
        "peak_qty": float,
        "avg_px_open": float,
        "last_qty": float,
        "last_px": float,
        "avg_px_close": try_float,
        "realized_return": try_float,
    }
    values = {k: caster[k](v) if k in caster else v for k, v in data.items()}  # type: ignore
    if "realized_pnl" in values:
        realized = Money.from_str(values["realized_pnl"])
        values["realized_pnl"] = realized.as_double()
    if "unrealized_pnl" in values:
        unrealized = Money.from_str(values["unrealized_pnl"])
        values["unrealized_pnl"] = unrealized.as_double()
    return pa.RecordBatch.from_pylist([values], schema=SCHEMAS[type(event)])


def deserialize(cls):
    def inner(batch: pa.RecordBatch) -> PositionOpened | (PositionChanged | PositionClosed):
        def parse(data):
            for k in ("quantity", "last_qty", "peak_qty", "last_px"):
                if k in data:
                    data[k] = str(data[k])
            if "realized_pnl" in data:
                data["realized_pnl"] = f"{data['realized_pnl']} {data['currency']}"
            if "unrealized_pnl" in data:
                data["unrealized_pnl"] = f"{data['unrealized_pnl']} {data['currency']}"
            return data

        return [cls.from_dict(parse(d)) for d in batch.to_pylist()]

    return inner


SCHEMAS: dict[PositionEvent, pa.Schema] = {
    PositionOpened: pa.schema(
        {
            "trader_id": pa.dictionary(pa.int16(), pa.string()),
            "strategy_id": pa.dictionary(pa.int16(), pa.string()),
            "instrument_id": pa.dictionary(pa.int64(), pa.string()),
            "account_id": pa.dictionary(pa.int16(), pa.string()),
            "position_id": pa.string(),
            "opening_order_id": pa.string(),
            "entry": pa.string(),
            "side": pa.string(),
            "signed_qty": pa.float64(),
            "quantity": pa.float64(),
            "peak_qty": pa.float64(),
            "last_qty": pa.float64(),
            "last_px": pa.float64(),
            "currency": pa.string(),
            "avg_px_open": pa.float64(),
            "realized_pnl": pa.float64(),
            "event_id": pa.string(),
            "duration_ns": pa.uint64(),
            "ts_event": pa.uint64(),
            "ts_init": pa.uint64(),
        },
    ),
    PositionChanged: pa.schema(
        {
            "trader_id": pa.dictionary(pa.int16(), pa.string()),
            "strategy_id": pa.dictionary(pa.int16(), pa.string()),
            "instrument_id": pa.dictionary(pa.int64(), pa.string()),
            "account_id": pa.dictionary(pa.int16(), pa.string()),
            "position_id": pa.string(),
            "opening_order_id": pa.string(),
            "entry": pa.string(),
            "side": pa.string(),
            "signed_qty": pa.float64(),
            "quantity": pa.float64(),
            "peak_qty": pa.float64(),
            "last_qty": pa.float64(),
            "last_px": pa.float64(),
            "currency": pa.string(),
            "avg_px_open": pa.float64(),
            "avg_px_close": pa.float64(),
            "realized_return": pa.float64(),
            "realized_pnl": pa.float64(),
            "unrealized_pnl": pa.float64(),
            "event_id": pa.string(),
            "ts_opened": pa.uint64(),
            "ts_event": pa.uint64(),
            "ts_init": pa.uint64(),
        },
    ),
    PositionClosed: pa.schema(
        {
            "trader_id": pa.dictionary(pa.int16(), pa.string()),
            "account_id": pa.dictionary(pa.int16(), pa.string()),
            "strategy_id": pa.dictionary(pa.int16(), pa.string()),
            "instrument_id": pa.dictionary(pa.int64(), pa.string()),
            "position_id": pa.string(),
            "opening_order_id": pa.string(),
            "closing_order_id": pa.string(),
            "entry": pa.string(),
            "side": pa.string(),
            "signed_qty": pa.float64(),
            "quantity": pa.float64(),
            "peak_qty": pa.float64(),
            "last_qty": pa.float64(),
            "last_px": pa.float64(),
            "currency": pa.string(),
            "avg_px_open": pa.float64(),
            "avg_px_close": pa.float64(),
            "realized_return": pa.float64(),
            "realized_pnl": pa.float64(),
            "event_id": pa.string(),
            "ts_opened": pa.uint64(),
            "ts_closed": pa.uint64(),
            "duration_ns": pa.uint64(),
            "ts_init": pa.uint64(),
        },
    ),
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 3 function(s).

## Detailed Walkthrough

### Functions
- **`try_float()`**: Function defined in this file
- **`serialize()`**: Function defined in this file
- **`deserialize()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 6


**Functions**: `deserialize`, `serialize`, `try_float`
**Imports**: `nautilus_trader.model.events`, `nautilus_trader.model.objects`, `pyarrow`

## Related Files

This file is located in `nautilus_trader/serialization/arrow/implementations/`. Related files may include:
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
*Generated on 2025-11-18T21:55:05.923868Z*
