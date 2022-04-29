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


class Vaccines(Base):
    __tablename__ = "vaccines"
    __table_args__ = (TABLE_ARGS,)

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(50), nullable=False)
    created_on = Column(
        DateTime,
        default=datetime.datetime.utcnow(),
        server_default=func.now(),
        nullable=False,
    )
    created_by = Column(Integer, ForeignKey(SCHEMA + "users.id"), nullable=False)
    modified_on = Column(
        DateTime,
        onupdate=datetime.datetime.utcnow(),
        nullable=True,
    )
    modified_by = Column(Integer, ForeignKey(SCHEMA + "users.id"), nullable=True)
