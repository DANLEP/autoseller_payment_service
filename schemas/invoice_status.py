from pydantic import BaseModel
from pydantic.fields import Optional


class InvoiceStatus(BaseModel):
    id: Optional[int]
    name: str
