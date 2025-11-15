# Documentation: `nautilus_trader/examples/algorithms/blank.py`
**Generated:** 2025-11-15T19:40:04.847917Z
**File Size:** 4226 bytes
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

- **Path:** `nautilus_trader/examples/algorithms/blank.py`
- **Size:** 4,226 bytes
- **Lines:** 140
- **Extension:** `.py`
- **Type:** text
- **Imports:** 6
- **Classes:** 2
- **Functions:** 9

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

from nautilus_trader.common.component import LogColor
from nautilus_trader.config import ExecAlgorithmConfig
from nautilus_trader.execution.algorithm import ExecAlgorithm
from nautilus_trader.model.identifiers import ExecAlgorithmId
from nautilus_trader.model.orders import Order
from nautilus_trader.model.orders import OrderList


class MyExecAlgorithmConfig(ExecAlgorithmConfig, frozen=True):
    """
    Configuration for ``MyExecAlgorithm`` instances.

    Parameters
    ----------
    exec_algorithm_id : str | ExecAlgorithmId, optional
        The execution algorithm ID (will override default which is the class name).

    """

    exec_algorithm_id: ExecAlgorithmId | None = None


class MyExecAlgorithm(ExecAlgorithm):
    """
    A blank template execution algorithm.

    Parameters
    ----------
    config : MyExecAlgorithmConfig
        The configuration for the instance.

    """

    def __init__(self, config: MyExecAlgorithmConfig) -> None:
        super().__init__(config)
        # Optionally implement further initialization

    def on_start(self) -> None:
        """
        Actions to be performed when the algorithm component is started.
        """
        # Optionally implement

    def on_stop(self) -> None:
        """
        Actions to be performed when the algorithm component is stopped.
        """
        # Optionally implement

    def on_reset(self) -> None:
        """
        Actions to be performed when the algorithm component is reset.
        """
        # Optionally implement

    def on_dispose(self) -> None:
        """
        Actions to be performed when the algorithm component is disposed.

        Cleanup any resources used by the strategy here.

        """
        # Optionally implement

    def on_save(self) -> dict[str, bytes]:
        """
        Actions to be performed when the algorithm component is saved.

        Create and return a state dictionary of values to be saved.

        Returns
        -------
        dict[str, bytes]
            The strategy state dictionary.

        """
        return {}  # Optionally implement

    def on_load(self, state: dict[str, bytes]) -> None:
        """
        Actions to be performed when the algorithm component is loaded.

        Saved state values will be contained in the give state dictionary.

        Parameters
        ----------
        state : dict[str, bytes]
            The strategy state dictionary.

        """
        # Optionally implement

    def on_order(self, order: Order) -> None:
        """
        Actions to be performed when running and receives an order.

        Parameters
        ----------
        order : Order
            The order to be handled.

        Warnings
        --------
        System method (not intended to be called by user code).

        """
        self.log.info(repr(order), LogColor.CYAN)
        # Optionally implement

    def on_order_list(self, order_list: OrderList) -> None:
        """
        Actions to be performed when running and receives an order list.

        Parameters
        ----------
        order_list : OrderList
            The order list to be handled.

        Warnings
        --------
        System method (not intended to be called by user code).

        """
        self.log.info(repr(order_list), LogColor.CYAN)
        # Optionally implement
```


---

## Overview

This file is located at `nautilus_trader/examples/algorithms/blank.py` within the repository.

**Classes defined:** MyExecAlgorithmConfig, MyExecAlgorithm

**Functions defined:** __init__, on_start, on_stop, on_reset, on_dispose, on_save, on_load, on_order, on_order_list

**Import statements:** 6


---

## Detailed Analysis

### Classes

#### `MyExecAlgorithmConfig`

**Inherits from:** ExecAlgorithmConfig, frozen=True


#### `MyExecAlgorithm`

**Inherits from:** ExecAlgorithm


### Functions

#### `__init__(self, config: MyExecAlgorithmConfig)`


#### `on_start(self)`


#### `on_stop(self)`


#### `on_reset(self)`


#### `on_dispose(self)`


#### `on_save(self)`


#### `on_load(self, state: dict[str, bytes])`


#### `on_order(self, order: Order)`


#### `on_order_list(self, order_list: OrderList)`


### Imports

- `from nautilus_trader.common.component import LogColor`
- `from nautilus_trader.config import ExecAlgorithmConfig`
- `from nautilus_trader.execution.algorithm import ExecAlgorithm`
- `from nautilus_trader.model.identifiers import ExecAlgorithmId`
- `from nautilus_trader.model.orders import Order`
- `from nautilus_trader.model.orders import OrderList`


---

## Usage Examples

### Importing

```python
from nautilus_trader.examples.algorithms.blank import MyExecAlgorithmConfig
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.common.component import LogColor`
- `from nautilus_trader.config import ExecAlgorithmConfig`
- `from nautilus_trader.execution.algorithm import ExecAlgorithm`
- `from nautilus_trader.model.identifiers import ExecAlgorithmId`
- `from nautilus_trader.model.orders import Order`
- `from nautilus_trader.model.orders import OrderList`

**Directory:** `nautilus_trader/examples/algorithms`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


