# PRfectbot Automated PR Processing

This document explains how PRfectbot automatically processes pull requests when a comment requests fixes.

## Workflow

1. **Webhook receives an `issue_comment` event**
   - The bot checks if the comment mentions `@PRfectbot` and contains the word `fix`.
2. **Extract repository and branch information**
   - `extract_pr_repo_branch` gathers the PR owner, repository name, and branch from the event payload.
3. **Process the pull request**
   - `process_pull_request` clones the PR branch into a temporary directory.
   - It runs `black` and `prettier` to ensure consistent formatting.
   - If changes are detected, the bot commits and pushes them back to the same branch.
4. **Respond to the webhook**
   - The endpoint returns `{"status": "fix requested"}` when processing succeeds.

## Related Modules

- `prfectbot/pr_processor.py` – high level orchestration of cloning, linting, and pushing fixes.
- `prfectbot/gitutils.py` – helper functions for cloning repositories, running formatters, and pushing commits.
- `prfectbot/main.py` – FastAPI application exposing the `/webhook` endpoint and root page.

## Testing

All features are covered by unit tests in the `tests/` directory. Run tests with:

```bash
pytest -q
```
