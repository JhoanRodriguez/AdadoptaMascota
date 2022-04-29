from datetime import datetime
from ..utils import Config
from pydantic import BaseModel
from pydantic.dataclasses import dataclass


@dataclass(config=Config)
class VaccinesSchema(BaseModel):
    id: int
    name: str
    created_on: datetime
    created_by: int
    modified_on: datetime
    modified_by: int
