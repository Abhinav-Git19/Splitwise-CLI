from Splitwise import Splitwise
from models.ExpenseType import ExpenseType
from models.Split import Split
from models.PercentSplit import PercentSplit
from models.User import User


user_list = [User("Abhinav","@asd"),User("Murli","@mur"),User("Krutarth","@kar"),User("Shubham","@Phodenge")]

bookkeeper = Splitwise(user_list)

split_list = [PercentSplit(user_list[1],40),PercentSplit(user_list[2],35),PercentSplit(user_list[3],25)]
split_list2 = [Split(user_list[0],350),Split(user_list[2],150),Split(user_list[3],100)]


bookkeeper.addExpense("Esteem",added_by_user=user_list[0],splits=split_list,total_amount=475,
                      expensType=ExpenseType.PercentBasedExpense)

bookkeeper.showBalances()

print("\n\nNew Expense\n\n")
bookkeeper.addExpense("Salsa",added_by_user=user_list[1],splits=split_list2,total_amount=600,
                      expensType=ExpenseType.AmountBasedExpense)

bookkeeper.showBalances()