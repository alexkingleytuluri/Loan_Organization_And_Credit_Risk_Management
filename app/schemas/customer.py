from pydantic import BaseModel, Field, EmailStr

class CustomerCreate(BaseModel):
    full_name: str = Field(..., min_length=3, max_length=100)
    email: EmailStr
    phone: str = Field(..., min_length=10, max_length=15)
    age: int = Field(..., ge=18, le=100)
    monthly_income: float = Field(..., gt=0)

class CustomerUpdate(BaseModel):
    full_name: str = Field(..., min_length=3, max_length=100)
    email: EmailStr
    phone: str = Field(..., min_length=10, max_length=15)
    age: int = Field(..., ge=18, le=100)
    monthly_income: float = Field(..., gt=0)


from pydantic import BaseModel, Field, EmailStr, ConfigDict

class CustomerResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    phone: str
    age: int
    monthly_income: float

    model_config = ConfigDict(from_attributes=True)

class CustomerListResponse(BaseModel):
    total_customers: int
    customers: list[CustomerResponse]