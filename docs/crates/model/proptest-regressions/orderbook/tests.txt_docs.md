# Documentation: `crates/model/proptest-regressions/orderbook/tests.txt`
**Generated:** 2025-11-15T19:40:02.432052Z
**File Size:** 1328 bytes
**Extension:** .txt
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

- **Path:** `crates/model/proptest-regressions/orderbook/tests.txt`
- **Size:** 1,328 bytes
- **Lines:** 7
- **Extension:** `.txt`
- **Type:** text

---

## Source Code

```
# Seeds for failure cases proptest has generated in the past. It is
# automatically read and these particular cases re-run before any
# novel cases are generated.
#
# It is recommended to check this file in to source control so that
# everyone who runs the test benefits from these saved cases.
cc 379281a91fee19f3b66918a889501e49d101d1daabd5fd24297658ea188af62d # shrinks to config = (L3_MBO, [Add(BookOrder(side=BUY, price=0.00, size=0.00, order_id=0), 16, 0), Add(BookOrder(side=BUY, price=0.00, size=0.00, order_id=0), 0, 0), Add(BookOrder(side=BUY, price=0.00, size=0.00, order_id=0), 64, 0), Add(BookOrder(side=BUY, price=0.00, size=0.00, order_id=0), 0, 0), Update(BookOrder(side=BUY, price=0.00, size=0.00, order_id=456), 102, 3340468566711001376), Add(BookOrder(side=BUY, price=0.00, size=0.00000004, order_id=1476138048754645682), 134, 1384690343770193126), Update(BookOrder(side=BUY, price=0.00000005, size=0.06, order_id=14571573170843111871), 211, 14419176621694009536), Add(BookOrder(side=BUY, price=0.00000010, size=0.00, order_id=9546670571466725171), 170, 3991092649813248609), Add(BookOrder(side=BUY, price=0.00, size=0.00000006, order_id=1509329065075500458), 76, 7793173039032754027), Add(BookOrder(side=BUY, price=-3537820394.66, size=0.00000009, order_id=17969147389279393614), 113, 6655226418353692396)])
```


---

## Overview

This file is located at `crates/model/proptest-regressions/orderbook/tests.txt` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/model/proptest-regressions/orderbook`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


