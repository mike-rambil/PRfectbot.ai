from fastapi import FastAPI, Request, Response, status
from prfectbot.github_events import parse_pr_comment_event, is_fix_requested, extract_pr_repo_branch
from prfectbot.gitutils import clone_pr_branch
import logging
import tempfile

app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request):
    event = request.headers.get("X-GitHub-Event")
    if event == "issue_comment":
        payload = await request.json()
        comment_body = payload.get("comment", {}).get("body", "")
        if is_fix_requested(comment_body):
            # Extract repo/branch info from a related PR event (simulate for now)
            pr_info = extract_pr_repo_branch(payload)
            # Use a temp dir for cloning
            with tempfile.TemporaryDirectory() as tmpdir:
                result = clone_pr_branch(
                    pr_info.get('repo_owner'),
                    pr_info.get('repo_name'),
                    pr_info.get('branch'),
                    tmpdir
                )
                logging.warning(f"🤖 PRfectbot is warming up its fixing lasers! Pew pew! 🚀 Clone result: {result}")
            return {"status": "fix requested"}
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    return Response(status_code=status.HTTP_204_NO_CONTENT) 