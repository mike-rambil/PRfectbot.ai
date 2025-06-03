import logging
import tempfile
from typing import Optional
from .gitutils import (
    clone_pr_branch,
    run_linter_formatter,
    commit_and_push_fixes,
)
from .github_api import post_pr_comment


def process_pull_request(
    repo_owner: str,
    repo_name: str,
    branch: str,
    pr_number: Optional[int] = None,
) -> bool:
    """Clone the PR branch, run formatters, push fixes, and comment on the PR."""
    if not all([repo_owner, repo_name, branch]):
        logging.error("Missing repository information for processing PR")
        return False

    with tempfile.TemporaryDirectory() as tmpdir:
        # clone_pr_branch internally relies on run_git_clone to perform the
        # actual git command. This keeps the processor focused on high-level
        # orchestration while `gitutils` handles the low-level details.
        if not clone_pr_branch(repo_owner, repo_name, branch, tmpdir):
            logging.error("Failed to clone branch %s", branch)
            return False

        # Run code formatters
        run_linter_formatter("black", tmpdir)
        run_linter_formatter("prettier", tmpdir)

        # Commit and push any changes
        commit_and_push_fixes(tmpdir, branch)

        # Notify via PR comment when formatting is complete
        if pr_number is not None:
            post_pr_comment(
                repo_owner,
                repo_name,
                pr_number,
                "I have done linting and prettier checks.",
            )

    return True
