# Documentation: `.docker/docker-compose.yml`
**Generated:** 2025-11-15T19:40:00.217099Z
**File Size:** 1090 bytes
**Extension:** .yml
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

- **Path:** `.docker/docker-compose.yml`
- **Size:** 1,090 bytes
- **Lines:** 48
- **Extension:** `.yml`
- **Type:** text

---

## Source Code

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


---

## Overview

This file is located at `.docker/docker-compose.yml` within the repository.

This is a configuration file.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `.docker`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: password. Ensure proper handling of secrets.


