from fastapi import FastAPI, Request, Response, status
from prfectbot.github_events import (
    is_fix_requested,
    extract_pr_repo_branch,
)
from prfectbot.pr_processor import process_pull_request
import logging
from fastapi.responses import HTMLResponse

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

app = FastAPI()


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logging.info(f"Request: {request.method} {request.url}")
    logging.info(f"Path: {request.url.path}")
    logging.info(f"Query params: {request.query_params}")
    logging.info(f"Headers: {dict(request.headers)}")
    logging.info(f"Client IP: {request.client.host if request.client else 'unknown'}")
    logging.info(f"Cookies: {request.cookies}")
    response = await call_next(request)
    status_code = getattr(response, "status_code", None)
    headers = getattr(response, "headers", {})
    logging.info(f"Response status: {status_code}")
    logging.info(f"Response headers: {dict(headers)}")
    return response


@app.post("/webhook")
async def webhook(request: Request):
    event = request.headers.get("X-GitHub-Event")
    if event == "issue_comment":
        payload = await request.json()
        comment_body = payload.get("comment", {}).get("body", "")
        if is_fix_requested(comment_body):
            pr_info = extract_pr_repo_branch(payload)
            process_pull_request(
                pr_info.get("repo_owner"),
                pr_info.get("repo_name"),
                pr_info.get("branch"),
            )
            logging.warning(
                "🤖 PRfectbot processed the pull request and pushed any fixes."
            )
            return {"status": "fix requested"}
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <div style="text-align:center; font-family:sans-serif; padding:2em;">
      <img src="/static/@PRfectbot.ai.png" alt="PRfectbot Logo" style="width:120px; border-radius:24px; box-shadow:0 2px 8px #0001; margin-bottom:1em;"/>
      <h1>Welcome to <span style="color:#0070f3;">PRfectbot</span>!</h1>
      <p style="font-size:1.2em;">Automate your PR fixes with a single comment.</p>
      <h2>🚀 How to Install</h2>
      <ol style="text-align:left; display:inline-block; margin:0 auto; font-size:1.1em;">
        <li>Go to the <a href="https://github.com/apps/prfectbot/installations/new" target="_blank">PRfectbot GitHub App installation page</a>.</li>
        <li>Select your account or organization.</li>
        <li>Choose the repositories to install the bot on.</li>
        <li>Click <b>Install</b> and you're done!</li>
      </ol>
      <p style="margin-top:2em; color:#555;">Mention <b>@PRfectbot fix ...</b> in a PR comment to trigger automated fixes.</p>
    </div>
    """
