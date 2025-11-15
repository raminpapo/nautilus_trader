# Documentation: `tests/integration_tests/adapters/betfair/resources/streaming/streaming_mcm_UPDATE_md.json`
**Generated:** 2025-11-15T19:40:07.522975Z
**File Size:** 1289 bytes
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

- **Path:** `tests/integration_tests/adapters/betfair/resources/streaming/streaming_mcm_UPDATE_md.json`
- **Size:** 1,289 bytes
- **Lines:** 52
- **Extension:** `.json`
- **Type:** text

---

## Source Code

```json
{
  "op": "mcm",
  "id": 12345,
  "clk": "AKEIANcNANkP",
  "pt": 1478717720756,
  "mc": [
    {
      "id": "1.180770798",
      "marketDefinition": {
        "bspMarket": false,
        "turnInPlayEnabled": true,
        "persistenceEnabled": true,
        "marketBaseRate": 5,
        "eventId": "30363344",
        "eventTypeId": "2",
        "numberOfWinners": 1,
        "bettingType": "ODDS",
        "marketType": "GAME_BY_GAME_01_07",
        "marketTime": "2021-03-19T04:00:00+00:00",
        "suspendTime": "2021-03-19T04:00:00+00:00",
        "bspReconciled": false,
        "complete": true,
        "inPlay": true,
        "crossMatching": true,
        "runnersVoidable": false,
        "numberOfActiveRunners": 2,
        "betDelay": 5,
        "status": "SUSPENDED",
        "runners": [
          {
            "status": "ACTIVE",
            "sortPriority": 1,
            "id": "13834991"
          },
          {
            "status": "ACTIVE",
            "sortPriority": 2,
            "id": "3120169"
          }
        ],
        "regulators": [
          "MR_INT"
        ],
        "countryCode": "CO",
        "discountAllowed": true,
        "timezone": "UTC",
        "openDate": "2021-03-19T04:00:00+00:00",
        "version": 1488624717
      }
    }
  ]
}
```


---

## Overview

This file is located at `tests/integration_tests/adapters/betfair/resources/streaming/streaming_mcm_UPDATE_md.json` within the repository.

This is a configuration file.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `tests/integration_tests/adapters/betfair/resources/streaming`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


