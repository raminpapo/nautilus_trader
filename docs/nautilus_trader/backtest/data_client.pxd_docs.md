# Documentation: data_client.pxd

## File Metadata

- **Path**: `nautilus_trader/backtest/data_client.pxd`
- **Size**: 1,797 bytes
- **Lines**: 36
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

from nautilus_trader.backtest.models cimport SpreadQuoteAggregator
from nautilus_trader.data.client cimport DataClient
from nautilus_trader.data.client cimport MarketDataClient
from nautilus_trader.data.messages cimport SubscribeQuoteTicks
from nautilus_trader.data.messages cimport UnsubscribeQuoteTicks
from nautilus_trader.model.identifiers cimport InstrumentId
from nautilus_trader.model.instruments.base cimport Instrument


cdef class BacktestDataClient(DataClient):
    pass


cdef class BacktestMarketDataClient(MarketDataClient):
    cdef dict[InstrumentId, SpreadQuoteAggregator] _spread_quote_aggregators

    cdef Instrument _create_option_spread_from_components(self, InstrumentId spread_instrument_id)
    cpdef void _start_spread_quote_aggregator(self, SubscribeQuoteTicks command)
    cpdef void _stop_spread_quote_aggregator(self, UnsubscribeQuoteTicks command)
    cdef void _handle_spread_quote(self, quote)

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 31


**Identifiers**: `ANY`, `All`, `BASIS`, `BacktestDataClient`, `BacktestMarketDataClient`, `CONDITIONS`, `Copyright`, `DataClient`, `GNU`, `General`, `Instrument`, `InstrumentId`, `KIND`, `Lesser`, `License`, `Licensed`, `Ltd`, `MarketDataClient`, `Nautech`, `Pty`, `Public`, `See`, `SpreadQuoteAggregator`, `SubscribeQuoteTicks`, `Systems`, `Unless`, `UnsubscribeQuoteTicks`, `Version`, `WARRANTIES`, `WITHOUT` *(+1 more)*

## Related Files

This file is located in `nautilus_trader/backtest/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest nautilus_trader/backtest/data_client.pxd

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:05.037221Z*
