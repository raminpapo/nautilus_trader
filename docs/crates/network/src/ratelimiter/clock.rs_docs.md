# Documentation: `crates/network/src/ratelimiter/clock.rs`
**Generated:** 2025-11-15T19:40:03.231874Z
**File Size:** 6381 bytes
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

- **Path:** `crates/network/src/ratelimiter/clock.rs`
- **Size:** 6,381 bytes
- **Lines:** 208
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 10
- **Functions:** 15

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

//! Time sources for rate limiters.
//!
//! The time sources contained in this module allow the rate limiter
//! to be (optionally) independent of std, and additionally
//! allow mocking the passage of time.
//!
//! You can supply a custom time source by implementing both [`Reference`]
//! and [`Clock`] for your own types, and by implementing `Add<Nanos>` for
//! your [`Reference`] type:
use std::{
    fmt::Debug,
    ops::Add,
    prelude::v1::*,
    sync::{
        Arc,
        atomic::{AtomicU64, Ordering},
    },
    time::{Duration, Instant},
};

use super::nanos::Nanos;

/// A measurement from a clock.
pub trait Reference:
    Sized + Add<Nanos, Output = Self> + PartialEq + Eq + Ord + Copy + Clone + Send + Sync + Debug
{
    /// Determines the time that separates two measurements of a
    /// clock. Implementations of this must perform a saturating
    /// subtraction - if the `earlier` timestamp should be later,
    /// `duration_since` must return the zero duration.
    fn duration_since(&self, earlier: Self) -> Nanos;

    /// Returns a reference point that lies at most `duration` in the
    /// past from the current reference. If an underflow should occur,
    /// returns the current reference.
    fn saturating_sub(&self, duration: Nanos) -> Self;
}

/// A time source used by rate limiters.
pub trait Clock: Clone {
    /// A measurement of a monotonically increasing clock.
    type Instant: Reference;

    /// Returns a measurement of the clock.
    fn now(&self) -> Self::Instant;
}

impl Reference for Duration {
    /// The internal duration between this point and another.
    fn duration_since(&self, earlier: Self) -> Nanos {
        self.checked_sub(earlier)
            .unwrap_or_else(|| Self::new(0, 0))
            .into()
    }

    /// The internal duration between this point and another.
    fn saturating_sub(&self, duration: Nanos) -> Self {
        self.checked_sub(duration.into()).unwrap_or(*self)
    }
}

impl Add<Nanos> for Duration {
    type Output = Self;

    fn add(self, other: Nanos) -> Self {
        let other: Self = other.into();
        self + other
    }
}

/// A mock implementation of a clock. All it does is keep track of
/// what "now" is (relative to some point meaningful to the program),
/// and returns that.
///
/// # Thread safety
/// The mock time is represented as an atomic u64 count of nanoseconds, behind an [`Arc`].
/// Clones of this clock will all show the same time, even if the original advances.
#[derive(Debug, Clone, Default)]
pub struct FakeRelativeClock {
    now: Arc<AtomicU64>,
}

impl FakeRelativeClock {
    /// Advances the fake clock by the given amount.
    ///
    /// # Panics
    ///
    /// Panics if `by` cannot be represented as a `u64` number of nanoseconds (i.e., exceeds 584 years).
    pub fn advance(&self, by: Duration) {
        let by: u64 = by
            .as_nanos()
            .try_into()
            .expect("Cannot represent durations greater than 584 years");

        let mut prev = self.now.load(Ordering::Acquire);
        let mut next = prev + by;
        while let Err(e) =
            self.now
                .compare_exchange_weak(prev, next, Ordering::Release, Ordering::Relaxed)
        {
            prev = e;
            next = prev + by;
        }
    }
}

impl PartialEq for FakeRelativeClock {
    fn eq(&self, other: &Self) -> bool {
        self.now.load(Ordering::Relaxed) == other.now.load(Ordering::Relaxed)
    }
}

impl Clock for FakeRelativeClock {
    type Instant = Nanos;

    fn now(&self) -> Self::Instant {
        self.now.load(Ordering::Relaxed).into()
    }
}

/// The monotonic clock implemented by [`Instant`].
#[derive(Clone, Debug, Default)]
pub struct MonotonicClock;

impl Add<Nanos> for Instant {
    type Output = Self;

    fn add(self, other: Nanos) -> Self {
        let other: Duration = other.into();
        self + other
    }
}

impl Reference for Instant {
    fn duration_since(&self, earlier: Self) -> Nanos {
        if earlier < *self {
            (*self - earlier).into()
        } else {
            Nanos::from(Duration::new(0, 0))
        }
    }

    fn saturating_sub(&self, duration: Nanos) -> Self {
        self.checked_sub(duration.into()).unwrap_or(*self)
    }
}

impl Clock for MonotonicClock {
    type Instant = Instant;

    fn now(&self) -> Self::Instant {
        Instant::now()
    }
}

////////////////////////////////////////////////////////////////////////////////
// Tests
////////////////////////////////////////////////////////////////////////////////
#[cfg(test)]
mod test {
    use std::{sync::Arc, thread, time::Duration};

    use rstest::rstest;

    use super::*;

    #[rstest]
    fn fake_clock_parallel_advances() {
        let clock = Arc::new(FakeRelativeClock::default());
        let threads = std::iter::repeat_n((), 10)
            .map(move |()| {
                let clock = Arc::clone(&clock);
                thread::spawn(move || {
                    for _ in 0..1_000_000 {
                        let now = clock.now();
                        clock.advance(Duration::from_nanos(1));
                        assert!(clock.now() > now);
                    }
                })
            })
            .collect::<Vec<_>>();
        for t in threads {
            t.join().unwrap();
        }
    }

    #[rstest]
    fn duration_addition_coverage() {
        let d = Duration::from_secs(1);
        let one_ns = Nanos::from(1);
        assert!(d + one_ns > d);
    }
}
```


---

## Overview

This file is located at `crates/network/src/ratelimiter/clock.rs` within the repository.

**Classes defined:** FakeRelativeClock, MonotonicClock, Reference, Add, FakeRelativeClock, PartialEq, Clock, Add, Reference, Clock

**Functions defined:** duration_since, saturating_sub, now, duration_since, saturating_sub, add, advance, eq, now, add and 5 more


---

## Detailed Analysis

### Classes

#### `FakeRelativeClock`

**Type:** struct


#### `MonotonicClock`

**Type:** struct


#### `Reference`

**Type:** impl


#### `Add`

**Type:** impl


#### `FakeRelativeClock`

**Type:** impl


#### `PartialEq`

**Type:** impl


#### `Clock`

**Type:** impl


#### `Add`

**Type:** impl


#### `Reference`

**Type:** impl


#### `Clock`

**Type:** impl


### Functions

#### `duration_since(&self, earlier: Self)`


#### `saturating_sub(&self, duration: Nanos)`


#### `now(&self)`


#### `duration_since(&self, earlier: Self)`


#### `saturating_sub(&self, duration: Nanos)`


#### `add(self, other: Nanos)`


#### `advance(&self, by: Duration)`


#### `eq(&self, other: &Self)`


#### `now(&self)`


#### `add(self, other: Nanos)`


#### `duration_since(&self, earlier: Self)`


#### `saturating_sub(&self, duration: Nanos)`


#### `now(&self)`


#### `fake_clock_parallel_advances()`


#### `duration_addition_coverage()`



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


