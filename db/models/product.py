from .. import Base
from sqlalchemy import Unicode, Integer, Column


class Product(Base):
    __tablename__ ='products'
    id = Column(
        Integer,
        primary_key=True,
    )
    name = Column(
        Unicode,
        unique=True,
    )
