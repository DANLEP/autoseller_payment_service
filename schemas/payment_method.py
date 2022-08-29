from pydantic import BaseModel
from pydantic.fields import Optional, Field


class PaymentMethod(BaseModel):
    id: Optional[int]
    name: str
    network: str
    address: str
    currency: str
    api_key: str
    is_active: int
    