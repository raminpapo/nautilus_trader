# Documentation: test_perf_msgbus.py

## File Metadata

- **Path**: `tests/performance_tests/test_perf_msgbus.py`
- **Size**: 1,808 bytes
- **Lines**: 50
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

import random

from nautilus_trader.common.component import is_matching_py


def generate_topics(n: int, seed: int) -> list[str]:
    random.seed(seed)

    cat = ["data", "info", "order"]
    model = ["quotes", "trades", "orderbooks", "depths"]
    venue = ["BINANCE", "BYBIT", "OKX", "FTX", "KRAKEN"]
    instrument = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "XRPUSDT", "DOGEUSDT"]

    topics: list[str] = []

    for _ in range(n):
        c = random.choice(cat)  # noqa: S311
        m = random.choice(model)  # noqa: S311
        v = random.choice(venue)  # noqa: S311
        i = random.choice(instrument)  # noqa: S311
        topics.append(f"{c}.{m}.{v}.{i}")

    return topics


def test_topic_pattern_matching(benchmark) -> None:
    topics = generate_topics(1000, 42)
    pattern = "data.*.BINANCE.ETH???"

    def match_topics():
        for topic in topics:
            is_matching_py(pattern, topic)

    benchmark(match_topics)

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 2 function(s).

## Detailed Walkthrough

### Functions
- **`generate_topics()`**: Function defined in this file
- **`test_topic_pattern_matching()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 4


**Functions**: `generate_topics`, `test_topic_pattern_matching`
**Imports**: `nautilus_trader.common.component`, `random`

## Related Files

This file is located in `tests/performance_tests/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/performance_tests/test_perf_msgbus.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:07.312183Z*
