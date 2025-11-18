# Documentation: money.txt

## File Metadata

- **Path**: `crates/model/proptest-regressions/types/money.txt`
- **Size**: 1,341 bytes
- **Lines**: 13
- **Language**: Unknown

## Original Source

```
# Seeds for failure cases proptest has generated in the past. It is
# automatically read and these particular cases re-run before any
# novel cases are generated.
#
# It is recommended to check this file in to source control so that
# everyone who runs the test benefits from these saved cases.
cc 1eb7079d9790703b929362265dbfe8a018d36178602dc953e98794ac37586603 # shrinks to amount = 979.6522699506736, currency = Currency(code='JPY', precision=0, iso4217=392, name='Japanese yen', currency_type=FIAT)
cc 9d07b03fc9524d0c15813e1368dfe83ab34b2c0656a420b53ae92fba956505d7 # shrinks to money1 = Money(9223372036.00000000, USDT), money2 = Money(9223372036.00000000, USDT)
cc 3535454e76b67ded56747bdda3f9cd9ccdb8f1f164383bfd23ecb78dabb515b2 # shrinks to money1 = Money(8507059173022.99902344, ETH), money2 = Money(17014118346045.00000000, ETH)
cc c754810e44542b48e4b604e89a92901c6e9eefe31f9359251b46c5efa5a1981c # shrinks to money1 = Money(-17014118346045.99804688, USDT), money2 = Money(369.71589564, USDT)
cc bdae204d217d1cf4ea165c86826408162ee1a59cd1b53b8fc9ac3bf3dcf30fc8 # shrinks to money1 = Money(0.00, USD), money2 = Money(-17014118346046.00, USD)
cc afe40d290d723f7e153c4a6098e08a5b7cb8a7880c614df949da7d50529563f5 # shrinks to money1 = Money(0.00, USD), money2 = Money(-17014118346045.00, USD), money3 = Money(-17014118346045.00, USD)

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 9


**Identifiers**: `Currency`, `ETH`, `FIAT`, `JPY`, `Japanese`, `Money`, `Seeds`, `USD`, `USDT`

## Related Files

This file is located in `crates/model/proptest-regressions/types/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/model/proptest-regressions/types/money.txt

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:02.170789Z*
