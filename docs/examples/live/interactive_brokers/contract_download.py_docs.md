# Documentation: contract_download.py

## File Metadata

- **Path**: `examples/live/interactive_brokers/contract_download.py`
- **Size**: 1,268 bytes
- **Lines**: 49
- **Language**: Python

## Original Source

```python
import asyncio

from nautilus_trader.adapters.interactive_brokers.common import IBContract
from nautilus_trader.adapters.interactive_brokers.historical import HistoricInteractiveBrokersClient


async def main() -> None:
    host: str = "localhost"
    port: int = 7497

    client = HistoricInteractiveBrokersClient(host=host, port=port, log_level="DEBUG")
    await client.connect()
    await asyncio.sleep(1)

    nse_nifty_fut_contract = IBContract(
        secType="FUT",
        exchange="NSE",
        symbol="NIFTY50",
        lastTradeDateOrContractMonth="20250327",
    )
    ce_contract = IBContract(
        secType="OPT",
        exchange="NSE",
        symbol="NIFTY50",
        lastTradeDateOrContractMonth="20250227",
        strike=25000,
        right="C",
        includeExpired=True,
    )
    pe_contract = IBContract(
        secType="OPT",
        exchange="NSE",
        symbol="NIFTY50",
        lastTradeDateOrContractMonth="20250227",
        strike=25000,
        right="P",
        includeExpired=True,
    )
    contracts = [nse_nifty_fut_contract, ce_contract, pe_contract]

    instruments = await client.request_instruments(
        contracts=contracts,
    )
    print(instruments)


if __name__ == "__main__":
    asyncio.run(main())

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 3


**Imports**: `asyncio`, `nautilus_trader.adapters.interactive_brokers.common`, `nautilus_trader.adapters.interactive_brokers.historical`

## Related Files

This file is located in `examples/live/interactive_brokers/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.343900Z*
