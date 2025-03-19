from functools import wraps
from fastapi import HTTPException

def db_ensure_exists(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result is None:
            raise HTTPException(status_code=404, detail="Resource not found")
        return result
    return wrapper
