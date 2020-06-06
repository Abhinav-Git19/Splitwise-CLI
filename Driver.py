from Splitwise import Splitwise
from models.User import User
from models.ExpenseType import ExpenseType
from models.Split import Split
from models.PercentSplit import PercentSplit


def createSplitsList(splits, splitType,userlist):
    split_list = []
    for s in splits:
        s = s.split(':')

        if splitType == 'EXACT':
            splobj = Split(getUserObj(userlist,s[0]), int(s[1]))
        else:
            splobj = PercentSplit(getUserObj(userlist,s[0]), int(s[1]))
        split_list.append(splobj)

    return split_list


def getExpenseType(splitType):
    if splitType == 'EXACT':
        return ExpenseType.AmountBasedExpense
    else:
        return ExpenseType.PercentBasedExpense


def getUserObj(userlist, username):
    for user in userlist:
        if user.name == username:
            return user


def main():

    print('#######################')
    print("!!!!Hi Welcome to Abhinav's Splitwise!!!!")
    print('#######################')

    print("Possible Commands: EXPENSE SHOW SETTLE QUIT")
    print("Command Usage:")
    print("EXPENSE <name> <added_by_user> <splits> <total_amount> <split_type : EXACT or PERCENT>")
    print("e.g- EXPENSE exp1 u1 u2:30 u4:40 70 exact")
    print("SHOW")
    print("SETTLE <user1> <user2>")
    print("QUIT")

    # For now we are starting with fixed set of users, the code can be easily extended to include variable number of
    # users
    user_list = [User('u1', 'u1@sp.com'), User('u2', 'u2@sp.com'), User('u3', 'u3@sp.com'), User('u4', 'u4@sp.com')]
    bookkeeper = Splitwise(user_list)
    while True:
        command = input("Enter Command\n")
        command = command.split()

        if command[0] == 'EXPENSE':
            name = command[1]
            added_by_user = getUserObj(user_list, command[2])
            splits = createSplitsList(command[3:-2], command[-1],user_list)
            total_amt = int(command[-2])
            expenseType = getExpenseType(command[-1])
            bookkeeper.addExpense(name,added_by_user,splits,total_amt,expenseType)

        elif command[0] == 'SHOW':
            bookkeeper.showBalances()
        elif command[0] == 'SETTLE':
            user1 = getUserObj(user_list,command[1])
            user2 = getUserObj(user_list,command[2])
            bookkeeper.settleUp(user1,user2)
        elif command[0] =='QUIT':
            print("TataBye!!")
            break
        else:
            print("Unknown Command! Try again")

main()


