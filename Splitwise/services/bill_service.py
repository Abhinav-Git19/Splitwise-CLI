from typing import Tuple, List

from models.bill import Bill
from models.user import User
from repository.bill_repository import BillRepository
from repository.group_repository import GroupRepository
from repository.user_repository import UserRepository





class BillService:

    user_repository = UserRepository()
    group_repository = GroupRepository()

    bill_repository = BillRepository()

    def validate_bill_structure(self,input_dict):

        if 'desc' not in input_dict or 'totalAmount' not in input_dict:
            return False
        if 'groupId' not in input_dict:
            return False
        if 'contribution' not in input_dict or 'paidBy' not in input_dict:
            return False

        return True


    def calculate_share(self,group,contributors: List[Tuple[User,int]],paidBy: List[Tuple[User,int]]):


        for cont_user in contributors:
            user = cont_user[0]
            share = cont_user[1]

            group.group_balance[user.id]-=share

            user.total_amount_owed-=share


        for paid_user in paidBy:

            user = paid_user[0]

            share = paid_user[1]

            group.group_balance[user.id]+=share
            user.total_amount_owed+=share






    def add_bill(self,input_dict):

        if not self.validate_bill_structure(input_dict):
            print('Invalid Bill Structure')
            return


        if self.bill_repository.get_bill_by_desc(input_dict['desc']) is not None:
            print('Bill already present')
            return

        # Interger
        if input_dict['totalAmount']<=0:
            print('Invalid Total Amount')
            return

        group=self.group_repository.get_group_by_id(input_dict['groupId'])
        if group is None:
            print('Group not present')
            return

        contributor_list = input_dict['contribution']
        paid_by_list = input_dict['paidBy']

        cont_user_obj_list =[]
        share_value =0
        for contributor in contributor_list:
            try:
                user = self.user_repository.get_user_by_id(contributor['person'])
                share = contributor['share']
                if share<0:
                    raise('Negative Share not allowed')
            except Exception as e:
                print(str(e))
                return
            if user is None:
                print('User not present')
                return
            share_value+=share
            cont_user_obj_list.append((user,share))

        if share_value!=input_dict['totalAmount']:
            print('Contributor total amount does not match!')
            return

        paid_user_obj_list =[]
        share_value = 0
        for paidBy_user in paid_by_list:
            try:
                user = self.user_repository.get_user_by_id(paidBy_user['person'])
                share = paidBy_user['share']
                if share<0:
                    raise('Negative Share not allowed')
            except Exception as e:
                print(str(e))
                return
            if user is None:
                print('User not present')
                return
            share_value += share
            paid_user_obj_list.append((user,share))

        if share_value!=input_dict['totalAmount']:
            print('PaidBy amount does not match!')
            return

        self.calculate_share(group,cont_user_obj_list,paid_user_obj_list)


        desc = input_dict['desc']
        total_amount = input_dict['totalAmount']
        group_id = input_dict['groupId']
        contribution = input_dict['contribution']
        paidBy = input_dict['paidBy']
        new_bill = Bill(desc,total_amount,group_id,contribution,paidBy)
        self.bill_repository.add_bill(new_bill)
        print('Bill added')


    def show_group_balance(self):

        all_groups = self.group_repository.get_all_groups()

        for group in all_groups:
            print(group.group_balance)
            print('======')

    def show_all_person_balance(self):
        all_users = self.user_repository.get_all_users()
        for user in all_users:
            print('User {}: total balance {}'.format(user.name,user.total_amount_owed))






