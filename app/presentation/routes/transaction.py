from fastapi import APIRouter, Depends
from app.application.services.transaction import TransactionService
from app.core.container import Container
from dependency_injector.wiring import Provide, inject
from app.infrastructure.schemas.transaction import TransactionInput

router = APIRouter()

@router.post("/transactions")
@inject
def create_transaction(transaction:TransactionInput, transaction_service: TransactionService = Depends(Provide[Container.transaction_service])):
    return transaction_service.create_transaction(transaction.from_user_id, transaction.to_user_id, transaction.amount)