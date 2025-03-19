from fastapi import HTTPException
from app.domain.entities.user import UserBalanceType
from app.domain.models.user import User
from app.infrastructure.repositories.user import UserRepository
from app.infrastructure.schemas.user import UserBalance, UserOutput

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, name:str, email:str, initialBalance:int)->User:
        user = User(name=name, email=email, balance= initialBalance)
        user_result= self.user_repository.create_user(user)
        return UserOutput.model_validate(user_result)
    
    def get_user_balance(self, user_id:int):
        user= self.user_repository.get_user(user_id)
        user_balance= UserBalanceType(user.balance).__dict__
        return UserBalance.model_validate(user_balance)
    