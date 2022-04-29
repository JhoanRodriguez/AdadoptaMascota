from datetime import datetime
from ..utils import Config
from pydantic import BaseModel, EmailStr
from pydantic.dataclasses import dataclass
from typing import Optional
from ..models.pets import Pets
from ..models.company import Company


@dataclass(config=Config)
class UsersSchema(BaseModel):
    id: int
    name: str
    last_name: str
    email: EmailStr
    cellphone: str
    city: str
    country: str
    company_id: int
    created_on: datetime
    modified_on: datetime
    modified_by: int

    # Relationships
    pets: Optional[list[Pets]] = None
    company: Optional[Company] = None
