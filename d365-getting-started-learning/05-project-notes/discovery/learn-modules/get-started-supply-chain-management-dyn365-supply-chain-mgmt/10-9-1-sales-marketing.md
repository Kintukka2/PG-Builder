<!-- https://learn.microsoft.com/en-us/training/modules/get-started-supply-chain-management-dyn365-supply-chain-mgmt/9-1-sales-marketing -->
# Sales and marketing

Completed

* 8 minutes

Within the Sales and marketing module, users can store and use data related to their relationships with leads, opportunities, customers, and prospects. You can use marketing campaigns and activities to develop those relationships and use the sales functionality to create quotations, sales orders, and sales invoices.

Sales quotations enable your business to create a non-binding document with the items or services that a prospect or customer wants to buy from you. You can add any other charges or discounts to the quotation, and see a breakdown of any other information that may be required before creating a sales order. When the customer or prospect approves the quote, it is confirmed, and the system generates a sales order. You must create a customer account for a prospect prior to confirming the quotation.

A sales agreement is a contract between your business and a customer to purchase a product in a specific quantity over a specified period, in exchange for special pricing or discounts. These discounts or special prices are systematically applied when creating a sales order.
The sales order is considered a binding agreement between you and a customer to buy your company's item(s) or service(s).

The sales order type must be specified when creating a sales order. The sales order types are:

| **Sales order type** | **Description** |
| --- | --- |
| Journal | Use this type as a draft for a sales order. This type does not affect the stock quantities and doesn't generate item transactions. |
| Subscription | Use this type for recurring orders. When the order is invoiced, the order status is automatically set to an open order. The delivered quantity that was invoiced and the remaining deliveries are updated. You can't use this sales order type if you're using the Warehouse management functionality. |
| Sales order | Use this type when a customer has placed or confirmed an order. |
| Returned order | Use this type when a customer returns an item. A return-item number (RMA number) is automatically assigned. |
| Item requirements | This type is created automatically when you make an item sale through a project. |

The sales process involves three types of invoices:

* **Customer invoice** - A bill to the customer for a purchase. These are created based on sales orders and complete the process once the order is packed.
* **Free text invoice** – This invoice is not related to a sales order but contains order lines that include ledger accounts, a description, and a sales amount, but not an item number.
* **Proforma invoice** - This is a draft invoice that is generated prior to the invoice posting.

For more information about the Sales and Marketing module, see [Sales and marketing overview](/en-us/dynamics365/supply-chain/sales-marketing/overview-sales-marketing/?azure-portal=true).