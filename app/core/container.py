from dependency_injector import containers, providers
from app.infrastructure.database import SessionLocal
from app.infrastructure.repositories.user import UserRepository
from app.application.services.user import UserService
from app.application.services.transaction import TransactionService
from app.infrastructure.repositories.transaction import TransactionRepository

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["app.presentation.routes.user", "app.presentation.routes.transaction"])
    
    db_session = providers.Factory(SessionLocal)
    user_repository = providers.Factory(UserRepository, db_session=db_session)
    user_service = providers.Factory(UserService, user_repository=user_repository)
    transaction_repository = providers.Factory(TransactionRepository, db_session=db_session)
    transaction_service= providers.Factory(TransactionService, transaction_repository= transaction_repository, user_repository=user_repository)