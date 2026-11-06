from fastapi import FastAPI

from app.api.customer import router as customer_router
from app.core.database import engine, Base
from app.models import customer

app = FastAPI(
    title="Loan Organization and Credit Risk Management",
    description="A loan management system with ML-based credit risk assessment",
    version="1.0.0"
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Connect customer API
app.include_router(customer_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Loan Organization and Credit Risk Management System",
        "status": "Backend is running successfully"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }