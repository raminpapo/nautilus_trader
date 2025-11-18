# Documentation: streaming_ocm_multiple_fills.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/betfair/resources/streaming/streaming_ocm_multiple_fills.json`
- **Size**: 3,409 bytes
- **Lines**: 149
- **Language**: JSON

## Original Source

```json
[
  {
    "op": "ocm",
    "id": 2,
    "clk": "AITUAgDRrQIAqswCAJp6AKWMAg==",
    "pt": 1633905758394,
    "oc": [
      {
        "id": "1.179082386",
        "orc": [
          {
            "id": 50210,
            "uo": [
              {
                "id": "229435133092",
                "p": 5.8,
                "s": 20,
                "side": "B",
                "status": "E",
                "pt": "P",
                "ot": "L",
                "pd": 1633905366000,
                "md": 1633905758000,
                "avp": 5.8,
                "sm": 16.19,
                "sr": 3.809999999999999,
                "sl": 0,
                "sc": 0,
                "sv": 0,
                "rac": "",
                "rc": "REG_LGA",
                "rfo": "O-20211010-223605-000",
                "rfs": "TestStrategy-1."
              }
            ],
            "smc": {
              "TestStrategy-1.": {
                "mb": [
                  [
                    5.8,
                    16.19
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
    "clk": "AI3UAgDVrQIAsswCAJ56ALSMAg==",
    "pt": 1633905758690,
    "oc": [
      {
        "id": "1.179082386",
        "orc": [
          {
            "id": 50210,
            "uo": [
              {
                "id": "229435133092",
                "p": 5.8,
                "s": 20,
                "side": "B",
                "status": "E",
                "pt": "P",
                "ot": "L",
                "pd": 1633905366000,
                "md": 1633905758000,
                "avp": 5.8,
                "sm": 16.96,
                "sr": 3.039999999999999,
                "sl": 0,
                "sc": 0,
                "sv": 0,
                "rac": "",
                "rc": "REG_LGA",
                "rfo": "O-20211010-223605-000",
                "rfs": "TestStrategy-1."
              }
            ],
            "smc": {
              "TestStrategy-1.": {
                "mb": [
                  [
                    5.8,
                    16.96
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
    "clk": "AJfUAgDhrQIAvcwCAKB6AMSMAg==",
    "pt": 1633905759092,
    "oc": [
      {
        "id": "1.179082386",
        "orc": [
          {
            "id": 50210,
            "uo": [
              {
                "id": "229435133092",
                "p": 5.8,
                "s": 20,
                "side": "B",
                "status": "E",
                "pt": "P",
                "ot": "L",
                "pd": 1633905366000,
                "md": 1633905759000,
                "avp": 5.800000000000001,
                "sm": 17.73,
                "sr": 2.269999999999999,
                "sl": 0,
                "sc": 0,
                "sv": 0,
                "rac": "",
                "rc": "REG_LGA",
                "rfo": "O-20211010-223605-000",
                "rfs": "TestStrategy-1."
              }
            ],
            "smc": {
              "TestStrategy-1.": {
                "mb": [
                  [
                    5.8,
                    17.73
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

Total unique keywords extracted: 5


**Identifiers**: `AI3UAgDVrQIAsswCAJ56ALSMAg`, `AITUAgDRrQIAqswCAJp6AKWMAg`, `AJfUAgDhrQIAvcwCAKB6AMSMAg`, `REG_LGA`, `TestStrategy`

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
pytest tests/integration_tests/adapters/betfair/resources/streaming/streaming_ocm_multiple_fills.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.552175Z*
