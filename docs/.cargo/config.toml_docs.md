# Documentation: `.cargo/config.toml`
**Generated:** 2025-11-15T19:40:00.213057Z
**File Size:** 780 bytes
**Extension:** .toml
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

- **Path:** `.cargo/config.toml`
- **Size:** 780 bytes
- **Lines:** 30
- **Extension:** `.toml`
- **Type:** text

---

## Source Code

```toml
[build]
rustdocflags = ["--cfg", "docsrs", "-D", "warnings"]

[target.'cfg(all())']
rustflags = [
  # https://rust-lang.github.io/rust-clippy/master/index.html#drop_non_drop
  # Disable this lint as we explicitly drop even when `Drop` is not implemented
  "-Aclippy::drop_non_drop",
]

[target.'cfg(target_os = "linux")']
rustflags = [
  "-C",
  "link-arg=-Wl,--gc-sections",
  "-C",
  "link-arg=-Wl,--as-needed",
  "-C",
  "link-arg=-Wl,-z,norelro",
  "-C",
  "relocation-model=pic",
]

[target.x86_64-apple-darwin]
rustflags = ["-C", "link-arg=-undefined", "-C", "link-arg=dynamic_lookup"]

[target.aarch64-apple-darwin]
rustflags = ["-C", "link-arg=-undefined", "-C", "link-arg=dynamic_lookup"]

[target.x86_64-pc-windows-msvc]
rustflags = ["-C", "target-feature=+crt-static"]
```


---

## Overview

This file is located at `.cargo/config.toml` within the repository.

This is a configuration file.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `.cargo`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


