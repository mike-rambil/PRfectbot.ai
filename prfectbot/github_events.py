def parse_pr_comment_event(payload):
    return {
        "pr_number": payload["issue"]["number"],
        "repo_owner": payload["repository"]["owner"]["login"],
        "repo_name": payload["repository"]["name"],
        "comment_body": payload["comment"]["body"],
    }


def is_fix_requested(comment_body):
    body = comment_body.lower()
    return "@prfectbot" in body and "fix" in body


def extract_pr_repo_branch(payload):
    pr = payload.get("pull_request", {})
    pr_number = pr.get("number")
    head = pr.get("head", {})
    branch = head.get("ref")
    repo = head.get("repo", {})
    repo_owner = repo.get("owner", {}).get("login")
    repo_name = repo.get("name")
    # Fallback to top-level repository if missing in head
    if repo_owner is None or repo_name is None:
        repo_owner = payload.get("repository", {}).get("owner", {}).get("login")
        repo_name = payload.get("repository", {}).get("name")
    return {
        "pr_number": pr_number,
        "repo_owner": repo_owner,
        "repo_name": repo_name,
        "branch": branch,
    }
