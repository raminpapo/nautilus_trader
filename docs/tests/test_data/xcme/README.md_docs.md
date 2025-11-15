# Documentation: `tests/test_data/xcme/README.md`
**Generated:** 2025-11-15T19:40:08.883354Z
**File Size:** 606 bytes
**Extension:** .md
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

- **Path:** `tests/test_data/xcme/README.md`
- **Size:** 606 bytes
- **Lines:** 22
- **Extension:** `.md`
- **Type:** text

---

## Source Code

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


---

## Overview

This file is located at `tests/test_data/xcme/README.md` within the repository.

This is a Markdown documentation file.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `tests/test_data/xcme`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


