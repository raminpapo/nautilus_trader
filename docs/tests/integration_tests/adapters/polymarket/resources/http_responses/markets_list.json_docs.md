# Documentation: markets_list.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/polymarket/resources/http_responses/markets_list.json`
- **Size**: 1,328 bytes
- **Lines**: 42
- **Language**: JSON

## Original Source

```json
[
  {
    "conditionId": "0x4319532e181605cb15b1bd677759a3bc7f7394b2fdf145195b700eeaedfd5221",
    "questionId": "0x12345",
    "slug": "fed-rate-hike-in-2025",
    "question": "Fed rate hike in 2025?",
    "active": true,
    "closed": false,
    "archived": false,
    "clobTokenIds": [
      "60487116984468020978247225474488676749601001829886755968952521846780452448915",
      "81104637750588840860328515305303028259865221573278091453716127842023614249200"
    ]
  },
  {
    "conditionId": "0xabc123",
    "questionId": "0x67890",
    "slug": "btc-price-above-100k",
    "question": "Will BTC be above $100k by end of 2025?",
    "active": true,
    "closed": false,
    "archived": false,
    "clobTokenIds": [
      "12345678901234567890123456789012345678901234567890123456789012345678901234567",
      "98765432109876543210987654321098765432109876543210987654321098765432109876543"
    ]
  },
  {
    "conditionId": "0xdef456",
    "questionId": "0xabcde",
    "slug": "eth-price-above-5k",
    "question": "Will ETH be above $5k by end of 2025?",
    "active": false,
    "closed": true,
    "archived": false,
    "clobTokenIds": [
      "11111111111111111111111111111111111111111111111111111111111111111111111111111",
      "22222222222222222222222222222222222222222222222222222222222222222222222222222"
    ]
  }
]

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 4


**Identifiers**: `BTC`, `ETH`, `Fed`, `Will`

## Related Files

This file is located in `tests/integration_tests/adapters/polymarket/resources/http_responses/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/polymarket/resources/http_responses/markets_list.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:07.130676Z*
