from typing import Optional, List

from models.group import Group


class GroupRepository:

    # {id:GroupObj}
    group_repo = {}

    def get_group_by_id(self, id) -> Optional[Group]:
        if id in self.group_repo:
            return self.group_repo[id]
        return None

    def add_group(self, new_group : Group):
        self.group_repo[new_group.id]=new_group

    def get_all_groups(self) -> List[Group]:
        return list(self.group_repo.values())

