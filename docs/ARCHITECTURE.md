# Architecture

This document describes the **current** architecture of `estimador-cag`. It is the source of truth for
system structure, layer boundaries, and data flow.

**Maintainers and coding assistants:** when you change boundaries (new layers, routers, services,
providers, config, or CAG context flow), update this file in the **same change set** as the code.
See [`CONVENTION.md`](CONVENTION.md) and root `CLAUDE.md` / `.cursorrules`.

---

## Goals

- **Cache-augmented generation (CAG):** static reference data is injected into prompts from `app/context/`.
- **Scalable separation:** HTTP, business logic, and prompt context stay in distinct packages.
- **Multi-provider LLM:** OpenAI, Anthropic, and Gemini are selectable at runtime via configuration.

---

## Layered structure

| Layer | Package | Responsibility |
|-------|---------|----------------|
| HTTP | `app/routers/` | Routing, request/response models, status codes |
| Business | `app/services/` | Estimation orchestration, prompt assembly, LLM calls |
| Context | `app/context/` | Static CAG data (examples, templates) — no HTTP or SDK imports |
| Config | `app/config.py` | Settings from environment (`.env` locally, Infisical in deployed envs) |
| Entry | `app/main.py` | FastAPI app factory, router registration, health check |

**Dependency rule (strict):**

```text
routers  →  services  →  context
              ↓
           config
```

Routers must **not** import `app.context` directly. Services own prompt assembly and may read `EXAMPLES`.

---

## Repository layout

```text
estimador-cag/
├── app/
│   ├── main.py              # FastAPI app, /health
│   ├── config.py            # pydantic-settings
│   ├── routers/
│   │   └── estimations.py   # POST /estimations
│   ├── services/
│   │   └── llm_service.py   # complete(), estimate(), provider adapters
│   └── context/
│       └── examples.py      # EXAMPLES (CAG cache)
├── docs/
│   ├── ARCHITECTURE.md      # this file
│   └── CONVENTION.md
└── pyproject.toml
```

---

## Component diagram

```mermaid
flowchart TB
  subgraph http [HTTP layer]
    main[app/main.py]
    router[app/routers/estimations.py]
  end

  subgraph business [Business layer]
    llm[app/services/llm_service.py]
  end

  subgraph context [Context layer]
    examples[app/context/examples.py]
  end

  subgraph config [Configuration]
    settings[app/config.py]
  end

  subgraph external [External APIs]
    openai[OpenAI API]
    anthropic[Anthropic API]
    gemini[Google Gemini API]
  end

  main --> router
  router --> llm
  llm --> examples
  llm --> settings
  llm --> openai
  llm --> anthropic
  llm --> gemini
  main --> settings
```

---

## Request flow (current scaffold)

```mermaid
sequenceDiagram
  participant Client
  participant FastAPI as app/main.py
  participant Router as routers/estimations
  participant Service as services/llm_service
  participant Context as context/examples

  Client->>FastAPI: GET /health
  FastAPI-->>Client: 200 status ok

  Client->>FastAPI: POST /estimations
  FastAPI->>Router: create_estimation
  Router->>Service: estimate(input)
  Service->>Context: read EXAMPLES
  Note over Service: Scaffold returns not_implemented
  Service-->>Router: dict response
  Router-->>Client: JSON
```

**Future flow:** `estimate()` will build a prompt from `EXAMPLES` + user input, then call `complete()`
(which dispatches to the configured provider).

---

## LLM provider dispatch

Runtime selection uses `LLM_PROVIDER` (`openai` | `anthropic` | `gemini`). API keys are validated when
`complete()` runs, not at application import, so `/health` works with an empty `.env`.

```mermaid
flowchart LR
  estimate[estimate] --> complete[complete]
  complete --> dispatch{LLM_PROVIDER}
  dispatch -->|openai| oa[_call_openai]
  dispatch -->|anthropic| an[_call_anthropic]
  dispatch -->|gemini| ge[_call_gemini]
  oa --> sdkO[openai SDK]
  an --> sdkA[anthropic SDK]
  ge --> sdkG[google-genai Client]
```

| Provider | Env key | Default model if `LLM_MODEL` unset |
|----------|---------|--------------------------------------|
| `openai` | `OPENAI_API_KEY` | `gpt-4o-mini` |
| `anthropic` | `ANTHROPIC_API_KEY` | `claude-3-5-haiku-latest` |
| `gemini` | `GOOGLE_API_KEY` | `gemini-2.0-flash` |

---

## CAG (cache-augmented generation)

Static examples live in `app/context/examples.py` as `EXAMPLES: list[dict]`. The service layer merges
this cache into prompts before calling the LLM.

```mermaid
flowchart TB
  userInput[User input] --> assemble[Prompt assembly in llm_service]
  examples[EXAMPLES in context/examples.py] --> assemble
  assemble --> prompt[Final prompt]
  prompt --> complete[complete]
  complete --> provider[Selected LLM provider]
```

**Design intent:** context data changes rarely; keeping it out of routers and out of SDK code makes
updates and testing easier.

---

## Configuration

| Variable | Purpose |
|----------|---------|
| `LLM_PROVIDER` | `openai`, `anthropic`, or `gemini` |
| `OPENAI_API_KEY` | OpenAI credential |
| `ANTHROPIC_API_KEY` | Anthropic credential |
| `GOOGLE_API_KEY` | Gemini credential |
| `LLM_MODEL` | Optional override; provider defaults apply if omitted |

Settings are loaded via `pydantic-settings` with `env_file=".env"` for local development. Production
secrets should come from **Infisical** (see root `CLAUDE.md`), not committed files.

---

## Extension guidelines

When adding features, preserve layer boundaries:

| Change | Update |
|--------|--------|
| New HTTP endpoint | `app/routers/` (+ register in `app/main.py`) |
| New business rule or LLM behavior | `app/services/` |
| New static prompt / CAG data | `app/context/` |
| New env var or provider | `app/config.py`, README env table, **this file** |
| New external dependency | `pyproject.toml`, **this file** if architectural |

---

## Related documentation

- [`CONVENTION.md`](CONVENTION.md) — commits, PRs, and doc-update expectations
- [`../README.md`](../README.md) — setup, run commands, project tree
