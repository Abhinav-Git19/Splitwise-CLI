class Bill:

    def __init__(self,desc,total_amount,group_id,contribution,paidBy):
        self.desc = desc
        self.total_amount = total_amount
        self.group_id =group_id
        self.contribution = contribution
        self.paidBy = paidBy
        # Getter and setters not added in the intrest of time..But wherever validaiton is needed, I have added them
        # E.g in Group class
