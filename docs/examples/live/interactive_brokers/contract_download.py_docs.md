# Documentation: `examples/live/interactive_brokers/contract_download.py`
**Generated:** 2025-11-15T19:40:03.921978Z
**File Size:** 1268 bytes
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

- **Path:** `examples/live/interactive_brokers/contract_download.py`
- **Size:** 1,268 bytes
- **Lines:** 48
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3

---

## Source Code

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


---

## Overview

This file is located at `examples/live/interactive_brokers/contract_download.py` within the repository.

**Import statements:** 3


---

## Detailed Analysis

### Imports

- `import asyncio`
- `from nautilus_trader.adapters.interactive_brokers.common import IBContract`
- `from nautilus_trader.adapters.interactive_brokers.historical import HistoricInteractiveBrokersClient`


---

## Usage Examples

### Importing

```python
import examples.live.interactive_brokers.contract_download
```


---

## Related Files

This file imports from the following modules:

- `import asyncio`
- `from nautilus_trader.adapters.interactive_brokers.common import IBContract`
- `from nautilus_trader.adapters.interactive_brokers.historical import HistoricInteractiveBrokersClient`

**Directory:** `examples/live/interactive_brokers`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


