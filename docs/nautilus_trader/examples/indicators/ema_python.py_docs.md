# Documentation: `nautilus_trader/examples/indicators/ema_python.py`
**Generated:** 2025-11-15T19:40:04.852989Z
**File Size:** 4229 bytes
**Extension:** .py
**Type:** text

---

## Table of Contents

1. [File Metadata](#file-metadata)
2. [Source Code](#source-code)
3. [Overview](#overview)
4. [Detailed Analysis](#detailed-analysis)
5. [Usage Examples](#usage-examples)
6. [Related Files](#related-files)
7. [Notes](#notes)

---

## File Metadata

- **Path:** `nautilus_trader/examples/indicators/ema_python.py`
- **Size:** 4,229 bytes
- **Lines:** 130
- **Extension:** `.py`
- **Type:** text
- **Imports:** 6
- **Classes:** 1
- **Functions:** 6

---

## Source Code

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


---

## Overview

This file is located at `nautilus_trader/examples/indicators/ema_python.py` within the repository.

**Classes defined:** PyExponentialMovingAverage

**Functions defined:** __init__, handle_quote_tick, handle_trade_tick, handle_bar, update_raw, _reset

**Import statements:** 6


---

## Detailed Analysis

### Classes

#### `PyExponentialMovingAverage`

**Inherits from:** Indicator


### Functions

#### `__init__(self, period: int, price_type: PriceType = PriceType.LAST)`


#### `handle_quote_tick(self, tick: QuoteTick)`


#### `handle_trade_tick(self, tick: TradeTick)`


#### `handle_bar(self, bar: Bar)`


#### `update_raw(self, value: float)`


#### `_reset(self)`


### Imports

- `from nautilus_trader.core.correctness import PyCondition`
- `from nautilus_trader.indicators import Indicator`
- `from nautilus_trader.model.data import Bar`
- `from nautilus_trader.model.data import QuoteTick`
- `from nautilus_trader.model.data import TradeTick`
- `from nautilus_trader.model.enums import PriceType`


---

## Usage Examples

### Importing

```python
from nautilus_trader.examples.indicators.ema_python import PyExponentialMovingAverage
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.core.correctness import PyCondition`
- `from nautilus_trader.indicators import Indicator`
- `from nautilus_trader.model.data import Bar`
- `from nautilus_trader.model.data import QuoteTick`
- `from nautilus_trader.model.data import TradeTick`
- `from nautilus_trader.model.enums import PriceType`

**Directory:** `nautilus_trader/examples/indicators`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


