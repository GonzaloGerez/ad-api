from pydantic import BaseModel, ConfigDict, field_validator

class TransactionInput(BaseModel):
    from_user_id:int
    to_user_id:int
    amount:float

    model_config= ConfigDict(extra="forbid")

    @field_validator("amount")
    @classmethod
    def validate_amount(cls, value):
        if value <= 0:
            raise ValueError("Amount must be greater than 0")
        return value

class TransactionOutput(BaseModel):
    id:int
    from_user_id:int
    to_user_id:int
    amount:float