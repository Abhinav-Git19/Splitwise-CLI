from abc import ABC, abstractmethod


class Expense(ABC):
    counter = 0

    def __init__(self, name, added_by_user, splits, total_amount):
        self._name = name
        self._added_by_user = added_by_user
        self._total_amount = total_amount
        self._splits = splits
        self.id = Expense.counter + 1
        Expense.counter += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def added_by_user(self):
        return self._added_by_user

    @added_by_user.setter
    def added_by_user(self, user):
        self._added_by_user = user

    @property
    def splits(self):
        return self._splits

    @splits.setter
    def splits(self, splits):
        self._splits = splits

    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, amt):
        self._total_amount = amt

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def recalculate(self):
        pass
