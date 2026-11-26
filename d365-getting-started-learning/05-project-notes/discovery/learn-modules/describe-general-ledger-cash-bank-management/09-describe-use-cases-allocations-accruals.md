<!-- https://learn.microsoft.com/en-us/training/modules/describe-general-ledger-cash-bank-management/9-describe-use-cases-allocations-accruals -->
<!-- refetched: original harvest URL returned 404 -->
# Describe use cases for allocations and accruals

Completed

* 6 minutes

Organizations often need to distribute costs or recognize revenue and expenses in the correct accounting period. Dynamics 365 Finance provides tools to automate these processes through ledger allocations and accruals, ensuring accurate financial reporting and supporting consistent accounting practices.

## Allocations

Allocations distribute amounts to different ledger accounts so that expenses or revenue are recorded in the right places. This process helps organizations assign shared costs, like rent or utilities, to the departments or cost centers that use them.

The ledger allocation rules describe the various components of these allocation rules and the allocation methods that can be used for them.

Dynamics 365 Finance makes allocations easier by letting you set up allocation terms on main accounts. When you post a transaction to these accounts, the system automatically splits the amount based on your settings. You can also use ledger allocation rules to run allocations as a scheduled process, such as at month-end, to distribute balances or fixed amounts.

In addition to automated options, users can manually allocate transaction amounts when necessary by splitting accounting distributions or applying financial dimension default templates to a document.

Allocations distribute monetary amounts to one or more ledger accounts, where a ledger account consists of a main account and optional financial dimensions. In Finance, allocations can therefore occur in two primary ways: triggered automatically when posting to a main account with allocation terms or processed periodically based on rules that allocate balances across accounts according to defined percentages or drivers.

## Accruals

Accruals make sure that revenue and expenses are recorded in the period when they happen, not when cash is received or paid. This process helps organizations follow accounting rules like Generally Accepted Accounting Principles (GAAP) and International Financial Reporting Standards (IFRS).

Dynamics 365 Finance uses accrual journals to record these adjustments. An accrual journal allows an expense or revenue amount to be posted in the appropriate period while automatically generating a reversing entry in the following period. This reversal prevents overstatement and removes the need for manual correction. Accruals are especially important during period-end close, when organizations must reflect prepaid expenses, outstanding liabilities, or revenue earned but not yet invoiced.

Typical examples include accruing expenses for utilities, payroll, bonuses, or interest when invoices aren't yet received. Other examples are spreading prepaid items such as insurance or subscriptions over multiple periods, and recognizing revenue for work performed before billing occurs.