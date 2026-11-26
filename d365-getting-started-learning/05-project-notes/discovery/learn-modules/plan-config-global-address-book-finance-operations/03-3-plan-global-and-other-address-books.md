<!-- https://learn.microsoft.com/en-us/training/modules/plan-config-global-address-book-finance-operations/3-plan-gab -->
<!-- refetched: original harvest URL returned 404 -->
# Plan for the global address book and other address books

Completed

* 7 minutes

You must consider many scenarios when you make decisions during the planning process, before you set up and configure the global address book and any additional address books in finance and operations apps. Some of the decisions will require that you confirm the decisions that have been made for other areas of the product, such as the organization hierarchy.

Before you begin to work with the global address book, you must determine the default values for it. These default values are then used for any additional address books that you create.

The following are some examples of the decisions that you need to make:

* What sequence should names be displayed in for party records of the person type? For example, one sequence is last name, middle name, first name.
* Should party records be deleted from the address book when the role record is deleted? For example, if a customer record is deleted, should the party record also be deleted?
* When a new record is created, should users be notified if a duplicate record is found in the global address book?
* Should the Data Universal Numbering System (DUNS) number be included in a party record’s information?
* If the DUNS number is included in a party record, should the uniqueness of the number be checked?
* When a party record is created in the global address book, do you want a default party type, person, or organization?
* Which user roles should have access to the private addresses and contact information of party records?

After you create the global address book, you can create additional address books if needed, such as a separate address book for each company in your organization or for each line of business.

To create additional address books, go to **Organization administration > Global address book > Address books**.

When you create a new address book, you first have an opportunity to select **Teams** to populate the address book with members of Teams that have been created.

[![Screenshot of the Address books page showing how to assign teams to an address book.](media/03-add-teams-address-book.svg)](media/add-teams-address-book.svg)

To set up **Teams**, go to **Organization administration > Organizations > Teams**. From there, you can add members to a team, which will then be added to a specific address book.

[![Screenshot the Teams page showing how to add team members.](media/03-teams.svg)](media/teams.svg#lightbox)

## Scenario

Adventure Works Cycles is an international organization that has multiple companies and multiple lines of business. Adventure Works Cycles plans to create an address book for each line of business. For lines of business that occur in more than one location, such as the retail business, Adventure Works Cycles plans to create an address book for each store location.

Assume that the IT manager at Adventure Works Cycles has created the following list of address books and describes the party records that each address book must include.

* **Public sector contracts** - Party records for all parties that are involved in the public sector contracts that Adventure Works Cycles holds.
* **Private sector contracts** - Party records for all parties that are involved in the private sector contracts that Adventure Works Cycles holds.
* **Electronic tools** - Party records for all parties that are involved in the purchase or sale of electronic tools, or that otherwise interact with the electronic tools that are provided by or purchased for Adventure Works Cycles in the Adventure Works Cycles -Italy company.
* **Pneumatic tools (PTJPN)** – Party records for all parties that are involved in the purchase or sale of pneumatic tools, or that otherwise interact with the pneumatic tools that are provided by or purchased for Adventure Works Cycles in the Adventure Works Cycles -Japan company.
* **Pneumatic tools (PTUSA)** – Party records for all parties that are involved in the purchase or sale of pneumatic tools, or that otherwise interact with the pneumatic tools that are provided by or purchased for Adventure Works Cycles in the Adventure Works Cycles -US company.

The IT manager must make the decision regarding how many additional address books need to be created.