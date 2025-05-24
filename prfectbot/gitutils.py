import subprocess


def run_git_clone(repo_url, branch, dest_dir):
    try:
        subprocess.run([
            "git", "clone", "--single-branch", "--branch", branch, repo_url, dest_dir
        ], check=True)
        return True
    except Exception:
        return False


def clone_pr_branch(repo_owner, repo_name, branch, dest_dir):
    if not all([repo_owner, repo_name, branch, dest_dir]):
        return False
    repo_url = f"https://github.com/{repo_owner}/{repo_name}.git"
    return run_git_clone(repo_url, branch, dest_dir)


def run_linter_formatter(tool, target_dir):
    try:
        subprocess.run([tool, target_dir], check=True)
        return True
    except Exception:
        return False 