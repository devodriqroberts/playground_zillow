from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from scrapy.utils.project import get_project_settings

Base = declarative_base()

def db_connect():
    """
    Performs DB connection using database settings from settings.py.
    Returns sqlalchemy engine.
    """
    return create_engine(get_project_settings().get("DB_CONNECTION_STRING"))

def create_table(engine):
    Base.metadata.create_all(engine)

class House(Base):
    __tablename__ = "house"

    id = Column(Integer, primary_key=True)
    houseId = Column("houseId", Integer(), unique=True)
    address = Column("address", String(50))
    addressCity = Column("addressCity", String(50))
    addressState = Column("addressState", String(50))
    addressStreet = Column("addressStreet", String(50))
    addressZipcode = Column("addressZipcode", Integer())
    baths = Column("baths", Float())
    beds = Column("beds", Integer())
    detailUrl = Column("detailUrl", Text())
    homeStatus = Column("homeStatus", String(50))
    homeType = Column("homeType", String(50))
    imgSrc = Column("imgSrc", Text())
    isZillowOwned = Column("isZillowOwned", String(50))
    latitude = Column("latitude", Float())
    longitude = Column("longitude", Float())
    lotAreaUnit = Column("lotAreaUnit", String(50), nullable=True)
    lotAreaValue = Column("lotAreaValue", Float(), nullable=True)
    price = Column("price", Integer())
    rentZestimate = Column("rentZestimate", Integer(), nullable=True)
    sgapt = Column("sgapt", String(50))

