import json
import scrapy
from itemloaders import ItemLoader
from ..utils import URL, parse_cookies, parse_new_url
from ..items import ZillowItem
from scrapy.utils.project import get_project_settings



class HousesSpider(scrapy.Spider):
    name = 'houses'
    allowed_domains = ['www.zillow.com']
    settings = get_project_settings()
    ZILLOW_CITIES_DICT = settings["ZILLOW_CITIES_DICT"]
    ZILLOW_CITY_URL = None


    def start_requests(self):
        self.ZILLOW_CITY_URL = self.ZILLOW_CITIES_DICT[self.settings.get("ZILLOW_SELECTED_CITY", "Atlanta")]
        yield scrapy.Request(
            url=self.ZILLOW_CITY_URL,
            cookies=parse_cookies(),
            meta={
                "current_page": 1
            }
        )
    

    def parse(self, response):
        json_response = json.loads(response.body)
        houses = json_response.get("cat1").get("searchResults").get("listResults")
        total_pages = json_response.get("cat1").get("searchList").get("totalPages")
        current_page = response.meta.get("current_page")
        
        for house in houses:
            loader = ItemLoader(item=ZillowItem())
            loader.add_value("address", house.get("address"))
            loader.add_value("addressCity", house.get("addressCity"))
            loader.add_value("addressState", house.get("addressState"))
            loader.add_value("addressStreet", house.get("addressStreet"))
            loader.add_value("addressZipcode", house.get("addressZipcode"))
            loader.add_value("baths", house.get("baths"))
            loader.add_value("beds", house.get("beds"))
            loader.add_value("detailUrl", house.get("detailUrl"))
            loader.add_value("homeStatus", house.get("hdpData").get("homeInfo").get("homeStatus"))
            loader.add_value("homeType", house.get("hdpData").get("homeInfo").get("homeType"))
            loader.add_value("houseId", house.get("id"))
            # loader.add_value("image_urls", house.get("imgSrc"))
            loader.add_value("imgSrc", house.get("imgSrc"))
            loader.add_value("isZillowOwned", house.get("isZillowOwned"))
            loader.add_value("latitude", house.get("latLong").get("latitude"))
            loader.add_value("longitude", house.get("latLong").get("longitude"))
            loader.add_value("lotAreaValue", house.get("hdpData").get("homeInfo").get("lotAreaValue", 0.0))
            loader.add_value("lotAreaUnit", house.get("hdpData").get("homeInfo").get("lotAreaUnit", "Unknown"))
            loader.add_value("price", house.get("price"))
            loader.add_value("rentZestimate", house.get("hdpData").get("homeInfo").get("rentZestimate", 0.0))
            loader.add_value("sgapt", house.get("sgapt"))
            yield loader.load_item()


        if current_page <= total_pages:
            current_page += 1
            yield scrapy.Request(
                url=parse_new_url(self.ZILLOW_CITY_URL, current_page),
                cookies=parse_cookies(),
                meta={
                    "current_page": current_page
                    }
            )
