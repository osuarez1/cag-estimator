## cag-estimator

`cag-estimator` is a small FastAPI service scaffolded to support a cache-augmented generation (CAG) workflow.

## Real usage (no mock)

To use a **real** provider (not `mock`), configure your credentials (Infisical or `.env`) and start the server **without** `LLM_PROVIDER=mock`.

Start the server:

```bash
uv run uvicorn app.main:app --reload
```

In another terminal, test the endpoint:

```bash
curl -X POST http://localhost:8000/api/v1/estimate \
  -H "Content-Type: application/json" \
  -d '{
    "transcription": "En la reunión con el equipo de marketing, el cliente explicó que necesita una landing page con formulario de contacto, integración con su CRM actual (HubSpot), y una sección de blog con editor WYSIWYG. El plazo ideal sería tenerlo listo en 4 semanas. El diseño ya existe en Figma."
  }'
```

## Quickstart

Install dependencies:

```bash
uv sync
```

Run the API (no keys needed):

```bash
LLM_PROVIDER=mock uv run uvicorn app.main:app --reload
```

Swagger UI is available at `/docs`.

## Project tree

```text
cag-estimator/
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
├── exercises/
│   ├── README.md
│   └── transcripts/
│       └── meeting_transcript.md
├── scripts/
│   ├── verify.py
│   └── test_providers.py
├── reports/
│   └── providers/
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

## Verification (“tests”)

Automated verification is performed by:

```bash
uv run python scripts/verify.py
```

This script starts the API (default port `8001`), checks `/health` and `/docs`, then calls `POST /api/v1/estimate`
using the transcript at [`exercises/transcripts/meeting_transcript.md`](exercises/transcripts/meeting_transcript.md).
Run it locally or from your CI system of choice.

### Compare all LLM providers

To exercise every provider (`openai`, `anthropic`, `gemini`, `mock`) end-to-end and write one Markdown report per provider:

```bash
uv run python scripts/test_providers.py
```

Reports are written to `reports/providers/<provider>.md`. By default the script uses
[`exercises/transcripts/meeting_transcript.md`](exercises/transcripts/meeting_transcript.md). Optional transcription input:

```bash
uv run python scripts/test_providers.py --transcription-file path/to/transcript.md
uv run python scripts/test_providers.py --transcription "Meeting notes: ..."
```

Real providers require API keys (Infisical or `.env`). If a key is missing, the report records the API auth error instead of crashing.

## Setup & configuration

Configuration is loaded from the process environment. Use **either** Infisical or a local `.env` file in development.
See [`.env.example`](.env.example) for all variable names (no secret values).

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
| `LLM_PROVIDER` | `openai` | `openai`, `anthropic`, `gemini`, or `mock` |
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

## Exercises

See [`exercises/README.md`](exercises/README.md) for the exercise instructions and the transcript to use as input.

## Contributing

Commit messages and pull requests follow [`docs/CONVENTION.md`](docs/CONVENTION.md) (Conventional Commits,
imperative mood, and GitHub PR structure). Coding assistants should read that file before drafting commits
or PR descriptions.

Architectural changes must update [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) in the same change set
(see `CLAUDE.md` and `.cursorrules`).
