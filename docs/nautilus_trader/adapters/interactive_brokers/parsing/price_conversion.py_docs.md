# Documentation: price_conversion.py

## File Metadata

- **Path**: `nautilus_trader/adapters/interactive_brokers/parsing/price_conversion.py`
- **Size**: 2,969 bytes
- **Lines**: 97
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
"""
Price conversion utilities for Interactive Brokers adapter.

Interactive Brokers uses a price magnifier field in contract details to scale prices.
All prices received from IB need to be divided by the price magnifier to get the real
price. All prices sent to IB need to be multiplied by the price magnifier.

"""

from nautilus_trader.model.identifiers import InstrumentId


def ib_price_to_nautilus_price(ib_price: float, price_magnifier: int) -> float:
    """
    Convert an Interactive Brokers price to a Nautilus price.

    Parameters
    ----------
    ib_price : float
        The price received from Interactive Brokers.
    price_magnifier : int
        The price magnifier from the contract details.

    Returns
    -------
    float
        The real price for use in Nautilus.

    """
    if price_magnifier <= 0:
        return ib_price

    return ib_price / price_magnifier


def nautilus_price_to_ib_price(nautilus_price: float, price_magnifier: int) -> float:
    """
    Convert a Nautilus price to an Interactive Brokers price.

    Parameters
    ----------
    nautilus_price : float
        The price from Nautilus to send to Interactive Brokers.
    price_magnifier : int
        The price magnifier from the contract details.

    Returns
    -------
    float
        The scaled price for sending to Interactive Brokers.

    """
    if price_magnifier <= 0:
        return nautilus_price

    return nautilus_price * price_magnifier


def get_price_magnifier_for_instrument(
    instrument_id: InstrumentId,
    instrument_provider,
) -> int:
    """
    Get the price magnifier for an instrument.

    Parameters
    ----------
    instrument_id : InstrumentId
        The instrument identifier.
    instrument_provider : InteractiveBrokersInstrumentProvider | None
        The instrument provider to get contract details from.

    Returns
    -------
    int
        The price magnifier, defaults to 1 if not found or provider is None.

    """
    if instrument_provider is None:
        return 1

    return instrument_provider.get_price_magnifier(instrument_id)

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 3 function(s).

## Detailed Walkthrough

### Functions
- **`ib_price_to_nautilus_price()`**: Function defined in this file
- **`nautilus_price_to_ib_price()`**: Function defined in this file
- **`get_price_magnifier_for_instrument()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 4


**Functions**: `get_price_magnifier_for_instrument`, `ib_price_to_nautilus_price`, `nautilus_price_to_ib_price`
**Imports**: `nautilus_trader.model.identifiers`

## Related Files

This file is located in `nautilus_trader/adapters/interactive_brokers/parsing/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.875725Z*
