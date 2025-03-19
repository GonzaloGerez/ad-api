from pydantic import BaseModel, ConfigDict, EmailStr, field_validator

class UserInput(BaseModel):
    name:str
    email: EmailStr
    balance: float

    model_config= ConfigDict(extra="forbid")

    @field_validator("balance")
    @classmethod
    def validate_balance(cls, value):
        if value <= 0:
            raise ValueError("Balance must be greater than 0")
        return value

class UserOutput(BaseModel):
    id:int
    name:str
    email:str
    balance:float

class UserBalance(BaseModel):
    balance:float