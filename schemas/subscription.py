from pydantic import BaseModel
from pydantic.fields import Optional


class Subscription(BaseModel):
    id: Optional[int]
    name: str
    days: int
    price: float
