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
    houseId = Column("house_id", Integer(), unique=True)
    address = Column("address", String(50))
    addressCity = Column("address_city", String(50))
    addressState = Column("address_state", String(50))
    addressStreet = Column("address_street", String(50))
    addressZipcode = Column("address_zipcode", Integer())
    baths = Column("baths", Float())
    beds = Column("beds", Integer())
    detailUrl = Column("detail_url", Text())
    homeStatus = Column("home_status", String(50))
    homeType = Column("home_type", String(50))
    imgSrc = Column("img_src", Text())
    isZillowOwned = Column("is_zillow_owned", String(50))
    latitude = Column("latitude", Float())
    longitude = Column("longitude", Float())
    lotAreaUnit = Column("lot_area_unit", String(50), nullable=True)
    lotAreaValue = Column("lot_area_value", Float(), nullable=True)
    price = Column("price", Integer())
    rentZestimate = Column("rent_zestimate", Integer(), nullable=True)
    sgapt = Column("sgapt", String(50))

