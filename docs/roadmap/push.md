# Automating Code Changes and Pull Requests with a Bot

## Context: Existing FastAPI Features

- **Webhook Endpoint**: The FastAPI app exposes a `/webhook` POST endpoint that listens for GitHub webhook events, specifically `issue_comment` events.
- **Triggering Fixes**: When a comment contains `@PRfectbot fix`, the server extracts repository and branch information from the event payload.
- **Cloning**: The bot clones the relevant PR branch into a temporary directory for processing.
- **Logging**: All incoming requests and key actions (such as cloning) are logged at the INFO level for traceability.
- **No Automated PRs Yet**: The current implementation does not make code changes, push commits, or create PRs on GitHub. This document describes how to extend the bot to do so.

---

This guide outlines how to automate the process of making code changes, committing, pushing, and creating/updating a pull request (PR) to GitHub from a server or bot.

## 1. Clone the Target Repository and Branch

- Use `git` to clone the repository and checkout the target branch.
- Example (Python):

  ```python
  import subprocess
  subprocess.run(["git", "clone", "--single-branch", "--branch", branch, repo_url, clone_dir])
  ```

## 2. Make Code Changes

- Programmatically modify files as needed (e.g., fix lint errors, update code).

## 3. Commit the Changes

- Stage and commit the changes:

  ```python
  subprocess.run(["git", "add", "."], cwd=clone_dir)
  subprocess.run(["git", "commit", "-m", "Automated fix by PRfectbot"], cwd=clone_dir)
  ```

## 4. Push to a Branch on GitHub

- Push to a new or existing branch (requires authentication, e.g., a GitHub token):

  ```python
  subprocess.run(["git", "push", "origin", branch_name], cwd=clone_dir)
  ```

## 5. Create or Update a Pull Request

- Use the [GitHub API](https://docs.github.com/en/rest/pulls/pulls?apiVersion=2022-11-28#create-a-pull-request) to create or update a PR.
- Example (Python, using `requests`):

  ```python
  import requests
  headers = {"Authorization": f"token {GITHUB_TOKEN}"}
  data = {
      "title": "Automated Fix by PRfectbot",
      "head": branch_name,
      "base": base_branch,
      "body": "This PR was created automatically by PRfectbot."
  }
  response = requests.post(
      f"https://api.github.com/repos/{owner}/{repo}/pulls",
      headers=headers,
      json=data
  )
  print(response.json())
  ```

## 6. Notes

- Use a GitHub App or Personal Access Token with appropriate permissions.
- Clean up temporary files/directories after the process.
- Handle errors and edge cases (e.g., branch already exists, PR already open).

---

This workflow enables a bot to automatically fix code and open PRs, streamlining repository maintenance and automation.
