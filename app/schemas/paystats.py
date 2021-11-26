from pydantic import BaseModel
from datetime import date
#from bson import ObjectId

class PayStatsSchema(BaseModel):
    amount: float
    p_month: date
    p_age: str
    p_gender: str
    postal_code_id: str
    id: str