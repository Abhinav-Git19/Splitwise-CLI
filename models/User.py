from models.Balance import Balance


class User:
    counter = 0

    def __init__(self, name, email):
        self._name = name
        self._email = email
        self._balance = Balance()
        self.id = User.counter + 1
        User.counter += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        # TODO
        # Name validation (say No longer 10 characrters)
        self._name = name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        # TODO
        # Email validation (Must be a registered email verified by a email service)
        self._email = email

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance
