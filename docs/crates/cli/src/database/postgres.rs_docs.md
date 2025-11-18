# Documentation: postgres.rs

## File Metadata

- **Path**: `crates/cli/src/database/postgres.rs`
- **Size**: 2,927 bytes
- **Lines**: 77
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`run_database_command()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 1


**Functions**: `run_database_command`

## Related Files

This file is located in `crates/cli/src/database/`. Related files may include:
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

⚠️ **Security**: This file may handle sensitive data. Ensure proper encryption and access controls.

⚠️ **Security**: This file may perform database operations. Use parameterized queries to prevent SQL injection.

---
*Generated on 2025-11-18T21:55:00.941833Z*
