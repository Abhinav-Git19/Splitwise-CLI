from ExpenseFactory import ExpenseFactory
from exceptions import InvalidExpense, SettleUpException


class Splitwise:

    def __init__(self, users):
        self.users = users
        # Each of the expense object will be retrieved by names
        self.expenses = {}

    def addExpense(self, name, added_by_user, splits, total_amount, expensType):

        exp_obj = ExpenseFactory.getExpense(name, added_by_user, splits, total_amount, expensType)

        try:
            if name in self.expenses:
                raise InvalidExpense("Expense Already There! Insert this expense with new name!")
            elif not exp_obj.validate():
                raise InvalidExpense("Total Amount and Splits Do not match! Enter correct set of values")
            exp_obj.recalculate()
        except InvalidExpense as e:
            print(e.message)
            return

        self.expenses[name] = exp_obj

    def showBalances(self):
        for user in self.users:
            print(user.name + " Balance Sheet")
            for key, value in user.balance.balance_sheet.items():
                print(key.name + " : Rs" + str(value))
            print("========")

    def settleUp(self, user1, user2):

        try:
            if user1 not in user2.balance.balance_sheet:
                raise SettleUpException("Nothing to Settle Up here!")
        except SettleUpException as e:
            print(e.message)
            return

        print(user1.name+" settled with "+user2.name+" with Transaction of "+str(user1.balance.getBalance(user2)))

        user1.balance.removeBalance(user2)
        user2.balance.removeBalance(user1)

