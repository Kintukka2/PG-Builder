# D365 F&O: AR Collections Statement Distribution Procedure Guide

> **SME REVIEW DRAFT. Not validated or approved.**
>
> This is a Markdown preview of the Word guide [`TBC-AR Collections Statement Distribution PG v0.1.docx`](TBC-AR%20Collections%20Statement%20Distribution%20PG%20v0.1.docx). That guide was built from the PG master template in [`/templates`](../../templates/). **The Word file is the editable source.**
>
> `[VG-xx]` markers show unconfirmed items. In the Word file, each one is a review comment. Full details are in the [validation register](../03-validation/PG-AR-Statement-Distribution-Validation.md). The markers are not part of the guide text.

The fixed template content is not repeated here: cover, Contents, *About this guide* and *Additional Resources*.

**Version history**

| ID | Date | Author/s | BPO | Description of change |
|---|---|---|---|---|
| 0.1 | October 2026 | Daniel Moreira | To be confirmed `[VG-20]` | SME review draft created from the PG master template. Not validated or approved. |

Guide code and final title: `[VG-21]`.

---

## Part 1: What do I need to know? (AR Collections Statement Distribution)

### High-level process

##### Part Description

This guide explains how a Collections Officer generates a customer statement and sends it to the customer through **Print management destination**, then verifies that it was delivered. Previewing a statement without sending it is covered by the AR Collections Statement Preview guide. Excluding customers from statements is outside the scope of this guide.

##### Initiation

- A customer statement must be sent to the customer. `[VG-18]`

##### Stream

| Stream | Process Area | Key Roles |
|---|---|---|
| Accounts Receivable `[VG-19]` | AR Collections | • Collections Officer |

##### Process

| # | Action | Who | When | Where |
|---|---|---|---|---|
| 1 | [Generate and Send a Customer Statement](#1-generate-and-send-a-customer-statement) | Collections Officer | When a customer statement must be sent to the customer | D365 |

### Roles and responsibilities

##### Overview

The Collections Officer sends statements in their own D365 session.

| Tasks / Business Roles | Collections Officer |
|---|---|
| [Generate and Send a Customer Statement](#1-generate-and-send-a-customer-statement) | R |

### Key concepts

##### Overview

Before you start, you need to know how a statement reaches the customer, how delivery is checked, and what to check before you send.

##### Statement distribution

| Term | Description |
|---|---|
| **Print management destination** | The destination that delivers the statement to the customer. When it is selected, generating the statement sends it. `[VG-05, VG-06]` |
| **Delivery message** | The message D365 shows after the statement is generated, which indicates whether it was sent. `[VG-08]` |
| **Collections sent mailbox** | A mailbox where sent statements can be checked when required. `[VG-09]` |

##### Before sending

| Rule | Description |
|---|---|
| **Check the customer can receive a statement** | Before you send, check that the customer is not excluded from statements and is not affected by the known multi-currency limitations. `[VG-12, VG-13]` |
| **Use the approved parameters** | Send statements only with the approved statement parameters. `[VG-17]` |

---

## Part 2: How do I do it? (AR Collections Statement Distribution)

### 1. Generate and Send a Customer Statement

##### Description

Use this topic to send a customer statement and check that it was delivered. You set the statement options, select **Print management destination**, generate the statement and then verify delivery. To review a statement before sending it, use the AR Collections Statement Preview guide.

##### Responsibility

- Collections Officer: sends customer statements and verifies delivery.

##### Initiation

- A customer statement must be sent to the customer.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| [Send the Statement](#11-send-the-statement) | Set the statement options and generate it with Print management destination. Output: the statement is sent. |
| [Verify Statement Delivery](#12-verify-statement-delivery) | Check the delivery message and, where required, the Collections sent mailbox. Output: delivery is confirmed. |

#### 1.1 Send the Statement

##### Procedure

Complete these steps to send the statement:

| Action | Description |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to customer statements.<br>• The customer account number.<br>• The customer can receive a statement (see **Key concepts**).<br>*Responsibility:*<br>• Collections Officer |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Open* the **Statements** page. `[VG-01]` | Open the customer statement page. |
| 3. *Select* the customer. `[VG-02]` | Select the customer account the statement is for. |
| 4. *Select* **Only open**. `[VG-03]` | Include only open transactions. |
| 5. *Include* the company logo. `[VG-04]` | Select the option that includes the company logo. |
| 6. *Select* **Print management destination**. `[VG-05, VG-06]` | Select this option so the statement is delivered to the customer. |
| 7. *Generate* the statement. `[VG-07]` | Generate the statement. D365 sends it to the customer. |
| *STEP COMPLETE* (light blue) | • *The statement has been generated and sent.*<br>• *Continue to [Verify Statement Delivery](#12-verify-statement-delivery)* |

#### 1.2 Verify Statement Delivery

##### Procedure

Complete these steps to verify statement delivery:

| Action | Description |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• The statement has been sent (see [Send the Statement](#11-send-the-statement)).<br>*Responsibility:*<br>• Collections Officer |
| 1. *Check* the delivery message. `[VG-08]` | Read the message D365 shows after the statement is generated, and check that it confirms the statement was sent. |
| 2. *Check* the Collections sent mailbox. `[VG-09]` | Optional. Where required, check that the statement appears in the Collections sent mailbox. Otherwise, go to step 3. |
| 3. *Confirm* the statement was delivered. `[VG-10]` | If the delivery message or mailbox shows that the statement was not sent, follow the failed-delivery process. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• The statement has been sent to the customer and its delivery confirmed. `[VG-11]` |

---

## Part 3: Reports (AR Collections Statement Distribution)

##### Overview

Reports for this process are pending SME confirmation. `[VG-22]`

---

## Additional Resources

The standard template block, unchanged.
