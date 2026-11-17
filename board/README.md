# PG Builder Board

**[Open the board](https://claude.ai/artifact/5GPzzPrEYyUSAn12EBgWLf)**

The board is the single status tracker for every procedure guide in every stream (D-068). It is a claude.ai page with its own database. [`PG-Board.html`](PG-Board.html) is its page code; the records live in the database, not in this repository. The user and Claude both edit the board, and every edit is logged.

It is private to its owner. Anyone the owner shares it with can view it; only the owner and people given Editor access can change it.

## Tabs

| Tab | What it shows |
|---|---|
| Board | One card per guide, in the lane for whose turn it is. Blocked and Withdrawn sit below the lanes. |
| Questions | The question rounds (D-069): to send, with the SME, answers to apply, closed. Copy a round into the ADO ticket, mark it sent, paste the answers. |
| Weekly Sync | Meeting notes. Claude turns new notes into decisions, actions and proposed card changes. |
| Numbering | A read-only view of the master register in [`standards/numbering/`](../standards/numbering/). |
| How we work | The process, the lanes, the question-round and comment rules, roles, and where things live. |

## Data model

| Collection | Document | Fields |
|---|---|---|
| `guides` | `g-<code>` (for example `g-220`, `g-t-0001`), or `g-<name>` for a guide with no code | `title`, `code`, `streams[]`, `stage`, `confirmed`, `assignedTo`, `source`, `approver`, `bpo`, `ticket`, `version`, `next`, `notes`, `links{word, preview, register, decisions, draft, hub}`, `items{open, blocking, carried, comments}`, `references[]`, `history[]` (imported entries), `updatedAt`, `updatedBy` |
| `rounds` | `r-<code>-<n>` | `title`, `guideIds[]`, `askTo`, `ticket`, `status` (`draft`, `ready`, `sent`, `answered`, `closed`), `intro`, `outro`, `questions[{n, theme, text, parts[{label, text, items[]}], items[]}]`, `customText`, `answer`, `sentAt`, `answeredAt`, `statusNote` |
| `meetings` | any id | `date`, `title`, `notes`, `decisions`, `actions`, `guideIds[]`, `processed` |
| `log` | any id | `at`, `by` (a viewer id, `claude` or `chatgpt`), `guideId`, `kind` (`edit`, `note`, `round`, `create`), `text` |
| `meta` | `register` | A copy of `PG_Numbering_Master_Register.json` |
| `meta` | `sync` | `lastSyncAt`, `by`, `note` |

`stage` is one of `intake`, `drafting`, `sme`, `updating`, `signoff`, `ready`, `published`, `blocked` or `withdrawn`. `confirmed: false` marks a lane Claude inferred and the user has not confirmed.

## Claude's routine

1. **Start of session:** read `meta/sync`, then the `log` entries newer than `lastSyncAt` that are not by `claude`, the rounds with status `answered` and the meetings with `processed: false`. Carry them into the repository, then update `meta/sync`.
2. **After any change to a guide:** update its card (lane, version, next action, item counts, links) and add a `log` entry with `by: "claude"`, in the same turn as the commit.
3. **When the numbering register changes:** refresh `meta/register`.

Claude never moves a card to Sign-off, Ready to publish or Published, and never marks a round sent, unless the user says it happened.

## Origin

Seeded on 2026-11-17 from the board kept in ChatGPT (23 cards, one meeting, the 240 questions), brought in line with this repository, plus T-0001. The ChatGPT board is no longer updated. Each imported card keeps its ChatGPT history.
