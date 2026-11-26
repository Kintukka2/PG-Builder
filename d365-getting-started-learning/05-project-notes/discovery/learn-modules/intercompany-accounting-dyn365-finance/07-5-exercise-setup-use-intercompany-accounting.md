<!-- https://learn.microsoft.com/en-us/training/modules/intercompany-accounting-dyn365-finance/5-exercise -->
<!-- refetched: original harvest URL returned 404 -->
# Exercise - Set up and use intercompany accounting

Completed

* 30 minutes

## Scenario

You need to set up and use intercompany accounting between **USP2** and **USMF**. These companies are using the same chart of accounts. You will:

1. Configure intercompany accounting.
2. Use intercompany accounting with general journals.
3. Use audit trails to verify the intercompany accounting posting.

## Configure intercompany accounting

1. Change company to **USP2**.
2. Go to **General ledger > Chart of accounts > Accounts > Main accounts**.
3. Select **New**.
4. In the **Main account** field, enter **100100**.
5. In the **Name** field, enter **Due to USMF**.
6. In the **Main account type** field, select **Balance sheet**.
7. Select **Save**.
8. Select **New**.
9. In the **Main account** field, enter **100101**.
10. In the **Name** field, enter **Due from USMF**.
11. In the **Main account type** field, select **Balance sheet**.
12. Select **Save**.
13. Close the page.
14. Change company to **USMF**.
15. Go to **General ledger > Chart of accounts > Accounts > Main accounts**.
16. Verify the two accounts that you created in the steps 4 and 9 are listed considering that the two companies are sharing the same chart of account.
17. Select **New**.
18. In the **Main account** field, enter **100106**.
19. In the **Name** field, enter **Due to USP2**.
20. In the **Main account type** field, select **Balance sheet**.
21. Select **Save**.
22. Select **New**.
23. In the **Main account** field, enter **100107**.
24. In the **Name** field, enter **Due from USP2**.
25. In the **Main account type** field, select **Balance sheet**.
26. Select **Save**.
27. Close the page.
28. Go to **General ledger > Posting setup > Intercompany accounting**.
29. Select **New**.
30. In the **Originating company** field, select **USMF**.
31. In the **Debit account** field, select **100107 Due from USP2**.
32. In the **Credit account** field, select **100106 Due to USP2**.
33. In the **Destination company** field, select **USP2**.
34. In the **Debit account** field, select **100101 Due from USMF**.
35. In the **Credit account** field, select **100100 Due to USMF**.
36. In the **Journal** field, select **Allocation**.
37. Select **Create reciprocal relationship**.
38. Select **Save**.
39. Close the page.

## Use intercompany accounting with general journals

1. Go to **General ledger > Journal entries > Global general journals**.
2. Select **New journal** to open the drop-down dialog.
3. In the **Company** field, select **USMF**.
4. In the **Name** field, select **GenJrn** (General Journal).
5. Select **OK**.
6. Select the new journal that you just created (00629), and then select **Lines**.
7. In the **Account type** column, select **Bank**.
8. In the **Account** column, specify the values **USMF OPER**.
9. In the **Description** column, enter **Wire**.
10. Set **Credit** to **1000000**.
11. In the **Offset company** field, select **USP2**.
12. In the **Offset account type** field, select account **Ledger**.
13. In the **Offset account** field, select an offset account such as **110110-069-023**.
14. Select **Inquiries** in the Action Pane.
15. Select **Balance control**, and then view the results.
16. Select **Close**.
17. Select **Validate > Validate** in the Action Pane.
18. In the Action Pane select **Post**. In the drop-down of the "Operation completed" information bar, you will see that two vouchers have been posted, one per company.
19. Close the page.

## Use audit trails to verify the intercompany accounting posting

1. In company **USMF**, go to **General ledger > Inquiries and reports > Audit trail**.
2. Select the row with the intercompany transaction you created earlier.
3. Select **Voucher transactions**. Review the intercompany transactions.
4. Select **Related vouchers** to view the intercompany in the destination company. To access this you may need to temporarily reduce the font size in the internet browser: Select the Tools icon and then **Zoom(50%)**.
5. Close the **Related ledger transaction vouchers** page.
6. Switch to **USP2** company.
7. Select **Cancel** in the **Inquiry** page that opens.
8. Go to **General ledger > Inquiries and reports > Audit trail**.
9. Select the row with the intercompany transaction you created earlier.
10. Select **Voucher transactions**. Review the intercompany transactions.
11. Close the **Voucher transactions** page.
12. Close the **Audit trail** page.
13. Go to **Cash and bank management > Bank accounts > Bank accounts**.
14. Select **USP2 OPER**
15. Select **Balance**.
16. Select **OK**.
17. Select **Transactions**.
18. Select **Voucher**.
19. Close all pages.

## Close the lab environment

1. Select the **Next** button in the bottom-right corner of the side bar.
2. Select **Leave** in the pop-up window that appears.