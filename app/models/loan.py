
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from app.core.database import Base


class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True, index=True)

    customer_id = Column(
        Integer,
        ForeignKey("customers.id"),
        nullable=False
    )

    loan_amount = Column(Float, nullable=False)
    interest_rate = Column(Float, nullable=False)
    loan_duration = Column(Integer, nullable=False)
    loan_status = Column(String(30), default="Pending")
