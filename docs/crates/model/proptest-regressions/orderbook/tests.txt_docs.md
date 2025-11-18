# Documentation: tests.txt

## File Metadata

- **Path**: `crates/model/proptest-regressions/orderbook/tests.txt`
- **Size**: 1,328 bytes
- **Lines**: 8
- **Language**: Unknown

## Original Source

```
# Seeds for failure cases proptest has generated in the past. It is
# automatically read and these particular cases re-run before any
# novel cases are generated.
#
# It is recommended to check this file in to source control so that
# everyone who runs the test benefits from these saved cases.
cc 379281a91fee19f3b66918a889501e49d101d1daabd5fd24297658ea188af62d # shrinks to config = (L3_MBO, [Add(BookOrder(side=BUY, price=0.00, size=0.00, order_id=0), 16, 0), Add(BookOrder(side=BUY, price=0.00, size=0.00, order_id=0), 0, 0), Add(BookOrder(side=BUY, price=0.00, size=0.00, order_id=0), 64, 0), Add(BookOrder(side=BUY, price=0.00, size=0.00, order_id=0), 0, 0), Update(BookOrder(side=BUY, price=0.00, size=0.00, order_id=456), 102, 3340468566711001376), Add(BookOrder(side=BUY, price=0.00, size=0.00000004, order_id=1476138048754645682), 134, 1384690343770193126), Update(BookOrder(side=BUY, price=0.00000005, size=0.06, order_id=14571573170843111871), 211, 14419176621694009536), Add(BookOrder(side=BUY, price=0.00000010, size=0.00, order_id=9546670571466725171), 170, 3991092649813248609), Add(BookOrder(side=BUY, price=0.00, size=0.00000006, order_id=1509329065075500458), 76, 7793173039032754027), Add(BookOrder(side=BUY, price=-3537820394.66, size=0.00000009, order_id=17969147389279393614), 113, 6655226418353692396)])

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 6


**Identifiers**: `Add`, `BUY`, `BookOrder`, `L3_MBO`, `Seeds`, `Update`

## Related Files

This file is located in `crates/model/proptest-regressions/orderbook/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/model/proptest-regressions/orderbook/tests.txt

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:02.169145Z*
