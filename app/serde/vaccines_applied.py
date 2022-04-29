from datetime import datetime
from ..utils import Config
from pydantic import BaseModel
from pydantic.dataclasses import dataclass


@dataclass(config=Config)
class VaccinesAppliedSchema(BaseModel):
    id: int
    vaccine_id: int
    pet_id: int
    applied_on: datetime
    applied_at: str
    proof: str
