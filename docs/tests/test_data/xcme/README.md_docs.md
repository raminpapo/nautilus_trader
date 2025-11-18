# Documentation: README.md

## File Metadata

- **Path**: `tests/test_data/xcme/README.md`
- **Size**: 606 bytes
- **Lines**: 23
- **Language**: Markdown

## Original Source

```markdown
# File: `6EH4.XCME_1min_bars_20240101_20240131.csv.gz`

- Instrument: 6E
- Expiration: H4 (March 2024)
- Exchange:   XCME (MIC code)
- Period      2024-01-01 --> 2024-01-31 (UTC timestamp, no contract rollover occurs in this period)
- Bar type:   1-minute bars

# Zipped format

We used zipped data, because they are 9x smaller than original CSV file and can be DIRECTLY read by [pandas](https://pandas.pydata.org/)
using code like this:

```python
import pandas as pd

df = pd.read_csv(
    "6EH4.XCME_1min_bars_20240101_20240131.csv.gz",  # update path as needed
    header=0,
    index_col=False,
)
```

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a Markdown documentation file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 15


**Identifiers**: `Bar`, `CSV`, `DIRECTLY`, `Exchange`, `Expiration`, `False`, `File`, `Instrument`, `MIC`, `March`, `Period`, `UTC`, `XCME`, `XCME_1min_bars_20240101_20240131`, `Zipped`

## Related Files

This file is located in `tests/test_data/xcme/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/test_data/xcme/README.md

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:11.095247Z*
