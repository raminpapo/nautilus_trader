# Documentation: README.md

## File Metadata

- **Path**: `examples/backtest/example_10_messaging_with_actor_data/README.md`
- **Size**: 653 bytes
- **Lines**: 18
- **Language**: Markdown

## Original Source

```markdown
# Example - Messaging with Actor Data

This example demonstrates how to work with custom data classes
and the Actor's publish/subscribe mechanism in NautilusTrader.

## What You'll Learn

- How to create custom data classes (both serializable and non-serializable).
- How to publish and subscribe to custom data using Actor methods.
- How to handle custom data events in your strategy.

## Implementation Details

The strategy showcases two approaches to custom data classes:

- `Last10BarsStats`: A simple non-serializable data.
- `Last10BarsStatsSerializable`: A serializable data showing proper setup for data persistence and transfer between nodes.

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a Markdown documentation file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 15


**Identifiers**: `Actor`, `Data`, `Details`, `Example`, `How`, `Implementation`, `Last10BarsStats`, `Last10BarsStatsSerializable`, `Learn`, `Messaging`, `NautilusTrader`, `The`, `This`, `What`, `You`

## Related Files

This file is located in `examples/backtest/example_10_messaging_with_actor_data/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest examples/backtest/example_10_messaging_with_actor_data/README.md

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:04.254432Z*
