from fastapi import FastAPI
from app.presentation.routes.user import router as userRoutes
from app.presentation.routes.transaction import router as transactionRoutes
from app.core.container import Container


app = FastAPI()
container = Container()
container.wire(modules=["app.presentation.routes.user", "app.presentation.routes.transaction"])
app.include_router(userRoutes, prefix="/api", tags=["users"])
app.include_router(transactionRoutes, prefix="/api", tags=["transactions"])