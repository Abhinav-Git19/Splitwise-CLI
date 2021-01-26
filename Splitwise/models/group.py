class Group:

    def __init__(self,id,name,members):
        self.id = id
        self.name = name
        self.members = members

        self.group_balance = {}
        for member_id in self.members:
            self.group_balance[member_id]=0


    @property
    def members(self):
        return self._members

    @members.setter
    def members(self,member_list):
        if len(member_list)==0:
            raise Exception('Invalid Group member needs to atleast one user')
        self._members = member_list
