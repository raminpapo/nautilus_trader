# Documentation: README.md

## File Metadata

- **Path**: `examples/backtest/example_11_messaging_with_actor_signals/README.md`
- **Size**: 669 bytes
- **Lines**: 17
- **Language**: Markdown

## Original Source

```markdown
# Actor-Based Signal Messaging Example

This example demonstrates the simplest form of messaging in NautilusTrader using *actor-based signals*.
It shows how to implement lightweight notifications between components using *string-based signals*.

## What You'll Learn

- How to use signals for simple notifications (price extremes in this case).
- How to publish signals with single string values.
- How to subscribe to signals and handle them in `on_signal` callback.

## Implementation Highlights

- Uses `SimpleNamespace` for signal name constants.
- Shows both signal publishing and subscription.
- Demonstrates signal handling with pattern matching in `on_signal`.

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a Markdown documentation file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 17


**Identifiers**: `Actor`, `Based`, `Demonstrates`, `Example`, `Highlights`, `How`, `Implementation`, `Learn`, `Messaging`, `NautilusTrader`, `Shows`, `Signal`, `SimpleNamespace`, `This`, `Uses`, `What`, `You`

## Related Files

This file is located in `examples/backtest/example_11_messaging_with_actor_signals/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest examples/backtest/example_11_messaging_with_actor_signals/README.md

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:04.258546Z*
