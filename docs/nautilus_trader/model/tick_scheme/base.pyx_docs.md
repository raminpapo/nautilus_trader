# Documentation: base.pyx

## File Metadata

- **Path**: `nautilus_trader/model/tick_scheme/base.pyx`
- **Size**: 4,687 bytes
- **Lines**: 156
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

from libc.math cimport ceil as cceil
from libc.math cimport floor as cfloor
from libc.math cimport round as cround

from nautilus_trader.core.correctness cimport Condition
from nautilus_trader.model.objects cimport Price


cdef class TickScheme:
    """
    Represents an instrument tick scheme.

    Maps the valid prices available for an instrument.

    Parameters
    ----------
    name : str
        The name of the tick scheme.
    min_tick : Price
        The minimum possible tick `Price`.
    max_tick: Price
        The maximum possible tick `Price`.

    Raises
    ------
    ValueError
        If `name` is not a valid string.
    """

    def __init__(
        self,
        str name not None,
        Price min_tick not None,
        Price max_tick not None,
    ):
        Condition.valid_string(name, "name")

        self.name = name
        self.min_price = min_tick
        self.max_price = max_tick

    cpdef Price next_ask_price(self, double value, int n=0):
        """
        Return the price `n` ask ticks away from value.

        If a given price is between two ticks, n=0 will find the nearest ask tick (inclusive).

        Parameters
        ----------
        value : double
            The reference value.
        n : int, default 0
            The number of ticks to move.

        Returns
        -------
        Price

        """
        raise NotImplementedError()  # pragma: no cover

    cpdef Price next_bid_price(self, double value, int n=0):
        """
        Return the price `n` bid ticks away from value.

        If a given price is between two ticks, n=0 will find the nearest bid tick (inclusive).

        Parameters
        ----------
        value : double
            The reference value.
        n : int, default 0
            The number of ticks to move.

        Returns
        -------
        Price

        """
        raise NotImplementedError()  # pragma: no cover


cpdef double round_down(double value, double base):
    """
    Returns a value rounded down to a specific number of decimal places.

    If value is already on the boundary, returns the same value (price-inclusive).
    """
    if base <= 0:
        raise ValueError(f"base must be positive, was {base}")

    cdef double base_multiple = value / base
    cdef double rounded_multiple = cround(base_multiple)

    # Check if we're already on a tick boundary (within floating point precision)
    if is_close(base_multiple, rounded_multiple):
        return value
    else:
        # Round down to previous boundary using floor
        return cfloor(base_multiple) * base


cpdef double round_up(double value, double base):
    """
    Returns a value rounded up to a specific number of decimal places.

    If value is already on the boundary, returns the same value (price-inclusive).
    """
    if base <= 0:
        raise ValueError(f"base must be positive, was {base}")

    cdef double base_multiple = value / base
    cdef double rounded_multiple = cround(base_multiple)

    # Check if we're already on a tick boundary (within floating point precision)
    if is_close(base_multiple, rounded_multiple):
        return value
    else:
        # Round up to next boundary using ceil
        return cceil(base_multiple) * base


cdef dict[str, TickScheme] TICK_SCHEMES = {}

cpdef void register_tick_scheme(TickScheme tick_scheme):
    Condition.not_none(tick_scheme, "tick_scheme")

    global TICK_SCHEMES
    Condition.not_in(tick_scheme.name, TICK_SCHEMES, "name", "TICK_SCHEMES")
    TICK_SCHEMES[tick_scheme.name] = tick_scheme


cpdef TickScheme get_tick_scheme(str name):
    Condition.valid_string(name, "name")
    Condition.is_in(name, TICK_SCHEMES, "name", "TICK_SCHEMES")
    return TICK_SCHEMES[name]


cpdef list list_tick_schemes():
    return list(TICK_SCHEMES)

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 38


**Identifiers**: `ANY`, `All`, `BASIS`, `CONDITIONS`, `Check`, `Condition`, `Copyright`, `GNU`, `General`, `KIND`, `Lesser`, `License`, `Licensed`, `Ltd`, `Maps`, `Nautech`, `None`, `NotImplementedError`, `Parameters`, `Price`, `Pty`, `Public`, `Raises`, `Represents`, `Return`, `Returns`, `Round`, `See`, `Systems`, `TICK_SCHEMES` *(+8 more)*

## Related Files

This file is located in `nautilus_trader/model/tick_scheme/`. Related files may include:
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
*Generated on 2025-11-18T21:55:05.836299Z*
