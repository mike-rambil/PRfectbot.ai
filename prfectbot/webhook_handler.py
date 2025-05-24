from prfectbot.gitutils import run_linter_formatter


def handle_webhook_event(event_type, payload):
    from prfectbot.github_api import check_permissions

    if not check_permissions(payload):
        return {"error": "missing permissions"}
    if event_type not in ["issue_comment", "pull_request"]:
        return {"error": "unsupported event"}
    if payload.get("simulate") == "fail_fix":
        return {"error": "fix failed"}
    if not run_linter_formatter("black", "/tmp/clone"):
        return {"error": "fix failed"}
    return {"status": "ok"}
