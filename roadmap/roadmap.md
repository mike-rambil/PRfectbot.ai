# PRfectbot Development Roadmap (TDD)

> **Note:** The auto-fix on @PRfectbot mention feature is being integrated soon! A placeholder is present in the code and will be replaced with the full implementation.

## 1. GitHub App Integration

- [ ] 1.1. Register GitHub App and configure permissions
- [ ] 1.2. Write tests for webhook signature verification
- [ ] 1.3. Implement webhook signature verification logic
- [ ] 1.4. Write tests for event payload parsing (e.g., PR comment events)
- [ ] 1.5. Implement event payload parsing

## 2. Webhook Server (FastAPI)

- [ ] 2.1. Write tests for webhook endpoint (e.g., POST /webhook)
- [ ] 2.2. Implement webhook endpoint to receive GitHub events
- [ ] 2.3. Write tests for event routing (e.g., only respond to PR comments)
- [ ] 2.4. Implement event routing logic

## 3. PR Comment Detection Logic

- [ ] 3.1. Write tests for detecting @PRfectbot mention and fix requests in comments
- [ ] 3.2. Implement mention and intent detection logic

## 4. PR Code Fetching & Cloning

- [ ] 4.1. Write tests for extracting repo/branch info from event payload
- [ ] 4.2. Write tests for cloning the correct PR branch
- [ ] 4.3. Implement repo/branch extraction and cloning logic

## 5. Automated Fixes (Linters/Formatters)

- [ ] 5.1. Write tests for running linter/formatter on cloned code
- [ ] 5.2. Implement linter/formatter integration (e.g., black, ruff)
- [ ] 5.3. Write tests for detecting and collecting code changes

## 6. Commit & Push Fixes

- [ ] 6.1. Write tests for committing changes to the PR branch
- [ ] 6.2. Implement commit and push logic

## 7. PR Comment Update

- [ ] 7.1. Write tests for posting a comment back to the PR via GitHub API
- [ ] 7.2. Implement comment posting logic

## 8. Error Handling & Edge Cases

- [ ] 8.1. Write tests for unsupported events, missing permissions, or failed fixes
- [ ] 8.2. Implement robust error handling and fallback responses

## 9. Deployment & Configuration

- [ ] 9.1. Write tests for environment/config loading (e.g., secrets, tokens)
- [ ] 9.2. Implement config loading and Dockerization
