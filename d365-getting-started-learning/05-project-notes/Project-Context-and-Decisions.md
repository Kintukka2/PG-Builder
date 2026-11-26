# Project Context and Decisions: D365 F&O Getting Started

| Field | Value |
|---|---|
| Topic | Shared D365 skills and finance basics for every D365 user, in every stream (O2C, P2P, R2R, Tax) |
| Guides | **D365 F&O Getting Started** (all D365 users) and **D365 Finance Basics** (finance users), both planned, no code yet (D-101, D-102). A third guide on Copilot and AI features is parked (D-104). |
| Discovery | [Discovery map](Discovery-Map.md), 26 November 2026, with the research in [`discovery/`](discovery/) |
| Board | [PG Builder Board](https://claude.ai/artifact/5GPzzPrEYyUSAn12EBgWLf): `g-d365-getting-started`, `g-d365-finance-basics`, `g-d365-ai-features` (D-105) |
| Last updated | 2026-11-26 |

Decision IDs continue the repository sequence, so they never clash with the other logs ([AR decisions](../../ar-collections-learning/05-project-notes/Project-Context-and-Decisions.md), [GL decisions](../../gl-cw1-migration-learning/05-project-notes/Project-Context-and-Decisions.md)).

## 1. The two guides

From the [discovery map](Discovery-Map.md), section 3, split under D-101:

| | D365 F&O Getting Started | D365 Finance Basics |
|---|---|---|
| Audience | All D365 users | Finance users, after Getting Started |
| Part 1 key concepts | How the guides fit; the parts of the screen; legal entities; what you can see (D-083); system messages; filter operators and query syntax; views and personalization; workflow statuses and notifications; keyboard shortcuts | Financial dimensions and the account field; journals and vouchers; periods and dates; corrections are reversals; currencies, GST, parties, number sequences, intercompany; why won't it post? |
| Part 2 topics | 1 Set Up Your D365 Session; 2 Open a Page; 3 Switch Legal Entity; 4 Work with Records; 5 Find Records with Filters; 6 Create a Personalized View; 7 Manage Saved Views and Personalizations; 8 Export Data and Work in Excel; 9 Run a Report; 10 Attach a Document; 11 Submit and Approve Workflow Items; 12 Set Up an Alert; 13 Get Help and Report a Problem | 1 Enter an Account and Financial Dimensions; 2 Work with a Journal (header and lines, validate, post, open lines in Excel); 3 Find a Posted Transaction (Voucher transactions, Transaction origin, customer and vendor transactions); 4 Reverse a Posted Entry |
| Part 3 reports | The report dialog and destinations as a reference; where background output lands | Voucher transactions, Trial balance, customer and vendor transactions, Financial reports (the 90-day expiry) |

The topic lists are proposals for drafting; the subtopics are in the discovery map, section 3. Topic 15.2 *Ask Copilot* is removed from Getting Started (D-104).

## 2. Decisions log

| ID | Date | Decision | Rationale | Status |
|---|---|---|---|---|
| D-101 | 2026-11-26 | **The discovery becomes two guides.** *D365 F&O Getting Started* teaches the shared system skills (pages, workspaces, filtering, views, records, Excel, reports, attachments, workflow, alerts, help) to **all D365 users**. *D365 Finance Basics* teaches the finance concepts and tasks (dimensions and the account field, journals, vouchers, periods and dates, finding and reversing posted transactions) to **finance users**, with Getting Started as its prerequisite. The split follows section 1. If it does not work, the two can be consolidated later. | User (decisions 3 and 5 on the discovery map: "lets try go for 2"; "the audience will be all D365 users … then we could have a topic thats more finance focused"). Claude recommended placing the finance-focused content in the second guide rather than as a topic inside Getting Started, so the basic guide stays short for every user and the finance guide can go deeper. | Adopted |
| D-102 | 2026-11-26 | **High-level and general guides take the 100 series.** Both guides get codes in the 100 series once 460 Tangible Fixed Assets, 461 Intangible Fixed Assets and 462 Asset Leasing are approved and the legacy fixed assets documents now in 100 are retired (register: 100 is the former *Fixed Assets combined predecessor*, successor 460 / 461). Until then the guides have no code, and the register is unchanged: the family is defined and the codes allocated by the register owner when 100 is released, under the controlled-reuse rule. Working files use `TBC` in place of the code (for example `CLAUDE-TBC-D365 F&O Getting Started PG v0.1.docx`), renamed when the code is allocated. | User (decision 1) | Adopted; codes pending |
| D-103 | 2026-11-26 | **260 O2C Getting Started stays as it is.** O2C users use 260 until the new guides have been reviewed and approved; the decision on 260 is then revisited. This defers the archiving in D-098. | User (decision 2) | Adopted |
| D-104 | 2026-11-26 | **Copilot and AI features are out of both guides.** The research stays in [`discovery/D-workflow-help-copilot.md`](discovery/D-workflow-help-copilot.md) (Copilot sidecar, summaries on by default, Immersive Home, finance agents, licensing). If the content becomes needed, it can be a third guide; its card is parked in Blocked. | User (decision 4) | Adopted |
| D-105 | 2026-11-26 | **The cards come before the tickets.** The board gets three cards now: the two guides in Initial Ticket Created and the parked AI guide in Blocked. The user creates an ADO ticket to match each card, and Claude adds the ticket numbers when they come. This replaces D-098's "no card until it is ticketed" for these guides. | User (decision 6) | Adopted |

## 3. Open items

| # | Item | Owner |
|---|---|---|
| 1 | ADO tickets for the three cards | User |
| 2 | Codes in the 100 series, when 460 to 462 are approved (D-102) | Register owner |
| 3 | The points in the discovery map, section 5: the clean-session test and the configuration questions for IT | Claude (test plan), user (IT) |
| 4 | BPO, PG approver and SME for each guide | User |
