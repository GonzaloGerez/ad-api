from sqlalchemy import Column, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.infrastructure.database import Base

class Transaction(Base):
    __tablename__ = "transactions"
    id= Column(Integer, primary_key=True, index=True)
    from_user_id= Column(Integer, ForeignKey('users.id'), nullable=False)
    to_user_id= Column(Integer, ForeignKey('users.id'), nullable=False)
    amount= Column(Float)

    from_user = relationship("User", foreign_keys=[from_user_id], back_populates="transactions_sent")
    to_user = relationship("User", foreign_keys=[to_user_id], back_populates="transactions_received")