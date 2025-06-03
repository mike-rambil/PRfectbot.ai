import os
import requests

def post_comment(repo_owner, repo_name, pr_number, message):
    """Post a comment to a GitHub PR using the GitHub API."""
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise RuntimeError("GITHUB_TOKEN environment variable not set.")
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues/{pr_number}/comments"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }
    data = {"body": message}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        return True
    else:
        print(f"Failed to post comment: {response.status_code} {response.text}")
        return False


def post_pr_comment(repo_owner, repo_name, pr_number, message):
    try:
        return post_comment(repo_owner, repo_name, pr_number, message)
    except Exception as e:
        print(f"Error posting PR comment: {e}")
        return False


def check_permissions(payload):
    # Stub: always return True unless mocked
    return True
