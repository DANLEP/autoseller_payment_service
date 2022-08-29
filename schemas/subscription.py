from pydantic import BaseModel, Field
from pydantic.fields import Optional


class Subscription(BaseModel):
    id: Optional[int]
    name: str
    days: int
    price: float
