from fastapi import HTTPException
from app.domain.repositories.user import UserRepositoryI
from sqlalchemy.orm import Session
from app.domain.models.user import User
from app.infrastructure.handlers.db_ensure_exists import db_ensure_exists
from app.infrastructure.handlers.db_insert_exception import handle_insert_db_exceptions

class UserRepository(UserRepositoryI):

    def __init__(self, db_session: Session):
        self.db = db_session

    @handle_insert_db_exceptions
    def create_user(self, user):
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user.__dict__
    
    @db_ensure_exists
    def get_user(self, user_id):
        return self.db.query(User).filter(User.id == user_id).first()
    
    def update_user(self, user_id, user):
        user_result = self.get_user(user_id)
    
        for key, value in user.items():
            setattr(user_result, key, value)

        self.db.commit()