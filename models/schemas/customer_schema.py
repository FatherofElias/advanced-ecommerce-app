from pydantic import BaseModel, EmailStr
from typing import Optional

class CustomerSchema(BaseModel):
    id: Optional[int]
    name: str
    email: EmailStr
    phone: Optional[str] = None
