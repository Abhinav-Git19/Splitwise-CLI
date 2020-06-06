from models.Expense import Expense
from models.Utils import Utils


class ExactExpense(Expense):

    def __init__(self, name, added_by_user, splits, total_amount):
        super().__init__(name, added_by_user, splits, total_amount)

    def validate(self):

        x = sum([s.amount for s in self.splits])

        if Utils.roundEqual(x, self.total_amount):
            return True
        return False

    def recalculate(self):
        '''
        Update the balances or create new ones if needed
        '''
        for s in self.splits:
            # Update balance from paying user to split users
            if s.user not in self.added_by_user.balance.balance_sheet:
                self.added_by_user.balance.addBalance(s.user, s.amount)
            else:
                self.added_by_user.balance.updateBalance(s.user, s.amount)

            # Update balance in negative from split user to paying user
            if self.added_by_user not in s.user.balance.balance_sheet:
                s.user.balance.addBalance(self.added_by_user, -s.amount)
            else:
                s.user.balance.updateBalance(self.added_by_user, -s.amount)

