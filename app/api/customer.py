from fastapi import APIRouter , HTTPException
from app.schemas.customer import CustomerCreate , CustomerUpdate

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

# Get all customers
@router.get("/")
def get_all_customers():

    return {
        "total_customers": len(customers),
        "customers": customers
    }

# Get customer by ID
@router.get("/{customer_id}")
def get_customer(customer_id: int):

    for customer in customers:
        if customer["id"] == customer_id:
            return customer

    raise HTTPException(
        status_code=404,
        detail="Customer not found"
    )

# Update customer
@router.put("/{customer_id}")
def update_customer(customer_id: int, updated_data: CustomerUpdate):

    for customer in customers:
        if customer["id"] == customer_id:

            customer.update(updated_data.model_dump())

            return {
                "message": "Customer updated successfully",
                "customer": customer
            }

    raise HTTPException(
        status_code=404,
        detail="Customer not found"
    )

    # Delete customer
@router.delete("/{customer_id}")
def delete_customer(customer_id: int):

    for customer in customers:
        if customer["id"] == customer_id:

            customers.remove(customer)

            return {
                "message": "Customer deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Customer not found"
    )