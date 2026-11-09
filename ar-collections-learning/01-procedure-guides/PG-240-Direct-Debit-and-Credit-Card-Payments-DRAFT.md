# D365 F&O: Direct Debit and Credit Card Payments Procedure Guide

> **WORKING DRAFT. Not validated or approved.**
>
> This is a Markdown preview of the Word guide [`240-Direct Debit and Credit Card Payments PG v0.1.docx`](240-Direct%20Debit%20and%20Credit%20Card%20Payments%20PG%20v0.1.docx). It was assembled from the topic drafts named in its version history, under D-045 and D-046. **The Word file is the editable source.**
>
> Markers such as `[G240-01]` show unconfirmed items. In the Word file, each one is a review comment. Guide-level items and the index of carried items are in the [validation register](../03-validation/240-Direct-Debit-and-Credit-Card-Payments-Validation.md). The markers are not part of the guide text.

The fixed template content is not repeated here: cover, Contents, *About this guide* and *Additional Resources*.

**Version history**

| ID | Date | Author/s | BPO | Description of change |
|---|---|---|---|---|
| 0.1 | November 2026 | Daniel Moreira | To be confirmed `[G240-02]` | Working draft skeleton (ADO 16894), structured as agreed on 9 November. Topics 1 and 2.1 show legacy steps to check against the 11 November recording; other topics are placeholders. Not validated or approved. |

Guide code, title and scope: `[G240-01]`.

---

## Part 1: What do I need to know? (Direct Debit and Credit Card Payments)

### High-level process

##### Part Description

This guide covers customer direct debit and credit card payments in D365: maintaining a customer's payment details, running direct debit collections, approving them, sending them to the bank, and handling failed payments, errors and reversals. Credit card payments follow the direct debit topics. Customer alternate names for payment matching stay in the receiving team's process in 220 Customer Payments.

Topics marked **Being worked on** are placeholders: their steps come from Maria Pabalan's training recording of 11 November, or a later session. Topics 1 and 2.1 show the steps from the legacy guides (230 Collections 2.4 and 220 Customer Payments 5) until the recording confirms them. `[G240-03]`

##### Initiation

- A customer returns a direct debit or credit card form, or their payment details change. `[G240-04]`
- A direct debit run is due: the mid-month batch, or an ad hoc run.
- A direct debit run is ready for approval.
- A direct debit fails, shows an error, or is reversed.

##### Stream

| Stream | Process Area | Key Roles |
|---|---|---|
| Order to Cash (O2C) | Direct Debit and Credit Card Payments | • Collections Officer `[G240-05]`<br>• Receipting Officer (receiving team)<br>• Approvers: Chris Clarke, Arash Najafi |

##### Process

The high-level process is as follows:

| # | Action | Who | When | Where |
|---|---|---|---|---|
| 1 | [Maintain a Customer's Direct Debit Details](#1-maintain-a-customers-direct-debit-details) | Collections Officer | When a customer returns a direct debit form, or their details change | D365 |
| 2 | [Process a Direct Debit Run](#2-process-a-direct-debit-run) | Receipting Officer | Mid-month, and ad hoc when required (regional schedule) | D365 |
| 3 | [Approve a Direct Debit Run](#3-approve-a-direct-debit-run) | Approver (Chris Clarke, Arash Najafi) | When the D365 workflow notification arrives | D365; internal chat |
| 4 | [Handle Direct Debit Exceptions](#4-handle-direct-debit-exceptions) | Collections Officer; Receipting Officer | When a direct debit fails, shows an error, or is reversed | D365; receiving spreadsheets |
| 5 | [Credit Card Payments](#5-credit-card-payments) | Collections Officer; Receipting Officer | When a customer pays by credit card (not live yet) | D365 |

### Roles and responsibilities

##### Overview

The receiving team processes direct debits in D365. Collections Officers talk to customers, collect and confirm their payment details, maintain them in D365 without a separate review, and follow up failed payments. Chris Clarke and Arash Najafi approve each run.

| **Tasks / Business Roles** | Collections Officer | Receipting Officer | Approver |
|---|---|---|---|
| 1 [Maintain a Customer's Direct Debit Details](#1-maintain-a-customers-direct-debit-details) | R |   |   |
| 2 [Process a Direct Debit Run](#2-process-a-direct-debit-run) |   | R |   |
| 2.1 [Run the Mid-Month Direct Debit Batch](#21-run-the-mid-month-direct-debit-batch) |   | R |   |
| 2.2 [Run an Ad Hoc Direct Debit](#22-run-an-ad-hoc-direct-debit) |   | R |   |
| 3 [Approve a Direct Debit Run](#3-approve-a-direct-debit-run) |   |   | R |
| 4 [Handle Direct Debit Exceptions](#4-handle-direct-debit-exceptions) | R | R |   |
| 4.1 [Follow Up a Failed Direct Debit](#41-follow-up-a-failed-direct-debit) | R | R |   |
| 4.2 [Fix Direct Debit Errors](#42-fix-direct-debit-errors) |   | R |   |
| 4.3 [Process a Direct Debit Reversal](#43-process-a-direct-debit-reversal) | TBC | TBC |   |
| 5 [Credit Card Payments](#5-credit-card-payments) | R | R |   |
| 5.1 [Maintain a Customer's Credit Card Details](#51-maintain-a-customers-credit-card-details) | R |   |   |
| 5.2 [Send a Customer a Credit Card Payment Link](#52-send-a-customer-a-credit-card-payment-link) | R |   |   |
| 5.3 [Process an Ad Hoc Credit Card Payment](#53-process-an-ad-hoc-credit-card-payment) | R | R |   |
| 5.4 [Handle Credit Card Exceptions](#54-handle-credit-card-exceptions) | TBC | TBC |   |

\*R = Responsible; TBC = to be confirmed. Approvers: Chris Clarke and Arash Najafi

### Key concepts

##### Overview

Before you start, you need to know where direct debit details are kept, how a run moves from preparation to the bank, and who handles each kind of exception.

##### eBanking details

| Term | Description |
|---|---|
| **Customer eBanking details** | The Treasury Automation Suite record for a customer. It holds the customer's alternate names and, for direct debit and credit card customers, their payment details. |
| **Alternate names** | Names that help Treasury Automation Suite match incoming payments to the customer. The receiving team adds new customers to eBanking and maintains their alternate names (220 Customer Payments). |
| **Bank account and payment specification** | Added by the Collections Officer for each direct debit or credit card customer. They pull the customer into the correct direct debit file. Australian customers need a specific payment specification. |

##### Direct debit runs

| Term | Description |
|---|---|
| **Mid-month batch** | The regular direct debit run. Regional timing is in Maria Pabalan's scheduling file. |
| **Ad hoc run** | A run outside the batch, when required. |
| **Approval** | A D365 workflow emails the approvers a link to review the file or journal. The receiving team also messages them in the internal chat, because workflow emails are easy to miss. |
| **Bank submission** | After approval, the receiving team processes the file to the bank. |

##### Exceptions

| Term | Description |
|---|---|
| **Failed payment** | The receiving team's manual spreadsheets show failed payments and tag the Collections Officer. |
| **Customer-side failure** | Insufficient funds, or the customer declines: the Collections Officer contacts the customer. |
| **System failure** | The receiving team investigates. |
| **Reversal** | Arrives a few days after the original transaction. Being worked on. |
| **Excluding a customer** | Collections Officers use their normal dispute process (credit management exclusion, 230 Collections topic 7.3). |

##### Credit cards

| Term | Description |
|---|---|
| **Status** | Not live yet. The topics are placeholders until the process is confirmed. |
| **Collecting card details** | Today by form, as for direct debit. In D365, a link sent to the customer from their account. |
| **Processing** | The receiving team today. Collections Officers will also process their own ad hoc payments. |

##### Not in this guide

- Customer alternate names and payment matching: 220 Customer Payments.
- Recording a customer payment: 220 Customer Payments.
- Parent accounts paying for child accounts: not a direct debit use case today.

##### Resources

Links to these come with the next version: `[G240-06]`

- Direct debit scheduling file (regional timing).
- The latest direct debit user story in ADO.
- Direct debit training recording, 11 November 2026.

---

## Part 2: How do I do it? (Direct Debit and Credit Card Payments)

### 1. Maintain a Customer's Direct Debit Details

##### Description

Use this topic to set up or update a customer's direct debit details after the customer returns a direct debit form: their payment defaults, eBanking payment specification and bank account. 230 Collections links here from its topic on direct debit and eBanking details.

##### Responsibility

- Collections Officer: collects and confirms the customer's details and maintains them in D365.

##### Initiation

- A customer returns a direct debit form, or their payment details change.

> **Note:** These steps come from legacy 230 Collections 2.4 (v2.1, April 2026) and are checked against the 11 November recording. New customers are added to eBanking by the receiving team. `[G240-07]`

##### Procedure

Complete the steps below to Maintain Customer Direct Debit & eBanking Details:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | **Pre-requisite:**<br>1. *The customer account must exist in D365 F&O, and the approved customer authorisation form with current banking details must be available before creating or updating direct debit and eBanking records.* |
| 2. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 3. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 4. *Navigate* to the **All Customers** page. | From the Navigation pane, select;<br>5. **Accounts receivable >**<br>6. **Customers >**<br>7. **All customers.**<br>The **All customers** page is displayed. |
| 8. *Search* for the **Customer.** | In the **Filter** field, start *typing* the **customer’s** **name** or **account**.<br>If searching by customer name, select **Name** from the dropdown list (alternatively *select* **Account** or **Invoice** **account** as required).<br>The matching customer records are displayed in the list. |
| 9. *Open the* **Customer Record.** | *Click* the **Account** hyperlink for the selected customer to open the record. |
| 10. *Open* the **Payment defaults** FastTab. | *Scroll* to and *expand* the **Payment defaults** FastTab.<br>This section controls how customer payments are processed in D366. |
| 11. *Edit* the **Payment defaults.** | On the Main Toolbar, *click* **Edit** to update the customer payment configuration fields. |
| 12. *Update* **Method of payment** field. | In the **Method of payment** field, *select* the required direct debit payment method from the dropdown list, e.g., DDHDBCAU, DDHSBCUS.<br>The Method of payment determines how customer payments are generated and processed during direct debit payment runs.<br>Important:<br>When Method of payment is selected, D365 may automatically populate the related Payment specification field based on the configured payment setup. |
| 13. *Validate* the **Payment specification** field. | Review the **Payment specification** and confirm that the automatically populated value is correct for the customer direct debit setup e.g., ACH-CCD = DDHSBCUS, DE = DDWBCAU.<br>The Payment specification identified the banking configuration and payment file format used during direct debit processing.<br>If the Payment specification field does not automatically populate, manually select the correct value from the dropdown list. |
| 14. *Save* the **Payment** **default** **changes.** | On the Main toolbar, *click* **Save** to save the update before continuing. |
| 15. *Click* **Modules**. | From the navigation pane, *click* **Modules** to expand the list of available functional areas. |
| 16. *Navigate* to the **Customer eBanking details** page. | From the Navigation pane, select;<br>17. **Treasury Automation Suite** ><br>18. **Common** ><br>19. **Customer eBanking details.**<br>The Customer eBanking details page is used to maintain customer eBanking records by Treasury Automation Suite for payment processing. |
| 20. *Search* for the **Customer** **eBanking** **record**. | Search for the customer using the customer account or customer name. If an existing customer eBanking record is displayed, review and update the existing information as required. |
| 21. *Create* a **New** **eBanking** **record** (If required). | If the customer does not already exist in Customer eBanking details, *click* **+New.** Populate the required fields:<br>Note: The Customer eBanking details record links the customer account to Treasury Automation Suite (TAS) payment processing functionality and is used during automated payment matching, direct debit processing, and customer settlement activities. Alternate customer names may assist TAS in identifying customer payments where the bank transaction narrative differs from the official customer’s name. |
| 22. *Configure* the **eSettlement / Lockbox settings***.* | Scroll to and expand the eSettlement / Lockbox section and complete the following fields:<br>Note: The eSettlement/lockbox settings control how imported customer payments and bank transactions are matched and settled against customer invoices during automated settlement processing. Incorrect settlement configuration may result in unmatched transactions, incorrect invoice allocations, or failed automated settlement processing. |
| 23. *Configure* the **Direct Debit settings**. | Scroll to the Direct Debits section and update the required fields to enable the customer for direct debit processing.<br>Note: The Direct debit settings section controls whether the customer is enabled for automated direct debit processing within TAS. If these settings are not configured correctly, the customer may not be included in direct debit payment proposal processing. |
| 24. *Create* a **Customer bank account.** | On the Main Toolbar, *click* **Customer bank accounts**.<br>The Customer bank accounts page is displayed. |
| 25. *Click* **+New***.* | On the Main Toolbar, *click* **+New** to create a customer bank record.<br>This stores the customer’s banking information used for direct debit processing. |
| 26. *Click* **Edit***.* | On the Main Toolbar, *click* **Edit**. |
| 27. *Enter* the **Customer Bank Account** fields*.* | Scroll to and expand the General section.<br>Complete the required bank account fields;<br>Important:<br>Banking details must match exactly the approved customer authorization form. Incorrect banking information may cause direct debit errors. |
| 28. *Add* **Address information***.* | Scroll to and expand the Address section. On the Address Toolbar, *click* +New. The New address pane will open.<br>Note: A full physical bank address is not required for this process. |
| 29. *Click* **Save***.* | On the Main toolbar, *click* **Save** to save the customer's bank account configuration. |
| 30. *Return* to **Customer eBanking details** screen. | On the Main Toolbar, *click* the **back arrow** to return to the **Customer eBanking details** screen. |
| 31. *Create* a **Payment specifications** record*.* | On the Main toolbar, *click* **Payment specifications** tab to open the Customer eBanking payment spec details. |
| 32. *Click* **+New***.* | On the Main Toolbar, *click* **+New** to create a new payment specification record used for direct debit processing. |
| 33. *Populate* the **Payment specifications** fields*.* | In the Customer eBanking spec details page, complete the following fields: |
| 34. *Save* the **Payment** **specification** **record***.* | On the Main toolbar, *click* Save to finalize the direct debit payment specification setup. |
| 35. *Validate the Direct Debit configuration.* | Review and confirm the following information is correctly configured:<br>36. Method of payment is correct.<br>37. Payment specifications are assigned.<br>38. Customer bank accounts exist.<br>39. The currency is correct. Direct debits are activated.<br>40. The company's bank account is assigned. |
| 41. *OPTIONAL:Update or Remove* **Direct Debit Details**. | If a customer changes payment method or opts out of direct debit processing:<br>42. Update or remove the Method of payment<br>43. Update or remove the Payment specification<br>44. Remove direct debit related banking details where required.<br>45. Update the customer to a new agreed payment arrangement.<br>Examples include:<br>46. Customer changing from Direct Debit to EFT<br>47. Customer moving to Credit Card payments<br>48. Customer temporarily opting out of direct debit processing. |
| *PROCESS COMPLETE* | **Outcomes***:*<br>49. *Customer direct debit and eBanking details are correctly configured in D365 F&O and TAS.*<br>50. *Customer payment methods and banking information are accurately maintained for direct debit processing.*<br>51. *Customer records reflect current payment arrangements and direct debit status.* |

### 2. Process a Direct Debit Run

##### Description

Use this topic to collect direct debit payments from customers: prepare the run in D365, check it, send it for approval and process the approved file to the bank. Runs follow the regional schedule.

##### Responsibility

- Receipting Officer: prepares the run, fixes errors, asks for approval and sends the file to the bank.

##### Initiation

- The mid-month batch is due, or an ad hoc run is required.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| [Run the Mid-Month Direct Debit Batch](#21-run-the-mid-month-direct-debit-batch) | Create the payment proposal and journal, validate, get approval and send the file. |
| [Run an Ad Hoc Direct Debit](#22-run-an-ad-hoc-direct-debit) | Run a direct debit outside the batch. Being worked on. |

#### 2.1 Run the Mid-Month Direct Debit Batch

> **Note:** These steps come from legacy 220 Customer Payments 5 (v2.1) and are checked against the 11 November recording. `[G240-08]`

##### Procedure

Complete these steps to Process Direct Debit Customer Payments:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | **Pre-requisites:**<br>1. *Customers are configured with Direct Debit (DD) Method of payment, and Payment specification.*<br>2. *Open invoices customer invoices exist and fall within the selected payment proposal date range.*<br>3. *The Company bank account for Direct Debit processing is available for selection.* |
| 4. *Check* the **Entity**. | Confirm that you are signed into the correct legal entity. The entity name is shown in the top-right corner of the screen. |
| 5. *Click* **Modules**. | From the left-hand navigation pane, *click* **Modules** to display the full list of available modules in Finance and Operations. |
| 6. *Navigate* to the **Customer Payment Journals** page. | From the Navigation Pane, select:<br>7. **Accounts Receivable** ><br>8. **Payments** ><br>9. **Customer payment journals**.<br>The Customer Payment Journal page is displayed, showing all existing journal in the system. |
| 10. *Create* a new **General** **journal**. | On the Main Toolbar*, click* **+ New** to create a new journal line. A journal batch number is automatically generated. |
| 11. *Enter* **Journal** **Header details**. | Complete the required fields:<br>Note: The journal name controls posting behavior and approval workflow. Always select the journal name that aligns to the transaction type. |
| 12. *Open* the **Journal**. | *Click* the **Journal batch number** to open the journal line page. |
| 13. *Open* the **Payment proposal** page. | On the Main Toolbar, *click* **Payment proposal** > **Create payment proposal.**<br>The Customer payment proposal page is displayed. |
| 14. *Enter* **Proposal** criteria. | Complete the following fields: |
| 15. *Apply* **Filters.** | *Click* the **Filter (funnel icon)** under **Records to include** to display the Customer payment proposal page*.* |
| 16. *Click* **OK.** | *Click* **OK** to return to the Customer payment proposal page. |
| 17. *Generate* **Proposal**. | *Click* **OK.** The system retrieves customer setup for Direct Debit based on selected criteria. Only customers with the configured method of payment will be displayed. |
| 18. *Select* the **Required** **customers**. | Customer payment proposal page will display all the customers that have been setup for Direct Debit processing.<br>Review the proposal list to confirm:<br>19. Method of payment is a DD bank account<br>20. Payment date is correct<br>21. All customers align to the same payment method (one method per run). |
| 22. *Remove* **Unwanted** **customers***.* | If required, highlight any customers that should not be included and click **Remove** to remove them from the proposal. |
| 23. *Select* **Required customers***.* | Select all customers or only the required ones to include in the payment run. |
| 24. *Identify* **Incorrect payment methods**. | *R*eview the **Method of payment** column. If customers display an incorrect method e.g. EFT instead of DD, they must be correct before creating the payments. |
| 25. *Apply* **Multiple changes***.* | If any payment attributes, e.g. Payment date or Method of payments need to be added or updated, *click* to the left of each invoice line to select it, *click* **Multiple change** on the Toolbar.<br>The **Modify changes attributes** panel is displayed. |
| 26. *Update* **Payment attributes***.* | Select the required checkboxes and update the relevant fields e.g. Payment date. |
| 27. *Click* **OK***.* | *Click* **OK** to apply the changes. The system displays a message confirming the payment attributes have been updated and returns to the Customer payments page. |
| 28. *Confirm* the **Updates**. | Review the proposal list to ensure the updates have been applied. |
| 29. *Click* **Create payments.** | *Click* **Create payments**. The system generates the payment journal lines. |
| 30. *Validate* the **Journal** | On the Main Toolbar, *click* **Validate** > **Validate direct debit** to check the journal for errors before posting. |
| 31. *Review* **Exceptions***.* | If there are any Exceptions, *click* **Exception** **list** on the Main Toolbar. Remove or correct invalid lines before submission. |
| 32. *Submit* for **Approval**. | On the Main Toolbar, *click* **Approval** > **Submit** to send the journal for approval.<br>Approval is not immediate and may take time depending on the approver availability. |
| 33. *Monitor* **Approval***.* | To monitor progress, on the Main Toolbar *click* **Workflow** > **History** and review the status e.g. Submitted, In review, Approved. |
| 34. *Navigate* to the **Create and send direct debit** page*.* | Once the journal has been approved, navigate to:<br>35. **Treasury Automation Suite** ><br>36. **Periodic** ><br>37. **Accounts receivable** ><br>38. **Create and send direct debit**.<br>Create and send direct debit page is displayed. |
| 39. *Select* the **Approved journal**. | Select the approved journal. |
| 40. *Click* **Select / View payment**s details. | On the Main Toolbar, click Select / View payments. Review the details to ensure it is correct. |
| 41. *Return* to **Create and send direct debit** screen. | *Click* the **back arrow** to return to the Create and send direct debit screen. |
| 42. *Process* **Payments.** | *Select* the **payment line** to highlight it.<br>On the Main toolbar, *click* **Begin Processing** to generate and send the direct debit file.<br>The system will display a message that the file has been successfully generated and transmitted. |
| *PROCESS COMPLETE* | **Outcomes***:*<br>43. *Direct debit payments payment journal has been created, reviewed and approved.*<br>44. *Payment file has been generated and transmitted successfully to the bank.*<br>45. *Customer payments are scheduled for collection via direct debit on the defined payment date.* |

#### 2.2 Run an Ad Hoc Direct Debit

##### Description

Use this procedure to run a direct debit outside the mid-month batch.

##### Procedure

> **Being worked on.** The steps for an ad hoc run come from the 11 November recording. This topic will be updated; until then, ask the receiving team or Maria Pabalan.

### 3. Approve a Direct Debit Run

##### Description

Use this topic to review and approve a direct debit file or journal. A D365 workflow emails you a link when a run is ready; the receiving team also messages you in the internal chat.

##### Responsibility

- Approver (Chris Clarke, Arash Najafi): reviews and approves each direct debit run.

##### Initiation

- A D365 workflow notification says a direct debit run is ready for approval.

##### Procedure

> **Being worked on.** The approval steps (the workflow link, what to check and the approve control) come from the 11 November recording. This topic will be updated; until then, ask the receiving team or Maria Pabalan.

### 4. Handle Direct Debit Exceptions

##### Description

Use this topic when a direct debit fails, shows an error, or is reversed. Customer-side failures go to the Collections Officer; system issues and errors stay with the receiving team.

##### Responsibility

- Collections Officer: contacts the customer about a customer-side failure.
- Receipting Officer: investigates system failures and fixes errors.

##### Initiation

- A failed payment appears in the receiving spreadsheets, a run shows an error, or a reversal arrives.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| [Follow Up a Failed Direct Debit](#41-follow-up-a-failed-direct-debit) | Contact the customer, or investigate a system failure. |
| [Fix Direct Debit Errors](#42-fix-direct-debit-errors) | Check a run for errors and fix them. Being worked on. |
| [Process a Direct Debit Reversal](#43-process-a-direct-debit-reversal) | Handle a reversal that arrives days later. Being worked on. |

#### 4.1 Follow Up a Failed Direct Debit

##### Description

Use this procedure when the receiving spreadsheet tags you about a failed payment. For insufficient funds, or a customer who declines, the Collections Officer contacts the customer. For a system failure, the receiving team investigates.

##### Procedure

> **Being worked on.** The steps in D365 for a failed payment come from the 11 November recording. This topic will be updated; until then, ask the receiving team or Maria Pabalan.

#### 4.2 Fix Direct Debit Errors

##### Description

Use this procedure when a run shows errors before approval.

##### Procedure

> **Being worked on.** The errors to check for and how to fix them come from the 11 November recording. This topic will be updated; until then, ask the receiving team or Maria Pabalan.

#### 4.3 Process a Direct Debit Reversal

##### Description

Use this procedure when a direct debit is reversed, which happens a few days after the original transaction.

##### Procedure

> **Being worked on.** Reversals are covered in a later session with Maria Pabalan. This topic will be updated; until then, ask the receiving team or Maria Pabalan.

### 5. Credit Card Payments

##### Description

Use this topic for customers who pay by credit card. Credit card payments are not live yet; these topics are placeholders until the process is confirmed. `[G240-09]`

##### Responsibility

- Collections Officer: maintains card details, sends payment links and processes their own ad hoc payments.
- Receipting Officer: processes credit card payments today.

##### Initiation

- A customer chooses to pay by credit card.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| [Maintain a Customer's Credit Card Details](#51-maintain-a-customers-credit-card-details) | Set up or update the customer's card details. Being worked on. |
| [Send a Customer a Credit Card Payment Link](#52-send-a-customer-a-credit-card-payment-link) | Send a payment link from the customer's account. Being worked on. |
| [Process an Ad Hoc Credit Card Payment](#53-process-an-ad-hoc-credit-card-payment) | Take a one-off card payment. Being worked on. |
| [Handle Credit Card Exceptions](#54-handle-credit-card-exceptions) | Failed or disputed card payments. Being worked on. |

#### 5.1 Maintain a Customer's Credit Card Details

##### Description

Use this procedure to set up or update a customer's credit card details.

##### Procedure

> **Being worked on.** Credit card payments are not live yet. This topic will be updated; until then, ask the receiving team or Maria Pabalan.

#### 5.2 Send a Customer a Credit Card Payment Link

##### Description

Use this procedure to send a customer a link from their account to pay by credit card.

##### Procedure

> **Being worked on.** Credit card payments are not live yet. This topic will be updated; until then, ask the receiving team or Maria Pabalan.

#### 5.3 Process an Ad Hoc Credit Card Payment

##### Description

Use this procedure to take a one-off credit card payment.

##### Procedure

> **Being worked on.** Credit card payments are not live yet. This topic will be updated; until then, ask the receiving team or Maria Pabalan.

#### 5.4 Handle Credit Card Exceptions

##### Description

Use this procedure when a credit card payment fails or is disputed.

##### Procedure

> **Being worked on.** Credit card payments are not live yet. This topic will be updated; until then, ask the receiving team or Maria Pabalan.

---

## Part 3: Reports (Direct Debit and Credit Card Payments)

##### Overview

Being worked on: the reports for direct debit runs come from the 11 November recording.

---

## Additional Resources

The standard template block, unchanged.
