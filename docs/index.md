# Agent Integration Scope Index

The smallest set of OAuth scopes or permissions an AI agent needs for common
tasks, per provider, with what each scope actually exposes and what review it
triggers.

If you're building an agent that reads a user's inbox, posts to Slack or opens
a pull request, this is the page that answers "what's the least I can ask for?"

**Canonical site:** https://agenticfabriq.github.io/agent-integration-scope-index/
**Maintainer:** [Agentic Fabriq](https://www.agenticfabriq.com/developers) · **Data:** CC BY 4.0 · **Code:** Apache-2.0

---

## What's in each record

One YAML file per provider in [`providers/`](https://github.com/agenticfabriq/agent-integration-scope-index/tree/main/providers), validated by
[`schema/provider.schema.json`](https://github.com/agenticfabriq/agent-integration-scope-index/blob/main/schema/provider.schema.json):

- **auth_mechanisms** — OAuth app, app installation, API key, service account
- **tasks** — a common agent task (for example "send an email as the user") with
  the minimum scopes, what else those scopes unlock, and safer alternatives
- **review_triggers** — provider verification or admin consent the scope causes
- **token_behavior** — lifetime and refresh notes that break long-running agents
- **sources** — links to the provider's own documentation for every claim
- **verification** — who last checked the record against provider docs, and when

## Providers

| Provider | File | Status |
|---|---|---|
| Gmail | [`providers/gmail.yaml`](https://github.com/agenticfabriq/agent-integration-scope-index/blob/main/providers/gmail.yaml) | needs-review |
| Google Drive | [`providers/google-drive.yaml`](https://github.com/agenticfabriq/agent-integration-scope-index/blob/main/providers/google-drive.yaml) | needs-review |
| Slack | [`providers/slack.yaml`](https://github.com/agenticfabriq/agent-integration-scope-index/blob/main/providers/slack.yaml) | needs-review |
| GitHub | [`providers/github.yaml`](https://github.com/agenticfabriq/agent-integration-scope-index/blob/main/providers/github.yaml) | needs-review |
| Microsoft Graph (Outlook, OneDrive, Teams) | [`providers/microsoft-graph.yaml`](https://github.com/agenticfabriq/agent-integration-scope-index/blob/main/providers/microsoft-graph.yaml) | needs-review |

Records move to `verified` only after someone checks every task against the
linked provider docs and fills in `verification.checked_on`.

## Principles

1. **Provider docs are the source of truth.** Every scope claim links to them.
2. **Least privilege first.** Each task lists the narrowest option, then broader
   ones with what they add.
3. **Vendor-neutral.** Records describe providers, not any integration
   platform. Nothing here requires using the maintainer's product.

## How to cite

See [`CITATION.cff`](https://github.com/agenticfabriq/agent-integration-scope-index/blob/main/CITATION.cff).

## Related

- [Agent Integration Playbook](https://agenticfabriq.github.io/): guides on OAuth flows, credential handling and failure modes
- [Agent Access Control Taxonomy](https://github.com/agenticfabriq/agent-access-control-taxonomy)

## About the maintainer

Agentic Fabriq builds [Fabriq Developer](https://www.agenticfabriq.com/developers),
an MCP gateway that brokers per-user OAuth for agents across 150+ tools. This
index is published so the scope decisions are open whichever stack you use.
