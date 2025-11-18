# Documentation: test_grpc_account.py

## File Metadata

- **Path**: `tests/integration_tests/adapters/dydx/test_grpc_account.py`
- **Size**: 4,037 bytes
- **Lines**: 140
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
Unit tests for the GRPC client.
"""

import pytest
from v4_proto.dydxprotocol.clob.order_pb2 import Order
from v4_proto.dydxprotocol.clob.order_pb2 import OrderId
from v4_proto.dydxprotocol.subaccounts.subaccount_pb2 import SubaccountId

from nautilus_trader.adapters.dydx.grpc.order_builder import DYDXGRPCOrderType
from nautilus_trader.adapters.dydx.grpc.order_builder import OrderBuilder


@pytest.fixture
def order_builder() -> OrderBuilder:
    """
    Construct an OrderBuilder instance.

    The settings are based on the ETH-USD symbol.

    """
    return OrderBuilder(
        atomic_resolution=-9,
        step_base_quantums=1_000_000,
        subticks_per_tick=100_000,
        quantum_conversion_exponent=-9,
        clob_pair_id=1,
    )


def test_calculate_quantums(order_builder: OrderBuilder) -> None:
    """
    Test converting an order size to quantums.
    """
    # Prepare
    expected_result = 100_0000

    # Act
    result = order_builder.calculate_quantums(size=0.001)

    # Assert
    assert expected_result == result


def test_calculate_subticks(order_builder: OrderBuilder) -> None:
    """
    Test converting an order price to subticks.
    """
    # Prepare
    expected_result = 3_264_300_000

    # Act
    result = order_builder.calculate_subticks(price=3264.309572)

    # Assert
    assert expected_result == result


def test_create_order_id(order_builder: OrderBuilder) -> None:
    """
    Test creating an OrderId.
    """
    # Prepare
    expected_result = OrderId(
        subaccount_id=SubaccountId(
            owner="dydx1kzsvkf2ghjqlysuffdkhcdctknl4rsvcx5hkm5",
            number=0,
        ),
        client_id=3,
        order_flags=0,
        clob_pair_id=1,
    )

    # Act
    result = order_builder.create_order_id(
        address="dydx1kzsvkf2ghjqlysuffdkhcdctknl4rsvcx5hkm5",
        subaccount_number=0,
        client_id=3,
        order_flags=0,
    )

    # Assert
    assert isinstance(result, OrderId)
    assert result == expected_result


def test_create_order(order_builder: OrderBuilder) -> None:
    """
    Test creating an Order.
    """
    # Prepare
    order_id = order_builder.create_order_id(
        address="dydx1kzsvkf2ghjqlysuffdkhcdctknl4rsvcx5hkm5",
        subaccount_number=0,
        client_id=3,
        order_flags=0,
    )
    expected_result = Order(
        order_id=order_id,
        side=Order.Side.SIDE_BUY,
        quantums=100_0000,
        subticks=3_264_300_000,
        good_til_block=None,
        good_til_block_time=None,
        time_in_force=Order.TimeInForce.TIME_IN_FORCE_UNSPECIFIED,
        reduce_only=False,
        client_metadata=0,
        condition_type=Order.ConditionType.CONDITION_TYPE_UNSPECIFIED,
        conditional_order_trigger_subticks=0,
    )

    # Act
    result = order_builder.create_order(
        order_id=order_id,
        order_type=DYDXGRPCOrderType.LIMIT,
        side=Order.Side.SIDE_BUY,
        size=0.001,
        price=3264.309572,
        time_in_force=Order.TimeInForce.TIME_IN_FORCE_UNSPECIFIED,
        reduce_only=False,
    )

    # Assert
    assert isinstance(result, Order)
    assert result == expected_result

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 5 function(s).

## Detailed Walkthrough

### Functions
- **`order_builder()`**: Function defined in this file
- **`test_calculate_quantums()`**: Function defined in this file
- **`test_calculate_subticks()`**: Function defined in this file
- **`test_create_order_id()`**: Function defined in this file
- **`test_create_order()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 9


**Functions**: `order_builder`, `test_calculate_quantums`, `test_calculate_subticks`, `test_create_order`, `test_create_order_id`
**Imports**: `nautilus_trader.adapters.dydx.grpc.order_builder`, `pytest`, `v4_proto.dydxprotocol.clob.order_pb2`, `v4_proto.dydxprotocol.subaccounts.subaccount_pb2`

## Related Files

This file is located in `tests/integration_tests/adapters/dydx/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/dydx/test_grpc_account.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.843696Z*
