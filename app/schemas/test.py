from pydantic import BaseModel
from bson import ObjectId

class Test(BaseModel):
    test: bool