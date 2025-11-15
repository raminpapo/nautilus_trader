# Documentation: `scripts/test-examples.sh`
**Generated:** 2025-11-15T19:40:05.531157Z
**File Size:** 985 bytes
**Extension:** .sh
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

- **Path:** `scripts/test-examples.sh`
- **Size:** 985 bytes
- **Lines:** 36
- **Extension:** `.sh`
- **Type:** text

---

## Source Code

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


---

## Overview

This file is located at `scripts/test-examples.sh` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `scripts`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


