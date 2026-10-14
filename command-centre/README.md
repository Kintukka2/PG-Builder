# Command Centre

Source for the two project pages published as claude.ai artifacts. The published pages are the live versions. These files are the source they were published from.

| Page | Source | Published artifact | Data it keeps |
|---|---|---|---|
| PG Command Centre | [`command-centre.html`](command-centre.html) | [claude.ai/artifact/G3PMkvp68jSbqULxECehCi](https://claude.ai/artifact/G3PMkvp68jSbqULxECehCi) | `items`, `gaps`, `activity`, `decisions` |
| PG Delivery Flow (proof of concept) | [`delivery-flow.html`](delivery-flow.html) | [claude.ai/artifact/Qb7C1s8Vmnt8av3ams3jrJ](https://claude.ai/artifact/Qb7C1s8Vmnt8av3ams3jrJ) | `flow/draft`, `flow/status` |

Both artifacts are private to their owner until shared from the page's Share menu.

## How the data works

- Each page declares the artifact `db` capability. Records live in the artifact's tracker database, **not** in the HTML. A republished page keeps its data.
- The command centre derives everything it shows (counts, gauge, attention list, radar) from the four collections. Moving a card writes `items/<id>.stage`. Ticking a gap writes `gaps/<id>.status`. Each move also adds an `activity` entry.
- The delivery flow renders the built-in proposal until a draft is saved. **Save draft** writes `flow/draft`. **Approve flow** writes `flow/status`.
- [`data/tracker-seed.json`](data/tracker-seed.json) is the initial snapshot loaded on 2026-10-14. It came from the roadmap master backlog and the two validation registers. It is a starting point, not the live state; read the tracker for that.

### Record shapes

| Collection | Key fields |
|---|---|
| `items` | `rank`, `title`, `short`, `release` (1–4), `priority`, `type`, `readiness`, `module`, `batch`, `risk`, `stage`, `version`, `next`, `updated`, `pr {num, state}`, `files {docx, preview, validation, screenshots}` (repo paths prefixed with the branch) |
| `gaps` | `pg` (item id), `vg`, `title`, `pri` (`B` or `N`), `area`, `method`, `status` (`Open`, `Closed`, `Deferred`, `Withdrawn`) |
| `activity` | `date`, `at`, `kind` (`draft`, `merge`, `decision`, `move`, `sync`), `text`, `ref` |
| `decisions` | `code`, `title`, `status` (`Open`, `Provisional`) |

`stage` is one of the eight development gates: `identified`, `source-reviewed`, `gap-validated`, `drafted`, `system-tested`, `sme-validated`, `approved`, `published`.

## Keeping it current

When a guide moves, a register changes or a PR opens or merges, Claude updates the tracker records directly. The page does not need republishing. Change the HTML only to change the page itself, then republish it to the same artifact URL.

## Local preview

```bash
python3 tools/make_preview.py command-centre.html data/tracker-seed.json /tmp/preview.html
NODE_PATH=$(npm root -g) node tools/screenshot.js /tmp /tmp/preview.html
```

`make_preview.py` wraps a page in the viewer's skeleton with an in-memory stand-in for the tracker. `screenshot.js` captures dark, light and phone layouts with Playwright and reports horizontal overflow and console errors.

## Constraints of the artifact viewer

- Scripts load only from approved CDNs and stylesheets only from Google Fonts. Both pages are vanilla HTML, CSS and JavaScript, with no libraries.
- No `alert`, `confirm` or `prompt`. Confirmations are built into the page.
