from abc import ABC, abstractmethod
from app.domain.models.user import User

class UserRepositoryI(ABC):

    @abstractmethod
    def create_user(self, user: User):
        pass

    def get_user_balance(self, user_id: int)->int:
        pass

    def update_user(self,user_id, user: dict):
        pass
    