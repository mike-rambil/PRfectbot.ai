def post_comment(repo_owner, repo_name, pr_number, message):
    # This would call the GitHub API in real usage
    return True

def post_pr_comment(repo_owner, repo_name, pr_number, message):
    try:
        return post_comment(repo_owner, repo_name, pr_number, message)
    except Exception:
        return False

def check_permissions(payload):
    # Stub: always return True unless mocked
    return True 