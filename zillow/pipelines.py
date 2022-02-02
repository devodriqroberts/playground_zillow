# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from typing import final
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
from asyncio.log import logger
from sqlalchemy.orm.session import sessionmaker
from .models import *
from scrapy.exceptions import DropItem


class ZillowImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        urls = ItemAdapter(item).get(self.images_urls_field, [])
        return [Request(u, meta={'houseId': item.get('id')}) for u in urls]


    def file_path(self, request, response=None, info=None, *, item=None):
        image_name = request.meta["houseId"]
        return f'full/{image_name}.jpg'


class SaveZillowHousePipeline(object):
    def __init__(self) -> None:
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(engine)

    def process_item(self, item, spider):
        session = self.Session()
        house = House()

        house.houseId = item["houseId"]
        house.address = item["address"]
        house.addressCity = item["addressCity"]
        house.addressState = item["addressState"]
        house.addressStreet = item["addressStreet"]
        house.addressZipcode = item["addressZipcode"]
        house.baths = item["baths"]
        house.beds = item["beds"]
        house.detailUrl = item["detailUrl"]
        house.homeStatus = item["homeStatus"]
        house.homeType = item["homeType"]
        house.imgSrc = item["imgSrc"]
        house.isZillowOwned = item["isZillowOwned"]
        house.latitude = item["latitude"]
        house.longitude = item["longitude"]
        house.lotAreaUnit = item["lotAreaUnit"]
        house.lotAreaValue = item["lotAreaValue"]
        house.price = item["price"]
        house.rentZestimate = item["rentZestimate"]
        house.sgapt = item["sgapt"]


        try:
            existing_house = session.query(House).filter_by(houseId = house.houseId).first()
            if existing_house is None:
                session.add(house)
                session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item


class DuplicatesPipeline(object):
    def __init__(self) -> None:
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(engine)
        logger.info("****** Duplicates Pipeline: Connected to database. *****")

    def process_item(self, item, spider):
        session = self.Session()
        existing_house = session.query(House).filter_by(houseId= item["houseId"]).first()
        session.close()

        if existing_house is not None:
            raise DropItem("Duplicate Found: %s" % item["houseId"])
        else:
            return item

