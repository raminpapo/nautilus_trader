# Documentation: matching.rs

## File Metadata

- **Path**: `crates/common/src/msgbus/matching.rs`
- **Size**: 2,714 bytes
- **Lines**: 74
- **Language**: Rust

## Original Source

```rust
// -------------------------------------------------------------------------------------------------
//  Copyright (C) 2015-2025 2Nautech Systems Pty Ltd. All rights reserved.
//  https://nautechsystems.io
//
//  Licensed under the GNU Lesser General Public License Version 3.0 (the "License");
//  You may not use this file except in compliance with the License.
//  You may obtain a copy of the License at https://www.gnu.org/licenses/lgpl-3.0.en.html
//
//  Unless required by applicable law or agreed to in writing, software
//  distributed under the License is distributed on an "AS IS" BASIS,
//  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//  See the License for the specific language governing permissions and
//  limitations under the License.
// -------------------------------------------------------------------------------------------------

use super::core::{MStr, Pattern, Topic};

/// Match a topic and a string pattern using iterative backtracking algorithm
/// pattern can contains -
/// '*' - match 0 or more characters after this
/// '?' - match any character once
/// 'a-z' - match the specific character
pub fn is_matching_backtracking(topic: MStr<Topic>, pattern: MStr<Pattern>) -> bool {
    let topic_bytes = topic.as_bytes();
    let pattern_bytes = pattern.as_bytes();

    is_matching(topic_bytes, pattern_bytes)
}

#[must_use]
pub fn is_matching(topic: &[u8], pattern: &[u8]) -> bool {
    // Stack to store states for backtracking (topic_idx, pattern_idx)
    let mut stack = vec![(0, 0)];

    while let Some((mut i, mut j)) = stack.pop() {
        loop {
            // Found a match if we've consumed both strings
            if i == topic.len() && j == pattern.len() {
                return true;
            }

            // If we've reached the end of the pattern, break to try other paths
            if j == pattern.len() {
                break;
            }

            // Handle '*' wildcard
            if pattern[j] == b'*' {
                // Try skipping '*' entirely first
                stack.push((i, j + 1));

                // Continue with matching current character and keeping '*'
                if i < topic.len() {
                    i += 1;
                    continue;
                }
                break;
            }
            // Handle '?' or exact character match
            else if i < topic.len() && (pattern[j] == b'?' || topic[i] == pattern[j]) {
                // Continue matching linearly without stack operations
                i += 1;
                j += 1;
                continue;
            }

            // No match found in current path
            break;
        }
    }

    false
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 2 function(s).

## Detailed Walkthrough

### Functions
- **`is_matching_backtracking()`**: Function defined in this file
- **`is_matching()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 2


**Functions**: `is_matching`, `is_matching_backtracking`

## Related Files

This file is located in `crates/common/src/msgbus/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

Tests for this file may be located in:
- `tests/` directory in the same folder
- Corresponding test module in the project

Run the full test suite to verify functionality.

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:01.227587Z*
