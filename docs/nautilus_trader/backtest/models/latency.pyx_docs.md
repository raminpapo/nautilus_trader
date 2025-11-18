# Documentation: latency.pyx

## File Metadata

- **Path**: `nautilus_trader/backtest/models/latency.pyx`
- **Size**: 3,610 bytes
- **Lines**: 85
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

import random

from libc.stdint cimport uint64_t

from nautilus_trader.core.correctness cimport Condition
from nautilus_trader.core.rust.core cimport NANOSECONDS_IN_MILLISECOND
from nautilus_trader.core.rust.model cimport LiquiditySide
from nautilus_trader.model.book cimport OrderBook
from nautilus_trader.model.functions cimport liquidity_side_to_str
from nautilus_trader.model.instruments.base cimport Instrument
from nautilus_trader.model.objects cimport Money
from nautilus_trader.model.objects cimport Price
from nautilus_trader.model.objects cimport Quantity
from nautilus_trader.model.orders.base cimport Order


cdef class LatencyModel:
    """
    Provides a latency model for simulated exchange message I/O.

    Parameters
    ----------
    base_latency_nanos : int, default 1_000_000_000
        The base latency (nanoseconds) for the model.
    insert_latency_nanos : int, default 0
        The order insert latency (nanoseconds) for the model.
    update_latency_nanos : int, default 0
        The order update latency (nanoseconds) for the model.
    cancel_latency_nanos : int, default 0
        The order cancel latency (nanoseconds) for the model.
    config : FillModelConfig, optional
        The configuration for the model.

    Raises
    ------
    ValueError
        If `base_latency_nanos` is negative (< 0).
    ValueError
        If `insert_latency_nanos` is negative (< 0).
    ValueError
        If `update_latency_nanos` is negative (< 0).
    ValueError
        If `cancel_latency_nanos` is negative (< 0).
    """

    def __init__(
        self,
        uint64_t base_latency_nanos = NANOSECONDS_IN_MILLISECOND,
        uint64_t insert_latency_nanos = 0,
        uint64_t update_latency_nanos = 0,
        uint64_t cancel_latency_nanos = 0,
        config = None,
    ) -> None:
        if config is not None:
            # Initialize from config
            base_latency_nanos = config.base_latency_nanos
            insert_latency_nanos = config.insert_latency_nanos
            update_latency_nanos = config.update_latency_nanos
            cancel_latency_nanos = config.cancel_latency_nanos

        Condition.not_negative_int(base_latency_nanos, "base_latency_nanos")
        Condition.not_negative_int(insert_latency_nanos, "insert_latency_nanos")
        Condition.not_negative_int(update_latency_nanos, "update_latency_nanos")
        Condition.not_negative_int(cancel_latency_nanos, "cancel_latency_nanos")

        self.base_latency_nanos = base_latency_nanos
        self.insert_latency_nanos = base_latency_nanos + insert_latency_nanos
        self.update_latency_nanos = base_latency_nanos + update_latency_nanos
        self.cancel_latency_nanos = base_latency_nanos + cancel_latency_nanos

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 40


**Identifiers**: `ANY`, `All`, `BASIS`, `CONDITIONS`, `Condition`, `Copyright`, `FillModelConfig`, `GNU`, `General`, `Initialize`, `Instrument`, `KIND`, `LatencyModel`, `Lesser`, `License`, `Licensed`, `LiquiditySide`, `Ltd`, `Money`, `NANOSECONDS_IN_MILLISECOND`, `Nautech`, `None`, `Order`, `OrderBook`, `Parameters`, `Price`, `Provides`, `Pty`, `Public`, `Quantity` *(+10 more)*

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
pytest nautilus_trader/backtest/models/latency.pyx

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:05.100650Z*
