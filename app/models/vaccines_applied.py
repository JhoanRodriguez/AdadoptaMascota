import datetime
import enum

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    func,
)

from sqlalchemy.orm import relationship
from ..database import Base
from app.models import SCHEMA, TABLE_ARGS


class VaccinesApplied(Base):
    __tablename__ = "vaccines_applied"
    __table_args__ = (TABLE_ARGS,)

    id = Column(Integer, nullable=False, primary_key=True)
    vaccine_id = Column(Integer, ForeignKey(SCHEMA + "vaccines.id"), nullable=False)
    pet_id = Column(Integer, ForeignKey(SCHEMA + "pets.id"), nullable=False)
    applied_on = Column(
        DateTime,
        default=datetime.datetime.utcnow(),
        server_default=func.now(),
        nullable=False,
    )
    applied_at = Column(String(50), nullable=False)
    proof = Column(String(250), nullale=False)
