# app/routes.py

from fastapi import APIRouter, HTTPException
from app.models import (
    fetch_payments,
    create_payment,
    update_payment,
    delete_payment
)
from app.schemas import PaymentSchema, UpdatePaymentSchema

router = APIRouter()


@router.get("/payments")
async def get_payments():
    payments = fetch_payments()
    if not payments:
        raise HTTPException(status_code=404, detail="No payments found")
    return {"payments": payments}


@router.post("/payments")
async def add_payment(payment: PaymentSchema):
    payment_id = create_payment(payment.dict())
    return {"payment_id": payment_id}


@router.put("/payments/{payment_id}")
async def modify_payment(payment_id: str, updates: UpdatePaymentSchema):
    if not update_payment(payment_id, updates.dict(exclude_unset=True)):
        raise HTTPException(
            status_code=404, detail="Payment not found or not updated"
        )
    return {"message": "Payment updated successfully"}


@router.delete("/payments/{payment_id}")
async def remove_payment(payment_id: str):
    if not delete_payment(payment_id):
        raise HTTPException(status_code=404, detail="Payment not found")
    return {"message": "Payment deleted successfully"}
