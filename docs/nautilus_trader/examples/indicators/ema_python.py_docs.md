# Documentation: ema_python.py

## File Metadata

- **Path**: `nautilus_trader/examples/indicators/ema_python.py`
- **Size**: 4,229 bytes
- **Lines**: 131
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

from nautilus_trader.core.correctness import PyCondition
from nautilus_trader.indicators import Indicator
from nautilus_trader.model.data import Bar
from nautilus_trader.model.data import QuoteTick
from nautilus_trader.model.data import TradeTick
from nautilus_trader.model.enums import PriceType


# It's generally recommended to code indicators in Cython as per the built-in
# indicators found in the `indicators` subpackage. This is an example
# demonstrating an equivalent EMA indicator written in Python.

# Note: The `MovingAverage` base class has not being used in this example to
# provide more clarity on how to implement custom indicators. Basically you need
# to inherit from `Indicator` and override the methods shown below.


class PyExponentialMovingAverage(Indicator):
    """
    An indicator which calculates an exponential moving average across a rolling window.

    Parameters
    ----------
    period : int
        The rolling window period for the indicator (> 0).
    price_type : PriceType
        The specified price type for extracting values from quotes.

    Raises
    ------
    ValueError
        If `period` is not positive (> 0).

    """

    def __init__(self, period: int, price_type: PriceType = PriceType.LAST):
        PyCondition.positive_int(period, "period")
        super().__init__(params=[period])

        self.period = period
        self.price_type = price_type
        self.alpha = 2.0 / (period + 1.0)
        self.value = 0.0  # <-- stateful value
        self.count = 0  # <-- stateful value

    def handle_quote_tick(self, tick: QuoteTick):
        """
        Update the indicator with the given quote tick.

        Parameters
        ----------
        tick : QuoteTick
            The update tick to handle.

        """
        PyCondition.not_none(tick, "tick")

        self.update_raw(tick.extract_price(self.price_type).as_double())

    def handle_trade_tick(self, tick: TradeTick):
        """
        Update the indicator with the given trade tick.

        Parameters
        ----------
        tick : TradeTick
            The update tick to handle.

        """
        PyCondition.not_none(tick, "tick")

        self.update_raw(tick.price.as_double())

    def handle_bar(self, bar: Bar):
        """
        Update the indicator with the given bar.

        Parameters
        ----------
        bar : Bar
            The update bar to handle.

        """
        PyCondition.not_none(bar, "bar")

        self.update_raw(bar.close.as_double())

    def update_raw(self, value: float):
        """
        Update the indicator with the given raw value.

        Parameters
        ----------
        value : double
            The update value.

        """
        # Check if this is the initial input
        if not self.has_inputs:
            self.value = value

        self.value = self.alpha * value + ((1.0 - self.alpha) * self.value)
        self.count += 1

        # Initialization logic
        if not self.initialized:
            self._set_has_inputs(True)
            if self.count >= self.period:
                self._set_initialized(True)

    def _reset(self):
        # Override this method to reset stateful values introduced in the class.
        # This method will be called by the base when `.reset()` is called.
        self.value = 0.0
        self.count = 0

```

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`PyExponentialMovingAverage`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 5


**Classs**: `PyExponentialMovingAverage`
**Imports**: `nautilus_trader.core.correctness`, `nautilus_trader.indicators`, `nautilus_trader.model.data`, `nautilus_trader.model.enums`

## Related Files

This file is located in `nautilus_trader/examples/indicators/`. Related files may include:
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
*Generated on 2025-11-18T21:55:05.426113Z*
