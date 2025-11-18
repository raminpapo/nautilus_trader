# Documentation: README.md

## File Metadata

- **Path**: `examples/backtest/example_05_using_portfolio/README.md`
- **Size**: 1,660 bytes
- **Lines**: 45
- **Language**: Markdown

## Original Source

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

## High-Level Overview

This file is part of the NautilusTrader repository. This is a Markdown documentation file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 31


**Identifiers**: `API`, `Additional`, `After`, `Before`, `Best`, `Cache`, `Example`, `Final`, `For`, `Gets`, `Highlights`, `Initial`, `Key`, `Mid`, `Might`, `More`, `NautilusTrader`, `Open`, `Portfolio`, `Position`, `Provides`, `Resources`, `Should`, `State`, `Stores`, `The`, `Trade`, `Two`, `Updates`, `Useful` *(+1 more)*

## Related Files

This file is located in `examples/backtest/example_05_using_portfolio/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest examples/backtest/example_05_using_portfolio/README.md

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:04.233642Z*
