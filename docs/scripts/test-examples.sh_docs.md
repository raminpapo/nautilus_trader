# Documentation: test-examples.sh

## File Metadata

- **Path**: `scripts/test-examples.sh`
- **Size**: 985 bytes
- **Lines**: 37
- **Language**: Shell

## Original Source

```bash
#!/bin/bash
# Fail fast
set -e

# Backtest examples
example_scripts=(
  "crypto_ema_cross_ethusdt_trade_ticks.py"
  "crypto_ema_cross_ethusdt_trailing_stop.py"
  "fx_ema_cross_audusd_bars_from_ticks.py"
  "fx_ema_cross_bracket_gbpusd_bars_external.py"
  "fx_ema_cross_bracket_gbpusd_bars_internal.py"
  "fx_market_maker_gbpusd_bars.py"
)

total_runtime=0
for script in "${example_scripts[@]}"; do
  start_time=$(date +%s)

  # Run the backtest script
  chmod +x "examples/backtest/$script"
  yes | python "examples/backtest/$script"

  # Get the exit status of the last example run
  exit_status=$?

  # Check if the exit status is 0 (success)
  if [ $exit_status -eq 0 ]; then
    end_time=$(date +%s)
    runtime=$((end_time - start_time))
    echo "$script finished successfully in $runtime seconds"
    total_runtime=$((total_runtime + runtime))
  else
    echo "$script failed with exit status $exit_status."
  fi
done
echo "Total runtime of all examples: $total_runtime seconds"

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 6


**Identifiers**: `Backtest`, `Check`, `Fail`, `Get`, `Run`, `Total`

## Related Files

This file is located in `scripts/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest scripts/test-examples.sh

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.167942Z*
