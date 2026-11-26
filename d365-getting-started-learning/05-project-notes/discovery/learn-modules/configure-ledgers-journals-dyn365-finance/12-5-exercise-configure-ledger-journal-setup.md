<!-- https://learn.microsoft.com/en-us/training/modules/configure-ledgers-journals-dyn365-finance/5-exercise -->
<!-- refetched: original harvest URL returned 404 -->
# Exercise - Configure ledger and journal setup

Completed

* 15 minutes

## Scenario

You are the functional consultant for the **USMF** Company, setting up the journal names, journal
descriptions and default descriptions for your business users to use
when posting journals.

## Create Journal names

**Journal names** are defined for a specific task according to its type
and purpose. Once you have set this up, they can then choose the journal
they want to use by the name you have defined here. Let's walk through
creating a new **Journal name.**

1. Go to **General Ledger > Journal setup > Journal names**.
2. In the Action Pane, select **New**.
3. Enter the new journal **Name** as **Transport**.
4. Enter the **Description** as **Transportation Expenses**.
5. Select the **Journal type** from the drop-down menu. Select **Project - expenses**.
6. Select a value in the **Voucher series** field.
7. Select **Save**.

## Create Journal descriptions

**Journal descriptions** help the business to ensure they are selecting the correct journal for their need. Let's set up a **Journal description.**

1. Go to **General Ledger > Journal setup > Journal descriptions**.
2. In the Action Pane, select **New**.
3. In the **Identification** field, enter **cc**.
4. In the **Search name** field, enter **cc**.
5. In the **Description** field, enter **Credit card**.
6. Select **Save**.

## Create Default descriptions used for automatic postings to the general ledger

**Default descriptions** are created to facilitate automatic postings to the general ledger, such as vendor payments. Let's create a new **Default description** for your users.

1. Go to **General Ledger > Journal setup > Default descriptions**.
2. In the Action Pane, select **New** to create a new default description.
3. Use the drop-down menu on the **Description** field and select **Ledger - generated allocation**.
4. Select **en-us** from the **Language** drop-down menu.
5. In the **Text** field, you can use fixed variables. These are called out in the **Reference** field at the bottom of the screen. For example, enter **Invoice%2**.
6. Select **Save**.