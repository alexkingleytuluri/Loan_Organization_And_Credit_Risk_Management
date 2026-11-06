from sqlalchemy import Column, Integer, String, Float
from app.core.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False, index=True)
    phone = Column(String(15), nullable=False)
    age = Column(Integer, nullable=False)
    monthly_income = Column(Float, nullable=False)