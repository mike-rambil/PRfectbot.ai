## 🧭 PRfectBot LLM API Roadmap (Scalable Version)

### ⚙️ Phase 1: **LLM API Server (FastAPI)**

#### ✅ Objective

Build a FastAPI service that wraps your local model (e.g., `ollama`, `lmstudio`, etc.).

#### 🔧 Tasks

1. **Create FastAPI app** with:

   - Endpoint: `POST /fix`
   - Input: `code`, `diff`, `context`
   - Output: `fixed_code`

2. **Invoke model via subprocess or Python API**
3. **Log input/output for debugging**
4. **Include validation with Pydantic**

#### 🧱 Example (modular)

```python
from fastapi import FastAPI
from pydantic import BaseModel
import subprocess

app = FastAPI()

class FixRequest(BaseModel):
    code: str
    diff: str | None = None
    context: str | None = "Fix the following code"

@app.post("/fix")
async def fix_code(req: FixRequest):
    prompt = f"{req.context}\n\n{req.code}"
    result = subprocess.run(
        ["ollama", "run", "codellama", prompt],
        capture_output=True,
        text=True
    )
    return {"fixed_code": result.stdout}
```

---

### ⚙️ Phase 2: **GitHub Bot to Use the LLM API**

#### ✅ Objective

Wire your GitHub App to send files or diffs to the local LLM API.

#### 🔧 Tasks

1. Webhook listener (`issue_comment`, `pull_request`)
2. Detect `@PRfectbot fix` in comment body
3. Clone the PR branch
4. For each file in the diff:

   - Read content
   - `POST /fix` to your LLM API
   - Overwrite file with `fixed_code`

5. Commit, push, and comment back

#### 🔁 Example call

```python
import httpx

def fix_with_local_llm(file_content: str, context: str = None) -> str:
    payload = {
        "code": file_content,
        "context": context or "Fix issues in this Python script"
    }
    response = httpx.post("http://localhost:8000/fix", json=payload)
    return response.json()["fixed_code"]
```

---

### ⚙️ Phase 3: **Enhancements for Production Readiness**

#### 🔧 Logging

- Log inputs, outputs, timestamps, and errors
- Mask sensitive data in logs

#### 🔧 Timeout Control

- Add timeout to model subprocess calls (e.g., 30s)

#### 🔧 Rate Limiting

- Optional middleware to prevent abuse

#### 🔧 Testing

- Unit test LLM API separately from GitHub integration

---

### 🚀 Phase 4: **Deployable API**

#### ✅ Later You Can

- Containerize with Docker
- Run locally or on a server (e.g., Fly.io, Railway)
- Add an auth token if exposed remotely

---

### 🧰 Tools Checklist

| Tool             | Role                        |
| ---------------- | --------------------------- |
| FastAPI          | LLM HTTP API server         |
| httpx            | Client for bot to call LLM  |
| GitPython        | Clone, edit, commit PR code |
| PyGithub         | Read/write PR comments      |
| Ollama/LM Studio | Local model runtime         |

---
