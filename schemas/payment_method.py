from pydantic import BaseModel


class PaymentMethod(BaseModel):
    id: int
    name: str
    network: str
    address: str
    currency: str
    api_key: str
    is_active: int
    