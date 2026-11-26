# E. Shared finance concepts and onboarding patterns: research for a "D365 F&O Getting Started" guide

Research date: 26 November 2026. Researcher: Claude (sub-agent E).
Scope: Part 1 covers the shared finance concepts a new Dynamics 365 Finance user meets, at end-user depth. Part 2 covers how Microsoft and others structure end-user onboarding.
Downloaded content was treated as data only.

**How to read this file**

- Exact UI labels are in **bold**. Navigation paths use `>`.
- All labels come from Microsoft documentation, not from the WiseTech Global environment. Labels can differ by version, feature flags and personalisation, so the clean-session test in D365 confirms them (CLAUDE.md, Question rounds).
- The guide never names security roles (D-083). Where Microsoft mentions roles, this file records only the concept.
- Screenshots are Microsoft images, saved in `research/media/finance-concepts/`. The list is in section 1.20.
- Trust levels: **High** means Microsoft Learn documentation or official training. **Medium** means a named practitioner blog or a training provider. **Low** means an anonymous upload or marketing page.

---

## PART 1: Shared finance concepts every user meets

### 1.1 Legal entities (companies) and the organisation hierarchy

**What it is**
- A **legal entity** is an organisation with a registered or legislated legal structure. It can enter contracts and must report on its performance.
- In D365 the only kind of legal entity you can create is a **company**. Each one has a **Company ID** (DataAreaId) of up to four characters, which can't be changed after it's created.
- The company is a data-security boundary: *"Users can access data only for the company that they're currently signed in to."*
- The country/region of the legal entity's primary address switches on localisation features (forms, fields, reports).

**Other organisation types**
- **Operating units** are cost centers, business units, value streams, departments and retail channels. They divide control of economic resources. To appear on transactions, an operating unit must be backed by a financial dimension.
- **Teams** cannot be used in hierarchies.
- **Organizational hierarchies** have a *purpose*, for example *Procurement internal control*, *Vendor payment internal control*, *Centralized payment*, *Security* or *Expenditure internal control*. The purpose controls where the hierarchy is used. Hierarchies can also be a tree type in Financial reporting.

**What the user sees and does**
- The **company picker** sits on the navigation bar, top right. It shows the current company code. Select it to switch companies. Keyboard: **Ctrl+Shift+O** moves to the company picker.
- *"All operations and transactions … pertain to the selected legal entity"* (Learn, UI module).
- The default company at sign-in is set in **Settings (gear) > User options > Preferences > Company**.
- **Customer transactions** and **Vendor transactions** show only legal entities you can access. **Global transactions** (Customer/Vendor tab > Transactions group) shows transactions across legal entities for the same party.
- The **Global general journal** (General ledger > Journal entries > Global general journals) lets a user create journals in any legal entity without switching company. Use **New journal** and pick the legal entity.

**Intercompany (concept)**
- Pairs of legal entities that may transact are set up on the shared **Intercompany accounting** page. Each pair has **Due to** and **Due from** main accounts and a destination journal name.
- When a journal line names another company in the **Company** or **Offset company** column, posting creates the due to/due from entries in both companies automatically.
- The active company is always the *originating* company and must appear on at least one line of the voucher.
- Single-line entries (account and offset on one line) default dimensions correctly. Multi-line intercompany vouchers can't reliably default dimensions on the due to/from lines.
- **View a related intercompany voucher from a journal** is an available task.
- Intercompany sales and purchase orders exist for trading goods between legal entities.

**Gotchas for new users**
- The most common new-user error is working or posting in the wrong company. The company code on the navigation bar is the check. Saved views and defaults can also differ by legal entity.
- Sales tax works only on legal entities, not on financial dimensions that represent entities.
- A party (customer or vendor) has a separate account in each company, but the same party ID links them (see 1.2).

**Sources**
- [Organizations and organizational hierarchies overview](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/organizations-organizational-hierarchies) (High)
- [Learn: Describe organization and legal entities](https://learn.microsoft.com/en-us/training/modules/explore-microsoft-dynamics-365-finance-core-capabilities/3-explore-organization-legal-entities) (High)
- [Intercompany accounting setup](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/intercompany-accounting-setup) (High)
- [Intercompany journal: multi-line vs single line](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/intercompany-journal) (High)
- [General journal processing: Global general journals](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/general-journal-processing) (High)
- [Customer transactions list page](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/customer-transactions-list-page) (High)
- [Keyboard shortcuts](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/shortcut-keys) (High)
- [Rand Group: intercompany common errors](https://www.randgroup.com/insights/microsoft/dynamics-365/finance-operations/intercompany-accounting-in-dynamics-365-finance-setup-steps-common-errors-and-best-practices/) (Medium; advises testing in both entities)

**Screenshots**
- `learn-legal-entities-page.svg`
- `learn-operating-unit-types.svg`
- `learn-organization-hierarchy-view.svg`

### 1.2 Global address book and parties

**What it is**
- The **global address book** is one shared store of every person and organisation the company deals with.
- Each record is a **party** of type *Person* or *Organization*.
- A party can hold several **party roles**: Customer, Prospect, Worker, User, Vendor, Competitor, Applicant and Contact. Roles can sit in several companies. Microsoft's example is one organisation that is a customer and vendor in CEE and a vendor in CEU.
- Addresses and contact information belong to the party and are shared across all its roles. Change an address once and it updates everywhere.
- Legal entities are parties too, and they can't be deleted from the address book.

**What the user sees and does**
- Creating a customer on **All customers**, or a vendor on **All vendors**, automatically creates or links the party. The duplicate check may warn of a party that already exists.
- **Global transactions** relies on the shared party ID.
- Organization administration > Global address book lists all parties.

**Gotchas**
- If you edit a customer's address, you also change that party's address for its vendor role and in other companies.
- Duplicate parties break the cross-company view.

**Sources**
- [Global address book overview](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/organization-administration/overview-global-address-book) (High)
- [Plan for the global address book](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/plan-configuration-global-address-book-additional-address-books) (High)
- Learn module [Describe shared features](https://learn.microsoft.com/en-us/training/modules/describe-shared-features/) (High; lists the global address book as a shared feature)

**Screenshot:** `global-address-book-party-structure-diagram.png`

### 1.3 Chart of accounts and main accounts

**What it is**
- A **chart of accounts** is the structured list of a legal entity's ledger accounts. Several legal entities can share one chart. It's chosen on the **Ledger** page.
- A **main account** is the natural account, for example 110110 Bank Account - USD.
- **Main account types:**
  - Posting accounts: **Profit and loss**, **Revenue** and **Expense**.
  - Transaction accounts: **Balance sheet**, **Asset**, **Liability** and **Equity**.
  - **Total** accounts add intervals.
  - **Reporting** is for Brazil only.
- Main accounts are linked to **main account categories** for the default financial reports.

**Main account settings a user feels in journals**
- **DC/CR requirement** limits an account to debit or credit postings.
- **Default offset account**.
- **Suspended**: blocked for all companies or for one.
- **Do not allow manual entry**: control accounts such as AR/AP can be posted only through their subledger.
- **Default/Validate currency**.
- **Legal entity overrides**: default sales tax, and default dimensions as **Not fixed** or **Fixed value**.
- **Posting validation**: user validation and posting type validation.

**Path:** General ledger > Chart of accounts > Accounts > Main accounts

**Gotchas**
- "Do not allow manual entry" blocks journal lines to control accounts.
- Suspended accounts are rejected on validate or post.
- Don't use the chart-of-accounts delimiter in values (see 1.4).

**Sources**
- [Plan your chart of accounts](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/plan-chart-of-accounts) (High)
- [Main account types](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/main-account-types) (High)
- [General journal processing: Main account](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/general-journal-processing) (High)
- [Create a main account](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/tasks/create-main-account) (High)

### 1.4 Financial dimensions, account structures and the segmented entry control

#### 1.4.1 Financial dimensions

**What it is**
- Financial dimensions categorise transactions. Their values become **segments** of the ledger account and allow reporting by dimension, for example P&L by department or trial balance by cost center.
- There are two kinds:
  - **Custom dimensions**: values maintained by hand on **Financial dimension values**. They are always shared across legal entities. Values can be up to 30 characters.
  - **Entity-backed dimensions**: values come from another record, set in **Use values from**, such as customers, projects or operating units. They can be shared or company-specific.
- An entity-backed value isn't selectable until it has been used in a transaction, posting profile or journal.
- **Legal entity overrides** can suspend a value for a company or set its active dates.
- **Financial tags** are a separate, lighter alternative: up to 20 user-defined tags.

**Path:** General ledger > Chart of accounts > Dimensions > Financial dimensions

#### 1.4.2 Account structures and advanced rules (what the user experiences)

- An **account structure** is a rule set of the main account plus up to 10 dimensions, so 11 segments. It decides which dimensions are offered and required, and which value combinations are valid, for a range of main accounts.
- A ledger has one or more account structures that don't overlap. A typical design has one structure for balance sheet accounts and one for P&L accounts.
- **Advanced rules** add extra segments when criteria are met, for example "if main account is 400000–499999, add Customer". The total is up to 16 segments. Several rules apply in alphabetical order.
- **What the user sees:** the segments offered after the main account change with the account. A balance sheet account may ask for fewer segments than an expense account.
- **Balancing dimension** (optional, on the **Ledger** page): posting automatically creates entries so that each value of that dimension balances. This usually matters where a dimension represents an entity or unit.

#### 1.4.3 Segmented entry control (how to enter Main account + dimensions)

The **Account** and **Offset account** fields on journal lines (and budget, posting definitions and so on) are segmented entry controls. One field holds the whole ledger account, with segments separated by the chart-of-accounts delimiter. Microsoft's screenshot shows `110110-001-024`, which is MainAccount 110110, BusinessUnit 001 and Department 024.

- **Type or pick.** Type the values with the delimiter, or open the lookup.
- **The lookup is a flyout with two panes.** The right pane lists each segment by name (MainAccount, BusinessUnit, Department) with the value and its description. The left grid lists **Value | Description** for the segment that has focus.
- **Searching** matches the start of the value or the description. Typing `180` finds values starting 180; typing `Cash` finds descriptions starting "Cash". Use `*Cash` or `*180` to search "contains".
- **Show all / Show valid** at the bottom of the lookup (**Alt+W**) switches between valid values only and all values.
- **Validation happens when you leave the field** (Tab, click away or take an action), not while you type. If the combination breaks the account structure or derived dimensions, the error appears then.
- **Keyboard with the lookup closed:**
  - **Alt+Down Arrow** opens the lookup. Press it again to move into the segments.
  - **Enter**, **Shift+Enter**, the delimiter key or the **Right/Left arrows** move between segments.
  - **Tab** moves to the next field.
- **Keyboard with the lookup open:**
  - **Esc** closes it.
  - **Up/Down**, **Page Up/Down** and **Home/End** move through the list.
  - **Alt+W** switches Show all / Show valid.
- **Copy/paste.** You can paste a whole combination into one control, or a value into one segment. You can't bulk-paste a column of accounts from Excel across many journal lines. For bulk entry use **Open lines in Excel** (Excel add-in) or the Data management framework.
- The **Account type** field (**Ledger**, **Customer**, **Vendor**, **Bank**, **Fixed assets**, **Project**) decides what the Account field means.
  - For non-ledger types the field holds the customer or vendor ID.
  - Dimensions for those lines are set through **Financial dimensions > Account** or **> Offset account** on the lines Action Pane or toolbar. The screenshot shows a **Financial dimensions** menu above the grid.
- **Ledger account alias:** a shortcut that fills the account and dimensions when you type it and press Tab (General ledger > Chart of accounts > Accounts).
- **Validate data integrity:** right-click a combination and select **Validate data integrity** (General journals > Lines).

#### 1.4.4 Default dimensions and how they flow

Defaults come from several places: master records (customer, vendor, bank, fixed asset, project, item), the **journal name**, the journal or document **header**, and the **main account**, where they can be *Not fixed* or *Fixed value* by legal entity.

The order Microsoft documents for financial journals:

1. **Journal name → journal header.** Header dimensions default from the journal name's **Financial dimensions** FastTab.
2. **Header → line Account.** If a dimension is still blank, it defaults from the customer, vendor, bank, fixed asset, project or ledger record.
   - For a *Ledger* account, a fixed dimension on the main account behaves as a default during entry.
   - For non-ledger account types, a fixed dimension never defaults, because the main account isn't known yet.
3. **Account → Offset account.** The offset account copies the Account line's dimensions first. Only blanks are then filled from the offset's own master record.
   - So a vendor-to-bank line takes the *vendor's* dimensions on the bank side.
   - A value that came from the account is not overridden by the offset main account's default or fixed value.
4. **Posting.**
   - A **Fixed** dimension on each line's main account replaces whatever is on the line.
   - This changes the *accounting entry* (seen in **Voucher**/**Voucher transactions**), not the journal line, which still shows the pre-posting value.
   - No other defaults are applied at posting. Penny-rounding and intercompany due to/from lines take the dimensions of the account or offset account.
   - A fixed *blank* value forces blank, which can cause a posting error if the structure needs a value.
5. **Derived dimensions:** one dimension's value sets others, by default only when the target is blank.

Gotchas:
- The system can't tell "deliberately blank" from "not yet defaulted". To keep a dimension blank you may need to clear it on the offset too, or use a "0"/"Blank" value.
- Fixed dimensions can make an advanced rule fire only at posting. This gives a posting error ("Customer is required") that the user never saw during entry. This is Microsoft's Example 3.

#### 1.4.5 Exact dimension error messages a user will see

From Microsoft's troubleshooting article:

- *The combination wasn't validated beyond the <DimensionName> financial dimension.*
- *You must select a value in the <DimensionName> field in combination with the following dimensions values that are valid.*
- *Blank isn't allowed for <DimensionName> for the combination.*
- *<DimensionName> is not an allowed value in combination with the following dimensions values that are valid.*
- *<DimensionName> is suspended.* / *<DimensionName> isn't active.*
- *<DimensionValue> isn't a valid dimension value in account structure.*
- *The <DimensionName> dimension with value <Value> isn't allowed due to derived dimension rules. The allowed value should be <AllowedValue>.*
- *The value <Value> doesn't exist for <DimensionName>.*

Microsoft's advice for users: check both sides of the journal line, and check defaulted or derived values.

**Sources**
- [Financial dimensions](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/financial-dimensions)
- [Enter account and dimension combinations (segmented entry control)](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/enter-account-dimension-combinations-segmented-entry-control). The URL in the brief, `.../enter-account-dimension-values-segmented-entry-control`, now returns 404.
- [Account structures overview](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/configure-account-structures)
- [Financial dimensions and posting](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/default-dimensions)
- [Default financial dimensions on financial journals](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/dimensions-default-values)
- [Derived dimensions](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/derived-dimensions)
- [Create advanced rules for journals](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/tasks/create-advanced-rules-journals)
- [Fix financial dimension-related errors](https://learn.microsoft.com/en-us/troubleshoot/dynamics-365/finance/general-ledger/common-dimension-related-errors)
- [Create and validate journals: Validate data integrity](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/tasks/create-validate-journals)
- [Learn: Configure and use journals (ledger account alias)](https://learn.microsoft.com/en-us/training/modules/configure-ledgers-journals-dyn365-finance/4-journals)

All High.

**Screenshots**
- `segmented-entry-control-general-journal-account-lookup.png`: the best single image. It shows a Journal voucher with the Account lookup open, segments on the right and Show all.
- `journal-names-financial-dimensions-defaulting.png`
- `general-journals-financial-dimensions-tab.png`
- `journal-voucher-lines-dimension-defaulting.png`
- `main-account-401100-fixed-default-dimension.png`
- `general-journal-header-default-financial-dimension.png`
- `journal-voucher-line-dimension-from-header.png`
- `voucher-transactions-fixed-dimension-applied-on-posting.png`
- `ledger-page-balancing-dimension-department.png`
- `voucher-transactions-balancing-entry.png`
- `ledger-account-lookup-advanced-rule-segment-missing.png`
- `dimension-validation-required-segment-error-message.png`
- `account-structure-allowed-values.png`
- `account-structure-tree-propagation-diagram.png`: setup-level, optional.

### 1.5 Ledger, subledgers, posting profiles: why most users never pick a ledger account

**What it is**
- Each legal entity has exactly one **ledger** (General ledger > Ledger setup > Ledger). It holds:
  - the chart of accounts and account structures
  - the **fiscal calendar**
  - the **accounting currency**, an optional **reporting currency**, and their exchange rate types
  - an optional balancing dimension
- **Subledgers** (modules) include Accounts receivable, Accounts payable, Bank, Fixed assets, Tax and Inventory. Posting a document such as a customer invoice records detail in each subledger.
- **Posting profiles** (for example Accounts receivable > Setup > Customer posting profile) supply the main accounts. The document supplies the dimensions.
- The subledger entry is balanced and transferred to the GL, in detail or summary, **asynchronously or by scheduled batch**.
- *"The voucher is used as the shared reference between the subledger document and the accounting entries in the ledger."*

**Why it matters to end users**
- AR and AP users rarely type a ledger account. Their account type is Customer or Vendor, and the posting profile decides the control account.
- A short delay between posting and the GL is possible when transfer runs asynchronously or in batch.
- **Documents pending accounting** and the **View subledger journal** tab on Voucher transactions show the subledger detail.

**Sources**
- [Ledger and subledger accounting overview](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/ledger-subledger)
- [Configure ledgers](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/configure-ledger)
- [Subledger transfer to the general ledger](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/subledger-transfer)
- [Posting profiles overview](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/pstg-prfles-ovrvw)
- [Accounting distributions](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/accounting-distributions)

All High.

### 1.6 Fiscal and ledger calendars, periods, period status, and why posting fails

**What it is**
- A **fiscal calendar** holds fiscal years. Each year holds periods: Opening, Operating periods 1–12, and Closing periods, often a 13th "Close" period with the same dates as period 12.
- One fiscal calendar can serve many legal entities. Selecting it on the **Ledger** page creates that entity's **ledger calendar**, where period statuses and module access are kept.
- If no calendar is selected, posting fails.

**Period status** (General ledger > Period close > Ledger calendars, and per ledger from **Ledger > Ledger calendar**):
- **Open**: can be posted to, provided the user has access.
- **On hold**: can't be posted to, but can be reopened. This is the recommended status at period end.
- **Permanently closed**: can never be reopened, and no adjustments can be posted. Microsoft warns: *"Don't set a period to Permanently closed until all adjustments and audits are complete."*

**Module access**
- Each period also has access per application module (General ledger, Accounts receivable, Accounts payable and so on).
- The access level is **All**, **None** or a specific **user group**, through **Update module access**.
- So a period can be open for GL but closed for AP, or open only to the close team.

**Why posting fails (date and period)**
- The posting date is in a period that is On hold or Permanently closed for that module, or the user isn't in the allowed user group.
- The date falls outside any defined fiscal year or period.
- Reversals into a closed period need a new date: the **Reverse** dialog asks *use existing transaction dates? Yes/No*.
- AP has a parameter, **Adjust invoice posting date automatically**, that can move pending vendor invoices to the system date when their period is closed or On hold.

**Sources**
- [Fiscal calendars, fiscal years, and periods](https://learn.microsoft.com/en-us/dynamics365/finance/budgeting/fiscal-calendars-fiscal-years-periods)
- [Mass financial period close](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/tasks/mass-financial-period-close)
- [Close the general ledger at period end](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/close-general-ledger-at-period-end)
- [Configure ledgers: calendars](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/configure-ledger)
- [Vendor invoice dates](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/vendor-invoice-dates)
- [Year-end close](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/year-end-close)

All High.

### 1.7 Journals: header and lines, journal names, validate, post, Post and transfer

**What it is**
- A journal is a batch of unposted entries with a **header** and **lines**.
- The header holds the **journal batch number** (from a number sequence), the **Name** (journal name), **Description**, and default fields on its tabs (currency, offset account, financial dimensions and so on).
- The lines hold:
  - **Date**: the posting date. It defaults from the session date.
  - **Voucher**.
  - **Company**.
  - **Account type** and **Account**.
  - **Description**.
  - **Debit** and **Credit**.
  - **Offset company**, **Offset account type** and **Offset account**.
  - **Currency** and exchange rate.
  - Sales tax groups.

**Journal names** (General ledger > Journal setup > Journal names) are templates:
- **Journal type**: for example *Daily* for the general journal, *Vendor disbursement* for AP payments, *Customer payment* for AR payments, *Approval*, *Invoice register*, *Vendor invoice recording*, *Periodic*, *Allocation*.
- The voucher number sequence.
- Default dimensions and currency.
- **Workflow approval**.
- **Journal control**, which restricts account types, companies or segment values.
- **Lines limit** and posting layer.

Microsoft recommends a separate journal name for each purpose (intercompany, accrual, error correction). Once the header is committed, the name can't be changed.

**Standard flow** (General ledger > Journal entries > General journals):
1. Select **New**.
2. Pick the **Name**.
3. Select **Lines**.
4. Enter the lines.
5. Select **Validate**.
6. Select **Post**.
7. Check the posted vouchers through **Voucher**.

**Validate options**
- **Validate** checks for errors.
- **Simulate posting** (on the Validate menu) runs the whole posting logic without posting. It can't run in batch.

**Post options**
- **Post**.
- **Post in batch** (visible in the Microsoft screenshot).
- **Post and transfer** posts the vouchers that pass and moves the vouchers with errors to a new journal to fix later. It was described in AX 2012 as a separate command. The Learn module says: *"If a journal has vouchers with errors, you still can post the journals for those vouchers, which are validated before they are transferred with errors."* Its current menu location still needs to be confirmed in the clean-session test.
- **Post journals** (multiple journals, batch) is available in GL, AR, AP and Project.

**Workflow**
- Where a journal name has approval workflow, **Post** is replaced by workflow actions: submit, approve, then post.
- **Locked by system** and **Journal unlock** apply when a batch job holds the journal.

**Other journal functions**
- **Functions > Save voucher template** stores a posted voucher as a template, either *Percent* or *Amount*.
- **Functions > Select voucher template** applies a template to a new journal.
- **Periodic journals** (recurring) are kept under General ledger > Periodic tasks > Periodic journals, and pulled in with **Period journal > Retrieve journal**.
- **Reversing entry** with a **Reversing date** creates an automatic reversal, used for accruals.
- **Open lines in Excel** opens the lines in the Excel add-in.
- **Functions > Load ledger transactions** brings in posted ledger transactions.
- **Functions > Delete journal lines** deletes all lines.
- Posted transactions can't be deleted, only reversed.

**Other journal entry points users meet:** payment journals (AR/AP), invoice journals, invoice register and approval journals, fixed asset journals, and the **Journal voucher** page (lines).

**Gotchas**
- Choosing the wrong journal name bypasses controls and approvals, and the name can't be changed afterwards.
- A journal that is "Locked by system" is being posted by a batch job, so don't force it.
- Large journals over 1,000 lines are split automatically when that feature is on.

**Sources**
- [General journal processing](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/general-journal-processing)
- [Ledger journal types](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/ledger-journal-types)
- [Create and validate journals](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/tasks/create-validate-journals)
- [Create a journal entry using a template](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/tasks/create-journal-entry-template)
- [Post periodic journals](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/tasks/post-periodic-journals)
- [Financial journal posting performance](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/posting-performance)
- [Learn: Work with general ledger processes (Post and transfer, Post journals, Line limits)](https://learn.microsoft.com/en-us/training/modules/general-ledger-daily-procedures-dyn365-finance/4-gl-processes)
- [Learn: Configure and use journals](https://learn.microsoft.com/en-us/training/modules/configure-ledgers-journals-dyn365-finance/4-journals)

All High.
- [Solving Dynamics 365: General journal entry workflow](https://solvingdynamics365.com/guides/general-journal-entry-workflow-in-f-and-o/) (Medium; useful pitfall list, but some claims are unverified, such as auto-routing to the next open period)

**Screenshots**
- `journal-names-journal-control-account-types.png`
- `journal-names-journal-control-segment.png`
- `general-journal-reversing-entry-accrual.png`
- `learn-general-ledger-parameters-voucher-check.svg`

### 1.8 Vouchers, balancing, and why posting fails (balance and currency)

**What it is**
- A **voucher** is the unique number that groups the lines of one accounting entry. It comes from the journal name's voucher number sequence.
- Every voucher must balance: debits equal credits.
  - It must balance in the **transaction currency** when all lines share one currency.
  - It must balance in the **accounting currency** and **reporting currency**.
- Small rounding differences within **Maximum penny difference** go automatically to the penny difference account.

**What the user sees**
- Totals at the bottom of the journal lines are in accounting and reporting currency, not transaction currency.
- The imbalance error reads: *"The transactions on a specific voucher don't balance as of a certain date (accounting currency: 0.01 - reporting currency: 0.06)."*
- Lines that share a voucher number must also share a date.
- **Check for voucher used** in GL parameters (Reject duplicate / Reject duplicates within fiscal year / Accept duplicates / Warn in case of duplicates) controls reuse of voucher numbers across dates.

**One voucher**
- One voucher with several customers, vendors or assets is allowed but discouraged.
- It causes problems with settlement, tax, reversal and reports. Reports show only the first account.
- Teach "one voucher per business transaction".

**Sources**
- [Journal posting failure due to imbalance](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/posting-fail-imbalance)
- [One voucher](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/one-voucher)
- [Learn: Configure and use journals](https://learn.microsoft.com/en-us/training/modules/configure-ledgers-journals-dyn365-finance/4-journals)

All High.

### 1.9 Number sequences (user view)

**What it is**
- Number sequences generate readable, unique IDs for master records and transactions: customer accounts, invoices, journal batch numbers and vouchers.
- Each sequence has a **scope**: Shared, Company, Legal entity, Operating unit, and optionally Fiscal calendar period.
- The format is built from segments: Constant, Alphanumeric (`#` for digits, `&` for letters), and scope segments.
- Microsoft's example: `CS-EXPENSE-0039`.
- A **continuous** sequence never skips numbers but is slower. A **non-continuous** one may skip numbers.

**What the user sees**
- IDs fill in automatically when a record is created. A greyed-out ID field means the sequence controls it.
- A **Company** scope means the same number (for example SO-0029) can exist in each company, so always read numbers together with the company.
- Gaps in voucher or journal numbers are normal for non-continuous sequences and are not a fault.

**Sources:** [Number sequences overview](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/number-sequence-overview) (High)

### 1.10 Dates: posting date, document date, session date, fiscal year

**Posting (accounting) date**
- The journal line **Date** and the document **Posting date** decide the period and the exchange rate.
- The default is the **session date**.

**Document / invoice date**
- On a vendor invoice, the header shows four dates:
  - **Invoice received date**: defaults to today.
  - **Invoice date**: blank by default. It's the vendor's document date.
  - **Posting date**: defaults to today.
  - **Due date**: calculated from the invoice date if entered, otherwise from the posting date, plus the payment terms.
- Parameters control whether the exchange rate uses the posting date or the document date (**Default exchange rate date**), whether the invoice date is required, and whether duplicate checks are per fiscal year.
- On journals, a **Document date** field (and **Document** number) records the source document. Microsoft has no single definitional article for it. A community KA reports that when all lines share one voucher, settlement shows the first line's document date.

**Session date**
- Navigation pane > Modules > Common > Common > **Session date and time**, or the calendar on the dashboard.
- It changes the default date for the session, so it can be used to back-date entries.
- A new user who changes it and forgets will misdate everything until sign-out. This is a classic mistake.

**Fiscal year**
- The fiscal year is defined by the fiscal calendar, which may not be a calendar year.
- Year-end close (General ledger > Period close > Year-end close) transfers P&L to retained earnings and creates opening balances.

**Time zone** comes from User options > Preferences and affects batch scheduling.

**Sources**
- [Vendor invoice dates](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/vendor-invoice-dates) (High)
- [Change the date for a session](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/tasks/change-date-session) (High)
- [Set a user's preferred time zone](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/tasks/set-users-preferred-time-zone) (High)
- [Year-end close](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/year-end-close) (High)
- [Community KA-26203](https://community.dynamics.com/article/KA-26203) (Medium)

### 1.11 Currencies and exchange rates

**What it is**
- Each legal entity has an **accounting currency**, set on the Ledger page. An optional **reporting currency** acts as a full second accounting currency (dual currency).
- Transactions can be in any **transaction currency**. Amounts are converted to the accounting and reporting currencies by **exchange rate type**, for example Default, Buy, Sell, Spot or Budget.
- Rates are **shared across all legal entities**.
- The system uses the latest rate on or before the posting date.
- Only one direction of each currency pair is stored, and the reciprocal is calculated.
- If no rate exists for a pair, the transaction can't be processed.

**Paths**
- General ledger > Currencies > **Currencies**
- General ledger > Currencies > **Currency exchange rates**
- General ledger > Currencies > **Exchange rate types**
- General ledger > Currencies > **Import currency exchange rates**
- General ledger > Currencies > **Configure exchange rate providers**

**What the user sees**
- The **Currency** and **Exchange rate** columns on journal lines.
- Transaction, accounting and reporting currency columns in **Voucher transactions**.
- **Foreign currency revaluation** at period end, which creates unrealised gains and losses.
- **Hide currency revaluations** on customer and vendor transaction lists.

**Gotchas**
- The posting date drives the rate, so changing the date changes the amounts.
- A voucher can balance in transaction currency and still fail in accounting currency (see 1.8).

**Sources**
- [Configure ledgers: currencies](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/configure-ledger)
- [Learn: Configure and import currency exchange rates](https://learn.microsoft.com/en-us/training/modules/configure-currencies-dyn365-finance/3-currency-exchange-rate)
- [Learn: Describe reporting currency and accounting currency](https://learn.microsoft.com/en-us/training/modules/explore-microsoft-dynamics-365-finance-core-capabilities/4-reporting-currency-accounting-currency)
- [Import currency exchange rates](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/import-currency-exchange-rates)
- [Dual currency](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/dual-currency)

All High.

**Screenshots**
- `learn-currency-exchange-rates-page.png`
- `learn-manual-exchange-rates-entry.svg`
- `learn-exchange-rate-types-page.svg`
- `learn-ledger-page-accounting-currency-exchange-rate-type.svg`

### 1.12 Sales tax / GST (concept level)

**What it is**
- The same framework handles sales tax, VAT, GST, withholding and fees.
- Setup chain: **Sales tax codes** (rates and rules) → **Sales tax settlement period** → **Sales tax authority**. Each code also has a **ledger posting group**, which holds the main accounts.
- On every taxable line, the system intersects two groups:
  - **Sales tax group**, which comes from the party (customer, vendor, or a ledger account).
  - **Item sales tax group**, which comes from the item, procurement category or ledger line.
- The tax codes present in **both** groups apply. No overlap means no tax.
- Defaults come from master data. They can be changed on the transaction, and on some documents the calculated tax can be adjusted.

**What the user sees**
- **Sales tax group** and **Item sales tax group** fields on journal and document lines.
- The **Sales tax** button opens **Sales tax transactions**. Some documents allow tax adjustments.
- Settlement uses **Settle and post sales tax** (Tax > Declarations). It's done by the tax team, not covered in a getting-started guide.

**Path:** Tax > Indirect taxes > Sales tax > Sales tax groups / Item sales tax groups / Sales tax codes

**Gotchas**
- A blank or wrong group means no tax or the wrong tax.
- Conditional sales tax (cash basis), where used, is reported on payment.
- Tax works per legal entity only.

**Sources**
- [Sales tax overview](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/indirect-taxes-overview) (High)
- [Set up sales tax groups and item sales tax groups](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/tasks/set-up-sales-tax-groups-item-sales-tax-groups) (High)
- [Learn: Explore tax capabilities](https://learn.microsoft.com/en-us/training/modules/explore-microsoft-dynamics-365-finance-core-capabilities/5-explore-tax-capabilities) (High)

**Screenshot:** `sales-tax-setup-entities-overview-diagram.jpg`

### 1.13 Inquiry pages: Trial balance, Voucher transactions, Transaction origin, Customer/Vendor transactions

**Trial balance** (General ledger > Inquiries and reports > **Trial balance**)
- A list page of balances by account and/or dimensions for a date range.
- **Parameters** set the dates, posting layer, opening balance display and closing types.
- **Financial dimension set** chooses which dimensions show, optionally in separate columns.
- You can drill down to transactions.
- Newer versions add **Trial balance snapshots**, for export.

**Voucher transactions** (General ledger > Inquiries and reports > **Voucher transactions**)
- A query-based inquiry. It opens with a query dialog with **Range**, **Joins** and **Sorting** tabs. Default fields are journal number, voucher, date and main account.
- Ranges use `..`, for example `01/07/2026..31/07/2026`.
- From a result, the Action Pane offers:
  - **Transaction origin**: all lines of the voucher across the modules it touched.
  - **Original document**.
  - **View subledger journal** (tab).
  - **Reverse** (where the feature is on).
- The same Voucher transactions view also opens through the **Voucher** button on posted journals, invoices, customer and vendor transactions and so on. This "Voucher" drill-back is the most useful audit habit to teach.

**Transaction origin**
- Shown both as a button on Voucher transactions and as a ledger report.
- It shows the account by journal and by transaction, accounting and reporting currency, plus each offset line.

**Audit trail** (General ledger > Inquiries and reports > Audit trail) shows who created which posting and when.

**Accounting source explorer** traces GL balances back to source documents and dimensions. It needs filters first and opens blank.

**Ledger reports**
- **Dimension statement**
- **Ledger transaction list**
- **Print journal**
- **Posted transactions by journal**
- **Transaction list by date**
- **Transaction origin**

Also **Financial reports** (General ledger > Inquiries and reports > Financial reports), the Financial reporting add-in with drill-down.

**Customer transactions / Vendor transactions**
- Open from All customers > Customer tab > **Transactions** (or All vendors > Vendor tab > **Transactions**).
- **Show** filter: **All**, **Closed**, **Open**, **Open including closed on or after date**.
- **Hide currency revaluations**.
- **View settlements**, with **View related** inside it.
- **Global transactions** shows all companies for the same party.
- **Voucher** and **Transaction origin** are available here too.
- Due dates can be editable, controlled by a parameter.

**"Related information"**
- In the current UI, the **Related information** button on a page's Action Pane or toolbar opens the **FactBox pane**: summary panes about the selected record, such as customer balance or related invoices (AX7.uk, Part 3).
- Workspaces also have a **Related information** links section, for example the Vendor payments workspace links to the **Vendor aging report** and **Payment summary by date**.
- Microsoft's UI glossary calls these elements **FactBox** and **FactBox pane**.

**Sources**
- [View journal entries and transactions](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/view-journal-entries-transactions)
- [View journal entries or transactions (task)](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/tasks/view-journal-entries-or-transactions)
- [General ledger account balances](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/general-ledger-account-balances)
- [Accounting source explorer](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/accounting-source-explorer)
- [Customer transactions list page](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/customer-transactions-list-page)
- [Vendor transactions list page](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/vendor-transaction-list-page)
- [Trial balance financial reports](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/trial-balance-financial-reports)
- [Learn: Configure and use journals (Voucher transactions, Audit trail)](https://learn.microsoft.com/en-us/training/modules/configure-ledgers-journals-dyn365-finance/4-journals)

All High.
- [AX7.uk: Navigating the D365 F&O interface Part 3](https://ax7.uk/2024/02/06/navigating-the-d365-fo-interface-part-3/) (Medium; Related information button)

**Screenshots**
- `learn-voucher-transactions-page.svg`
- `learn-audit-trail-page.svg`
- `voucher-transactions-original-journal-vouchers.png`

### 1.14 Reversals and corrections

- Posted transactions are never edited or deleted. They are reversed and re-entered.
- **Reverse entire journal** works on a posted journal's lines. Voucher transactions offers reverse for selected vouchers through the **Mass reversals for multiple documents** feature.
- The reversal dialog has three parts:
  - A **Yes/No** choice to keep the original dates. Choose No if the original period is closed.
  - A new date.
  - A comment.
- Over 100 lines runs in batch.
- Vendor payments are reversed differently (Reverse a vendor payment).
- Some transactions can't be reversed. See *Why can't I reverse this transaction?*

**Sources**
- [Reverse journal posting](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/reverse-journal-posting) (High)
- [Why can't I reverse this transaction?](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/cant-reverse-transctns) (High)

### 1.15 Workspaces in finance

**What it is**
- Workspaces are activity-oriented pages with three areas:
  - Summary **tiles**: counts, KPIs, new-task buttons.
  - Tabbed **lists**.
  - **Links**: pages and reports.
- Optional charts and a Power BI **Analytics** tab appear in some.
- Most have a workspace-wide filter, for example company or pool. Some are configurable.
- *"Access to the various workspaces depends on the roles that users have in the organization."* Do not name the roles (D-083).

**Finance workspaces found in Microsoft docs**
- **Customer payments** (Accounts receivable > Workspaces). Learn uses it as its example workspace.
- **Customer invoicing**.
- **Collections coordinator**: newer, enabled through Feature management.
- Credit and collections.
- **Vendor payments**: My work and Analytics; Summary tiles for unposted payment journals, invoices past due and vendors on hold; **Related information** links.
- **Vendor invoice entry**.
- Invoice capture.
- **Bank management**.
- **Financial period close**: closing schedules, tasks by company, area and person; past-due (!) and blocked (padlock) indicators; **Task complete**.
- **Fixed asset management**.
- **Account reconciliation**.
- Cost control / Cost administration.
- **Ledger budgets and forecasts** and **General journal processing** are named in the brief, but I found no Microsoft article for them. Confirm both in the clean-session test.

**What the user does**
- Open a workspace from a dashboard tile, from **Workspaces** in the navigation pane, or through search.
- Set the filter, for example the company, then work from the tiles.
- A tile is counted for the signed-in company only, unless the workspace filter says otherwise.

**Sources**
- [Learn: Navigation elements](https://learn.microsoft.com/en-us/training/modules/navigate-finance-operations/2-navigation-elements)
- [Learn: Workspaces driving productivity](https://learn.microsoft.com/en-us/training/modules/navigate-finance-operations/3-workspaces-driving-productivity)
- [Configure and filter workspaces](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/configure-filter-workspaces)
- [Vendor payments workspace](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/vendor-payments-workspace)
- [Collections coordinator workspace](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/collectionsworkspace)
- [Financial period close workspace](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/financial-period-close-workspace)

All High.

**Screenshots**
- `learn-customer-payments-workspace.svg`
- `learn-customer-invoicing-workspace-key-areas.svg`
- `workspace-filter-expanded.png`
- `workspace-section-filters.png`
- `default-dashboard.png`
- `learn-dashboard-main.svg`

### 1.16 Security roles (concept only; the guide never names them, D-083)

- Access is role-based. Permissions make up privileges, privileges make up duties, and duties make up roles.
- A user with no role has no access. Roles decide which workspaces, pages and actions a user sees. Navigation search shows only pages the user can access.
- Data security can limit a role to some organisations.
- Segregation of duties is built in, for example the person who enters a journal is not the person who approves it.
- **For the guide:** say the user's manager requests their D365 profile, which gives them the access they need. Tell users to contact the **BAU Support team** if a page, module or button is missing. Never list or ask about roles.

**Sources:** [Role-based security](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/role-based-security) (High)

### 1.17 Workflow and approvals (concept)

- Journals (by journal name), vendor invoices, and customer and vendor master changes can go through approval workflow.
- Users see:
  - **Workflow** buttons: Submit, Approve, Reject, Recall, View history.
  - **Work items assigned to me** on the dashboard.
  - Notifications in the **Action center**.
- Delegation is set in **User options > Workflow**.

**Sources**
- [General journal processing: workflow](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/general-journal-processing) (High)
- [Dynamics Tips: Introduction basics and navigation](https://sites.google.com/view/dynamicstips/common/introduction-basics-and-navigation) (Medium)

### 1.18 Navigation basics that every concept above depends on (overlaps with other agents)

**Navigation bar**
- Dynamics 365 portal, **Search** (Alt+G or Ctrl+/), the **company picker**, **Action center**, **Settings**, **Help & Support** and the user profile.

**Navigation pane** (Alt+F1)
- **Favorites**, **Recent**, **Workspaces** and **Modules**.
- Under 260, Favorites is taught in 260 O2C Getting Started (D-084).

**Page elements**
- **Action Pane** with tabs, and **Action search** (Ctrl+' or Alt+Q).
- **FastTabs**, **FactBox pane** (Related information), **Filter pane** (Alt+M, F or Ctrl+F3), **QuickFilter**, grid column filters, **Advanced filter/sort** (Ctrl+Shift+F3).
- Views: **Grid**, **Details**, **Header** and **Lines**.
- **Saved views**.
- **Open in Microsoft Office / Export to Excel** (Ctrl+Shift+E).
- **Attachments** (Ctrl+Shift+A).
- **Refresh** and **Open in new window**.
- The back arrow. Don't use the browser's back button.
- Edit/view mode, set in User options > Preferences > **Default view/edit mode**.
- Lookups: type an ID *or a name*. Alt+Down opens the lookup, then Ctrl+G filters inside it.

**Help**
- In-product Help with Microsoft Learn articles and **task guides** (Task recorder).

**Sources**
- [User interface elements](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/user-interface-elements)
- [Keyboard shortcuts](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/shortcut-keys)
- [Find information by using lookups](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/use-lookups-to-find-information)
- [Saved views](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/saved-views)
- [Help system](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/help-overview)
- [Learn: Search, filtering, views modules](https://learn.microsoft.com/en-us/training/modules/navigate-finance-operations/)

All High.

**Screenshots**
- `learn-filter-pane.svg`
- `learn-navigation-search-results.png`

### 1.19 Consolidated "why won't it post?" checklist (from the sources above)

| Symptom / message | Usual cause | Where the user looks |
|---|---|---|
| Voucher doesn't balance (accounting/reporting currency …) | A missing offset line, one-sided amounts, mixed dates on one voucher, or rounding | Journal totals; Voucher column; Simulate posting |
| Period not open / closed / on hold | Posting date in a period that is On hold or Permanently closed for that module, or the user isn't in the allowed user group | Line **Date**; session date; ask the close team |
| Dimension combination errors (1.4.5) | Account structure or advanced rule needs a segment; a suspended or inactive value; a default or derived value | Segmented entry lookup (Show valid); both sides of the line |
| Account doesn't allow manual entry / is suspended | Control account, or a main account suspended for this company | Use the right account type (Customer/Vendor) |
| Exchange rate not found | No rate for the pair and type on or before the date | Currency exchange rates (ask the owner) |
| Journal locked by system | Batch posting in progress | Wait; BAU Support |
| Button or page missing | Access | BAU Support team (D-083) |
| Wrong company | Company picker | Navigation bar |

### 1.20 Screenshots downloaded (all Microsoft, `research/media/finance-concepts/`)

| File | Shows | Source page |
|---|---|---|
| segmented-entry-control-general-journal-account-lookup.png | Journal voucher; Account lookup with segments (MainAccount/BusinessUnit/Department), Value/Description, Show all | Segmented entry control |
| journal-names-journal-control-account-types.png | Journal control: allowed account types | General journal processing |
| journal-names-journal-control-segment.png | Journal control: segment restriction | General journal processing |
| general-journal-reversing-entry-accrual.png | Reversing entry/date on a journal line | General journal processing |
| voucher-transactions-original-journal-vouchers.png | Voucher transactions grid | General journal processing |
| main-account-401100-fixed-default-dimension.png | Main account legal entity override, Fixed dimension | Financial dimensions and posting |
| general-journal-header-default-financial-dimension.png | Journal header Financial dimensions | same |
| journal-voucher-line-dimension-from-header.png | Line with defaulted dimension | same |
| voucher-transactions-fixed-dimension-applied-on-posting.png | Posted voucher showing fixed dimension applied | same |
| ledger-page-balancing-dimension-department.png | Ledger page balancing dimension | same |
| voucher-transactions-balancing-entry.png | Balancing entries in voucher | same |
| ledger-account-lookup-advanced-rule-segment-missing.png | Lookup without advanced-rule segment | same |
| dimension-validation-required-segment-error-message.png | Posting error: required segment | same |
| account-structure-allowed-values.png | Account structure allowed values | Account structures overview |
| account-structure-tree-propagation-diagram.png | Tree diagram (setup level) | same |
| journal-names-financial-dimensions-defaulting.png | Journal names: default dimensions | Default dimensions on financial journals |
| general-journals-financial-dimensions-tab.png | General journals header Financial dimensions tab | same |
| journal-voucher-lines-dimension-defaulting.png | Journal voucher lines with defaulted accounts | same |
| global-address-book-party-structure-diagram.png | Party / role / location diagram | Global address book overview |
| sales-tax-setup-entities-overview-diagram.jpg | Tax setup entity diagram | Sales tax overview |
| default-dashboard.png | Default dashboard | Default dashboard |
| workspace-filter-expanded.png / workspace-section-filters.png | Workspace filters | Configure and filter workspaces |
| learn-dashboard-main.svg | Dashboard (Learn) | Learn: Navigation elements |
| learn-customer-payments-workspace.svg | Customer payments workspace | same |
| learn-customer-invoicing-workspace-key-areas.svg | Workspace key areas | Learn: Workspaces |
| learn-filter-pane.svg | Filter pane | Learn: Filtering |
| learn-navigation-search-results.png | Navigation search results | Learn: Searching |
| learn-currency-exchange-rates-page.png / learn-manual-exchange-rates-entry.svg / learn-exchange-rate-types-page.svg / learn-ledger-page-accounting-currency-exchange-rate-type.svg | Currency pages | Learn currency units |
| learn-legal-entities-page.svg / learn-operating-unit-types.svg / learn-organization-hierarchy-view.svg | Organisation pages | Learn: organization and legal entities |
| learn-voucher-transactions-page.svg / learn-audit-trail-page.svg / learn-general-ledger-parameters-voucher-check.svg | Inquiries and GL parameters | Learn: Configure and use journals |

These show Microsoft demo data (USMF and others). Use them for layout reference only. The guide's own screenshots should come from the WiseTech environment.

---

## PART 2: How end-user onboarding is structured elsewhere

### 2.1 Microsoft Success by Design: training strategy chapter (High)

**URLs**
- [training-strategy](https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/training-strategy)
- [scope and audience](https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/training-strategy-training-plan-scope-and-audience)
- [schedule and materials](https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/training-strategy-training-plan-schedule-and-materials)
- [delivery approach](https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/training-strategy-training-plan-delivery-approach)
- [process and best practices](https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/training-strategy-process-and-best-practices)
- [checklist](https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/training-strategy-checklist)
- [case study](https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/training-strategy-case-study)

**Outline:** Objectives (SMART) → Training plan elements → Scope → Audience/personas → Schedule → Materials → Delivery approach → Assessment → Assumptions/risks → Ongoing training → Best practices → Finance and operations specifics → Checklist → Case study.

**Notable ideas for a Getting Started guide**
- **Separate system training from business-process training.** Give changed processes special attention, and handle organisational change separately. This supports a Getting Started guide (system concepts) that sits apart from the process PGs.
- **Avoid overlap.** Where processes differ in business terms but are almost the same in the system, train them once as a shared system training area. That is exactly the case for a shared-concepts guide.
- **Personas by business role, not security role.** This makes onboarding new hires easier, so structure materials for staff turnover. It is consistent with D-083/D-099.
- **Materials:** documents are the least interactive but easiest to update. Other types are videos (short ones per topic), Microsoft Learn, guided help / task guides, and digital adoption platforms.
- Keep one central store of content, not email attachments. Plan for languages and accessibility (Office accessibility checker).
- **Training before UAT** means fewer "bugs" that are really training issues. Train super users and trainers first.
- **Training environment** needs realistic data. "Test 1/Test 2" data teaches users to enter fake data in production.
- **Assess** with end-of-training checks on the most frequent processes, day-in-the-life tests, UAT findings and helpdesk tickets after go-live. Feed results back into the materials.
- **Best practices:**
  - "Earlier is better".
  - "More is (usually) better": D365 has several ways to do the same thing, so repetition helps. Avoid duplicating Learn content, though.
  - Train with the adoption goal in mind.
  - Assume the same baseline for every participant.
  - Identify ongoing challenges.
- **F&O specifics:**
  - Microsoft Learn docs (use `site:learn.microsoft.com Dynamics 365 "term"`).
  - **In-product Help**, which is contextual to the page.
  - **Task recorder / task guides**: interactive and played from the Help pane.
  - Size the training environment tier for the number of concurrent users.
- **Checklist items:** SMART objectives; a plan updated incrementally; system plus business processes; personas matched to roles; a schedule aligned to the project; content types; a realistic, refreshed training environment; trainers trained before UAT; accessibility; a feedback loop; continuous training through updates and role changes.

### 2.2 Microsoft Success by Design: change management chapter (High)

**URLs**
- [change-management](https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/change-management)
- [assessing business process change](https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/change-management-assessing-business-process-change)

**Ideas**
- Avoid both the "too much theory" trap and the "we don't need change management" trap.
- Score each process by how much change it brings for each user group, then focus effort where the change is biggest. The same scoring helps find champions.
- After go-live, measure adoption: interviews, surveys, sign-ins and transaction counts.

### 2.3 Microsoft Learn: "Get started with finance and operations apps" learning path (High; beginner; business user)

URL: [learning path](https://learn.microsoft.com/en-us/training/paths/get-started-finance-operations/), 8 modules.

1. **Navigate finance and operations apps** ([module](https://learn.microsoft.com/en-us/training/modules/navigate-finance-operations/)), with these units:
   1. Navigation elements: dashboard, tiles, UI element glossary, navigation pane (Favorites, Recent, Workspaces, Modules), workspaces.
   2. How workspaces drive productivity, with the Customer invoicing workspace as the example.
   3. Filtering techniques: Filter pane, QuickFilter, grid column header filter, wildcards.
   4. Searching: navigation search, `form:` search, results capped at 10, action search.
   5. Comparing views: Grid, Details, Line, Header.
   6. View and edit mode.
   7. Summary.
   8. Quiz.
2. Get started with Dynamics 365 Finance (feature overview).
3. Get started with Supply Chain Management.
4. Production control.
5. Commerce.
6. Human Resources.
7. Project Operations.
8. **Get help and learn more**: Microsoft Learn docs, in-product help, customising help topics, privacy.

**Notable points**
- Navigation is taught generically, with no finance concepts.
- The finance overview module *assumes* "general knowledge of basic navigation".
- The path stops at UI basics, so no dimensions, periods or vouchers.

### 2.4 Microsoft Learn: AB-6002 "Introduction to finance in Dynamics 365" (High; 1 day; beginners and business users)

**URLs**
- [course](https://learn.microsoft.com/training/courses/ab-6002)
- [learning path](https://learn.microsoft.com/en-us/training/paths/introduction-finance-dynamics-365/), 7 modules.

**Modules**
1. **Describe finance and operations apps**: ERP, Copilot and agent use cases, *navigate efficiently within and across apps*.
2. **Describe reporting and integration**: built-in reports, Power BI, Microsoft 365, Power Platform, business events, Electronic reporting, Finance insights.
3. **Describe shared features**: security, workflow, **batch jobs**, organisation and legal entities, **record templates**, **global address book**, **alerts**, **number sequences**, **attachments**.
4. **Describe Finance core capabilities**: capabilities, **reporting vs accounting currency**, **tax**, cost accounting, electronic payment formats.
5. **Describe GL and cash and bank management**: **chart of accounts and main accounts**, **financial dimensions, dimension sets, financial tags**, **accounting structure**, **financial journal concepts**, Financial reporting, cash and bank, allocations and accruals, periodic processes.
6. **Describe AP and AR**: payment setup, vendors, POs, invoices, **posting profiles and account/offset dimensions in journals**, payments and settlement, three-way match, customers, free text invoices, netting, credit management, collections, subscription billing.
7. Expense, fixed assets, budgeting, project accounting.

**Notable points**
- This is Microsoft's closest equivalent to the guide being scoped. Its ordering is UI, then shared features (org, GAB, number sequences, workflow, batch, alerts, attachments), then core finance concepts (currency, tax), then GL concepts (CoA, dimensions, structures, journals), then process areas.
- Its depth is conceptual ("Describe …"), with hands-on labs in the instructor-led version.

### 2.5 Other Microsoft Learn modules used as onboarding

All High.
- [Describe Dynamics 365 Finance core capabilities](https://learn.microsoft.com/en-us/training/modules/explore-microsoft-dynamics-365-finance-core-capabilities/): legal entities, currencies, tax, cost accounting, agents.
- [Perform daily procedures in General ledger](https://learn.microsoft.com/en-us/training/modules/general-ledger-daily-procedures-dyn365-finance/): GL processes, balance control accounts, journal controls, voucher templates, ledger settlements. Its prerequisite is "basic navigation".
- [Configure and use journals unit](https://learn.microsoft.com/en-us/training/modules/configure-ledgers-journals-dyn365-finance/4-journals): journal flow (create, lines, validate, post), voucher inquiries, ledger account alias, Excel.
- [Set up financial dimensions](https://learn.microsoft.com/en-us/training/modules/set-up-financial-dimensions-finance): consultant-level.
- [Configure your UI (personalisation)](https://learn.microsoft.com/en-us/training/modules/configure-your-ui-dynamics-365-finance-operations-apps/): favourites, role dashboards, KPI tiles, form and report fields.

**What Microsoft's own modules don't do**
- They don't teach *data entry concepts* such as the segmented entry control, default dimension order, or period status from the user's side.
- They don't teach diagnosing posting errors.
- They don't teach the company picker as a risk, or the session date.
- They are written for consultants or "describe" level, not "do".

### 2.6 Koenig Solutions: "End User Training for Microsoft Dynamics 365 Finance" (Medium; training provider; 2 days)

**URLs**
- [2026 TOC PDF](https://www.koenig-solutions.com/CourseContent/custom/20260930001954746_10023-end-user-training-for-microsoft-dynamics-365-finance-TOC.pdf)
- [2021 PDF](https://www.koenig-solutions.com/CourseContent/custom/20214968-EndUserTrainingforMicrosoftDynamics365Finance.pdf)

**Audience:** finance users, AP and AR clerks, fixed asset administrators, budget administrators.

**16 topics:**
1. Create Chart of Accounts.
2. Main account.
3. Process General Journal.
4. Reverse the General Entry.
5. Use allocation.
6. Invoice Journal.
7. Invoice Register.
8. Create Vendor.
9. Vendor Payments.
10. SO invoice.
11. Free text invoice.
12. Customer payment.
13. Acquire Fixed Asset.
14. Depreciate.
15. Dispose.
16. Budget Register entry.

Hands-on exercises are included.

**Notable points**
- It is task-first, with no navigation or concepts module.
- It includes setup tasks (CoA and main account creation) that end users don't normally do.
- It shows that some providers skip a basics module altogether.

### 2.7 Koenig / edutechsuvidha: MB-300 "Core Finance and Operations" outline (Medium; consultant course)

URL: [PDF](http://edutechsuvidha.com/wp-content/uploads/2020/09/202071379-MicrosoftDynamics365CoreFinanceandOperations1.pdf)

**15 modules:** Get started; LCS; LCS design and plan; Reporting and analytics; Mobile apps; **Workflows**; **Legal entities**; **Users and security**; **Personalization**; Integration; Data migration; Data management; UAT; Go-live; Conclusion.

**Relevance:** it shows the consultant curriculum. Only workflow, legal entities, personalisation and reporting are end-user relevant.

### 2.8 Andreas Luszczak: *Using Microsoft Dynamics 365 for Finance and Operations*, 2nd ed., Springer 2023 (Medium-High; published textbook used for university/self-study)

**URLs**
- [book](https://link.springer.com/book/10.1007/978-3-658-40453-6)
- [2019 chapter](https://link.springer.com/chapter/10.1007/978-3-658-24107-0_2)

**Outline**
- Ch. 1 What is Dynamics 365 (pp. 1–4).
- **Ch. 2 Getting Started: Navigation and General Options (pp. 5–48)**.
- Purchase; Sales; Production; Forecasts/Master planning; Inventory; Finance chapters, and so on.
- It includes a case study with exercises for self-study.

**Notable points**
- Navigation comes first at about 44 pages, which is substantial, and exercises run through every chapter.
- The detailed Ch. 2 TOC couldn't be read (paywalled; the dokumen.pub mirror returned 5xx).

### 2.9 Dynamics Tips: "Introduction: Basics and Navigation" (Medium; practitioner site)

URL: [page](https://sites.google.com/view/dynamicstips/common/introduction-basics-and-navigation)

**Outline**
- Login.
- Landing page: navigation pane, company logo, calendar, work items, workspaces, search, company, Action center, settings, help.
- Companies.
- **User options**:
  - Visual.
  - Preferences: default company, initial page, **default view/edit mode** (it suggests Edit), language, **date/time/number format**, **time zone**, country/region, document handling, enhanced tab sequence.
  - Account: email provider.
  - Workflow: email and Action center notifications, **delegation**.
- Search bar; navigation pane; area page; list page; multiple windows; ribbon; FastTabs; FactBoxes; create/delete; data entry; view details.
- Filtering and sorting: grid filter, sort, side filter panel, advanced filter, search-bar filter, Export to Excel.
- Keyboard shortcuts; document handling; Help; Takeaways.

**Includes beyond Microsoft modules:** user options in detail (time zone affects batch timing), workflow delegation, and document handling.

### 2.10 Digital Architect Group: "Basic user guide: Searching & filtering" PDF (Medium; consultancy; 17 pp.)

URL: [PDF](https://www.digitalarchitectgroup.com/wp-content/uploads/2020/05/User-Guide_Searching-and-filtering.pdf). It is part 1 of a free three-part series: Searching and filtering; Personalization and Workspaces; Bringing it all together.

**Outline**
1. Overview: searching (finding pages) vs filtering (narrowing data).
2. Searching.
3. Basic filtering: Filter pane, Form filter, Grid filters.
4. Filtering options table, with advanced syntax for each: Is exactly; Is not (`!`); Contains (`*x*`); Does not contain (`!*x*`); Begins with (`x*`); Is one of (comma list); After (`x..`); Before (`..x`); blanks with `""`.
5. Advanced filtering: Options > Advanced Filter & Sort, with Range, Joins, Sorting and Date options; saving filters.

**Notable points**
- A short illustrated PDF per skill is offered as an editable, re-brandable template.
- The query syntax table is more practical than Microsoft's.
- Voucher transactions uses the same Range/Joins query dialog, so this skill carries over directly to finance inquiries.

### 2.11 Ms. Dynamic Millennial: "Dynamics 365 for Finance: Basic Navigation Concepts" (Low-Medium; personal blog, 2020)

URL: [post](https://msdynamicmillennial.wordpress.com/2020/08/22/dynamics-365-for-finance-basic-navigation-concepts/)

**Outline**
- Sign-in.
- Home page elements: **legal entity switch**, messages (Ctrl+Shift+F7), settings, help, user account, navigation search, navigation pane (Alt+F1), **calendar = session date**, work items, workspaces.
- Navigation pane sections.
- Workspace anatomy: tiles, lists, links; personalising a workspace.
- Form anatomy: Action pane, action search vs navigation search, PowerApps, Office.

**Notable point:** it explicitly ties the dashboard calendar to the **session date** and gives a real use: post-dated cheques.

### 2.12 AX7.uk: "Navigating the D365 F&O interface" series (Medium; named practitioner blog, 2024)

URL: [Part 3](https://ax7.uk/2024/02/06/navigating-the-d365-fo-interface-part-3/). Part 1 covers the default dashboard and Part 2 covers user options.

**Outline:** a numbered callout of the grid view covering 20 elements. Highlights:
- Home shortcut.
- Navigation path (breadcrumb).
- **Back button: use it rather than the browser back button.**
- Edit/New/Delete. Delete with care and check which records are selected.
- Action pane, tabs and search.
- Power Apps.
- **Open in Office**: Export to Excel is static; Open in Excel links back.
- Attachments, refresh, open in new window.
- **Filter pane and Related information buttons**.
- View selector, QuickFilter, column header functions.
- Hyperlinked text opens details.
- Selection circles.
- Grid options: **Show footer** for row counts.

**Notable point:** it uses an annotated-screenshot "numbered callouts" format, and its "gems" are tips experienced users miss.

### 2.13 Encore Business Solutions: "How to Navigate Through the D365 F&O Interface" (Medium; partner blog)

URL: [post](https://www.encorebusiness.com/blog/how-to-navigate-through-the-dynamics-365-finance-operations-interface/)

**Outline:** Homepage (Favorites, Recent, Workspaces, Modules) → navigating to customer records → All customers page → adding columns → custom view → navigating customer records → tips (Filter box, wildcard, breadcrumb).

**Notable point:** it teaches navigation through one realistic record journey, the customer, instead of an element glossary.

### 2.14 Dummies: "D365O: Navigation and User Preferences" (Medium; published book excerpt)

URL: [article](https://www.dummies.com/article/d365o-navigation-and-user-preferences-in-dynamics-365-finance-and-operations-258717)

**Outline**
- Tile types: Standard, Count, KPI, Link.
- Step-by-step user options: default company, initial page, view/edit mode, language, date/number format, time zone, country/region; Save.

### 2.15 Guide to Learn: "D365 F&O Overview | Navigation, Workspaces & Modules" (Low-Medium; commercial video course, about 29 min)

URL: [course](https://guidetolearn.com/microsoft-dynamics-365-finance-operations-overview-navigation-workspaces-modules-training)

**Outline:** access the app → interface and basic navigation → operational workspaces → major modules → how Finance and SCM modules relate → cross-application processes.

### 2.16 Solving Dynamics 365: "General journal entry workflow" (Medium; named consultant, independent reference site)

URL: [guide](https://solvingdynamics365.com/guides/general-journal-entry-workflow-in-f-and-o/)

**Outline**
- Journal architecture: name, journal, lines.
- Creating a journal; line structure; account types; voucher and balance.
- **Validation chain**: fields → account → tax → balance → period → approval.
- Approval workflows; posting restrictions; recurring; reversing; audit trail.
- Posted vs draft.
- Operational rhythm.
- **Common pitfalls**: wrong journal name; unbalanced voucher; invalid dimension combination; closed period; wrong posting layer.

**Notable point:** the "validation chain" is a teachable mental model for why posting fails.

### 2.17 Other sources consulted (lower value or inaccessible)

- Scribd user uploads, including [Navigation guide](https://www.scribd.com/document/487494212/microsoft-dynamics-365-navigation-step-by-step), [MSD365 F&O](https://www.scribd.com/document/919844947/MSD365-F-O), [Training Manual Finance AFZ](https://www.scribd.com/document/726464692/Training-Manual-Finance-Merged-AFZ-V-1-5-04-09-2023) and [Project management manual](https://www.scribd.com/document/960516109/End-Users-Training-Manual-Project-Managemet-and-Accounting-V2). Low trust, paywalled, and not read.
- [AXcademy intro course](https://axcademy.com/courses/introduction-to-microsoft-dynamics-365-for-finance-and-operations/). The course content wasn't visible.
- [ERP Software Blog: Financial dimensions tips](https://erpsoftwareblog.com/2026/09/financial-dimensions-setup-in-dynamics-365-finance/) (Medium; design-side mistakes such as over-dimensioning and not using defaults).
- [RSM: saved views](https://technologyblog.rsmus.com/microsoft/dynamics-365-for-finance-and-operations/using-the-new-views-functionality-in-dynamics-365-finance-and-supply-chain-management/) (Medium, 2020). Published views go to roles and legal entities, which helps new hires.
- University and public-sector PDFs: searches across .edu, .gov, .gov.au and .ac.uk found **no** published D365 F&O end-user navigation guide. Hits were job ads and spam pages. This is a gap worth noting: public examples come from partners and Microsoft only.

### 2.18 Common mistakes new users make (consolidated from all sources)

1. **Working in the wrong legal entity.** No warning appears. Check the company picker before entering data. (Learn UI module; Dynamics Tips; Ms. Dynamic Millennial)
2. **Leaving a changed session date in place**, which misdates postings. (Session date doc; Ms. Dynamic Millennial)
3. **Choosing the wrong journal name**, which bypasses controls and can't be renamed later. (Microsoft GJ processing; Solving D365)
4. **Unbalanced vouchers**: missing offset, mixed dates on one voucher, or foreign-currency rounding. (Microsoft imbalance doc)
5. **Invalid dimension combinations or blanks**, and **not checking both sides of the line**. Surprises from offset-account defaulting and fixed dimensions. (Microsoft dimension docs and troubleshooter)
6. **Posting into a closed or On hold period.** (Microsoft period docs)
7. **Using One voucher for many customers or vendors.** (Microsoft One voucher)
8. **Using the browser Back button** instead of the page back arrow, and **deleting the wrong selected rows**. (AX7.uk)
9. **Not saving personalisation as a view.** Views aren't saved automatically. (Saved views doc)
10. **Confusing navigation search (pages) with filtering (data) or action search (buttons).** (Learn; Digital Architect Group)
11. **Expecting to edit or delete posted transactions.** The fix is reversal. (Microsoft)
12. **Leaving the default view/edit mode on View** and hunting for Edit. (Dynamics Tips; Dummies)
13. **Time zone not set**, so batch schedules run at unexpected times. (Dynamics Tips)
14. **Exporting to Excel (static) when Open in Excel (live) was needed**, or the other way round. (AX7.uk)

### 2.19 Comparison table: topics × sources

Key: ● = covered in depth, ○ = mentioned, blank = absent.
Column codes: SbD = Success by Design; LP-GS = Learn "Get started with F&O" path; AB6002 = Learn AB-6002; MS-docs = Microsoft docs; KoenEU = Koenig end-user course; MB300 = MB-300 outline; Lusz = Luszczak book; DTips = Dynamics Tips; DAG = Digital Architect Group; MsDM = Ms. Dynamic Millennial; AX7 = AX7.uk; Enc = Encore; Dum = Dummies; G2L = Guide to Learn; SolvD = Solving Dynamics 365.

| Topic | SbD | LP-GS | AB6002 | MS-docs | KoenEU | MB300 | Lusz | DTips | DAG | MsDM | AX7 | Enc | Dum | G2L | SolvD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sign-in, dashboard, tiles | | ● | ○ | ● | | | ● | ● | | ● | ○ | ● | ● | ● | |
| Navigation pane, search, action search | | ● | ○ | ● | | | ● | ● | ● | ● | ● | ● | | ● | |
| Company picker / legal entity | | ○ | ● | ● | | ● | ○ | ● | | ● | | | ○ | | |
| User options (default company, time zone, view/edit) | | | | ● | | ● | ● | ● | | | ○ | | ● | | |
| Session date | | | | ● | | | | | | ● | | | | | |
| Filtering, query syntax, advanced filter | | ● | | ● | | | ○ | ● | ● | | ● | ○ | | | |
| Views (grid/details/header/lines), saved views | | ● | | ● | | ● | | ○ | | | ● | ● | | | |
| Workspaces | | ● | ○ | ● | | | | ○ | ○ | ● | | ● | ○ | ● | |
| FactBoxes / Related information | | ○ | | ● | | | | ● | | | ● | | | | |
| Excel (export/open lines) | | | ○ | ● | | | | ● | | ○ | ● | | | | |
| Help, task guides | ● | ● | | ● | | ● | | ● | | ○ | | | | | |
| Workflow / work items / delegation | | | ● | ● | | ● | | ● | | ○ | | | | | ● |
| Org structure, operating units, intercompany | | | ● | ● | | ● | | | | | | | | ○ | |
| Global address book / parties | | | ● | ● | | | | | | | | | | | |
| Number sequences | | | ● | ● | | | | | | | | | | | |
| Chart of accounts / main accounts | | | ● | ● | ● | | ● | | | | | | | | |
| Financial dimensions | | | ● | ● | | | ○ | | | | | | | | ○ |
| Segmented entry control (how to enter) | | | | ● | | | | | | | | | | | |
| Default dimension flow | | | ○ | ● | | | | | | | | | | | |
| Fiscal calendar, period status | | | ○ | ● | | | ○ | | | | | | | | ○ |
| Journals (name, validate, post, templates) | | | ● | ● | ● | | ● | | | | | | | | ● |
| Vouchers and balancing | | | ○ | ● | ○ | | ● | | | | | | | | ● |
| Voucher transactions / Transaction origin / Trial balance | | | ○ | ● | | ○ | ○ | | | | | | | | |
| Currencies and exchange rates | | | ● | ● | | | ○ | | | | | | | | ○ |
| Sales tax groups | | | ● | ● | | | ○ | | | | | | | | ○ |
| Reversal / correction | | | | ● | ● | | | | | | | | | | ● |
| Security concept | ○ | ○ | ● | ● | | ● | | | | | | | | | |
| Exercises / hands-on | ● (UAT, day-in-life) | ○ (quiz) | ● (labs) | ○ (task guides) | ● | ● | ● | | | | | | | | |

**Observations**
- No single source joins *navigation* with *shared finance concepts at do-level*.
- Microsoft splits them across a navigation module, AB-6002 "describe" modules and scattered docs.
- Training providers skip to tasks.
- Practitioner guides stop at UI.
- The segmented entry control, default dimension flow, session date and "why won't it post?" diagnostics are almost absent from training material, though Microsoft docs cover them well.

---

## Conclusions

### (1) Ranked suggestions: Getting Started topics and key concepts from this area

**MUST**

1. **Legal entities and the company picker.** WTG is multi-entity, and posting in the wrong company is the top silent error. Covers checking and switching company, the default company, and why lists show one company.
2. **Financial dimensions and the segmented entry control.** Every O2C, P2P, R2R and Tax guide has lines with Account fields. Teach the segments, the lookup, Show all/Show valid, type-ahead by value or description, validation on leaving the field, and Account vs Offset account dimensions.
3. **Default dimensions: where values come from.** Explains "why is this dimension filled in?" and "why did the posted voucher differ from the line?" Cover the order (journal name → header → account → offset), fixed dimensions at posting, and checking both sides.
4. **Journals concept.** Header and lines, journal name, Lines, Validate, Post, and the Voucher drill-back. This is shared by payment, invoice, general and allocation journals across all streams. Mention Simulate posting, Post and transfer, workflow submit, and "locked by system".
5. **Vouchers and balancing.** One voucher per business transaction, debits equal credits, the imbalance message, and the penny difference. This is the most frequent posting failure.
6. **Periods and period status, and why posting fails.** Open, On hold and Permanently closed; access per module; the date drives the period. Process guides reference month-end constantly.
7. **Posting date, document date and session date.** Dates drive the period, the exchange rate, due dates and discounts. Changing the session date is a known trap.
8. **Finding posted transactions.** Voucher transactions with query ranges, **Transaction origin**, Trial balance drill-down, customer and vendor **Transactions** with the Show filter and **View settlements**, plus **Related information** (FactBoxes). This is the universal "check your work" step for every completion check.
9. **Corrections are reversals.** Posted entries can't be edited. Reverse with a new date if the period is closed.
10. **Access and support.** The manager requests the D365 profile; for missing pages, contact the BAU Support team (D-083). Don't name roles.

**SHOULD**

11. **Chart of accounts and main account basics.** Account types; suspended accounts; "do not allow manual entry" on control accounts; why AR and AP users pick a customer or vendor, not a ledger account (posting profiles and subledgers).
12. **Currencies and exchange rates.** Accounting vs reporting vs transaction currency; rates shared across entities; the rate on or before the posting date; three currency columns in inquiries. WTG is multi-currency.
13. **Sales tax / GST concept.** The intersection of the sales tax group and the item sales tax group, the **Sales tax** button on lines, and "blank group means no tax". Tax and O2C/P2P guides rely on it.
14. **Global address book and parties.** Customers and vendors are parties shared across companies; **Global transactions**; an address change applies everywhere.
15. **Workspaces in finance.** Anatomy (tiles, lists, links), the company and workspace filter, and examples (Customer payments, Vendor payments, Financial period close, Collections). Confirm the workspace names in the environment.
16. **Number sequences (user view).** Auto IDs, numbers repeating per company, and gaps that are normal.
17. **Intercompany at concept level.** The Company and Offset company columns, automatic due to/from entries, and preferring single-line entries.
18. **Workflow and approvals (user view).** Submit, Work items, Action center, delegation.

**NICE-TO-HAVE**

19. **Voucher templates and periodic (recurring) journals.** Productivity tips for R2R and AP.
20. **Excel add-in.** **Open lines in Excel** for bulk lines; Export to Excel (static) vs Open in Excel (live).
21. **Financial tags vs dimensions.** Only if WTG uses tags.
22. **Accounting source explorer / Audit trail.** Mostly R2R.
23. **Organisation hierarchies and operating units.** Background on why dimensions such as Department exist.
24. **"Why won't it post?" troubleshooting table** (section 1.19) as a closing reference or an appendix in the guide.

### Design ideas from Part 2 worth adopting (for the guide's structure)

- **Organise by the user's question.** Order it as: "Where am I?" (company, workspace), "How do I enter it?" (segmented entry, defaults), "Will it post?" (periods, balance, validate), "Where did it go?" (voucher inquiries). This is a concept-to-action ladder no source has.
- **Keep system training separate from process training** (SbD). The Getting Started guide holds the shared concepts once, and process PGs cross-reference it. This avoids the overlap SbD warns about.
- **Annotated screenshots with numbered callouts** (AX7.uk), and **one realistic record journey** (Encore: follow one customer or one journal).
- **Short practice exercises** in a training environment with realistic data (SbD, Luszczak, Koenig). For example: switch company; find a page by search; enter a two-line journal with dimensions and validate it; open Voucher transactions for the posted voucher and use Transaction origin; filter customer transactions to Open.
- A **filter syntax table** (DAG). It also covers Voucher transactions ranges with `..`.
- Point to **in-product Help and task guides** for self-service (SbD F&O guidance).
- **Structure for staff turnover**: new hires should be able to self-onboard from the guide (SbD).

---

## (2) Every URL consulted

**Microsoft Learn documentation (Finance / fin-ops-core)**
- https://learn.microsoft.com/en-us/dynamics365/finance/
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/financial-dimensions
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/enter-account-dimension-values-segmented-entry-control (404 now)
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/enter-account-dimension-combinations-segmented-entry-control
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/general-journal-processing
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/organizations-organizational-hierarchies
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/organization-administration/overview-global-address-book
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/plan-configuration-global-address-book-additional-address-books
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/default-dimensions
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/configure-default-dimensions (404)
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/dimensions-default-values
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/configure-account-structures
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/main-account-types
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/plan-chart-of-accounts
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/tasks/create-main-account
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/tasks/create-advanced-rules-journals
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/derived-dimensions
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/tasks/maintain-financial-dimension-default-templates
- https://learn.microsoft.com/en-us/dynamics365/finance/budgeting/fiscal-calendars-fiscal-years-periods
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/close-general-ledger-at-period-end
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/tasks/mass-financial-period-close
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/financial-period-close-workspace
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/year-end-close
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/change-mdfy-clndr-to-ledger
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/view-journal-entries-transactions
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/tasks/view-journal-entries-or-transactions
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/general-ledger-account-balances
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/trial-balance-financial-reports
- https://learn.microsoft.com/en-us/dynamics365/finance/public-sector/general-ledger-public-sector-trial-balance
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/ledger-journal-types
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/posting-fail-imbalance
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/reverse-journal-posting
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/cant-reverse-transctns
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/tasks/create-journal-entry-template
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/tasks/create-validate-journals
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/tasks/post-periodic-journals
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/posting-performance
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/one-voucher
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/ledger-subledger
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/configure-ledger
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/subledger-transfer
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/pstg-prfles-ovrvw
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/intercompany-accounting-setup
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/intercompany-journal
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/tasks/view-related-intercompany-voucher-journal
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/example-balanced-journals-interunit-accounting
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/indirect-taxes-overview
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/tasks/set-up-sales-tax-groups-item-sales-tax-groups
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/import-currency-exchange-rates
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/dual-currency
- https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/accounting-distributions
- https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/accounting-source-explorer
- https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/vendor-invoice-dates
- https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/vendor-payments-workspace
- https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/vendor-transaction-list-page
- https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/customer-transactions-list-page
- https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/collectionsworkspace
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/number-sequence-overview
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/tasks/change-date-session
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/user-interface-elements
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/configure-filter-workspaces
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/use-lookups-to-find-information
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/default-dashboard
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/navigation-search
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/help-overview
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/saved-views
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/shortcut-keys
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/user-interface/task-recorder-training-docs
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/analytics/financial-reporting-intro
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/role-based-security
- https://learn.microsoft.com/en-us/troubleshoot/dynamics-365/finance/general-ledger/common-dimension-related-errors

**Microsoft Success by Design / adoption**
- https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/ (index; dynamic, not readable)
- https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/training-strategy
- https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/training-strategy-training-plan-scope-and-audience
- https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/training-strategy-training-plan-schedule-and-materials
- https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/training-strategy-training-plan-delivery-approach
- https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/training-strategy-process-and-best-practices
- https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/training-strategy-checklist
- https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/training-strategy-case-study
- https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/change-management
- https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/change-management-assessing-business-process-change
- https://learn.microsoft.com/en-us/dynamics365/adoption/adoption-guide-envision (redirected to a general page)

**Microsoft Learn training**
- https://learn.microsoft.com/en-us/training/paths/get-started-finance-operations/
- https://learn.microsoft.com/en-us/training/modules/navigate-finance-operations/ (units 2–7)
- https://learn.microsoft.com/en-us/training/modules/get-introduced-finance-operations-apps/
- https://learn.microsoft.com/en-us/training/modules/configure-your-ui-dynamics-365-finance-operations-apps/
- https://learn.microsoft.com/en-us/training/paths/introduction-finance-dynamics-365/
- https://learn.microsoft.com/training/courses/ab-6002
- https://learn.microsoft.com/en-us/training/modules/describe-finance-operations-apps/
- https://learn.microsoft.com/en-us/training/modules/describe-report-integration/
- https://learn.microsoft.com/en-us/training/modules/describe-shared-features/
- https://learn.microsoft.com/en-us/training/modules/describe-dynamics-365-finance-core-capabilities/
- https://learn.microsoft.com/en-us/training/modules/describe-general-ledger-cash-bank-management/
- https://learn.microsoft.com/en-us/training/modules/describe-account-payables-account-receivables/
- https://learn.microsoft.com/en-us/training/modules/get-help-finance-operations/
- https://learn.microsoft.com/en-us/training/modules/get-started-financial-management-dyn365-finance/
- https://learn.microsoft.com/en-us/training/modules/set-up-financial-dimensions-finance
- https://learn.microsoft.com/en-us/training/modules/explore-microsoft-dynamics-365-finance-core-capabilities/ (units 3, 4, 5)
- https://learn.microsoft.com/en-us/training/modules/general-ledger-daily-procedures-dyn365-finance/ (unit 4)
- https://learn.microsoft.com/en-us/training/modules/configure-currencies-dyn365-finance/3-currency-exchange-rate
- https://learn.microsoft.com/en-us/training/modules/configure-ledgers-journals-dyn365-finance/4-journals

**Third-party**
- https://www.koenig-solutions.com/CourseContent/custom/20214968-EndUserTrainingforMicrosoftDynamics365Finance.pdf
- https://www.koenig-solutions.com/CourseContent/custom/20260930001954746_10023-end-user-training-for-microsoft-dynamics-365-finance-TOC.pdf
- http://edutechsuvidha.com/wp-content/uploads/2020/09/202071379-MicrosoftDynamics365CoreFinanceandOperations1.pdf
- https://www.digitalarchitectgroup.com/wp-content/uploads/2020/05/User-Guide_Searching-and-filtering.pdf
- https://dynamics-tips.com/wp-content/uploads/2024/04/Product-Information-Management-User-Guide.pdf (download failed)
- https://sites.google.com/view/dynamicstips/common/introduction-basics-and-navigation
- https://ax7.uk/2024/02/06/navigating-the-d365-fo-interface-part-3/
- https://msdynamicmillennial.wordpress.com/2020/08/22/dynamics-365-for-finance-basic-navigation-concepts/
- https://www.encorebusiness.com/blog/how-to-navigate-through-the-dynamics-365-finance-operations-interface/
- https://www.dummies.com/article/d365o-navigation-and-user-preferences-in-dynamics-365-finance-and-operations-258717
- https://guidetolearn.com/microsoft-dynamics-365-finance-operations-overview-navigation-workspaces-modules-training
- https://axcademy.com/courses/introduction-to-microsoft-dynamics-365-for-finance-and-operations/
- https://link.springer.com/book/10.1007/978-3-658-40453-6
- https://link.springer.com/chapter/10.1007/978-3-658-24107-0_2
- https://dokumen.pub/using-microsoft-dynamics-365-for-finance-and-operations-learn-and-understand-the-dynamics-365-supply-chain-management-and-finance-apps-2nbsped-3658404523-9783658404529.html (server error)
- https://solvingdynamics365.com/guides/general-journal-entry-workflow-in-f-and-o/
- https://erpsoftwareblog.com/2026/09/financial-dimensions-setup-in-dynamics-365-finance/
- https://www.randgroup.com/insights/microsoft/dynamics-365/finance-operations/intercompany-accounting-in-dynamics-365-finance-setup-steps-common-errors-and-best-practices/
- https://technologyblog.rsmus.com/microsoft/dynamics-365-for-finance-and-operations/using-the-new-views-functionality-in-dynamics-365-finance-and-supply-chain-management/ (search result only)
- https://community.dynamics.com/article/KA-26203 (search result only)
- Scribd uploads listed in 2.17 (search results only, not read)
