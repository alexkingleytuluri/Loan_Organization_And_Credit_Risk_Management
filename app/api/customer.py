from fastapi import APIRouter
from app.schemas.customer import CustomerCreate

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)

# Temporary storage
customers = []

@router.post("/")
def register_customer(customer: CustomerCreate):

    customer_data = customer.model_dump()

    customer_data["id"] = len(customers) + 1

    customers.append(customer_data)

    return {
        "message": "Customer registered successfully",
        "customer": customer_data
    }