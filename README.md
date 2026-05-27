## estimador-cag

`estimador-cag` is a small FastAPI service scaffolded to support a cache-augmented generation (CAG) workflow.

## Project tree

```text
estimador-cag/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── routers/
│   │   ├── __init__.py
│   │   └── estimations.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── llm_service.py
│   └── context/
│       ├── __init__.py
│       └── examples.py
├── docs/
│   ├── ARCHITECTURE.md
│   └── CONVENTION.md
├── .env
├── .env.example
├── .gitignore
├── pyproject.toml
└── README.md
```

## Architecture

Layered design: `routers` → `services` → `context`, with multi-provider LLM dispatch in `app/services/llm_service.py`.

Full diagrams, request flows, provider tables, and extension rules:
[`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).

## Setup

This repository uses `uv`.

```bash
uv sync
```

Configuration is loaded from the process environment. Use **either** Infisical or a local `.env` file in development; production/CI typically uses Infisical. See [`.env.example`](.env.example) for all variable names (no secret values).

### Option A — Infisical (development or production)

```bash
infisical run --env=dev -- uv run uvicorn app.main:app --reload
```

Use the Infisical environment that matches your deployment (`dev`, `staging`, `prod`, etc.). Secret keys must match `.env.example`.

### Option B — Local `.env`

```bash
cp .env.example .env
# Edit .env with your API keys (file is gitignored)
uv run uvicorn app.main:app --reload
```

### Environment variables

| Variable | Default | Notes |
|----------|---------|--------|
| `LLM_PROVIDER` | `openai` | `openai`, `anthropic`, or `gemini` |
| `LLM_MODEL` | `gpt-4o-mini` | Per-provider defaults apply if not set in env |
| `OPENAI_API_KEY` | — | Required when `LLM_PROVIDER=openai` |
| `ANTHROPIC_API_KEY` | — | Required when `LLM_PROVIDER=anthropic` |
| `GOOGLE_API_KEY` | — | Required when `LLM_PROVIDER=gemini` |
| `APP_ENV` | `development` | Environment label |
| `LOG_LEVEL` | `DEBUG` | `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL` |

Process environment overrides `.env` when both define the same key.

## Run

```bash
uv run uvicorn app.main:app --reload
```

(Wrap with `infisical run` when using Infisical.)

## Contributing

Commit messages and pull requests follow [`docs/CONVENTION.md`](docs/CONVENTION.md) (Conventional Commits,
imperative mood, and GitHub PR structure). Coding assistants should read that file before drafting commits
or PR descriptions.

Architectural changes must update [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) in the same change set
(see `CLAUDE.md` and `.cursorrules`).
