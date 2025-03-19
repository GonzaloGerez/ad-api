from app.infrastructure.schemas.transaction import TransactionOutput


class MockTransactionService:

    def create_transaction(self, from_user_id:int, to_user_id:int, amount:float):
        transaction = {"id":1, "from_user_id": from_user_id, "to_user_id": to_user_id, "amount": amount}
        return TransactionOutput.model_validate(transaction)