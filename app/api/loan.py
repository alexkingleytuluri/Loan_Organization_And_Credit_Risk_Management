from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.loan import Loan
from app.models.customer import Customer
from app.schemas.loan import (
    LoanCreate,
    LoanResponse,
    LoanListResponse,
    LoanRegistrationResponse
)

router = APIRouter(
    prefix="/loans",
    tags=["Loans"]
)


# Apply for a loan
@router.post("/")
def apply_for_loan(
    loan_data: LoanCreate,
    db: Session = Depends(get_db)
):
    # Check whether the customer exists
    customer = db.query(Customer).filter(
        Customer.id == loan_data.customer_id
    ).first()

    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    # Create a new loan application
    new_loan = Loan(
        customer_id=loan_data.customer_id,
        loan_amount=loan_data.loan_amount,
        interest_rate=loan_data.interest_rate,
        loan_duration=loan_data.loan_duration,
        loan_status="Pending"
    )

    db.add(new_loan)
    db.commit()
    db.refresh(new_loan)

    return {
        "message": "Loan application submitted successfully",
        "loan": {
            "id": new_loan.id,
            "customer_id": new_loan.customer_id,
            "loan_amount": new_loan.loan_amount,
            "interest_rate": new_loan.interest_rate,
            "loan_duration": new_loan.loan_duration,
            "loan_status": new_loan.loan_status
        }
    }

    # Get all loan applications
@router.get("/")
def get_all_loans(db: Session = Depends(get_db)):
    loans = db.query(Loan).all()

    return {
        "total_loans": len(loans),
        "loans": loans
    }

# Get loan by ID
@router.get("/{loan_id}")
def get_loan(loan_id: int, db: Session = Depends(get_db)):
    loan = db.query(Loan).filter(
        Loan.id == loan_id
    ).first()

    if loan is None:
        raise HTTPException(
            status_code=404,
            detail="Loan not found"
        )

    return loan