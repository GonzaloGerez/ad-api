from app.domain.models.user import User
from app.infrastructure.schemas.user import UserBalance, UserOutput


class MockUserService:
    def create_user(self, name:str, email:str, initialBalance:int)->User:
        user = {"id":2, "name": name, "email":email, "balance": initialBalance}
        return UserOutput.model_validate(user)
    
    def get_user_balance(self, user_id:int):
        return UserBalance.model_validate({"balance": 250000})