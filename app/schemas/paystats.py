from pydantic import BaseModel
from datetime import date

# from bson import ObjectId


class PaystatsSchema(BaseModel):
    amount: float
    p_month: date
    p_age: str
    p_gender: str
    postal_code_id: int
    id: int


class TotalAmountByPostalCodeSchema(BaseModel):
    postal_code_id: int
    total_amount: float
