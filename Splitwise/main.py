from services.user_group_service import UserGroupService
from services.bill_service import BillService

def main():
    user_grp_service = UserGroupService()
    bill_service = BillService()


    user_grp_service.add_user('add_user person1@email.com person1')
    user_grp_service.add_user('add_user person2@email.com person2')

    user_grp_service.add_group('add_group group1 group1_name person1@email.com person2@email.com ')
    user_grp_service.add_group('add_group group2 group2_name person1@email.com person2@email.com ')


    bill_dict1 ={
        'desc':'Bill1',
        'totalAmount':100,
        'groupId': 'group1',
        'contribution':[
            {'person':'person1@email.com',
             'share':50
             },
            {'person': 'person2@email.com',
             'share': 50
             }
        ],
        'paidBy':[
            {'person': 'person1@email.com',
             'share': 100
             }
        ]

    }

    bill_dict2 = {
        'desc': 'Bill2',
        'totalAmount': 300,
        'groupId': 'group2',
        'contribution': [
            {'person': 'person1@email.com',
             'share': 170
             },
            {'person': 'person2@email.com',
             'share': 130
             }
        ],
        'paidBy': [
            {'person': 'person2@email.com',
             'share': 300
             }
        ]

    }

    bill_service.add_bill(bill_dict1)
    bill_service.add_bill(bill_dict2)

    bill_service.show_group_balance()
    bill_service.show_all_person_balance()

if __name__ == '__main__':
    main()