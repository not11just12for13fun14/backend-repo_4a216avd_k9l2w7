from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class Contact(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    message: str = Field(..., min_length=5, max_length=5000)
    company: Optional[str] = None
    subject: Optional[str] = None

    # timestamps will be injected by create_document helper
