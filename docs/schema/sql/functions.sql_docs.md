# Documentation: functions.sql

## File Metadata

- **Path**: `schema/sql/functions.sql`
- **Size**: 2,501 bytes
- **Lines**: 83
- **Language**: SQL

## Original Source

```sql
CREATE OR REPLACE FUNCTION get_all_tables ()
    RETURNS TEXT[] AS $$
DECLARE
    result TEXT[];
BEGIN
    SELECT
        array_agg(t.table_name) INTO result
    FROM information_schema.tables t
    WHERE table_schema = current_schema();
    RETURN result;
END
$$ LANGUAGE plpgsql;

CREATE OR REPLACE function truncate_all_tables()
    RETURNS VOID AS $$
DECLARE
    tables TEXT[];
    quoted_tables TEXT[];
    truncate_statement TEXT;
BEGIN
    SELECT get_all_tables() INTO tables;

    -- Quote each table name
    SELECT array_agg(quote_ident(t)) INTO quoted_tables FROM unnest(tables) AS t;

    -- Construct the TRUNCATE statement
    truncate_statement := 'TRUNCATE TABLE ' || array_to_string(quoted_tables, ', ') || ' CASCADE';

    -- Execute the TRUNCATE statement
    EXECUTE truncate_statement;
END
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_last_continuous_block(blockchain_id INTEGER)
  RETURNS BIGINT AS $$
  DECLARE
      min_block BIGINT;
      max_block BIGINT;
      block_count BIGINT;
  BEGIN
      -- Fast: Get MAX using index
      SELECT number INTO max_block FROM block WHERE chain_id = blockchain_id ORDER BY number DESC LIMIT 1;
      -- If no blocks
      IF max_block IS NULL THEN
          RETURN 0;
      END IF;

      -- Fast: Get MIN using index
      SELECT number INTO min_block FROM block WHERE chain_id = blockchain_id ORDER BY number ASC LIMIT 1;

      -- Slower but necessary: Get COUNT
      SELECT COUNT(*) INTO block_count
      FROM block
      WHERE chain_id = blockchain_id;

      -- If continuous: count should equal (max - min + 1)
      IF block_count = (max_block - min_block + 1) THEN
          RETURN max_block;  -- No gaps, return max
      ELSE
          -- Only if gaps exist, use slower gap detection
          RETURN (SELECT COALESCE(
              (SELECT CASE
                  WHEN gap_start = 1 THEN 0
                  ELSE gap_start - 1
               END
               FROM (
                   SELECT number + 1 AS gap_start
                   FROM (
                       SELECT number,
                              LEAD(number) OVER (ORDER BY number) AS next_number
                       FROM block
                       WHERE chain_id = blockchain_id
                   ) gaps
                   WHERE next_number != number + 1
                   ORDER BY number
                   LIMIT 1
               ) first_gap),
              max_block,
              0
          ));
      END IF;
  END
  $$ LANGUAGE plpgsql;
```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 43


**Identifiers**: `ASC`, `BEGIN`, `BIGINT`, `CASCADE`, `CASE`, `COALESCE`, `COUNT`, `CREATE`, `Construct`, `DECLARE`, `DESC`, `ELSE`, `END`, `EXECUTE`, `Execute`, `FROM`, `FUNCTION`, `Fast`, `Get`, `INTEGER`, `INTO`, `LANGUAGE`, `LEAD`, `LIMIT`, `MAX`, `MIN`, `NULL`, `ORDER`, `OVER`, `Only` *(+13 more)*

## Related Files

This file is located in `schema/sql/`. Related files may include:
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
*Generated on 2025-11-18T21:55:06.116505Z*
