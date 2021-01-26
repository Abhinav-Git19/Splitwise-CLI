from models.group import Group
from models.user import User
from repository.group_repository import GroupRepository
from repository.user_repository import UserRepository


class UserGroupService:


    user_repository = UserRepository()
    group_repository = GroupRepository()

    def add_user(self,cmdargs):
        cmdlist = cmdargs.split()
        if len(cmdlist)!=3:
            print('Invalid User command')
            return

        id,name = cmdlist[1:]

        if self.user_repository.get_user_by_id(id) is not None:
            print('User already present')
            return

        new_user = User(id,name)

        self.user_repository.add_user(new_user)
        print('User {} added'.format(id))

    def add_group(self, cmdargs):
        cmdlist = cmdargs.split()
        if len(cmdlist) <4:
            print('Invalid Group command')
            return

        group_id, group_name,member_list = cmdlist[1],cmdlist[2],cmdlist[3:]

        if self.group_repository.get_group_by_id(id) is not None:
            print('Group already present')
            return

        for member_id in member_list:
            if self.user_repository.get_user_by_id(member_id) is None:
                print('Member {} not present'.format(member_id))
                return

        try:
            new_group = Group(group_id,group_name,member_list)
        except Exception as e:
            print(str(e))
            return

        self.group_repository.add_group(new_group)
        print('Group {} Added'.format(group_id))




