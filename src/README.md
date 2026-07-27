# src

Application code for the **BIlingual AI**. Single top-level package — [`app/`](app/) — using the src-layout (`pythonpath = src` in [.code_quality/pytest.ini](../.code_quality/pytest.ini)).

## Layout

```text
app/
├── health.py   — liveness probe (ping/pong)
```

## Packages

| Module | Description |
| --- | --- |
| `app.health` | `ping() -> str` — returns `"pong"`; used as a liveness probe |

## Conventions

- All imports use the absolute `app.…` path (the src-layout makes `app` the package root). No `from .foo import …`.
- Public enums, dataclasses, and Pydantic models are re-exported through `__init__.py` (`app.utils`, `app.data.scrapers`, `app.data.gcs`, `app.data.bigquery`); reach for the re-export, not the inner module path, in callers.
- Dataclasses with multiple fields are declared `kw_only=True` — see `Bucket`/`ScraperBucket`, `Table`/`BronzeListingsTable`.
- Tests live in [`tests/`](../tests/) mirroring this tree; conventions documented in [tests/README.md](../tests/README.md).
