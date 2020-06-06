from models.ExactExpense import ExactExpense
from models.PercentExpense import PercentExpense
from models.ExpenseType import ExpenseType

class ExpenseFactory:

    @staticmethod
    def getExpense(name,added_by_user,splits,total_amount,expenseType):

        if expenseType is ExpenseType.PercentBasedExpense:
            return PercentExpense(name,added_by_user,splits,total_amount)
        else:
            return ExactExpense(name,added_by_user,splits,total_amount)