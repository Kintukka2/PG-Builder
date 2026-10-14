# Screenshot Register: AR Collections Personalized Views

| Field | Value |
|---|---|
| Related PG | [`../01-procedure-guides/TBC-AR Collections Personalized Views PG v0.1.docx`](../01-procedure-guides/TBC-AR%20Collections%20Personalized%20Views%20PG%20v0.1.docx) (editable source) |
| Source recording | *AR Training D365*. The timestamps for the views demonstration have **not been supplied** (`VG-27`). |
| Frames reviewed | None |
| Last updated | 2026-10-14 |

> **Template rule (PG Template Authoring Guide).** Screenshots are optional. The text must explain each action and result on its own, and a clean guide must not contain screenshot placeholders. The Word guide therefore has no figures (decision D-017). Only the candidates below that add context should be captured, once the control locations are confirmed.

The capture limitations, privacy rules and clean-session recapture specification in the [AR Collections Favorites screenshot register](PG-AR-Configure-Collections-Favourites-Screenshots.md#4-clean-session-recapture-specification) apply here as well.

## Candidate figures

Each candidate is a control whose location the text cannot fully describe until it is confirmed. Captions use the format `Figure n. <Outcome or screen name>`.

| Fig | Word guide step | Screen content | Draft caption | Required callouts | Timestamp | Status |
|---|---|---|---|---|---|---|
| 1 | 1.1 Step 3 | The grid with the **Insert columns** control visible | Figure 1. Insert columns on a D365 grid | **Insert columns** | Not supplied (`VG-27`) | Placeholder; resolves `VG-03` |
| 2 | 1.1 Step 4 | The column selection with the recommended columns selected | Figure 2. Select the columns to add | The selected columns; the apply control (`VG-04`) | Not supplied | Placeholder |
| 3 | 1.2 Step 2 | A column filter showing the **not equal to** operator and the value **0** | Figure 3. Exclude zero balances with a column filter | Operator; value; apply control (`VG-08`) | Not supplied | Placeholder; use mock data |
| 4 | 1.3 Step 2 | The grid footer with a **Sum** on an amount column | Figure 4. A footer total on an amount column | The footer; the **Sum** control (`VG-09`, `VG-10`) | Not supplied | Placeholder; mask amounts |
| 5 | 1.4 Steps 1–4 | The view controls showing **Save as** and **Pin as default** | Figure 5. Save and pin a personalized view | **Save as**; view name; **Pin as default** (`VG-11` to `VG-14`) | Not supplied | Placeholder; recommended if only one figure is used |

**Privacy.** Grids in this guide show customer names, account numbers and balances. Every figure must use mock or masked data. The masking policy is still open as item VG-27 in the Favorites validation register.

## Change log

| Date | Change |
|---|---|
| 2026-10-14 | Register created. There are no timestamps yet. |
