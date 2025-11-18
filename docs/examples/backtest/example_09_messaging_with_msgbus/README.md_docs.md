# Documentation: README.md

## File Metadata

- **Path**: `examples/backtest/example_09_messaging_with_msgbus/README.md`
- **Size**: 1,074 bytes
- **Lines**: 23
- **Language**: Markdown

## Original Source

```markdown
# Example: Self-Communication Using Message Bus

A practical demonstration of using NautilusTrader's message bus for self-communication within a strategy.
The example implements a "10th bar notification system" where the strategy:

1. Creates a custom event (using Python's dataclass) to represent the 10th bar occurrence.
2. Publishes this event to the message bus when the 10th bar arrives.
3. Subscribes to and handles these events within the same strategy.

**Key learning points**:

- Creating custom events with the message bus.
- Implementing publish/subscribe pattern for self-communication.
- Using events for condition-based notifications.
- Handling state changes through message bus events.

This pattern provides a clean, event-driven approach to handle conditional notifications
and state changes within your trading strategies.

**Note:**
While this example shows both publisher and subscriber roles within a single strategy, in practice these roles
can be distributed - any component can be a publisher and any other component can be a subscriber of events.

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a Markdown documentation file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 19


**Identifiers**: `Bus`, `Communication`, `Creates`, `Creating`, `Example`, `Handling`, `Implementing`, `Key`, `Message`, `NautilusTrader`, `Note`, `Publishes`, `Python`, `Self`, `Subscribes`, `The`, `This`, `Using`, `While`

## Related Files

This file is located in `examples/backtest/example_09_messaging_with_msgbus/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest examples/backtest/example_09_messaging_with_msgbus/README.md

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:04.250442Z*
