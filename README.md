# Splitwise Command Line App

### Mininmum Viable Solution

- Develop a solution for sharing expenses
- User can create an expense with another User and share the expense based on: Percentage share
- Exact amount of share
- User should be able to view pending balances with other users
- User should be able to record a payment settlement to clear balances with a user.

### Usage
````
abhinavsingh@Abhinavs-MacBook-Air:~/Desktop/Splitwise$ python Driver.py 
#######################
!!!!Hi Welcome to Abhinav's Splitwise!!!!
#######################
Possible Commands: EXPENSE SHOW SETTLE QUIT
Command Usage:
EXPENSE <name> <added_by_user> <splits> <total_amount> <split_type : EXACT or PERCENT>
e.g- EXPENSE exp1 u1 u2:30 u4:40 70 exact
SHOW
SETTLE <user1> <user2>
QUIT

````
### Extensible Ideas
- Variable Users
- User can be added/removed from Expense
- Group creation
- Simplify Debts