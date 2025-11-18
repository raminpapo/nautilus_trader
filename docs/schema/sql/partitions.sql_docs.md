# Documentation: partitions.sql

## File Metadata

- **Path**: `schema/sql/partitions.sql`
- **Size**: 5,971 bytes
- **Lines**: 161
- **Language**: SQL

## Original Source

```sql
CREATE OR REPLACE FUNCTION create_block_partition(blockchain_id INTEGER)
    RETURNS TEXT AS $$
DECLARE
    blockchain_name TEXT;
    partition_name TEXT;
BEGIN
    -- Get the blockchain name from the chain table
    SELECT lower(name) INTO blockchain_name FROM chain where chain.chain_id = blockchain_id;
    -- Check if blockchain was found
    IF blockchain_name IS NULL THEN
        RETURN 'Chain ID ' || blockchain_id || ' not found';
    END IF;

    partition_name := 'block_' || blockchain_name;

    -- Check if partition already exists
    IF EXISTS(
        SELECT 1 FROM pg_class c
                          JOIN pg_namespace ON pg_namespace.oid = c.relnamespace
        WHERE c."relkind" = 'r' AND c."relname" = partition_name
    ) THEN
        RETURN 'Partition ' || partition_name || ' already exists';
    END IF;

    -- Create the partition
    BEGIN
        EXECUTE format('CREATE TABLE %I PARTITION OF block FOR VALUES IN (%s)', partition_name, blockchain_id);
        RETURN 'Created partition ' || partition_name;
    EXCEPTION
        WHEN OTHERS THEN
            RETURN 'Failed to create partition ' || partition_name || ': ' || SQLERRM;
    END;
END
$$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE OR REPLACE FUNCTION delete_block_partition(blockchain_id INTEGER, force_delete BOOLEAN DEFAULT FALSE)
    RETURNS TEXT AS $$
DECLARE
    blockchain_name TEXT;
    partition_name TEXT;
    data_count BIGINT;
BEGIN
    -- Get the blockchain name from the chain table
    SELECT lower(name) INTO blockchain_name FROM chain where chain.chain_id = blockchain_id;

    -- Check if a blockchain was found
    IF blockchain_name IS NULL THEN
        RETURN 'Chain ID ' || blockchain_id || ' not found';
    END IF;

    partition_name := 'block_' || blockchain_name;

    -- Check if partition exists
    IF NOT EXISTS(
        SELECT 1 FROM pg_class c
                          JOIN pg_namespace ON pg_namespace.oid = c.relnamespace
        WHERE c."relkind" = 'r' AND c."relname" = partition_name
    ) THEN
        RETURN 'Partition ' || partition_name || ' does not exist';
    END IF;

    -- Check if partition has data
    EXECUTE format('SELECT COUNT(*) FROM %I', partition_name) INTO data_count;

    IF data_count > 0 AND NOT force_delete THEN
        RETURN format('Partition %s contains %s blocks. Use force=true to delete anyway', partition_name, data_count);
    END IF;

    -- Actually delete the partition and all data
    BEGIN
        -- WARNING: CASCADE will also delete all dependent blockchain data from other tables
        -- This permanently removes ALL blocks and related transaction data for this chain
        EXECUTE format('DROP TABLE %I CASCADE', partition_name);
        RETURN format('Successfully dropped partition %s (contained %s blocks)', partition_name, data_count);
    EXCEPTION
        WHEN OTHERS THEN
            RETURN 'Failed to drop partition ' || partition_name || ': ' || SQLERRM;
    END;
END
$$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE OR REPLACE FUNCTION create_token_partition(blockchain_id INTEGER)
    RETURNS TEXT AS $$
DECLARE
    blockchain_name TEXT;
    partition_name TEXT;
BEGIN
    -- Get the blockchain name from the chain table
    SELECT lower(name) INTO blockchain_name FROM chain where chain.chain_id = blockchain_id;
    -- Check if blockchain was found
    IF blockchain_name IS NULL THEN
        RETURN 'Chain ID ' || blockchain_id || ' not found';
    END IF;

    partition_name := 'token_' || blockchain_name;

    -- Check if partition already exists
    IF EXISTS(
        SELECT 1 FROM pg_class c
                          JOIN pg_namespace ON pg_namespace.oid = c.relnamespace
        WHERE c."relkind" = 'r' AND c."relname" = partition_name
    ) THEN
        RETURN 'Partition ' || partition_name || ' already exists';
    END IF;

    -- Create the partition
    BEGIN
        EXECUTE format('CREATE TABLE %I PARTITION OF token FOR VALUES IN (%s)', partition_name, blockchain_id);
        RETURN 'Created partition ' || partition_name;
    EXCEPTION
        WHEN OTHERS THEN
            RETURN 'Failed to create partition ' || partition_name || ': ' || SQLERRM;
    END;
END
$$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE OR REPLACE FUNCTION delete_token_partition(blockchain_id INTEGER, force_delete BOOLEAN DEFAULT FALSE)
    RETURNS TEXT AS $$
DECLARE
    blockchain_name TEXT;
    partition_name TEXT;
    data_count BIGINT;
BEGIN
    -- Get the blockchain name from the chain table
    SELECT lower(name) INTO blockchain_name FROM chain where chain.chain_id = blockchain_id;

    -- Check if a blockchain was found
    IF blockchain_name IS NULL THEN
        RETURN 'Chain ID ' || blockchain_id || ' not found';
    END IF;

    partition_name := 'token_' || blockchain_name;

    -- Check if partition exists
    IF NOT EXISTS(
        SELECT 1 FROM pg_class c
                          JOIN pg_namespace ON pg_namespace.oid = c.relnamespace
        WHERE c."relkind" = 'r' AND c."relname" = partition_name
    ) THEN
        RETURN 'Partition ' || partition_name || ' does not exist';
    END IF;

    -- Check if partition has data
    EXECUTE format('SELECT COUNT(*) FROM %I', partition_name) INTO data_count;

    IF data_count > 0 AND NOT force_delete THEN
        RETURN format('Partition %s contains %s tokens. Use force=true to delete anyway', partition_name, data_count);
    END IF;

    -- Actually delete the partition and all data
    BEGIN
        -- WARNING: CASCADE will also delete all dependent token data from other tables
        -- This permanently removes ALL tokens and related data for this chain
        EXECUTE format('DROP TABLE %I CASCADE', partition_name);
        RETURN format('Successfully dropped partition %s (contained %s tokens)', partition_name, data_count);
    EXCEPTION
        WHEN OTHERS THEN
            RETURN 'Failed to drop partition ' || partition_name || ': ' || SQLERRM;
    END;
END
$$ LANGUAGE plpgsql SECURITY DEFINER;
```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 52


**Identifiers**: `ALL`, `AND`, `Actually`, `BEGIN`, `BIGINT`, `BOOLEAN`, `CASCADE`, `COUNT`, `CREATE`, `Chain`, `Check`, `Create`, `Created`, `DECLARE`, `DEFAULT`, `DEFINER`, `DROP`, `END`, `EXCEPTION`, `EXECUTE`, `EXISTS`, `FALSE`, `FOR`, `FROM`, `FUNCTION`, `Failed`, `Get`, `INTEGER`, `INTO`, `JOIN` *(+22 more)*

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

⚠️ **Security**: This file may handle sensitive data. Ensure proper encryption and access controls.

---
*Generated on 2025-11-18T21:55:06.118722Z*
