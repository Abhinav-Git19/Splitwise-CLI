from models.Split import Split


class PercentSplit(Split):

    def __init__(self, user, percent):
        super().__init__(user, 0)
        self._percent = percent

    @property
    def percent(self):
        return self._percent

    @percent.setter
    def percent(self, percent):
        self._percent = percent
