# Documentation: node_test_factory.py

## File Metadata

- **Path**: `python/examples/blockchain/node_test_factory.py`
- **Size**: 2,928 bytes
- **Lines**: 76
- **Language**: Python

## Original Source

```python
#!/usr/bin/env python3
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

import os

from nautilus_trader.common import Environment
from nautilus_trader.common import ImportableActorConfig  # type: ignore[attr-defined]
from nautilus_trader.infrastructure import PostgresConnectOptions
from nautilus_trader.live import LiveNode  # type: ignore[attr-defined]
from nautilus_trader.model import TraderId


def test_factory_approach():
    """
    Test creating and adding actors using factory approach.

    Also tests PostgresConnectOptions Python bindings.

    """
    # Test PostgresConnectOptions creation
    postgres_config = PostgresConnectOptions(
        host=os.getenv("POSTGRES_HOST", "localhost"),
        port=int(os.getenv("POSTGRES_PORT", "5432")),
        user=os.getenv("POSTGRES_USERNAME", "nautilus"),
        password=os.getenv("POSTGRES_PASSWORD", "pass"),
        database=os.getenv("POSTGRES_DATABASE", "nautilus"),
    )
    print(f"PostgresConnectOptions created: {postgres_config}")
    print(f"  host: {postgres_config.host}")
    print(f"  port: {postgres_config.port}")
    print(f"  username: {postgres_config.username}")
    print(f"  database: {postgres_config.database}")

    trader_id = TraderId("TESTER-001")
    node = LiveNode.builder("test_factory", trader_id, Environment.SANDBOX).build()

    actor_config = ImportableActorConfig(
        actor_path="actors:BlockchainActor",
        config_path="actors:BlockchainActorConfig",
        config={
            "actor_id": "BLOCKCHAIN-001",
            "log_events": True,
            "log_commands": True,
            "chain": "Arbitrum",
            "client_id": "BLOCKCHAIN-Arbitrum",
            "pools": ["0xC31E54c7a869B9FcBEcc14363CF510d1c41fa443.Arbitrum:UniswapV3"],
        },
    )

    # Add actor using factory approach
    node.add_actor_from_config(actor_config)
    print("Successfully added actor from config")

    node.start()
    print("Successfully started node with factory-created actor")

    node.stop()
    print("Successfully stopped node")


if __name__ == "__main__":
    test_factory_approach()

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`test_factory_approach()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 6


**Functions**: `test_factory_approach`
**Imports**: `nautilus_trader.common`, `nautilus_trader.infrastructure`, `nautilus_trader.live`, `nautilus_trader.model`, `os`

## Related Files

This file is located in `python/examples/blockchain/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest python/examples/blockchain/node_test_factory.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

⚠️ **Security**: This file may handle sensitive data. Ensure proper encryption and access controls.

---
*Generated on 2025-11-18T21:55:06.049883Z*
