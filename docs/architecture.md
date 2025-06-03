# Architecture Overview

PRfectbot is built around a small FastAPI application that listens for GitHub webhook events.
The key components include:

- **Webhook Endpoint** (`prfectbot/main.py`)
  - Handles `issue_comment` events.
  - Triggers `process_pull_request` when a fix is requested.
- **Pull Request Processor** (`prfectbot/pr_processor.py`)
  - Clones the specified branch using helpers in `gitutils`.
  - Runs code formatters (`black` and `prettier`).
  - Commits and pushes any changes back to the branch.
- **Git Utilities** (`prfectbot/gitutils.py`)
  - Encapsulate git operations and command execution.

Tests cover each part of this flow, ensuring the bot behaves correctly without requiring network access.
