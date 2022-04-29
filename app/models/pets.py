import datetime
import enum

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    Enum,
    Boolean,
    func,
)
from sqlalchemy.orm import relationship
from ..database import Base
from app.models import SCHEMA, TABLE_ARGS


class PetSizeEnum(enum.Enum):
    SMALL = "Pequeño"
    MEDIUM = "Mediano"
    BIG = "Grande"


class PetKindEnum(enum.Enum):
    CAT = "Gato"
    DOG = "Perro"


class PetSexEnum(enum.Enum):
    MALE = "Macho"
    FEMALE = "Hembra"


class Pets(Base):
    __tablename__ = "pets"
    __table_args__ = (TABLE_ARGS,)

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(50), nullable=True)
    age = Column(Integer, nullable=True)
    size = Column(Enum(PetSizeEnum), nullable=False)
    kind = Column(Enum(PetKindEnum), nullable=False)
    sex = Column(Enum(PetSexEnum), nullable=False)
    sterilized = Column(Boolean, nullable=False, default=False)
    description = Column(String(280), nullale=False)
    picture = Column(String(250), nullale=False)
    responsable = Column(Integer, ForeignKey(SCHEMA + "users.id"), nullable=False)
    adopted = Column(Boolean, nullable=False, default=False)
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

    # Relationships
    user = relationship("User", back_populates="Pets")
    vaccines_applied = relationship("VaccinesApplied")
