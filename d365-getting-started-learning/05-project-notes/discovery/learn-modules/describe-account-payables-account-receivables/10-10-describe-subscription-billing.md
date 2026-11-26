<!-- https://learn.microsoft.com/en-us/training/modules/describe-account-payables-account-receivables/10-describe-subscription-billing -->
# Manage subscription billing in Dynamics 365 Finance

Completed

* 8 minutes

Organizations that need to manage subscription revenue and recurring billing by using a billing schedule. You can use the **Subscription billing** module in Dynamics 365 Finance to take advantage of these features. Examples include recurring software subscriptions, physical item subscriptions, and recurring fees for equipment rentals. Organizations dealing with consumption-based billing can also use this feature.

The **Subscription billing** module supports three individual functionalities as follows:

* Recurring contract billing
* Revenue and expense deferrals
* Multi-element revenue allocation

## Recurring contract billing

The recurring contract billing feature helps you to manage recurring billing and price management. It can control the pricing and billing parameters at the line-item level along with contract renewal and consolidated invoicing. It has a flexible pricing model that's beneficial for customer invoicing.

You configure the **Billing schedule** group from **Recurring contract billing** > **Setup menu** in the **Subscription billing** module.

[![Screenshot of a billing schedule group.](media/10-6-10-schedule-group.png)](media/6-10-schedule-group.png#lightbox)

Here you can define billing frequence and interval. You can also define the **Pricing method** and **Item type**. Item type defines the calculation for the product quantity to be billed. It has three possible values:

* **Standard**: Based on quantity selected on the Billing schedule line
* **Usage**: Based on usage for each billing period, where the consumption quantity is entered manually in Billing schedule line
* **Milestone**: Based on the milestone template configured

The Pricing method defines how the unit price is calculated for the items in the order. It has four values:

* **Standard:** Unit price is selected based on Base sales price selected for this product in the **Product information management** module.
* **Flat:** Unit price can be manually entered and edited on the **Billing schedule** page in each line.
* **Tier:** Can be used if the sales price varies based on the sales order quantity.
* **Tier flat:** Can be used if the sales amount varies based on the sales order quantity.

The **Milestone template** is another important setup in recurring contract billing. It's used for milestone-based billing systems. In each milestone template, you can define the allocation percentage or amount for every milestone line. This setup lets you assign the milestone template to billing schedule items that use milestone billing. It helps ensure each milestone event, allocation, and billing item is managed correctly in the billing process.

[![Screenshot of milestone templates.](media/10-6-10-milestone.png)](media/6-10-milestone.png#lightbox)

The allocation method plays an important role in defining the percentage and amount in the milestone lines.

Billing schedule is the most important configuration in the recurring contract billing. You can create it on the **All billing schedules** page under the **Recurring contract billing** > **Billing schedules** menu in the **Subscription billing** module. A billing schedule can be used to set up the recurring charge that is required to be billed to the customer. This approach helps to streamline the customer billing process.

## Revenue and expense deferrals

This feature is useful for industries like insurance, consumption, or subscription-based service providers. In these industries, you may get the entire subscription or premium during the beginning of the year. But you can't recognize the entire amount as revenue when receiving it. You need to credit it to a deferred revenue account. Every month, once you deliver the service, you can credit your revenue account with the proportion of the monthly amount and debit the deferred revenue amount with the same amount. In this process, you recognize the revenue every month when the actual service is delivered.

You can also defer expenses paid at the start of the year and recognize them monthly as the service is used.

You can use the **Deferral templates** page to define straight-line templates that are used for deferral schedules. This configuration helps to define the frequency to recognize the revenue or expense.

[![Screenshot of deferral templates.](media/10-6-10-deferral-template.png)](media/6-10-deferral-template.png#lightbox)

The period frequency can be defined as daily, monthly, or fiscal periods. Organizations that use quarterly fiscal periods can set the deferral template to quarterly. You can select **Skipped** to skip the revenue/expense recognition in the first two months.

You can navigate to the sales order page in the **Accounts receivables** module and create a new sales order. The sales line includes the **Deferrals** link.

When the transaction deferral dialog appears, you need to slide the **Deferred** field to **Yes**. Then you can select the template discussed previously.

You can select the **Preview** button to view the deferral schedule.

[![Screenshot of a deferral schedule line preview.](media/10-6-10-preview.png)](media/6-10-preview.png#lightbox)

## Multi-element revenue allocation

With the multiple element revenue allocation, you can configure different templates to calculate and allocate revenue across multiple items. For example, you provide annual maintenance to home appliances. You provide a service that includes maintenance of a set of appliances together. You can also sell the maintenance of each appliance separately. You might want to set up multiple element revenue allocation parameters to establish how the standalone selling price of individual maintenance would be determined.