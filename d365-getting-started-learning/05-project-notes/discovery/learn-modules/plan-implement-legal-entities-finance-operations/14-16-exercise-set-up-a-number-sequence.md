<!-- https://learn.microsoft.com/en-us/training/modules/plan-implement-legal-entities-finance-operations/16-exercise-4 -->
<!-- refetched: original harvest URL returned 404 -->
# Exercise - Set up a number sequence

Completed

* 3 minutes

## Scenario

Number sequences are used to generate readable, unique identifiers for master data records and transaction records that require them.

1. Go to **Organization administration** > **Number sequences** > **Number sequences**.
2. Select **Number sequence**, under the **New** sub-menu.
3. In the **Number sequence code** field, enter **Formulas**.
4. In the **Name** field, enter **Formulas**.
5. Expand the **Scope parameters** section, and select **Shared** as the scope for the number sequence.
6. Expand the **Segments** section, select **Add** and define the format for the number sequence as follows:
   * **Segment** – Constant; **Value** – FORM. Notice that the length is set to 4.
   * **Segment** – Alphanumeric; **Value** - ####. Notice that the length is set to 4.
7. Expand the **General** section, and specify whether the number sequence is manual, and continuous or non-continuous.
8. Under **NUMBER ALLOCATION**, set the **Largest** to **9999**.
9. Select **Save**.