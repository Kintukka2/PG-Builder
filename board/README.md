# PG Builder Board

**[Open the board](https://claude.ai/artifact/5GPzzPrEYyUSAn12EBgWLf)**

The board is the single status tracker for every procedure guide in every stream (D-068). It is a claude.ai page with its own database. [`PG-Board.html`](PG-Board.html) is its page code; the records live in the database, not in this repository. The user and Claude both edit the board, and every edit is logged.

It is private to its owner. Anyone the owner shares it with can view it; only the owner and people given Editor access can change it.

## Tabs

| Tab | What it shows |
|---|---|
| PG Board | One card per guide, in the lane for whose turn it is. Each card shows its streams, its ticket, shared draft and Training Hub links (a red **Draft?** or **Hub?** means the link is missing), its SME questions, the next action and the repository files. Blocked and Withdrawn guides open from the pills above the board. Any column can be hidden with its eye icon. |
| PG Weekly Sync | Meeting notes. Claude turns new notes into decisions, actions and proposed card changes. |
| PG Numbering | A read-only view of the master register in [`standards/numbering/`](../standards/numbering/). |
| How we work | The process, the lanes, the question and comment rules, roles, and where things live. |

**Questions live on each card** (D-077). The card's questions link (for example *6 open questions*, with *Not sent yet*, *Sent · awaiting SME*, *Answers to apply* or *On hold*) opens a popup for that ticket: copy the questions, edit them, mark them sent, or paste the SME's answers. A card with no questions can have them added the same way.

**Edit** on a card opens every detail: stage, streams, people, ticket, version, next action, notes, the shared draft and Hub links, the repository files, the reference links (editable, with a *needs checking* flag that shows an amber **Links !** pill on the card) and the card's recent updates.

**Settings** holds the ADO work item link pattern; with it set, every ticket number on the cards opens its work item.

## Data model

| Collection | Document | Fields |
|---|---|---|
| `guides` | `g-<code>` (for example `g-220`, `g-o-0001`), or `g-<name>` for a guide with no code | `title`, `code`, `streams[]`, `stage`, `confirmed`, `assignedTo`, `source`, `approver`, `bpo`, `ticket`, `version`, `next`, `notes`, `links{word, preview, register, decisions, draft, hub}`, `items{open, blocking, carried, comments}`, `references[{id, title, url, location, needsReview}]`, `hyperlinks{scannedAt, file, version, total, contents, internal, external, pgRefs, pgLinked, pgMissing, items[{n, ref, code, title, titled, where, status, url, hubUrl}], other[{text, url, where}], note}` (written by Claude from `tools/pg_links.py --json`; shown by the card's Links pill, D-096; `status` is `linked`, `other-link`, `missing` or `not-published`), `history[]` (imported entries), `updatedAt`, `updatedBy` |
| `rounds` | `r-<code>-<n>` | `title`, `guideIds[]`, `askTo`, `ticket`, `status` (`draft`, `ready`, `sent`, `answered`, `closed`), `intro`, `outro`, `questions[{n, theme, text, ref, page, parts[{label, text, ref, page, items[]}], items[]}]`, `pagesFrom` (`ref`: the section and step where the items sit, D-079; `page`: the pages to look at, shown in the copied text, D-080; `pagesFrom` says whether they are estimates or come from the copy saved in Word, D-082), `customText`, `answer`, `sentAt`, `answeredAt`, `statusNote` |
| `meetings` | any id | `date`, `title`, `notes`, `decisions`, `actions`, `guideIds[]`, `processed` |
| `log` | any id | `at`, `by` (a viewer id, `claude` or `chatgpt`), `guideId`, `kind` (`edit`, `note`, `round`, `create`), `text` |
| `meta` | `register` | A copy of `PG_Numbering_Master_Register.json` |
| `meta` | `sync` | `lastSyncAt`, `by`, `note` |
| `meta` | `settings` | `adoPattern` (the ADO work item link, with `{id}` for the ticket number) |

`stage` is one of `intake` (Initial Ticket Created), `drafting`, `sme` (Waiting for SME feedback), `updating`, `signoff` (Sent for sign-off), `ready`, `published`, `blocked` or `withdrawn`. `confirmed: false` marks a lane Claude inferred and the user has not confirmed.

## Claude's routine

1. **Start of session:** read `meta/sync`, then the `log` entries newer than `lastSyncAt` that are not by `claude`, the rounds with status `answered` and the meetings with `processed: false`. Carry them into the repository, then update `meta/sync`.
2. **After any change to a guide:** update its card (lane, version, next action, item counts, links) and add a `log` entry with `by: "claude"`, in the same turn as the commit.
3. **When the numbering register changes:** refresh `meta/register`.

Claude never moves a card to Sign-off, Ready to publish or Published, and never marks a round sent, unless the user says it happened.

## Origin

Seeded on 2026-11-17 from the board kept in ChatGPT (23 cards, one meeting, the 240 questions), brought in line with this repository, plus the CW1 manual (now O-0001). The ChatGPT board is no longer updated. Each imported card keeps its ChatGPT history.
