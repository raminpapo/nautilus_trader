# Documentation: `tests/integration_tests/adapters/betfair/resources/streaming/streaming_market_definition.json`
**Generated:** 2025-11-15T19:40:07.494860Z
**File Size:** 1712 bytes
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

- **Path:** `tests/integration_tests/adapters/betfair/resources/streaming/streaming_market_definition.json`
- **Size:** 1,712 bytes
- **Lines:** 86
- **Extension:** `.json`
- **Type:** text

---

## Source Code

```json
{
  "bspMarket": true,
  "turnInPlayEnabled": true,
  "persistenceEnabled": true,
  "marketBaseRate": 5,
  "eventId": "27890558",
  "eventTypeId": "7",
  "numberOfWinners": 1,
  "bettingType": "ODDS",
  "marketType": "WIN",
  "marketTime": "2016-08-17T18:10:00.000Z",
  "suspendTime": "2016-08-17T18:10:00.000Z",
  "bspReconciled": false,
  "complete": true,
  "inPlay": false,
  "crossMatching": false,
  "runnersVoidable": false,
  "numberOfActiveRunners": 7,
  "betDelay": 0,
  "status": "OPEN",
  "keyLineDefinition": {
    "kl": [
      {
        "hc": -2,
        "id": 11131804
      },
      {
        "hc": 2,
        "id": 11064886
      }
    ]
  },
  "runners": [
    {
      "adjustmentFactor": 44.323,
      "status": "ACTIVE",
      "sortPriority": 1,
      "id": 11131804
    },
    {
      "adjustmentFactor": 41.972,
      "status": "ACTIVE",
      "sortPriority": 2,
      "id": 11064886
    },
    {
      "adjustmentFactor": 6.006,
      "status": "ACTIVE",
      "sortPriority": 3,
      "id": 11404390
    },
    {
      "adjustmentFactor": 3.635,
      "status": "ACTIVE",
      "sortPriority": 4,
      "id": 11527192
    },
    {
      "adjustmentFactor": 3.129,
      "status": "ACTIVE",
      "sortPriority": 5,
      "id": 14341
    },
    {
      "adjustmentFactor": 0.468,
      "status": "ACTIVE",
      "sortPriority": 6,
      "id": 11530194
    },
    {
      "adjustmentFactor": 0.468,
      "status": "ACTIVE",
      "sortPriority": 7,
      "id": 10257411
    }
  ],
  "regulators": [
    "MR_INT"
  ],
  "venue": "Kempton",
  "countryCode": "GB",
  "discountAllowed": true,
  "timezone": "Europe/London",
  "openDate": "2016-08-17T17:40:00.000Z",
  "version": 1400311331
}
```


---

## Overview

This file is located at `tests/integration_tests/adapters/betfair/resources/streaming/streaming_market_definition.json` within the repository.

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


