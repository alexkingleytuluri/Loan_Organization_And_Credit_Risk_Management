
from fastapi import FastAPI

# Create the FastAPI application
app = FastAPI(
    title="Loan Organization and Credit Risk Management",
    description="A loan management system with ML-based credit risk assessment",
    version="1.0.0"
)

# Welcome endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to Loan Organization and Credit Risk Management System",
        "status": "Backend is running successfully"
    }

# Health check endpoint
@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
