# Documentation: http_get_account_positions-history.json

## File Metadata

- **Path**: `crates/adapters/okx/test_data/http_get_account_positions-history.json`
- **Size**: 707 bytes
- **Lines**: 32
- **Language**: JSON

## Original Source

```json
{
  "code": "0",
  "data": [
    {
      "cTime": "1736745586679",
      "ccy": "USDT",
      "closeAvgPx": "3224.8",
      "closeTotalPos": "0.1",
      "direction": "long",
      "fee": "-0.04516211",
      "fundingFee": "0",
      "instId": "ETH-USDT-SWAP",
      "instType": "SWAP",
      "lever": "3.0",
      "liqPenalty": "0",
      "mgnMode": "isolated",
      "openAvgPx": "3226.93",
      "openMaxPos": "0.1",
      "pnl": "-0.0213",
      "pnlRatio": "-0.0061788241455501",
      "posId": "2155643638909198336",
      "posSide": "long",
      "realizedPnl": "-0.06646211",
      "triggerPx": "",
      "type": "2",
      "uTime": "1736745929198",
      "uly": "ETH-USDT"
    }
  ],
  "msg": ""
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 3


**Identifiers**: `ETH`, `SWAP`, `USDT`

## Related Files

This file is located in `crates/adapters/okx/test_data/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/adapters/okx/test_data/http_get_account_positions-history.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:00.529932Z*
