from .. import Base
from sqlalchemy import Unicode, Integer, Column, ForeignKey


class User(Base):
    __tablename__ ='users'
    
    id = Column(
        Integer,
        primary_key=True,
    )
    name = Column(
        Unicode,
        unique=True,
    )
    country_id = Column(
        Integer,
        ForeignKey("countries.id", ondelete="CASCADE"),
    )
