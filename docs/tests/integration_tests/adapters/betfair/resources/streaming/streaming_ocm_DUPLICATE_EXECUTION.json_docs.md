# Documentation: streaming_ocm_DUPLICATE_EXECUTION.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/betfair/resources/streaming/streaming_ocm_DUPLICATE_EXECUTION.json`
- **Size**: 4,615 bytes
- **Lines**: 207
- **Language**: JSON

## Original Source

```json
[
  {
    "op": "ocm",
    "id": 2,
    "clk": "AOQXAPMdAJQWANAfAIQd",
    "pt": 1618710654660,
    "oc": [
      {
        "id": "1.180604981",
        "orc": [
          {
            "id": 1209555,
            "uo": [
              {
                "id": "230486317487",
                "p": 1.75,
                "s": 10,
                "side": "L",
                "status": "E",
                "pt": "P",
                "ot": "L",
                "pd": 1618710649000,
                "md": 1618710654000,
                "avp": 1.73,
                "sm": 1.12,
                "sr": 8.879999999999999,
                "sl": 0,
                "sc": 0,
                "sv": 0,
                "rac": "",
                "rc": "REG_LGA",
                "rfo": "O-20210418-015047-001-001-3",
                "rfs": "Test-001"
              }
            ],
            "ml": [
              [
                1.73,
                1.12
              ]
            ],
            "smc": {
              "Test-001": {
                "ml": [
                  [
                    1.73,
                    1.12
                  ]
                ]
              }
            }
          }
        ]
      }
    ]
  },
  {
    "op": "ocm",
    "id": 2,
    "clk": "AOAYAPUeAPMWANsgAOsd",
    "pt": 1618710658760,
    "oc": [
      {
        "id": "1.180604981",
        "orc": [
          {
            "id": 1209555,
            "uo": [
              {
                "id": "230486317487",
                "p": 1.75,
                "s": 10,
                "side": "L",
                "status": "EC",
                "pt": "P",
                "ot": "L",
                "pd": 1618710649000,
                "md": 1618710654000,
                "avp": 1.73,
                "sm": 1.12,
                "sr": 0,
                "sl": 0,
                "sc": 8.88,
                "sv": 0,
                "rac": "",
                "rc": "REG_LGA",
                "rfo": "O-20210418-015047-001-001-3",
                "rfs": "Test-001",
                "cd": 1618710658000
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "op": "ocm",
    "id": 2,
    "clk": "AJuJAwD5rgMAyPgCANqpAwD7oAQ=",
    "pt": 1618712776369,
    "oc": [
      {
        "id": "1.180604981",
        "orc": [
          {
            "id": 1209555,
            "uo": [
              {
                "id": "230487922962",
                "p": 2.88,
                "s": 10,
                "side": "B",
                "status": "E",
                "pt": "P",
                "ot": "L",
                "pd": 1618712771000,
                "md": 1618712776000,
                "avp": 3.1,
                "sm": 1.86,
                "sr": 8.14,
                "sl": 0,
                "sc": 0,
                "sv": 0,
                "rac": "",
                "rc": "REG_LGA",
                "rfo": "O-20210418-022610-001-001-19",
                "rfs": "Kobe-001"
              }
            ],
            "mb": [
              [
                3.1,
                1.86
              ]
            ],
            "smc": {
              "Kobe-001": {
                "mb": [
                  [
                    3.1,
                    1.86
                  ]
                ]
              }
            }
          }
        ]
      }
    ]
  },
  {
    "op": "ocm",
    "id": 2,
    "clk": "ALqJAwCRrwMA3vgCAPSpAwCaoQQ=",
    "pt": 1618712777299,
    "oc": [
      {
        "id": "1.180604981",
        "orc": [
          {
            "id": 1209555,
            "uo": [
              {
                "id": "230487922962",
                "p": 2.88,
                "s": 10,
                "side": "B",
                "status": "EC",
                "pt": "P",
                "ot": "L",
                "pd": 1618712771000,
                "md": 1618712777000,
                "avp": 2.9209199999999997,
                "sm": 10,
                "sr": 0,
                "sl": 0,
                "sc": 0,
                "sv": 0,
                "rac": "",
                "rc": "REG_LGA",
                "rfo": "O-20210418-022610-001-001-19",
                "rfs": "Kobe-001"
              }
            ],
            "mb": [
              [
                2.88,
                8.14
              ]
            ],
            "smc": {
              "Kobe-001": {
                "mb": [
                  [
                    2.88,
                    8.14
                  ]
                ]
              }
            }
          }
        ]
      }
    ]
  }
]
```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 7


**Identifiers**: `AJuJAwD5rgMAyPgCANqpAwD7oAQ`, `ALqJAwCRrwMA3vgCAPSpAwCaoQQ`, `AOAYAPUeAPMWANsgAOsd`, `AOQXAPMdAJQWANAfAIQd`, `Kobe`, `REG_LGA`, `Test`

## Related Files

This file is located in `tests/integration_tests/adapters/betfair/resources/streaming/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/betfair/resources/streaming/streaming_ocm_DUPLICATE_EXECUTION.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.526469Z*
