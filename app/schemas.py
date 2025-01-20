# app/schemas.py

from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime, date


class PaymentSchema(BaseModel):
    payee_first_name: str
    payee_last_name: str
    payee_payment_status: str
    payee_added_date_utc: datetime
    payee_due_date: date
    payee_address_line_1: str
    payee_address_line_2: Optional[str] = None
    payee_city: str
    payee_country: str
    payee_province_or_state: Optional[str] = None
    payee_postal_code: str
    payee_phone_number: str
    payee_email: EmailStr
    currency: str
    discount_percent: Optional[float] = 0.0
    tax_percent: Optional[float] = 0.0
    due_amount: float
    total_due: float


class UpdatePaymentSchema(BaseModel):
    payee_payment_status: Optional[str] = None
    payee_due_date: Optional[date] = None
    due_amount: Optional[float] = None
