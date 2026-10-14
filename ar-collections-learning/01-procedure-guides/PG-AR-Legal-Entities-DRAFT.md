# D365 F&O: AR Collections Legal Entities Procedure Guide

> **SME REVIEW DRAFT. Not validated or approved.**
>
> This is a Markdown preview of the Word guide [`TBC-AR Collections Legal Entities PG v0.1.docx`](TBC-AR%20Collections%20Legal%20Entities%20PG%20v0.1.docx). That guide was built from the PG master template in [`/templates`](../../templates/). **The Word file is the editable source.**
>
> `[VG-xx]` markers show unconfirmed items. In the Word file, each one is a review comment. Full details are in the [validation register](../03-validation/PG-AR-Legal-Entities-Validation.md). The markers are not part of the guide text.

The fixed template content is not repeated here: cover, Contents, *About this guide* and *Additional Resources*.

**Version history**

| ID | Date | Author/s | BPO | Description of change |
|---|---|---|---|---|
| 0.1 | October 2026 | Daniel Moreira | To be confirmed `[VG-16]` | SME review draft created from the PG master template. Not validated or approved. |

Guide code and final title: `[VG-17]`.

---

## Part 1: What do I need to know? (AR Collections Legal Entities)

### High-level process

##### Part Description

This guide explains how a Collections Officer switches D365 to the legal entity they need, using the legal entity selector or the ledger code in the D365 URL. It also covers confirming that the correct legal entity is active before any processing. Requesting access to a legal entity is outside the scope of this guide.

##### Initiation

- A Collections Officer needs to work in a legal entity other than the one that is active. `[VG-14]`

##### Stream

| Stream | Process Area | Key Roles |
|---|---|---|
| Accounts Receivable `[VG-15]` | AR Collections | • Collections Officer |

##### Process

| # | Action | Who | When | Where |
|---|---|---|---|---|
| 1 | [Switch Legal Entity with the Selector](#1-switch-legal-entity-with-the-selector) | Collections Officer | When work is needed in a different legal entity | D365 |
| 2 | [Switch Legal Entity Using the Ledger Code](#2-switch-legal-entity-using-the-ledger-code) | Collections Officer | When the D365 ledger code of the required legal entity is known | D365 |

### Roles and responsibilities

##### Overview

The Collections Officer switches legal entities in their own D365 session.

| Tasks / Business Roles | Collections Officer |
|---|---|
| [Switch Legal Entity with the Selector](#1-switch-legal-entity-with-the-selector) | R |
| [Switch Legal Entity Using the Ledger Code](#2-switch-legal-entity-using-the-ledger-code) | R |

### Key concepts

##### Overview

Before you start, you need to know what a legal entity is, how legal entities are identified, and the rule for confirming the active legal entity.

##### Legal entities

| Term | Description |
|---|---|
| **Legal entity** | A company set up in D365. The pages you open show data for the active legal entity, so you must work in the legal entity that holds the customer accounts you need. `[VG-22]` |
| **Business name** | The name of the business a legal entity represents. Use the business name to identify the legal entity you need. |
| **Ledger code** | The code D365 uses for a legal entity. D365 ledger codes differ from CargoWise ledger codes. `[VG-08]` |

##### Working in the correct legal entity

| Rule | Description |
|---|---|
| **Work with business names** | Identify legal entities by their business names rather than their ledger codes. `[VG-09]` |
| **Confirm before processing** | Confirm the active legal entity before you perform any transaction. `[VG-10]` |

---

## Part 2: How do I do it? (AR Collections Legal Entities)

### 1. Switch Legal Entity with the Selector

##### Description

Use this procedure to switch to another legal entity with the legal entity selector in the D365 header. You find the legal entity by its business name, select it and confirm that it is active.

##### Responsibility

- Collections Officer: works in the legal entity required for the task.

##### Initiation

- A Collections Officer needs to work in a legal entity other than the one that is active.

##### Procedure

Complete these steps to switch legal entity with the selector:

| Action | Description |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to the required legal entity.<br>• The business name of the required legal entity.<br>*Responsibility:*<br>• Collections Officer |
| 1. *Click* the legal entity selector. `[VG-01]` | In the D365 header (top-right), click the legal entity selector. It shows the active legal entity. |
| 2. *Find* the required legal entity. `[VG-02]` | Find the legal entity by its business name. |
| 3. *Select* the legal entity. `[VG-03]` | Select the legal entity. D365 switches to it. |
| 4. *Confirm* the active legal entity. `[VG-04]` | Check that the selector now shows the required legal entity before you continue. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• D365 is working in the required legal entity. |

### 2. Switch Legal Entity Using the Ledger Code

##### Description

Use this procedure to switch legal entity by changing the ledger code in the D365 URL. You replace the ledger code in the browser address bar and confirm that the required legal entity is active.

##### Responsibility

- Collections Officer: works in the legal entity required for the task.

##### Initiation

- The D365 ledger code of the required legal entity is known, and switching through the URL is appropriate. `[VG-07]`

##### Procedure

Complete these steps to switch legal entity using the ledger code:

| Action | Description |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to the required legal entity.<br>• The D365 ledger code of the required legal entity.<br>*Responsibility:*<br>• Collections Officer |
| 1. *Click* the browser address bar. | Click the address bar to edit the D365 URL. |
| 2. *Find* the ledger code in the URL. `[VG-05]` | Find the part of the URL that holds the ledger code of the active legal entity. |
| 3. *Enter* the required ledger code. `[VG-06]` | Replace the ledger code with the D365 ledger code of the required legal entity. Do not use the CargoWise code. |
| 4. *Press* **Enter**. | Press **Enter** to open D365 in the required legal entity. |
| 5. *Confirm* the active legal entity. | Check that the legal entity selector (top-right) shows the required legal entity before you continue. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• D365 is working in the required legal entity. |

---

## Part 3: Reports (AR Collections Legal Entities)

##### Overview

Reports for this process are pending SME confirmation. `[VG-18]`

---

## Additional Resources

The standard template block, unchanged.
