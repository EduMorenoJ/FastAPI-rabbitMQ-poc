from app.schemas.paystats import PayStatsSchema


class PayStats:
    def __init__(self, data:PayStatsSchema):
        self.model:PayStatsSchema = data
    
    def __eq__(self, __o: object) -> bool:
        self.model.amount == __o.amount