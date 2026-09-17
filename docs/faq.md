# FAQ

## What is the minimum Gmail scope for an agent to send email?
`https://www.googleapis.com/auth/gmail.send`. It grants send only, with no read access to the mailbox. It is a sensitive scope, so a Google OAuth app verification is required before external users can authorize it. See `providers/gmail.yaml`.

## Why not ask for the broadest scope and be done?
Broad scopes trigger stricter provider review (Google's restricted-scope assessment, Slack app review, GitHub App permission prompts) and widen the blast radius if a token leaks. Every record here pairs the minimum scope with what else it unlocks, so the trade-off is visible.

## What does `verification.status` mean?
`needs-review` means the record was written from provider documentation but has not yet been checked line by line by a named person. `verified` records carry `checked_on` and `checked_by`. Records older than twelve months flip to `stale`.

## How do I add a provider?
Copy `providers/slack.yaml`, keep tasks to the three to five most common agent jobs, link the provider's own docs for every claim, and run `python scripts/validate.py`.
