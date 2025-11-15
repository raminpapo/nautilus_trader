# Documentation: `crates/common/src/msgbus/matching.rs`
**Generated:** 2025-11-15T19:40:01.791514Z
**File Size:** 2714 bytes
**Extension:** .rs
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

- **Path:** `crates/common/src/msgbus/matching.rs`
- **Size:** 2,714 bytes
- **Lines:** 73
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 2

---

## Source Code

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


---

## Overview

This file is located at `crates/common/src/msgbus/matching.rs` within the repository.

**Functions defined:** is_matching_backtracking, is_matching


---

## Detailed Analysis

### Functions

#### `is_matching_backtracking(topic: MStr<Topic>, pattern: MStr<Pattern>)`


#### `is_matching(topic: &[u8], pattern: &[u8])`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/common/src/msgbus`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


