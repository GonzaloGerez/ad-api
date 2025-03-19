from fastapi import HTTPException
from app.domain.models.transaction import Transaction
from app.infrastructure.repositories.transaction import TransactionRepository
from app.infrastructure.repositories.user import UserRepository

class TransactionService:
    def __init__(
            self,
            transaction_repository: TransactionRepository,
            user_repository: UserRepository
        ):
        self.transaction_repository = transaction_repository
        self.user_repository = user_repository

    def create_transaction(self, from_user_id:int, to_user_id:int, amount: float):
        from_user= self.user_repository.get_user(from_user_id)
        to_user= self.user_repository.get_user(to_user_id)
        
        if from_user.balance < amount:
            raise HTTPException(detail="User insufficient balance", status_code=400)
        
        from_user.balance -= amount
        to_user.balance += amount

        self.user_repository.update_user(from_user.id, from_user.__dict__)
        self.user_repository.update_user(to_user.id, to_user.__dict__)
        
        transaction = Transaction(from_user_id= from_user_id, to_user_id= to_user_id, amount=amount)
        return self.transaction_repository.create_transaction(transaction)