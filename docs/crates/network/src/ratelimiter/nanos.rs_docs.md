# Documentation: `crates/network/src/ratelimiter/nanos.rs`
**Generated:** 2025-11-15T19:40:03.239008Z
**File Size:** 4026 bytes
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

- **Path:** `crates/network/src/ratelimiter/nanos.rs`
- **Size:** 4,026 bytes
- **Lines:** 162
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 14
- **Functions:** 16

---

## Source Code

```rust
// -------------------------------------------------------------------------------------------------
//  Copyright (C) 2015-2025 Nautech Systems Pty Ltd. All rights reserved.
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

//! A time-keeping abstraction (nanoseconds) that works for storing in an atomic integer.

use std::{
    fmt::Debug,
    ops::{Add, Div, Mul},
    prelude::v1::*,
    time::Duration,
};

use super::clock;

/// A number of nanoseconds from a reference point.
///
/// Nanos can not represent durations >584 years, but hopefully that
/// should not be a problem in real-world applications.
#[derive(PartialEq, Eq, Default, Clone, Copy, PartialOrd, Ord)]
pub struct Nanos(u64);

impl Nanos {
    pub const fn as_u64(self) -> u64 {
        self.0
    }
}

impl Nanos {
    pub const fn new(u: u64) -> Self {
        Self(u)
    }
}

impl From<Duration> for Nanos {
    fn from(d: Duration) -> Self {
        // This will panic:
        Self(
            d.as_nanos()
                .try_into()
                .expect("Duration is longer than 584 years"),
        )
    }
}

impl Debug for Nanos {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> Result<(), std::fmt::Error> {
        let d = Duration::from_nanos(self.0);
        write!(f, "Nanos({d:?})")
    }
}

impl Add<Self> for Nanos {
    type Output = Self;

    fn add(self, rhs: Self) -> Self::Output {
        Self(self.0 + rhs.0)
    }
}

impl Mul<u64> for Nanos {
    type Output = Self;

    fn mul(self, rhs: u64) -> Self::Output {
        Self(self.0 * rhs)
    }
}

impl Div<Self> for Nanos {
    type Output = u64;

    fn div(self, rhs: Self) -> Self::Output {
        self.0 / rhs.0
    }
}

impl From<u64> for Nanos {
    fn from(u: u64) -> Self {
        Self(u)
    }
}

impl From<Nanos> for u64 {
    fn from(n: Nanos) -> Self {
        n.0
    }
}

impl From<Nanos> for Duration {
    fn from(n: Nanos) -> Self {
        Self::from_nanos(n.0)
    }
}

impl Nanos {
    #[inline]
    pub const fn saturating_sub(self, rhs: Self) -> Self {
        Self(self.0.saturating_sub(rhs.0))
    }
}

impl clock::Reference for Nanos {
    #[inline]
    fn duration_since(&self, earlier: Self) -> Nanos {
        (*self as Self).saturating_sub(earlier)
    }

    #[inline]
    fn saturating_sub(&self, duration: Nanos) -> Self {
        (*self as Self).saturating_sub(duration)
    }
}

impl Add<Duration> for Nanos {
    type Output = Self;

    fn add(self, other: Duration) -> Self {
        let other: Self = other.into();
        self + other
    }
}

////////////////////////////////////////////////////////////////////////////////
// Tests
////////////////////////////////////////////////////////////////////////////////
#[cfg(test)]
mod test {
    use std::time::Duration;

    use rstest::rstest;

    use super::*;

    #[rstest]
    fn nanos_impls() {
        let n = Nanos::new(20);
        assert_eq!("Nanos(20ns)", format!("{n:?}"));
    }

    #[rstest]
    fn nanos_arith_coverage() {
        let n = Nanos::new(20);
        let n_half = Nanos::new(10);
        assert_eq!(n / n_half, 2);
        assert_eq!(30, (n + Duration::from_nanos(10)).as_u64());

        assert_eq!(n_half.saturating_sub(n), Nanos::new(0));
        assert_eq!(n.saturating_sub(n_half), n_half);
        assert_eq!(clock::Reference::saturating_sub(&n_half, n), Nanos::new(0));
    }
}
```


---

## Overview

This file is located at `crates/network/src/ratelimiter/nanos.rs` within the repository.

**Classes defined:** Nanos, Nanos, Nanos, From, Debug, Add, Mul, Div, From, From and 4 more

**Functions defined:** as_u64, new, from, fmt, add, mul, div, from, from, from and 6 more


---

## Detailed Analysis

### Classes

#### `Nanos`

**Type:** struct


#### `Nanos`

**Type:** impl


#### `Nanos`

**Type:** impl


#### `From`

**Type:** impl


#### `Debug`

**Type:** impl


#### `Add`

**Type:** impl


#### `Mul`

**Type:** impl


#### `Div`

**Type:** impl


#### `From`

**Type:** impl


#### `From`

**Type:** impl


#### `From`

**Type:** impl


#### `Nanos`

**Type:** impl


#### `clock`

**Type:** impl


#### `Add`

**Type:** impl


### Functions

#### `as_u64(self)`


#### `new(u: u64)`


#### `from(d: Duration)`


#### `fmt(&self, f: &mut std::fmt::Formatter<'_>)`


#### `add(self, rhs: Self)`


#### `mul(self, rhs: u64)`


#### `div(self, rhs: Self)`


#### `from(u: u64)`


#### `from(n: Nanos)`


#### `from(n: Nanos)`


#### `saturating_sub(self, rhs: Self)`


#### `duration_since(&self, earlier: Self)`


#### `saturating_sub(&self, duration: Nanos)`


#### `add(self, other: Duration)`


#### `nanos_impls()`


#### `nanos_arith_coverage()`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/network/src/ratelimiter`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


