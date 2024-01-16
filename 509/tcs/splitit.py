'''
Splitit
Problem Description
Amit is residing in a Paying Guest Accommodation with his friends and has encountered difficulties in tracking their shared expenses as the group's spending increased. To address this challenge, Amit decided to develop a mobile application for group expense management and payment settlement. The application aims to streamline group spending by automating expense tracking, group splits, and keeping records of transactions among friends.

Amit maintains a list of expenses in the following format:

Paid By/Amount/Person1/Person2....... /Person k
For example, A/240/A/B/C indicates that person A spent 240, which is split among individuals A, B, and C.

Settlements and transactions are recorded as:

Paid By/To/Amount (e.g., B/A/80 means B paid A 80).
Lent By/To/L<Amount> (e.g., A/B/L100 indicates A lend B 100).
The objective is to determine the balances at the end, indicating who owes whom and how much.

A rule is established that if a friend fails to repay a loan within a week, a 12% per annum compound interest, calculated weekly, is applied. The loan is considered paid if the transaction amount equals the incurred interest plus principal.

Rules for Settling two types of Transactions are as mentioned below.

Each line of input corresponds to one day. Only one transaction will happen on each day. Hence, if there are N lines in the input overall time over which all transactions are spread is, N days. Use this information to calculate interest on Loan(s)

Expense settlement (Non loan transaction):

No specific rules per se. Assume all expenses are to be borne equally by friends for whom the expenses are made.
Expense settlement can either be full amount or any arbitrary partial amount.
Loan Repayment:

A person can borrow more than once from the same counter party without settling prior loans.
A person can close at most two loans per transaction for a single lender. Loans owed to different lenders cannot be settled in the same transaction.
The loan is said to be paid if the transaction amount is equal to the incurred interest plus principal.
Since interest is calculated on a weekly basis, payment on any weekday will incur the same amount, for example if interest at the end of week 1 is 100 then payment on any day before end of week 2 will require only 100 to be paid. However, at the end of week 2, if the loan is still unpaid a new interest must be paid.
If a transaction amount equals principal plus interest for two or more loans of the same amount, then consider that this transaction is repaying the first loan. For example, A takes 100 loans from B on Day 1 and same amount on Day 2 then in the 7th day the interest plus principal will be same for both then the loan payment will be considered for the first one.
Assume that each person will pay only the full amount for closing the loan. No partial payment of loans is permitted.
A transaction can either be an Expense Settlement or Loan Repayment. These two types of transactions cannot be combined.
Reconciliation Rules

Following rules should be adhered to at reconciliation time:

Assume, A owes 40, B owes 40, C expects to receive 40 and D expects to receive 40, then reconciliation should also be in lexicographical order i.e. A will pay C and B will pay D
Obviously, the above applies only to break ties where amounts are the same. If amounts are unique then reconciliation is straight forward
Reconciliation should include both expense settlement as well as loan repayment amount(s).
Constraints
A person's name ranges from A to Z.

1 <= Amount <= 10^4

1 <= Transaction and Expenses <= 10^4

Input
The first line contains an integer N, representing the number of transactions and expenses.

The next N lines contain the expenses and transactions.

Output
Print who owes whom how much in lexicographical order of the payer. In the format <Payer/ Recipient / Amount> Ignore printing zero balance transactions. If there are no pending dues, print "NO DUES."

Time Limit (secs)
1

Examples
Example 1

Input

3

A/240/A/B/C

B/120/A/C

C/100/C/A

Output

C/A/50

C/B/40

Explanation

On the first day A spends 240 that is shared equally between A, B and C. Then B spends 120 that is shared between equally A and C and finally C spends 100 shared equally between C and A.

So, the final expenditure would be:

A: +50

B: +40

C: -90

Therefore, C will give 50 to A and 40 to B.

Example 2

Input

5

A/240/A/B/C

B/120/A/C

C/A/100

C/B/40

C/100/C/A

Output

A/C/50

Explanation

On the first day of input A spends 240 that is shared equally between A, B and C. On Second day, B spends 120 that is shared equally between A and C. By end of Day 2 C owed a total of 140 (-80 -60) and A had an outstanding of 100 to receive and B had a total of 40 to receive. Then on third and the fourth-day C settled his balance with A and B with amount 100 and 40. On the fifth day C spent 100 that is shared equally between C and A.

Therefore, the final expenditure would be:

A: -50

C: +50

Therefore, A will give C 50.

Example 3

Input

8

C/B/L100

A/240/A/B/C

B/120/A/C

C/A/100

C/100/C/A

B/A/L200

C/B/L300

B/C/100

Output

A/C/250

B/C/60

Explanation

The first day B took a loan of 100 from C and the next two days' expenses are normal spending of 240 and 120 done by A and B which is split between A, B, C and A, C respectively. The 4th day is a normal settlement of 100 done by C to A. On the 5th day C spends 100 which is split between C and A. Then the next two expenses are money lent by B and C to A and B respectively, of the amount of 200 and 300. And finally on the eight-day C pays a settlement of 100 which is the settlement of the money lent by C to B on the 1st day, so he has settled the amount of 100.

After reconciling, it is found that A owed an amount of 40 and amount of 10 to B and C respectively. But there is money that has been lent by B to A and C to B and C. But as a week has not passed by, no interest is incurred upon it.


Therefore, reconciliation will be done after the summation of the pending settlement and the interest. The final reconciliation will be that A will pay an additional 200 to B and B will pay additional 300 to C therefore after settlement the balance will be:

A/C/250

B/C/60
Note: Observe that expense settlement and the loan repayment are handled and reconciled separately.
'''