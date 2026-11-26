<!-- https://learn.microsoft.com/en-us/training/modules/describe-account-payables-account-receivables/8-describe-credit-management-processes -->
# Describe credit management processes in Dynamics 365

Completed

* 10 minutes

Customer credit management lets you manage credit limits and control the flow of sales orders through the posting process. Those credit limits are based on credit rules you create.

The credit management process can include any of the following steps:

* Update credit attributes for customers to provide additional information about their credit worthiness.
* Create credit limits for customers by using credit limit adjustments.
* Create temporary credit limits for customers by using credit limit adjustments. In this way, you can temporarily increase or decrease customer credit limits based on business requirements.
* Add information that can affect the credit limit, such as information about insurance and guarantees.
* Create customer credit groups that link customers together, so they share a single credit limit.
* Assign risk scores to customers and then use the scores to automatically generate credit limits for those customers through credit limit adjustments.
* Create blocking rules that put an order on hold during one or more posting processes based on factors such as:

  + Risk.
  + Payment terms.
  + Credit limits.
  + Overdue amounts.
  + Percentage of the credit limit that used.
* Manage a list of sales orders that are on hold, review the reasons for the hold, and mitigate issues.
* Release sales orders so they continue through the posting process.
* Set up a workflow to manage the approval of credit limit changes and sales order releases.

## Credit limit adjustment

You can navigate to the **Credit and collections module** > **Credit limit adjustments** > **Credit limit adjustments** page. You can make credit limit adjustments for an individual customer or for a customer credit group. Once you select the **Post** button on the **Credit limit adjustments** page, the newly adjusted limit is in effect.

[![Screenshot of a credit limit adjustment with the Post button highlighted.](media/08-6-8-credit-limit.png)](media/6-8-credit-limit.png#lightbox)

The customer credit group can be configured under the **Customers** menu in the **Credit and collections** module. This page isn't bound to a legal entity, and you can define any customer from any legal entity as a part of a customer credit group.

[![Screenshot of customer credit groups.](media/08-6-8-customer-credit-groups.png)](media/6-8-customer-credit-groups.png#lightbox)

All the customers defined in one group share the same credit limit. You can select the **Aged balances** button in the Action pane to view the aging balance for each customer based on the aging period definition selected.

View the following video to see a demonstration of the credit limit process.

## Credit risk

In Dynamics 365 Finance, you create scoring groups for assessing customers based on available data related to spending and payment habits of the customers. You can create scoring groups based on different types of data such as average balance held, country/region, number of years in business, or number of years as a client. Based on these values, you can define the risk categorization of the customer.

You can define the risk classification by assigning the scoring range that can mark a customer as a part of a risk group. Risk scores come from the scoring groups mentioned previously.

Scoring group and risk classification are the two variables for the **Automatic credit limit**. You can set up a credit limit configuration for a high-risk customer. If a customer in Finance meets the criteria for the high-risk configuration defined previously, the system automatically puts a credit limit on the customer account and applies the necessary blocking rules during the sales order processing.

## Blocking rules

Blocking rules define the setup to determine when a sales order should be put on hold. It follows several rules that are defined on the tabs of the **Blocking rules** page.

[![Screenshot of blocking rules parameters.](media/08-6-8-blocking-rules.png)](media/6-8-blocking-rules.png#lightbox)

On the **Days overdue** tab, you can define the overdue days that block the sales order from being processed based on the customer/credit management group and risk group.

The account status group checks the customer’s account status to determine if the sales order should be put on hold.

You can put a sales order on hold if the **terms of payment** on the order don't match the default payment terms for the customer. However, sometimes the payment terms differ but are so similar that you don’t want to put the order on hold. You can rank payment terms so that some of them have the same rank, whereas others have a higher or lower rank.

The next tab displays the credit limit expiration date of the customer and adds grace days. If the credit limit expires and the added grace days are exceeded, the sales order is put on hold.

On the **Overdue amount** tab, the system checks the combination of the overdue amount and percentage of the credit limit that's being used already and puts the sales order on hold if the threshold is met.

You can set up rules to put a sales order on hold based on the sales order amount. You can also configure logic to release the sales order from blocking.

The next tab displays the credit limit usage of a customer and determines whether the order should be put on hold. If the percentage of the credit limit is exceeded, the sales order is put on hold.