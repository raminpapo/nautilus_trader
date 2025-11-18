# Documentation: timer.rs

## File Metadata

- **Path**: `crates/common/src/python/timer.rs`
- **Size**: 9,519 bytes
- **Lines**: 306
- **Language**: Rust

## Original Source

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

use std::str::FromStr;

use nautilus_core::{
    UUID4, UnixNanos,
    python::{IntoPyObjectNautilusExt, to_pyvalue_err},
};
use pyo3::{
    IntoPyObjectExt,
    basic::CompareOp,
    prelude::*,
    types::{PyInt, PyString, PyTuple},
};
use ustr::Ustr;

use crate::timer::{TimeEvent, TimeEventCallback, TimeEventHandlerV2};

#[pyo3::pyclass(
    module = "nautilus_trader.core.nautilus_pyo3.common",
    name = "TimeEventHandler"
)]
/// Temporary time event handler for Python inter-operatbility
///
/// TODO: Remove once control flow moves into Rust
///
/// `TimeEventHandler` associates a `TimeEvent` with a callback function that is triggered
/// when the event's timestamp is reached.
#[allow(non_camel_case_types)]
#[derive(Debug)]
pub struct TimeEventHandler_Py {
    /// The time event.
    pub event: TimeEvent,
    /// The callable python object.
    pub callback: Py<PyAny>,
}

impl From<TimeEventHandlerV2> for TimeEventHandler_Py {
    /// # Panics
    ///
    /// Panics if the provided `TimeEventHandlerV2` contains a Rust callback,
    /// since only Python callbacks are supported by this handler.
    fn from(value: TimeEventHandlerV2) -> Self {
        Self {
            event: value.event,
            callback: match value.callback {
                #[cfg(feature = "python")]
                TimeEventCallback::Python(callback) => callback,
                TimeEventCallback::Rust(_) => {
                    panic!("Python time event handler is not supported for Rust callbacks")
                }
            },
        }
    }
}

#[pymethods]
impl TimeEvent {
    #[new]
    fn py_new(name: &str, event_id: UUID4, ts_event: u64, ts_init: u64) -> Self {
        Self::new(Ustr::from(name), event_id, ts_event.into(), ts_init.into())
    }

    fn __setstate__(&mut self, state: &Bound<'_, PyAny>) -> PyResult<()> {
        let py_tuple: &Bound<'_, PyTuple> = state.cast::<PyTuple>()?;

        let ts_event = py_tuple.get_item(2)?.cast::<PyInt>()?.extract::<u64>()?;
        let ts_init: u64 = py_tuple.get_item(3)?.cast::<PyInt>()?.extract::<u64>()?;

        self.name = Ustr::from(
            py_tuple
                .get_item(0)?
                .cast::<PyString>()?
                .extract::<&str>()?,
        );
        self.event_id = UUID4::from_str(
            py_tuple
                .get_item(1)?
                .cast::<PyString>()?
                .extract::<&str>()?,
        )
        .map_err(to_pyvalue_err)?;
        self.ts_event = ts_event.into();
        self.ts_init = ts_init.into();

        Ok(())
    }

    fn __getstate__(&self, py: Python) -> PyResult<Py<PyAny>> {
        (
            self.name.to_string(),
            self.event_id.to_string(),
            self.ts_event.as_u64(),
            self.ts_init.as_u64(),
        )
            .into_py_any(py)
    }

    fn __reduce__(&self, py: Python) -> PyResult<Py<PyAny>> {
        let safe_constructor = py.get_type::<Self>().getattr("_safe_constructor")?;
        let state = self.__getstate__(py)?;
        (safe_constructor, PyTuple::empty(py), state).into_py_any(py)
    }

    #[staticmethod]
    fn _safe_constructor() -> Self {
        Self::new(
            Ustr::from("NULL"),
            UUID4::new(),
            UnixNanos::default(),
            UnixNanos::default(),
        )
    }

    fn __richcmp__(&self, other: &Self, op: CompareOp, py: Python<'_>) -> Py<PyAny> {
        match op {
            CompareOp::Eq => self.eq(other).into_py_any_unwrap(py),
            CompareOp::Ne => self.ne(other).into_py_any_unwrap(py),
            _ => py.NotImplemented(),
        }
    }

    fn __repr__(&self) -> String {
        self.to_string()
    }

    #[getter]
    #[pyo3(name = "name")]
    fn py_name(&self) -> String {
        self.name.to_string()
    }

    #[getter]
    #[pyo3(name = "event_id")]
    const fn py_event_id(&self) -> UUID4 {
        self.event_id
    }

    #[getter]
    #[pyo3(name = "ts_event")]
    const fn py_ts_event(&self) -> u64 {
        self.ts_event.as_u64()
    }

    #[getter]
    #[pyo3(name = "ts_init")]
    const fn py_ts_init(&self) -> u64 {
        self.ts_init.as_u64()
    }
}

#[cfg(test)]
mod tests {
    use std::{num::NonZeroU64, sync::Arc};

    use nautilus_core::{
        UnixNanos, datetime::NANOSECONDS_IN_MILLISECOND, python::IntoPyObjectNautilusExt,
        time::get_atomic_clock_realtime,
    };
    use pyo3::prelude::*;
    use tokio::time::Duration;

    use crate::{
        runner::{TimeEventSender, set_time_event_sender},
        testing::wait_until,
        timer::{LiveTimer, TimeEvent, TimeEventCallback},
    };

    #[pyfunction]
    const fn receive_event(_py: Python, _event: TimeEvent) -> PyResult<()> {
        // TODO: Assert the length of a handler vec
        Ok(())
    }

    #[derive(Debug)]
    struct TestTimeEventSender;

    impl TimeEventSender for TestTimeEventSender {
        fn send(&self, _handler: crate::timer::TimeEventHandlerV2) {
            // Test implementation - just ignore the events
        }
    }

    #[tokio::test]
    async fn test_live_timer_starts_and_stops() {
        set_time_event_sender(Arc::new(TestTimeEventSender));

        Python::initialize();
        let callback = Python::attach(|py| {
            let callable = wrap_pyfunction!(receive_event, py).unwrap();
            let callable = callable.into_py_any_unwrap(py);
            TimeEventCallback::from(callable)
        });

        // Create a new LiveTimer with no stop time
        let clock = get_atomic_clock_realtime();
        let start_time = clock.get_time_ns();
        let interval_ns = NonZeroU64::new(100 * NANOSECONDS_IN_MILLISECOND).unwrap();

        let test_sender = Arc::new(TestTimeEventSender);
        let mut timer = LiveTimer::new(
            "TEST_TIMER".into(),
            interval_ns,
            start_time,
            None,
            callback,
            false,
            Some(test_sender),
        );

        let next_time_ns = timer.next_time_ns();
        timer.start();

        // Wait for timer to run
        tokio::time::sleep(Duration::from_millis(300)).await;

        timer.cancel();
        wait_until(|| timer.is_expired(), Duration::from_secs(2));
        assert!(timer.next_time_ns() > next_time_ns);
    }

    #[tokio::test]
    async fn test_live_timer_with_stop_time() {
        set_time_event_sender(Arc::new(TestTimeEventSender));

        Python::initialize();
        let callback = Python::attach(|py| {
            let callable = wrap_pyfunction!(receive_event, py).unwrap();
            let callable = callable.into_py_any_unwrap(py);
            TimeEventCallback::from(callable)
        });

        // Create a new LiveTimer with a stop time
        let clock = get_atomic_clock_realtime();
        let start_time = clock.get_time_ns();
        let interval_ns = NonZeroU64::new(100 * NANOSECONDS_IN_MILLISECOND).unwrap();
        let stop_time = start_time + 500 * NANOSECONDS_IN_MILLISECOND;

        let test_sender = Arc::new(TestTimeEventSender);
        let mut timer = LiveTimer::new(
            "TEST_TIMER".into(),
            interval_ns,
            start_time,
            Some(stop_time),
            callback,
            false,
            Some(test_sender),
        );

        let next_time_ns = timer.next_time_ns();
        timer.start();

        // Wait for a longer time than the stop time
        tokio::time::sleep(Duration::from_secs(1)).await;

        wait_until(|| timer.is_expired(), Duration::from_secs(2));
        assert!(timer.next_time_ns() > next_time_ns);
    }

    #[tokio::test]
    async fn test_live_timer_with_zero_interval_and_immediate_stop_time() {
        set_time_event_sender(Arc::new(TestTimeEventSender));

        Python::initialize();
        let callback = Python::attach(|py| {
            let callable = wrap_pyfunction!(receive_event, py).unwrap();
            let callable = callable.into_py_any_unwrap(py);
            TimeEventCallback::from(callable)
        });

        // Create a new LiveTimer with a stop time
        let clock = get_atomic_clock_realtime();
        let start_time = UnixNanos::default();
        let interval_ns = NonZeroU64::new(1).unwrap();
        let stop_time = clock.get_time_ns();

        let test_sender = Arc::new(TestTimeEventSender);
        let mut timer = LiveTimer::new(
            "TEST_TIMER".into(),
            interval_ns,
            start_time,
            Some(stop_time),
            callback,
            false,
            Some(test_sender),
        );

        timer.start();

        wait_until(|| timer.is_expired(), Duration::from_secs(2));
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 17 function(s) and 2 class(es).

## Detailed Walkthrough

### Functions
- **`from()`**: Function defined in this file
- **`py_new()`**: Function defined in this file
- **`__setstate__()`**: Function defined in this file
- **`__getstate__()`**: Function defined in this file
- **`__reduce__()`**: Function defined in this file
- **`_safe_constructor()`**: Function defined in this file
- **`__richcmp__()`**: Function defined in this file
- **`__repr__()`**: Function defined in this file
- **`py_name()`**: Function defined in this file
- **`py_event_id()`**: Function defined in this file
- **`py_ts_event()`**: Function defined in this file
- **`py_ts_init()`**: Function defined in this file
- **`receive_event()`**: Function defined in this file
- **`send()`**: Function defined in this file
- **`test_live_timer_starts_and_stops()`**: Function defined in this file
- **`test_live_timer_with_stop_time()`**: Function defined in this file
- **`test_live_timer_with_zero_interval_and_immediate_stop_time()`**: Function defined in this file

### Classes
- **`TimeEventHandler_Py`**: Class defined in this file
- **`TestTimeEventSender`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 22


**Functions**: `__getstate__`, `__reduce__`, `__repr__`, `__richcmp__`, `__setstate__`, `_safe_constructor`, `from`, `py_event_id`, `py_name`, `py_new`, `py_ts_event`, `py_ts_init`, `receive_event`, `send`, `test_live_timer_starts_and_stops`, `test_live_timer_with_stop_time`, `test_live_timer_with_zero_interval_and_immediate_stop_time`
**Impls**: `From`, `TimeEvent`, `TimeEventSender`
**Structs**: `TestTimeEventSender`, `TimeEventHandler_Py`

## Related Files

This file is located in `crates/common/src/python/`. Related files may include:
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
*Generated on 2025-11-18T21:55:01.289014Z*
