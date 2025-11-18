# Documentation: latency.pxd

## File Metadata

- **Path**: `nautilus_trader/backtest/models/latency.pxd`
- **Size**: 1,499 bytes
- **Lines**: 28
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

from libc.stdint cimport uint64_t


cdef class LatencyModel:
    cdef readonly uint64_t base_latency_nanos
    """The default latency to the exchange.\n\n:returns: `int`"""
    cdef readonly uint64_t insert_latency_nanos
    """The latency (nanoseconds) for order insert messages to reach the exchange.\n\n:returns: `int`"""
    cdef readonly uint64_t update_latency_nanos
    """The latency (nanoseconds) for order update messages to reach the exchange.\n\n:returns: `int`"""
    cdef readonly uint64_t cancel_latency_nanos
    """The latency (nanoseconds) for order cancel messages to reach the exchange.\n\n:returns: `int`"""

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 24


**Identifiers**: `ANY`, `All`, `BASIS`, `CONDITIONS`, `Copyright`, `GNU`, `General`, `KIND`, `LatencyModel`, `Lesser`, `License`, `Licensed`, `Ltd`, `Nautech`, `Pty`, `Public`, `See`, `Systems`, `The`, `Unless`, `Version`, `WARRANTIES`, `WITHOUT`, `You`

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
pytest nautilus_trader/backtest/models/latency.pxd

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:05.099206Z*
