## Exercise: estimador-cag (CAG Estimator)

This exercise validates a complete CAG-style flow:

receive transcript → inject reference examples (context) → call LLM provider → return estimation.

### Files

- `transcripts/meeting_transcript.md`: the meeting transcript you should pass as the `transcription` parameter.

### Run the API

```bash
uv sync
uv run uvicorn app.main:app --reload
```

Swagger UI is available at `/docs`.

### Call the estimation endpoint

```bash
curl -sS -X POST "http://127.0.0.1:8000/api/v1/estimate" \
  -H "Content-Type: application/json" \
  -d "$(python - <<'PY'
from pathlib import Path
import json

transcript = Path("exercises/transcripts/meeting_transcript.md").read_text(encoding="utf-8")
print(json.dumps({"transcription": transcript}))
PY
)"
```
