# Documentation: `tests/integration_tests/adapters/betfair/resources/requests/account_funds.json`
**Generated:** 2025-11-15T19:40:05.570168Z
**File Size:** 414 bytes
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

- **Path:** `tests/integration_tests/adapters/betfair/resources/requests/account_funds.json`
- **Size:** 414 bytes
- **Lines:** 17
- **Extension:** `.json`
- **Type:** text

---

## Source Code

```json
{
  "method": "POST",
  "url": "https://api.betfair.com/exchange/account/json-rpc/v1",
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
    "method": "AccountAPING/v1.0/getAccountFunds",
    "params": {}
  }
}
```


---

## Overview

This file is located at `tests/integration_tests/adapters/betfair/resources/requests/account_funds.json` within the repository.

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


