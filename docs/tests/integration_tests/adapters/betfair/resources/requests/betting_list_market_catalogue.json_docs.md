# Documentation: `tests/integration_tests/adapters/betfair/resources/requests/betting_list_market_catalogue.json`
**Generated:** 2025-11-15T19:40:05.572828Z
**File Size:** 585 bytes
**Extension:** .json
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

- **Path:** `tests/integration_tests/adapters/betfair/resources/requests/betting_list_market_catalogue.json`
- **Size:** 585 bytes
- **Lines:** 27
- **Extension:** `.json`
- **Type:** text

---

## Source Code

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


---

## Overview

This file is located at `tests/integration_tests/adapters/betfair/resources/requests/betting_list_market_catalogue.json` within the repository.

This is a configuration file.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `tests/integration_tests/adapters/betfair/resources/requests`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: token, auth, session. Ensure proper handling of secrets.

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


