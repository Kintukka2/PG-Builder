# D365 F&O: AR Collections Favorites Procedure Guide

> **SME REVIEW DRAFT. Not validated or approved.**
>
> This is a Markdown preview of the Word guide [`TBC-AR Collections Favorites PG v0.2.docx`](TBC-AR%20Collections%20Favorites%20PG%20v0.2.docx). That guide was built from the PG master template in [`/templates`](../../templates/). **The Word file is the editable source.** Make content changes there first, then update this preview.
>
> `[VG-xx]` markers show unconfirmed items. In the Word file, each one is a review comment for the SME. Full details are in the [validation register](../03-validation/PG-AR-Configure-Collections-Favourites-Validation.md). The markers are not part of the guide text.

The fixed template content is not repeated here: cover, Contents, *About this guide* and the *Additional Resources* links. The sections below are the content this guide adds.

**Version history**

| ID | Date | Author/s | BPO | Description of change |
|---|---|---|---|---|
| 0.2 | October 2026 | Daniel Moreira | To be confirmed `[VG-33]` | SME review draft created from the PG master template. Not validated or approved. |

Guide code and final title: `[VG-22]`.

---

## Part 1: What do I need to know? (AR Collections Favorites)

### High-level process

##### Part Description

This guide explains how an AR Collections user adds four D365 pages used in AR Collections work to their Favorites: **All customers**, **Aged balances**, **Customer payment journal** and **Open customer invoices**. Once added, these pages open directly from **Favorites** in the **Navigation Pane** instead of through the module menus. This is a day-one setup task, completed in D365 before routine AR Collections work begins. Switching the legal entity and creating personalized views are outside the scope of this guide.

##### Initiation

- A new AR Collections user is setting up D365 before starting routine AR Collections work. `[VG-30]`

##### Stream

| Stream | Process Area | Key Roles |
|---|---|---|
| Accounts Receivable `[VG-31]` | AR Collections | • Collections Officer |

##### Process

The high-level process is as follows:

| # | Action | Who | When | Where |
|---|---|---|---|---|
| 1 | [Configure AR Collections Favorites](#1-configure-ar-collections-favorites) | Collections Officer | When a new AR Collections user sets up D365 before starting routine AR Collections work | D365 |

### Roles and responsibilities

##### Overview

The Collections Officer completes this task in their own D365 session.

| Tasks / Business Roles | Collections Officer |
|---|---|
| [Configure AR Collections Favorites](#1-configure-ar-collections-favorites) | R |

\*R = Responsible

### Key concepts

##### Overview

Before you start, you need to know the two **Navigation Pane** options used in this guide and the four pages you add to your Favorites.

##### Navigation Pane options used in this guide

| Option | Description |
|---|---|
| **Modules** | Opens the list of D365 modules, such as **Credit and collections** and **Accounts receivable**. Clicking a module opens its module menu. |
| **Favorites** | Lists the pages you have added as favorites. Click a page in the list to open it. |

##### AR Collections pages to add to Favorites

| Page | Description |
|---|---|
| **All customers** | Located in the **Credit and collections** module. Used to open customer accounts and customer master details. |
| **Aged balances** | Located in the **Credit and collections** module. Used to review customer balances by aging period. `[VG-01]` |
| **Customer payment journal** | Located in the **Credit and collections** module. Identified in AR Collections training as a key page for AR Collections users. `[VG-18]` |
| **Open customer invoices** | Located in the **Accounts receivable** module. Used to review open customer invoices. `[VG-19]` |

---

## Part 2: How do I do it? (AR Collections Favorites)

### 1. Configure AR Collections Favorites

##### Description

Use this procedure to add **All customers**, **Aged balances** and **Customer payment journal** from the **Credit and collections** module, and **Open customer invoices** from the **Accounts receivable** module, to your Favorites. You then check that all four pages appear under **Favorites** in the **Navigation Pane**. When complete, you can open each page directly from **Favorites**.

##### Responsibility

- Collections Officer: adds the four AR Collections pages to their own Favorites.

##### Initiation

- A new AR Collections user is setting up D365 before starting routine AR Collections work.

##### Procedure

Complete these steps to add the AR Collections pages to your Favorites:

| Action | Description |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to the **Credit and collections** and **Accounts receivable** modules. `[VG-17]`<br>• The **Navigation Pane** is visible. `[VG-12]`<br>*Responsibility:*<br>• Collections Officer |
| 1. *Check* the **Entity**. `[VG-23, VG-10]` | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Modules**. `[VG-08]` | From the left-hand **Navigation Pane**, click **Modules**. |
| 3. *Click* **Credit and collections**. | From the list of modules, click **Credit and collections**. The **Credit and collections** module menu opens. |
| 4. *Click* the favorite star for **All customers**. `[VG-02, VG-06, VG-07]` | In the **Credit and collections** module menu, find **All customers** and click its favorite star. **All customers** is added to your Favorites. |
| 5. *Click* the favorite star for **Aged balances**. `[VG-01, VG-03]` | In the **Credit and collections** module menu, find **Aged balances** and click its favorite star. **Aged balances** is added to your Favorites. |
| 6. *Click* the favorite star for **Customer payment journal**. `[VG-04]` | In the **Credit and collections** module menu, find **Customer payment journal** and click its favorite star. **Customer payment journal** is added to your Favorites. |
| 7. *Click* **Modules**. | If the list of modules is not displayed, from the left-hand **Navigation Pane**, click **Modules**. |
| 8. *Click* **Accounts receivable**. | From the list of modules, click **Accounts receivable**. The **Accounts receivable** module menu opens. |
| 9. *Click* the favorite star for **Open customer invoices**. `[VG-05]` | In the **Accounts receivable** module menu, find **Open customer invoices** and click its favorite star. **Open customer invoices** is added to your Favorites. |
| 10. *Click* **Favorites**. `[VG-09, VG-28]` | From the left-hand **Navigation Pane**, click **Favorites**. Your favorites list is displayed. |
| 11. *Confirm* the four pages are listed. `[VG-13, VG-16]` | Confirm that **All customers**, **Aged balances**, **Customer payment journal** and **Open customer invoices** appear in your favorites list. If a module or page is not available to you, log a request through the D365 issue form (see **Additional Resources**). |
| 12. *Click* one of the four pages in your favorites list. | The selected page opens. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• **All customers**, **Aged balances**, **Customer payment journal** and **Open customer invoices** appear under **Favorites** in the **Navigation Pane**. `[VG-10, VG-11]`<br>• Each of the four pages opens from **Favorites**. |

---

## Part 3: Reports (AR Collections Favorites)

##### Overview

Reports for this process are pending SME confirmation. `[VG-32]`

---

## Additional Resources

The standard template block, unchanged: User Support (D365 issue form, Atlas D365 User Support Hub) and Self-Service Resources (AVA, Procedure Guides, Atlas Training Hub).
