from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import relationship
from app.infrastructure.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    balance= Column(Float)

    transactions_sent = relationship("Transaction", foreign_keys="[Transaction.from_user_id]", back_populates="from_user")
    transactions_received = relationship("Transaction", foreign_keys="[Transaction.to_user_id]", back_populates="to_user")