from fastapi import FastAPI, Request, Response, status

app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request):
    event = request.headers.get("X-GitHub-Event")
    if event == "issue_comment":
        return {"status": "received"}
    return Response(status_code=status.HTTP_204_NO_CONTENT) 