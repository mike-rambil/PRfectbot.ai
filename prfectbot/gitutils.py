import subprocess


def run_git_clone(repo_url, branch, dest_dir):
    try:
        subprocess.run(
            ["git", "clone", "--single-branch", "--branch", branch, repo_url, dest_dir],
            check=True,
        )
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


def detect_code_changes_v2(repo_dir, run=subprocess.run):
    try:
        result = run(
            ["git", "status", "--porcelain"],
            cwd=repo_dir,
            capture_output=True,
            text=True,
            check=True,
        )
        if hasattr(result, "stdout"):
            changes = result.stdout.strip().splitlines()
            return changes if changes else []
        return []
    except Exception:
        return None


def commit_and_push_fixes(repo_dir, branch):
    try:
        # Check for changes
        changes = detect_code_changes_v2(repo_dir)
        if not changes:
            return False
        # Add all changes
        subprocess.run(["git", "add", "-A"], cwd=repo_dir, check=True)
        # Commit
        subprocess.run(
            ["git", "commit", "-m", "fix: automated fixes by PRfectbot"],
            cwd=repo_dir,
            check=True,
        )
        # Push
        subprocess.run(["git", "push", "origin", branch], cwd=repo_dir, check=True)
        return True
    except Exception:
        return False
