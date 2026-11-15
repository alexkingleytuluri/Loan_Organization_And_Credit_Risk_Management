
from pydantic import BaseModel, Field


class LoanCreate(BaseModel):
    customer_id: int = Field(..., gt=0)
    loan_amount: float = Field(..., gt=0)
    interest_rate: float = Field(..., ge=0, le=100)
    loan_duration: int = Field(..., gt=0, le=360)
