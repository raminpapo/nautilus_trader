# Documentation: `tests/integration_tests/adapters/betfair/resources/streaming/streaming_market_definition_racing.json`
**Generated:** 2025-11-15T19:40:07.496067Z
**File Size:** 6999 bytes
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

- **Path:** `tests/integration_tests/adapters/betfair/resources/streaming/streaming_market_definition_racing.json`
- **Size:** 6,999 bytes
- **Lines:** 315
- **Extension:** `.json`
- **Type:** text

---

## Source Code

```json
{
  "op": "mcm",
  "id": 1,
  "initialClk": "mBzWkfrZC6Yci8vz5QudHPKO1d0L",
  "clk": "AAAAAAAA",
  "conflateMs": 0,
  "heartbeatMs": 5000,
  "pt": 1617253902641,
  "ct": "SUB_IMAGE",
  "mc": [
    {
      "id": "1.180737206",
      "rc": [
        {
          "id": 19248890,
          "atb": [
            [
              46.0,
              3.0
            ]
          ],
          "atl": null,
          "batb": null,
          "batl": null,
          "bdatb": null,
          "bdatl": null,
          "spb": null,
          "spl": null,
          "spn": null,
          "spf": null,
          "trd": null,
          "ltp": 0.0,
          "tv": 0.0,
          "hc": null
        },
        {
          "id": 38848248,
          "atb": [
            [
              2.54,
              7.95
            ]
          ],
          "atl": [
            [
              2.72,
              8.8
            ]
          ],
          "batb": null,
          "batl": null,
          "bdatb": null,
          "bdatl": null,
          "spb": null,
          "spl": null,
          "spn": null,
          "spf": null,
          "trd": null,
          "ltp": 0.0,
          "tv": 0.0,
          "hc": null
        },
        {
          "id": 10921178,
          "atb": [
            [
              4.6,
              3.69
            ]
          ],
          "atl": [
            [
              980.0,
              22.72
            ]
          ],
          "batb": null,
          "batl": null,
          "bdatb": null,
          "bdatl": null,
          "spb": null,
          "spl": null,
          "spn": null,
          "spf": null,
          "trd": null,
          "ltp": 0.0,
          "tv": 0.0,
          "hc": null
        },
        {
          "id": 3601619,
          "atb": [
            [
              5.8,
              3.44
            ]
          ],
          "atl": [
            [
              980.0,
              22.72
            ]
          ],
          "batb": null,
          "batl": null,
          "bdatb": null,
          "bdatl": null,
          "spb": null,
          "spl": null,
          "spn": null,
          "spf": null,
          "trd": null,
          "ltp": 0.0,
          "tv": 0.0,
          "hc": null
        },
        {
          "id": 13388439,
          "atb": [
            [
              1.8,
              21.32
            ]
          ],
          "atl": [
            [
              2.18,
              48.28
            ]
          ],
          "batb": null,
          "batl": null,
          "bdatb": null,
          "bdatl": null,
          "spb": null,
          "spl": null,
          "spn": null,
          "spf": null,
          "trd": null,
          "ltp": 0.0,
          "tv": 0.0,
          "hc": null
        },
        {
          "id": 35510787,
          "atb": [
            [
              4.6,
              3.69
            ]
          ],
          "atl": [
            [
              130.0,
              22.72
            ]
          ],
          "batb": null,
          "batl": null,
          "bdatb": null,
          "bdatl": null,
          "spb": null,
          "spl": null,
          "spn": null,
          "spf": null,
          "trd": null,
          "ltp": 0.0,
          "tv": 0.0,
          "hc": null
        },
        {
          "id": 10147870,
          "atb": [
            [
              42.0,
              3.0
            ]
          ],
          "atl": null,
          "batb": null,
          "batl": null,
          "bdatb": null,
          "bdatl": null,
          "spb": null,
          "spl": null,
          "spn": null,
          "spf": null,
          "trd": null,
          "ltp": 0.0,
          "tv": 0.0,
          "hc": null
        }
      ],
      "con": null,
      "img": true,
      "marketDefinition": {
        "betDelay": 0,
        "bettingType": "ODDS",
        "bspMarket": true,
        "bspReconciled": false,
        "competitionId": null,
        "competitionName": "",
        "complete": true,
        "countryCode": "GB",
        "crossMatching": false,
        "discountAllowed": true,
        "eachWayDivisor": null,
        "eventId": "30361178",
        "eventName": "",
        "eventTypeId": 7,
        "inPlay": false,
        "keyLineDefinition": null,
        "lineInterval": null,
        "lineMaxUnit": null,
        "lineMinUnit": null,
        "marketBaseRate": 5.0,
        "marketId": "",
        "marketName": "",
        "marketTime": "2021-03-19T12:07:00+10:00",
        "marketType": "WIN",
        "name": null,
        "numberOfActiveRunners": 7,
        "numberOfWinners": 1,
        "openDate": "2021-03-19T12:07:00+10:00",
        "persistenceEnabled": true,
        "priceLadderDefinition": null,
        "raceType": null,
        "regulators": [
          "MR_INT"
        ],
        "runners": [
          {
            "sortPriority": 1,
            "id": 19248890,
            "name": null,
            "hc": null,
            "status": "ACTIVE",
            "adjustmentFactor": 44.323,
            "bsp": null,
            "removalDate": null
          },
          {
            "sortPriority": 2,
            "id": 38848248,
            "name": null,
            "hc": null,
            "status": "ACTIVE",
            "adjustmentFactor": 41.972,
            "bsp": null,
            "removalDate": null
          },
          {
            "sortPriority": 3,
            "id": 10921178,
            "name": null,
            "hc": null,
            "status": "ACTIVE",
            "adjustmentFactor": 6.006,
            "bsp": null,
            "removalDate": null
          },
          {
            "sortPriority": 4,
            "id": 3601619,
            "name": null,
            "hc": null,
            "status": "ACTIVE",
            "adjustmentFactor": 3.635,
            "bsp": null,
            "removalDate": null
          },
          {
            "sortPriority": 5,
            "id": 13388439,
            "name": null,
            "hc": null,
            "status": "ACTIVE",
            "adjustmentFactor": 3.129,
            "bsp": null,
            "removalDate": null
          },
          {
            "sortPriority": 6,
            "id": 35510787,
            "name": null,
            "hc": null,
            "status": "ACTIVE",
            "adjustmentFactor": 0.468,
            "bsp": null,
            "removalDate": null
          },
          {
            "sortPriority": 7,
            "id": 10147870,
            "name": null,
            "hc": null,
            "status": "ACTIVE",
            "adjustmentFactor": 0.468,
            "bsp": null,
            "removalDate": null
          }
        ],
        "runnersVoidable": false,
        "settledTime": null,
        "status": "OPEN",
        "suspendTime": "2021-03-19T12:07:00+10:00",
        "timezone": "Europe/London",
        "turnInPlayEnabled": true,
        "venue": "Kempton",
        "version": 1400311331
      },
      "tv": 0.0
    }
  ]
}
```


---

## Overview

This file is located at `tests/integration_tests/adapters/betfair/resources/streaming/streaming_market_definition_racing.json` within the repository.

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


