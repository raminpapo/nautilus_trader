# Documentation: betting_list_market_catalogue.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/betfair/resources/requests/betting_list_market_catalogue.json`
- **Size**: 585 bytes
- **Lines**: 28
- **Language**: JSON

## Original Source

```json
{
  "method": "POST",
  "url": "https://api.betfair.com/exchange/betting/json-rpc/v1",
  "headers": {
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "content-type": "application/json",
    "X-Application": "app_key",
    "X-Authentication": "xxxsessionToken="
  },
  "json": {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "SportsAPING/v1.0/listMarketCatalogue",
    "params": {
      "filter": {
        "eventTypeIds": [
          "7"
        ],
        "marketBettingTypes": [
          "ODDS"
        ]
      },
      "maxResults": 1000
    }
  }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 8


**Identifiers**: `Accept`, `Application`, `Authentication`, `Connection`, `Encoding`, `ODDS`, `POST`, `SportsAPING`

## Related Files

This file is located in `tests/integration_tests/adapters/betfair/resources/requests/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/betfair/resources/requests/betting_list_market_catalogue.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.204132Z*
