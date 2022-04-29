from datetime import datetime
from ..utils import Config
from app.models.pets import PetKindEnum, PetSizeEnum, PetSexEnum
from pydantic import BaseModel
from pydantic.dataclasses import dataclass
from typing import Optional
from ..models.users import Users
from ..models.vaccines_applied import VaccinesApplied


@dataclass(config=Config)
class PetsSchema(BaseModel):
    id: int
    name: str
    age: int
    size: PetSizeEnum
    kind: PetKindEnum
    sex: PetSexEnum
    sterilized: bool
    description: str
    picture: str
    responsable: int
    adopted: bool
    created_on: datetime
    created_by: int
    modified_on: datetime
    modified_by: int

    # Relationships
    user: Optional[Users] = None
    vaccines_applied = Optional[list[VaccinesApplied]] = None
