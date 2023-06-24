from .base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine("postgresql+psycopg2://acuta:acuta@localhost/internet_shop", echo=True)   
session = Session(engine)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

from .models import Country, Product, User

