# Documentation: databento_download.py

## File Metadata

- **Path**: `examples/backtest/notebooks/databento_download.py`
- **Size**: 3,139 bytes
- **Lines**: 124
- **Language**: Python

## Original Source

```python
# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.3
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Databento Data Client with Backtest Node
#
# This example demonstrates how to use the Databento data client with a backtest node.

# %% [markdown]
# ## Imports

# %%
# Note: Use the jupytext python extension to be able to open this python file in jupyter as a notebook

# %%
import asyncio

import nautilus_trader.adapters.databento.data_utils as db_data_utils
from nautilus_trader.adapters.databento.config import DatabentoDataClientConfig
from nautilus_trader.adapters.databento.factories import DatabentoLiveDataClientFactory
from nautilus_trader.backtest.node import BacktestNode
from nautilus_trader.core.datetime import time_object_to_dt
from nautilus_trader.model.data import BarType
from nautilus_trader.model.identifiers import InstrumentId
from nautilus_trader.persistence.config import DataCatalogConfig


# from nautilus_trader.live.config import RoutingConfig


# %%
# We need to use nest_asyncio in a jupyter notebook to be able to run async code as sync for market data
# requests in a backtest
try:
    asyncio.get_running_loop()
except RuntimeError:
    pass  # No loop running
else:
    import nest_asyncio

    nest_asyncio.apply()

# %% [markdown]
# ## Parameters

# %%
# Set the data path for Databento data
# DATA_PATH = "/path/to/your/data"  # Use your own value here
# db_data_utils.DATA_PATH = DATA_PATH

catalog_folder = "download_catalog"
catalog = db_data_utils.load_catalog(catalog_folder)

# Small amount of data for testing
start_time_1 = "2024-05-07T10:00"
start_time_2 = "2024-05-08T10:00"
end_time_1 = "2024-05-08T10:01"
end_time_2 = "2024-05-08T10:04"
end_time_3 = "2024-05-08T10:06"

# %% [markdown]
# ## Strategy

# %%
# Configure the data catalog
catalog_config = DataCatalogConfig(path=catalog.path)

data_clients: dict = {
    "databento-001": DatabentoDataClientConfig(),
}
# api_key=None,  # 'DATABENTO_API_KEY' env var
# routing=RoutingConfig(
#     default=False,
#     venues=frozenset(["XCME"]),
# ),

# Create the backtest node
node = BacktestNode([])

# Register the Databento data client factory
node.add_data_client_factory("databento", DatabentoLiveDataClientFactory)

# Build download engine
node.setup_download_engine(catalog_config, data_clients)

# %%
node.download_data(
    "request_instrument",
    instrument_id=InstrumentId.from_str("ESM4.XCME"),
    start=time_object_to_dt(start_time_1),
    end=time_object_to_dt(end_time_1),
)

node.download_data(
    "request_bars",
    bar_type=BarType.from_str("ESM4.XCME-1-MINUTE-LAST-EXTERNAL"),
    start=time_object_to_dt(start_time_2),
    end=time_object_to_dt(end_time_3),
)

# %%
node.download_data(
    "request_order_book_depth",
    instrument_id=InstrumentId.from_str("ESM4.XCME"),
    start=time_object_to_dt(start_time_2),
    end=time_object_to_dt(end_time_1),
)

# %%
# # Clean up
node.dispose()

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 9


**Imports**: `asyncio`, `nautilus_trader.adapters.databento.config`, `nautilus_trader.adapters.databento.data_utils`, `nautilus_trader.adapters.databento.factories`, `nautilus_trader.backtest.node`, `nautilus_trader.core.datetime`, `nautilus_trader.model.data`, `nautilus_trader.model.identifiers`, `nautilus_trader.persistence.config`

## Related Files

This file is located in `examples/backtest/notebooks/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest examples/backtest/notebooks/databento_download.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

⚠️ **Security**: This file may handle sensitive data. Ensure proper encryption and access controls.

---
*Generated on 2025-11-18T21:55:04.281854Z*
