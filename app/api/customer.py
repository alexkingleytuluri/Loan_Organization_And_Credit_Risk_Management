
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.schemas.customer import CustomerCreate, CustomerUpdate
from app.models.customer import Customer
from app.core.database import get_db

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


# Register customer
@router.post("/")
def register_customer(
    customer: CustomerCreate,
    db: Session = Depends(get_db)
):
    # Check for duplicate email
    existing_customer = db.query(Customer).filter(
        Customer.email == customer.email
    ).first()

    if existing_customer:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    new_customer = Customer(
        full_name=customer.full_name,
        email=customer.email,
        phone=customer.phone,
        age=customer.age,
        monthly_income=customer.monthly_income
    )

    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)

    return {
        "message": "Customer registered successfully",
        "customer": {
            "id": new_customer.id,
            "full_name": new_customer.full_name,
            "email": new_customer.email,
            "phone": new_customer.phone,
            "age": new_customer.age,
            "monthly_income": new_customer.monthly_income
        }
    }


# Get all customers
@router.get("/")
def get_all_customers(db: Session = Depends(get_db)):
    customers = db.query(Customer).all()

    return {
        "total_customers": len(customers),
        "customers": customers
    }


# Get customer by ID
@router.get("/{customer_id}")
def get_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):
    customer = db.query(Customer).filter(
        Customer.id == customer_id
    ).first()

    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return customer


# Update customer
@router.put("/{customer_id}")
def update_customer(
    customer_id: int,
    updated_data: CustomerUpdate,
    db: Session = Depends(get_db)
):
    customer = db.query(Customer).filter(
        Customer.id == customer_id
    ).first()

    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    customer.full_name = updated_data.full_name
    customer.email = updated_data.email
    customer.phone = updated_data.phone
    customer.age = updated_data.age
    customer.monthly_income = updated_data.monthly_income

    db.commit()
    db.refresh(customer)

    return {
        "message": "Customer updated successfully",
        "customer": customer
    }


# Delete customer
@router.delete("/{customer_id}")
def delete_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):
    customer = db.query(Customer).filter(
        Customer.id == customer_id
    ).first()

    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    db.delete(customer)
    db.commit()

    return {
        "message": "Customer deleted successfully"
    }
