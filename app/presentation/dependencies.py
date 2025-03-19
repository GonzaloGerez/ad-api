from dependency_injector.wiring import Provide, inject
from fastapi import Depends
from app.core.container import Container
from app.application.services import UserService

def get_user_service(user_service: UserService = Depends(Provide[Container.user_service])):
    return user_service