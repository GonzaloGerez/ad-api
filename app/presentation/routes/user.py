from fastapi import APIRouter, Depends
from app.application.services.user import UserService
from app.core.container import Container
from dependency_injector.wiring import Provide, inject
from app.infrastructure.schemas.user import UserBalance, UserInput, UserOutput

router = APIRouter()

@router.get("/users/{user_id}/balance", response_model=UserBalance | None)
@inject
def get_user(user_id: int, user_service: UserService = Depends(Provide[Container.user_service])):
    return user_service.get_user_balance(user_id)

@router.post("/users", response_model= UserOutput)
@inject
def create_user(user: UserInput, user_service: UserService = Depends(Provide[Container.user_service])):
    return user_service.create_user(user.name, user.email, user.balance)
