from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from fastapi import HTTPException
from functools import wraps

def handle_insert_db_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        db = args[0].db 
        try:
            return func(*args, **kwargs)
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=400, detail="Integrity error: Duplicate entry or invalid data")
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    return wrapper
