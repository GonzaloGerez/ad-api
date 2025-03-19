from abc import ABC, abstractmethod
from app.domain.models.transaction import Transaction

class TransactionRepositoryI(ABC):
    
    @abstractmethod
    def create_transaction():
        pass