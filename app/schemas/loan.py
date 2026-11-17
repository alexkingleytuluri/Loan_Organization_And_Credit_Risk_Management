from pydantic import BaseModel, Field, ConfigDict


# Loan creation schema
class LoanCreate(BaseModel):
    customer_id: int = Field(..., gt=0)
    loan_amount: float = Field(..., gt=0)
    interest_rate: float = Field(..., ge=0, le=100)
    loan_duration: int = Field(..., gt=0, le=360)


# Loan response schema
class LoanResponse(BaseModel):
    id: int
    customer_id: int
    loan_amount: float
    interest_rate: float
    loan_duration: int
    loan_status: str

    model_config = ConfigDict(from_attributes=True)


# Loan list response schema
class LoanListResponse(BaseModel):
    total_loans: int
    loans: list[LoanResponse]


# Loan registration response schema
class LoanRegistrationResponse(BaseModel):
    message: str
    loan: LoanResponse