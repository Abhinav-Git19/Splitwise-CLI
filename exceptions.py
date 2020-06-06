class InvalidExpense(Exception):
    
    def __init__(self,message):
        self.message=message
        super().__init__(message)

class SettleUpException(Exception):

    def __init__(self,message):
        self.message=message
        super().__init__(message)