from typing import Optional, List

from models.user import User


class UserRepository:
    # {id:UserObj}
    user_repo = {}

    def get_user_by_id(self, id) -> Optional[User]:
        if id in self.user_repo:
            return self.user_repo[id]
        return None

    def add_user(self, new_user : User):
        self.user_repo[new_user.id] = new_user

    def get_all_users(self) -> List[User]:
        return list(self.user_repo.values())