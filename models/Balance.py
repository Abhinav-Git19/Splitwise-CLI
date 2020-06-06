class Balance:
    counter = 0
    def __init__(self):
        # This will contain the mapping
        self._balance_sheet={}
        self.id=Balance.counter+1
        Balance.counter+=1

    
    @property
    def balance_sheet(self):
        return self._balance_sheet
    @balance_sheet.setter
    def balance_sheet(self,bs):
        self._balance_sheet=bs


    def getBalance(self,user):
        return self.balance_sheet[user]
    def addBalance(self,user,amt):
        self.balance_sheet[user]=amt

    def updateBalance(self,user,amt):
        self.balance_sheet[user]+=amt
    
    def removeBalance(self,user):
        del self.balance_sheet[user]