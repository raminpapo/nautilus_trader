# Documentation: `crates/cli/src/database/postgres.rs`
**Generated:** 2025-11-15T19:40:01.622747Z
**File Size:** 2927 bytes
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

- **Path:** `crates/cli/src/database/postgres.rs`
- **Size:** 2,927 bytes
- **Lines:** 76
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 1

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

use nautilus_infrastructure::sql::pg::{
    connect_pg, drop_postgres, get_postgres_connect_options, init_postgres,
};

use crate::opt::{DatabaseCommand, DatabaseOpt};

/// Executes database management commands for PostgreSQL operations.
///
/// This function handles database initialization, schema setup, and database
/// dropping operations based on the provided command options.
///
/// # Errors
///
/// Returns an error if:
/// - Database connection fails
/// - Schema initialization fails
/// - Database dropping operation fails
/// - Any PostgreSQL operation encounters an error
pub async fn run_database_command(opt: DatabaseOpt) -> anyhow::Result<()> {
    let command = opt.command.clone();

    match command {
        DatabaseCommand::Init(config) => {
            let pg_connect_options = get_postgres_connect_options(
                config.host,
                config.port,
                config.username,
                config.password,
                config.database,
            );
            let pg = connect_pg(pg_connect_options.clone().into()).await?;
            log::info!(
                "Connected with Postgres on url: {}",
                pg_connect_options.connection_string()
            );
            init_postgres(
                &pg,
                pg_connect_options.database,
                pg_connect_options.password,
                config.schema,
            )
            .await?;
        }
        DatabaseCommand::Drop(config) => {
            let pg_connect_options = get_postgres_connect_options(
                config.host,
                config.port,
                config.username,
                config.password,
                config.database,
            );
            let pg = connect_pg(pg_connect_options.clone().into()).await?;
            log::info!(
                "Connected with Postgres on url: {}",
                pg_connect_options.connection_string()
            );
            drop_postgres(&pg, pg_connect_options.database).await?;
        }
    }
    Ok(())
}
```


---

## Overview

This file is located at `crates/cli/src/database/postgres.rs` within the repository.

**Functions defined:** run_database_command


---

## Detailed Analysis

### Functions

#### `run_database_command(opt: DatabaseOpt)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/cli/src/database`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: password. Ensure proper handling of secrets.


