# eetlijst-python

A simple Python API client for Eetlijst.

> [!NOTE]
> This project is made for use in a student house, and will probably not be maintained.
> Most of this Python port was converted from the TypeScript version (https://github.com/DJ1TJOO/eetlijst-api-ts) using Google Gemini.

## Usage

Create a virtual environment and install the package:

    python -m venv .venv
    # Activate virtual environment (.venv\Scripts\Activate.ps1 on Windows or source .venv/bin/activate on Linux/macOS)
    python -m pip install -e .

The API key can be retrieved from the account page, under Developer API key (BETA), at https://v5.eetlijst.nl/account

```python
import asyncio
from eetlijst_py import Eetlijst

eetlijst = Eetlijst("<API_KEY>")

async def main():
    app_status = await eetlijst.app.status()
    print(app_status)

if __name__ == "__main__":
    asyncio.run(main())
```

See Examples (./examples/) for more.

## What is Included

- Service classes for app, events, expenses, groups, users, groups.users, groups.list, events.attendance, and expenses.settlements.

## Development & Codegen

This project uses ariadne-codegen (https://github.com/mirumee/ariadne-codegen) for GraphQL code generation.

Run code generation:

```
ariadne-codegen
```

The configuration in pyproject.toml points to the GraphQL schema and outputs generated code into src/generated/.

### Building

To build the package locally, install the build tool first:

```
python -m pip install build
```

Build the package:

```
python -m build
```
