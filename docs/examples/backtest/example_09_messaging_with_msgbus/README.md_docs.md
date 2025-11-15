# Documentation: `examples/backtest/example_09_messaging_with_msgbus/README.md`
**Generated:** 2025-11-15T19:40:03.846038Z
**File Size:** 1074 bytes
**Extension:** .md
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

- **Path:** `examples/backtest/example_09_messaging_with_msgbus/README.md`
- **Size:** 1,074 bytes
- **Lines:** 22
- **Extension:** `.md`
- **Type:** text

---

## Source Code

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


---

## Overview

This file is located at `examples/backtest/example_09_messaging_with_msgbus/README.md` within the repository.

This is a Markdown documentation file.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `examples/backtest/example_09_messaging_with_msgbus`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


