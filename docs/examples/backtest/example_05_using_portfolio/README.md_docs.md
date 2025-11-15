# Documentation: `examples/backtest/example_05_using_portfolio/README.md`
**Generated:** 2025-11-15T19:40:03.829744Z
**File Size:** 1660 bytes
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

- **Path:** `examples/backtest/example_05_using_portfolio/README.md`
- **Size:** 1,660 bytes
- **Lines:** 44
- **Extension:** `.md`
- **Type:** text

---

## Source Code

```markdown
# Portfolio Example

A simple strategy demonstrating how to use Portfolio in NautilusTrader.

The Portfolio is a central component that tracks the state of your trading account.
It connects directly to the broker to get real-time positions, balances, and P&L.

## Example Highlights

The strategy shows portfolio information at four key points:

1. **Initial State**: Before any trades are executed.
2. **Position Open**: When a new position is created.
3. **Mid-Trade**: Two minutes after position opening.
4. **Final State**: After all positions are closed (when strategy stops).

To simulate these specific portfolio states, the strategy fires bracket order (a combination of an entry order
with associated take-profit and stop-loss orders), allowing us to demonstrate the complete lifecycle of portfolio states.

## Additional info

Key differences between `Portfolio` and `Cache`:

`Portfolio`:

- Gets data directly from broker for maximum accuracy.
- Best for real-time position and risk management.
- Provides authoritative account state (margins, balances).
- Should be used for critical trading decisions.

`Cache`:

- Stores all trading data in system memory.
- Useful for quick access to historical data and market state.
- More efficient for frequent queries as it avoids broker round-trips.
- Updates automatically as new data arrives.
- Might have minimal delay compared to broker data.

## Additional Resources

For more information about Portfolio in NautilusTrader, see:

- Portfolio API documentation - search the codebase for `Portfolio` class.
- Portfolio concept guide - see the "Portfolio" section in the documentation for more details.
```


---

## Overview

This file is located at `examples/backtest/example_05_using_portfolio/README.md` within the repository.

This is a Markdown documentation file.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `examples/backtest/example_05_using_portfolio`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: auth. Ensure proper handling of secrets.

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


