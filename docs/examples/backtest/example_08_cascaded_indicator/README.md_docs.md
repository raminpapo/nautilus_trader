# Documentation: README.md

## File Metadata

- **Path**: `examples/backtest/example_08_cascaded_indicator/README.md`
- **Size**: 839 bytes
- **Lines**: 17
- **Language**: Markdown

## Original Source

```markdown
# Example: Using cascaded technical indicators

This example demonstrates how to use cascaded technical indicators in a **NautilusTrader** strategy.

The example shows how to set up and use two Exponential Moving Average (EMA) indicators in a cascaded manner,
where the second indicator (EMA-20) is calculated using values from the first indicator (EMA-10),
demonstrating proper initialization, updating, and accessing indicator values in a cascaded setup.

**What this example demonstrates:**

- Creating and configuring multiple technical indicators (EMAs).
- Setting up a cascaded indicator relationship.
- Registering the primary indicator to receive bar data.
- Manually updating the cascaded indicator.
- Storing and accessing historical values for both indicators.
- Proper handling of indicator initialization in a cascaded setup.

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a Markdown documentation file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 17


**Identifiers**: `Average`, `Creating`, `EMA`, `EMAs`, `Example`, `Exponential`, `Manually`, `Moving`, `NautilusTrader`, `Proper`, `Registering`, `Setting`, `Storing`, `The`, `This`, `Using`, `What`

## Related Files

This file is located in `examples/backtest/example_08_cascaded_indicator/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest examples/backtest/example_08_cascaded_indicator/README.md

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:04.246495Z*
