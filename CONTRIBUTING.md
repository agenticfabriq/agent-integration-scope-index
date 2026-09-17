# Contributing
- Every scope claim needs a link to the provider's own docs in `sources`.
- To mark a record `verified`, check each task against those docs and set `checked_on` (YYYY-MM-DD) and `checked_by`.
- Records older than 12 months are flipped to `stale` automatically by CI.
- New provider? Copy `providers/slack.yaml`, keep tasks to the 3–5 most common agent jobs.
