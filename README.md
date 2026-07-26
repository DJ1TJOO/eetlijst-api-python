# Eetlijst Python

This folder contains a Python rewrite of the TypeScript client in `src/`.

## What is included

- A synchronous `eetlijst(...)` factory that mirrors the TS client shape.
- Service classes for `app`, `events`, `expenses`, `groups`, `users`, `groups.users`, `groups.list`, `events.attendance`, and `expenses.settlements`.
- A complete GraphQL operation manifest at `src/eetlijst/operations.graphql` for `ariadne-codegen`.
- Example scripts matching the TS examples.

## Codegen

The package is set up for `ariadne-codegen`. From inside `python/`, run:

```bash
ariadne-codegen
```

The config in `pyproject.toml` points the schema at the checked-in schema from the TypeScript project and writes generated code into `eetlijst_generated/`.

## Local environment

Create a virtual environment in `python/.venv` and activate it before installing anything:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

Install the package and its dependencies in editable mode:

```powershell
python -m pip install -e .
```

The editable install also brings in `ariadne-codegen`, so code generation is available without extra steps.

## Quick start

```py
import asyncio
from eetlijst import Eetlijst

eetlijst = Eetlijst("<API_KEY>")

async def main():
    app_status = await eetlijst.app.status()
    print(app_status)

if __name__ == "__main__":
    asyncio.run(main())
```
