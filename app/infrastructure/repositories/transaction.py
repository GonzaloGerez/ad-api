from app.domain.repositories.transaction import TransactionRepositoryI
from sqlalchemy.orm import Session
from app.domain.models.transaction import Transaction
from app.infrastructure.handlers.db_insert_exception import handle_insert_db_exceptions

class TransactionRepository(TransactionRepositoryI):

    def __init__(self, db_session:Session):
        self.db = db_session

    @handle_insert_db_exceptions
    def create_transaction(self, transaction: Transaction):
        self.db.add(transaction)
        self.db.commit()
        self.db.refresh(transaction)
        return transaction.__dict__