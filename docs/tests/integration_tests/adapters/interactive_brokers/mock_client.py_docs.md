# Documentation: mock_client.py

## File Metadata

- **Path**: `tests/integration_tests/adapters/interactive_brokers/mock_client.py`
- **Size**: 7,288 bytes
- **Lines**: 171
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

import asyncio
from collections.abc import Callable

from ibapi.client import EClient

from nautilus_trader.adapters.interactive_brokers.client.client import InteractiveBrokersClient
from nautilus_trader.adapters.interactive_brokers.client.wrapper import InteractiveBrokersEWrapper
from nautilus_trader.adapters.interactive_brokers.common import IBContract
from nautilus_trader.adapters.interactive_brokers.parsing.instruments import ib_contract_to_instrument_id
from nautilus_trader.common.enums import LogColor
from tests.integration_tests.adapters.interactive_brokers.test_kit import IBTestContractStubs


class MockEClient(EClient):
    """
    MockEClient is a subclass of EClient which is used for simulating Interactive
    Brokers' client operations.

    This class overloads a few methods of the parent class to better accommodate testing
    needs. More methods can be added as and when needed, depending on the testing
    requirements.

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._next_valid_counter = 0

    def _handle_task(self, handler: Callable, **kwargs):
        # Get the running loop from pytest-asyncio (session-scoped)
        loop = asyncio.get_running_loop()
        if loop.is_running():
            loop.create_task(handler(**kwargs))  # noqa: RUF006
        else:
            loop.run_until_complete(handler(**kwargs))

    #########################################################################
    ################## Market Data
    #########################################################################

    #########################################################################
    ################## Options
    #########################################################################

    #########################################################################
    ################## Orders
    #########################################################################

    #########################################################################
    ################## Account and Portfolio
    #########################################################################

    #########################################################################
    ################## Daily PnL
    #########################################################################

    #########################################################################
    ################## Executions
    #########################################################################

    #########################################################################
    ################## Contract Details
    #########################################################################

    def reqContractDetails(self, reqId: int, contract: IBContract):
        instrument_id = ib_contract_to_instrument_id(contract, contract.exchange)

        match instrument_id.value:
            case "AAPL.NASDAQ":
                self._handle_task(
                    self.wrapper._client.process_contract_details,
                    req_id=reqId,
                    contract_details=IBTestContractStubs.aapl_equity_contract_details(),
                )
            case "EUR/USD.IDEALPRO":
                self._handle_task(
                    self.wrapper._client.process_contract_details,
                    req_id=reqId,
                    contract_details=IBTestContractStubs.eurusd_forex_contract_details(),
                )

        self._handle_task(
            self.wrapper._client.process_contract_details_end,
            req_id=reqId,
        )

    #########################################################################
    ################## Market Depth
    #########################################################################

    #########################################################################
    ################## News Bulletins
    #########################################################################

    #########################################################################
    ################## Financial Advisors
    #########################################################################
    def reqManagedAccts(self):
        self._handle_task(
            self.wrapper._client.process_managed_accounts,
            accounts_list="DU1234567,",
        )

    #########################################################################
    ################## Historical Data
    #########################################################################

    #########################################################################
    ################## Market Scanners
    #########################################################################

    #########################################################################
    ################## Real Time Bars
    #########################################################################

    #########################################################################
    ################## Fundamental Data
    #########################################################################

    ########################################################################
    ################## News
    #########################################################################

    #########################################################################
    ################## Display Groups
    #########################################################################


class MockInteractiveBrokersClient(InteractiveBrokersClient):
    """
    MockInteractiveBrokersClient is a subclass of InteractiveBrokersClient used for
    simulating client operations.

    This class initializes the EClient with a mocked version for testing purposes.

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._eclient = MockEClient(
            wrapper=InteractiveBrokersEWrapper(
                nautilus_logger=self._log,
                client=self,
            ),
        )

    async def _start_async(self):
        self._start_tws_incoming_msg_reader()
        self._start_internal_msg_queue_processor()
        self._eclient.startApi()

        self._is_client_ready.set()
        self._log.debug("`_is_client_ready` set by `_start_async`.", LogColor.BLUE)
        self._connection_attempts = 0

```

## High-Level Overview

This file is part of the NautilusTrader repository. 2 class(es).

## Detailed Walkthrough


### Classes
- **`MockEClient`**: Class defined in this file
- **`MockInteractiveBrokersClient`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 11


**Classs**: `MockEClient`, `MockInteractiveBrokersClient`
**Imports**: `asyncio`, `collections.abc`, `ibapi.client`, `nautilus_trader.adapters.interactive_brokers.client.client`, `nautilus_trader.adapters.interactive_brokers.client.wrapper`, `nautilus_trader.adapters.interactive_brokers.common`, `nautilus_trader.adapters.interactive_brokers.parsing.instruments`, `nautilus_trader.common.enums`, `tests.integration_tests.adapters.interactive_brokers.test_kit`

## Related Files

This file is located in `tests/integration_tests/adapters/interactive_brokers/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/interactive_brokers/mock_client.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.881255Z*
