from typing import Optional

from models.bill import Bill


class BillRepository:
    #['desc': BillObj]
    bill_repo = {}
    def add_bill(self, new_bill:Bill):
        self.bill_repo[new_bill.desc]=new_bill

    def get_bill_by_desc(self, desc)-> Optional[Bill]:

        if desc in self.bill_repo:
            return self.bill_repo[desc]
        return None