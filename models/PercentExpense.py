from models.Expense import Expense
from models.Utils import Utils


class PercentExpense(Expense):

    def __init__(self, name, added_by_user, splits, total_amount):
        super().__init__(name, added_by_user, splits, total_amount)

    def validate(self):
        # In this case splits are in percents should it should sum up to hundred
        temp = 0
        for p in self.splits:
            temp += p.percent

        if not Utils.roundEqual(temp, 100):
            return False

        return True

    def recalculate(self):
        '''
        This function will recalculate exact share of each person and assign the
        required balance
        '''
        for p in self.splits:
            x = self.total_amount * (p.percent / 100)
            y = Utils.precion2places(x)
            p.amount = y

        # Readjust the amounts
        self.readjust()

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

    def readjust(self):
        '''
        Based on percent wise share amount needs to be readjusted to represnet share
        totalling to total_amount
        '''
        delta = self.total_amount - sum([s.amount for s in self.splits])
        # Adjust the remaining amount with first person
        self.splits[0].amount += delta
