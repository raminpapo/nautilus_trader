# Documentation: data_topics.pxd

## File Metadata

- **Path**: `nautilus_trader/common/data_topics.pxd`
- **Size**: 3,598 bytes
- **Lines**: 58
- **Language**: Unknown

## Original Source

```
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

from nautilus_trader.model.data cimport BarType
from nautilus_trader.model.data cimport DataType
from nautilus_trader.model.identifiers cimport InstrumentId
from nautilus_trader.model.identifiers cimport Venue


cdef class TopicCache:
    cdef dict[tuple[InstrumentId, bint], str] _topic_cache_instruments
    cdef dict[Venue, str] _topic_cache_instruments_pattern
    cdef dict[tuple[InstrumentId, bint], str] _topic_cache_deltas
    cdef dict[tuple[InstrumentId, bint], str] _topic_cache_depth
    cdef dict[tuple[InstrumentId, bint], str] _topic_cache_quotes
    cdef dict[tuple[InstrumentId, bint], str] _topic_cache_trades
    cdef dict[tuple[InstrumentId, bint], str] _topic_cache_status
    cdef dict[tuple[InstrumentId, bint], str] _topic_cache_mark_prices
    cdef dict[tuple[InstrumentId, bint], str] _topic_cache_index_prices
    cdef dict[tuple[InstrumentId, bint], str] _topic_cache_funding_rates
    cdef dict[tuple[InstrumentId, bint], str] _topic_cache_close_prices
    cdef dict[tuple[InstrumentId, int, bint], str] _topic_cache_snapshots
    cdef dict[tuple[DataType, InstrumentId, bint], str] _topic_cache_custom
    cdef dict[tuple[DataType, bint], str] _topic_cache_custom_simple
    cdef dict[tuple[BarType, bint], str] _topic_cache_bars
    cdef dict[str, str] _topic_cache_signal

    cpdef str get_instrument_topic(self, InstrumentId instrument_id, bint historical = *)
    cpdef str get_instruments_topic(self, Venue venue)
    cpdef str get_book_topic(self, type book_data_type, InstrumentId instrument_id, bint historical = *)
    cpdef str get_deltas_topic(self, InstrumentId instrument_id, bint historical = *)
    cpdef str get_depth_topic(self, InstrumentId instrument_id, bint historical = *)
    cpdef str get_quotes_topic(self, InstrumentId instrument_id, bint historical = *)
    cpdef str get_trades_topic(self, InstrumentId instrument_id, bint historical = *)
    cpdef str get_status_topic(self, InstrumentId instrument_id, bint historical = *)
    cpdef str get_mark_prices_topic(self, InstrumentId instrument_id, bint historical = *)
    cpdef str get_index_prices_topic(self, InstrumentId instrument_id, bint historical = *)
    cpdef str get_funding_rates_topic(self, InstrumentId instrument_id, bint historical = *)
    cpdef str get_close_prices_topic(self, InstrumentId instrument_id, bint historical = *)
    cpdef str get_snapshots_topic(self, InstrumentId instrument_id, int interval_ms, bint historical = *)
    cpdef str get_custom_data_topic(self, DataType data_type, InstrumentId instrument_id = *, bint historical = *)
    cpdef str get_bars_topic(self, BarType bar_type, bint historical = *)
    cpdef str get_signal_topic(self, str name)

    cpdef void clear_cache(self)

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 27


**Identifiers**: `ANY`, `All`, `BASIS`, `BarType`, `CONDITIONS`, `Copyright`, `DataType`, `GNU`, `General`, `InstrumentId`, `KIND`, `Lesser`, `License`, `Licensed`, `Ltd`, `Nautech`, `Pty`, `Public`, `See`, `Systems`, `TopicCache`, `Unless`, `Venue`, `Version`, `WARRANTIES`, `WITHOUT`, `You`

## Related Files

This file is located in `nautilus_trader/common/`. Related files may include:
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
*Generated on 2025-11-18T21:55:05.236317Z*
