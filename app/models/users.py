import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    func,
)

from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
from ..database import Base
from app.models import SCHEMA, TABLE_ARGS


class Users(Base):
    __tablename__ = "users"
    __table_args__ = (TABLE_ARGS,)

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    _password = Column(String(100), nullable=False)
    email = Column(String(50), nullable=False)
    cellphone = Column(String(20), nullable=True)
    city = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)
    company_id = Column(Integer, ForeignKey(SCHEMA + "company.id"), nullable=False)
    created_on = Column(
        DateTime,
        default=datetime.datetime.utcnow(),
        server_default=func.now(),
        nullable=False,
    )
    modified_on = Column(
        DateTime,
        onupdate=datetime.datetime.utcnow(),
        nullable=True,
    )
    modified_by = Column(
        Integer, ForeignKey(SCHEMA + "users.id"), nullable=True, ondelete="CASCADE"
    )

    # Relationships
    pets = relationship("Pets")
    company = relationship("Company")

    @property
    def password(self):
        """
        Reading ther plaintext password value is not possible or allowed.
        """
        raise AttributeError("cannot read password")

    @password.setter
    def password(self, password):
        """
        Intercept writes to the `password` attribue and hash the given password value.
        """
        self._password = generate_password_hash(password)

    def verify_password(self, password):
        """
        Accept a password and hash the value while comparing the hashed
        value to the password hash contained in the database.
        """
        return check_password_hash(self._password, password)
