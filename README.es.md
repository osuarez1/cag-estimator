## estimador-cag

`estimador-cag` es un pequeño servicio FastAPI diseñado como base para soportar un flujo de trabajo de generación aumentada con caché (CAG).

## Uso real (sin mock)

Para usar un proveedor **real** (no `mock`), configura tus credenciales (Infisical o `.env`) y arranca el servidor **sin** `LLM_PROVIDER=mock`.

Arranca el servidor:

```bash
uv run uvicorn app.main:app --reload
```

En otra terminal, prueba el endpoint:

```bash
curl -X POST http://localhost:8000/api/v1/estimate \
  -H "Content-Type: application/json" \
  -d '{
    "transcription": "En la reunión con el equipo de marketing, el cliente explicó que necesita una landing page con formulario de contacto, integración con su CRM actual (HubSpot), y una sección de blog con editor WYSIWYG. El plazo ideal sería tenerlo listo en 4 semanas. El diseño ya existe en Figma."
  }'
```

## Inicio rápido

Instala dependencias:

```bash
uv sync
```

Ejecuta la API (no se necesitan claves):

```bash
LLM_PROVIDER=mock uv run uvicorn app.main:app --reload
```

La Swagger UI está disponible en `/docs`.

## Árbol del proyecto

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
├── exercises/
│   ├── README.md
│   └── transcripts/
│       └── meeting_transcript.md
├── scripts/
│   └── verify.py
├── .env
├── .env.example
├── .gitignore
├── pyproject.toml
└── README.md
```

## Arquitectura

Diseño por capas: `routers` → `services` → `context`, con despacho multi-proveedor de LLM en `app/services/llm_service.py`.

Diagramas completos, flujos de request, tablas de proveedores y reglas de extensión:
[`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).

## Verificación (“tests”)

La verificación automatizada se realiza con:

```bash
uv run python scripts/verify.py
```

Este script levanta la API (puerto por defecto `8001`), comprueba `/health` y `/docs`, y luego llama a `POST /api/v1/estimate`
usando la transcripción en [`exercises/transcripts/meeting_transcript.md`](exercises/transcripts/meeting_transcript.md).
Ejecútalo localmente o desde tu sistema de CI preferido.

## Instalación y configuración

La configuración se carga desde el entorno del proceso. En desarrollo, usa **o bien** Infisical **o bien** un archivo `.env` local.
Consulta [`.env.example`](.env.example) para ver todos los nombres de variables (sin valores secretos).

### Opción A — Infisical (desarrollo o producción)

```bash
infisical run --env=dev -- uv run uvicorn app.main:app --reload
```

Usa el entorno de Infisical que corresponda con tu despliegue (`dev`, `staging`, `prod`, etc.). Las claves deben coincidir con `.env.example`.

### Opción B — `.env` local

```bash
cp .env.example .env
# Edita .env con tus claves de API (el archivo está en gitignore)
uv run uvicorn app.main:app --reload
```

### Variables de entorno

| Variable | Por defecto | Notas |
|----------|-------------|-------|
| `LLM_PROVIDER` | `openai` | `openai`, `anthropic`, `gemini` o `mock` |
| `LLM_MODEL` | `gpt-4o-mini` | Hay valores por defecto por proveedor si no se define en el entorno |
| `OPENAI_API_KEY` | — | Requerida cuando `LLM_PROVIDER=openai` |
| `ANTHROPIC_API_KEY` | — | Requerida cuando `LLM_PROVIDER=anthropic` |
| `GOOGLE_API_KEY` | — | Requerida cuando `LLM_PROVIDER=gemini` |
| `APP_ENV` | `development` | Etiqueta de entorno |
| `LOG_LEVEL` | `DEBUG` | `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL` |

El entorno del proceso tiene prioridad sobre `.env` cuando ambos definen la misma clave.

## Ejecutar

```bash
uv run uvicorn app.main:app --reload
```

(Envuélvelo con `infisical run` si usas Infisical.)

## Ejercicios

Consulta [`exercises/README.md`](exercises/README.md) para las instrucciones del ejercicio y la transcripción que se usa como input.

## Contribuir

Los mensajes de commit y los pull requests siguen [`docs/CONVENTION.md`](docs/CONVENTION.md) (Conventional Commits,
modo imperativo y estructura de PR en GitHub). Los asistentes de código deberían leer ese archivo antes de redactar commits
o descripciones de PR.

Los cambios arquitectónicos deben actualizar [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) en el mismo conjunto de cambios
(ver `CLAUDE.md` y `.cursorrules`).

