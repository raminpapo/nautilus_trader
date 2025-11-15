# Documentation: `tests/integration_tests/adapters/betfair/resources/streaming/streaming_mcm_SUB_IMAGE.json`
**Generated:** 2025-11-15T19:40:07.506355Z
**File Size:** 4090 bytes
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

- **Path:** `tests/integration_tests/adapters/betfair/resources/streaming/streaming_mcm_SUB_IMAGE.json`
- **Size:** 4,090 bytes
- **Lines:** 200
- **Extension:** `.json`
- **Type:** text

---

## Source Code

```json
{
  "op": "mcm",
  "id": 2,
  "initialClk": "ab34r43r",
  "clk": "AAAAAAAA",
  "conflateMs": 0,
  "heartbeatMs": 5000,
  "pt": 1471370159007,
  "ct": "SUB_IMAGE",
  "mc": [
    {
      "id": "1.180737206",
      "marketDefinition": {
        "bspMarket": true,
        "turnInPlayEnabled": true,
        "persistenceEnabled": true,
        "marketBaseRate": 5,
        "eventId": "30361178",
        "eventTypeId": "7",
        "numberOfWinners": 1,
        "bettingType": "ODDS",
        "marketType": "WIN",
        "marketTime": "2021-03-19T12:07:00+10:00",
        "suspendTime": "2021-03-19T12:07:00+10:00",
        "bspReconciled": false,
        "complete": true,
        "inPlay": false,
        "crossMatching": false,
        "runnersVoidable": false,
        "numberOfActiveRunners": 7,
        "betDelay": 0,
        "status": "OPEN",
        "runners": [
          {
            "adjustmentFactor": 44.323,
            "status": "ACTIVE",
            "sortPriority": 1,
            "id": "19248890"
          },
          {
            "adjustmentFactor": 41.972,
            "status": "ACTIVE",
            "sortPriority": 2,
            "id": "38848248"
          },
          {
            "adjustmentFactor": 6.006,
            "status": "ACTIVE",
            "sortPriority": 3,
            "id": "10921178"
          },
          {
            "adjustmentFactor": 3.635,
            "status": "ACTIVE",
            "sortPriority": 4,
            "id": "3601619"
          },
          {
            "adjustmentFactor": 3.129,
            "status": "ACTIVE",
            "sortPriority": 5,
            "id": "13388439"
          },
          {
            "adjustmentFactor": 0.468,
            "status": "ACTIVE",
            "sortPriority": 6,
            "id": "35510787"
          },
          {
            "adjustmentFactor": 0.468,
            "status": "ACTIVE",
            "sortPriority": 7,
            "id": "10147870"
          }
        ],
        "regulators": [
          "MR_INT"
        ],
        "venue": "Kempton",
        "countryCode": "GB",
        "discountAllowed": true,
        "timezone": "Europe/London",
        "openDate": "2021-03-19T12:07:00+10:00",
        "version": 1400311331
      },
      "rc": [
        {
          "atb": [
            [
              46,
              3
            ]
          ],
          "ltp": 0,
          "tv": 0,
          "id": "19248890"
        },
        {
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
          "ltp": 0,
          "tv": 0,
          "id": "38848248"
        },
        {
          "atb": [
            [
              4.6,
              3.69
            ]
          ],
          "atl": [
            [
              980,
              22.72
            ]
          ],
          "ltp": 0,
          "tv": 0,
          "id": "10921178"
        },
        {
          "atb": [
            [
              5.8,
              3.44
            ]
          ],
          "atl": [
            [
              980,
              22.72
            ]
          ],
          "ltp": 0,
          "tv": 0,
          "id": "3601619"
        },
        {
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
          "ltp": 0,
          "tv": 0,
          "id": "13388439"
        },
        {
          "atb": [
            [
              4.6,
              3.69
            ]
          ],
          "atl": [
            [
              130,
              22.72
            ]
          ],
          "ltp": 0,
          "tv": 0,
          "id": "35510787"
        },
        {
          "atb": [
            [
              42,
              3
            ]
          ],
          "ltp": 0,
          "tv": 0,
          "id": "10147870"
        }
      ],
      "img": true,
      "tv": 0
    }
  ]
}
```


---

## Overview

This file is located at `tests/integration_tests/adapters/betfair/resources/streaming/streaming_mcm_SUB_IMAGE.json` within the repository.

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


