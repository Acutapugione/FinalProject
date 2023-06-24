from .. import Base
from sqlalchemy import Unicode, Integer, Column


class Country(Base):
    __tablename__ ='countries'
    id = Column(
        Integer,
        primary_key=True,
    )
    name = Column(
        Unicode,
        unique=True,
    )
