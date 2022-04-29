from datetime import datetime
from ..utils import Config
from pydantic import BaseModel, EmailStr
from pydantic.dataclasses import dataclass
from typing import Optional
from ..models.pets import Pets
from ..models.users import Users


@dataclass(config=Config)
class CompanySchema(BaseModel):
    id: int
    name: str
    nit: str
    email: EmailStr
    cellphone: str
    city: str
    country: str
    address: str
    created_on: datetime
    created_by: int
    modified_on: datetime
    modified_by: int

    # Relationships
    pets: Optional[list[Pets]] = None
    company: Optional[list[Users]] = None
