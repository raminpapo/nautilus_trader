# Documentation: aggregator.pxd

## File Metadata

- **Path**: `nautilus_trader/backtest/models/aggregator.pxd`
- **Size**: 1,911 bytes
- **Lines**: 43
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

from nautilus_trader.cache.base cimport CacheFacade
from nautilus_trader.common.component cimport Component
from nautilus_trader.common.component cimport TimeEvent
from nautilus_trader.model.greeks cimport GreeksCalculator
from nautilus_trader.model.identifiers cimport InstrumentId


cdef class SpreadQuoteAggregator(Component):
    cdef readonly InstrumentId _spread_instrument_id
    cdef readonly object _handler
    cdef readonly CacheFacade _cache
    cdef readonly list _components
    cdef readonly GreeksCalculator _greeks_calculator
    cdef readonly double _vega_multiplier
    cdef readonly int _update_interval_seconds
    cdef readonly str _timer_name
    cdef readonly list _component_ids
    cdef readonly object _ratios
    cdef readonly object _mid_prices
    cdef readonly object _vegas
    cdef readonly object _deltas
    cdef readonly object _bid_ask_spreads
    cdef readonly object _bid_sizes
    cdef readonly object _ask_sizes

    cdef void _set_build_timer(self)
    cdef void _build_quote(self, TimeEvent event)

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 28


**Identifiers**: `ANY`, `All`, `BASIS`, `CONDITIONS`, `CacheFacade`, `Component`, `Copyright`, `GNU`, `General`, `GreeksCalculator`, `InstrumentId`, `KIND`, `Lesser`, `License`, `Licensed`, `Ltd`, `Nautech`, `Pty`, `Public`, `See`, `SpreadQuoteAggregator`, `Systems`, `TimeEvent`, `Unless`, `Version`, `WARRANTIES`, `WITHOUT`, `You`

## Related Files

This file is located in `nautilus_trader/backtest/models/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest nautilus_trader/backtest/models/aggregator.pxd

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:05.086694Z*
