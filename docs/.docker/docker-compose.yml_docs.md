# Documentation: docker-compose.yml

## File Metadata

- **Path**: `.docker/docker-compose.yml`
- **Size**: 1,090 bytes
- **Lines**: 49
- **Language**: YAML

## Original Source

```yaml
services:
  postgres:
    container_name: nautilus-database
    image: postgres
    environment:
      POSTGRES_USER: ${POSTGRES_USER:-nautilus}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:-pass}
      POSTGRES_DB: ${POSTGRES_DB:-nautilus}
      PGDATA: /data/postgres
    volumes:
      - nautilus-database:/data/postgres
    ports:
      - "5432:5432"
    networks:
      - nautilus-network
    restart: unless-stopped

  pgadmin:
    container_name: nautilus-pgadmin
    image: dpage/pgadmin4
    environment:
      PGADMIN_DEFAULT_EMAIL: ${PGADMIN_DEFAULT_EMAIL:-admin@mail.com}
      PGADMIN_DEFAULT_PASSWORD: ${PGADMIN_DEFAULT_PASSWORD:-admin}
    volumes:
      - pgadmin:/root/.pgadmin
    security_opt:
      - no-new-privileges:true
    ports:
      - "${PGADMIN_PORT:-5051}:80"
    networks:
      - nautilus-network
    restart: unless-stopped

  redis:
    container_name: nautilus-redis
    image: redis
    ports:
      - "6379:6379"
    restart: unless-stopped
    networks:
      - nautilus-network

networks:
  nautilus-network:

volumes:
  nautilus-database:
  pgadmin:

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a YAML configuration file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 7


**Identifiers**: `PGADMIN_DEFAULT_EMAIL`, `PGADMIN_DEFAULT_PASSWORD`, `PGADMIN_PORT`, `PGDATA`, `POSTGRES_DB`, `POSTGRES_PASSWORD`, `POSTGRES_USER`

## Related Files

This file is located in `.docker/`. Related files may include:
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
*Generated on 2025-11-18T21:54:58.789162Z*
