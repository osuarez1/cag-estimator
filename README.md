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

`.env` and `.env.example` are intentionally empty in this scaffold. If you want to call a real provider, put
environment variables in `.env` (the file is gitignored).

Supported variables:

- `LLM_PROVIDER`: `openai` | `anthropic` | `gemini`
- `OPENAI_API_KEY`
- `ANTHROPIC_API_KEY`
- `GOOGLE_API_KEY`
- `LLM_MODEL` (optional; per-provider defaults are used if omitted)

## Run

```bash
uv run uvicorn app.main:app --reload
```

## Contributing

Commit messages and pull requests follow [`docs/CONVENTION.md`](docs/CONVENTION.md) (Conventional Commits,
imperative mood, and GitHub PR structure). Coding assistants should read that file before drafting commits
or PR descriptions.

Architectural changes must update [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) in the same change set
(see `CLAUDE.md` and `.cursorrules`).

