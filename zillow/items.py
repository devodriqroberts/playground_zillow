# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose
from scrapy import Field

def convert_to_int(value):
    if value:
        if isinstance(value, str):
            if "$" in value:
                value = value.replace("$", "").replace(",", "").replace("+", "")
                try:
                    return int(value)
                except:
                    return value

            else:
                try:
                    return int(value)
                except:
                    return value

        else:
            return value
    else:
        return None

def convert_to_sentence_case(value):
    if value:
        try:
            value = value.replace("_", " ").strip()
            return value.title()
        except:
            return value
    else:
        return "Unknown"

def truncate_float(value):
    if value:
        try:
            return round(value,4)
        except:
            return value
    else:
        return 0.0


class ZillowItem(scrapy.Item):
    address = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
        )
    addressCity = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
    addressState = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
    addressStreet = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
    addressZipcode = Field(
        input_processor=MapCompose(convert_to_int),
        output_processor=TakeFirst()
    )
    baths = Field(output_processor=TakeFirst())
    beds = Field(output_processor=TakeFirst())
    detailUrl = Field(output_processor=TakeFirst())
    homeStatus = Field(
        input_processor=MapCompose(convert_to_sentence_case),
        output_processor=TakeFirst()
    )
    homeType = Field(
        input_processor=MapCompose(convert_to_sentence_case),
        output_processor=TakeFirst()
    )
    houseId = Field(
        input_processor=MapCompose(convert_to_int),
        output_processor=TakeFirst()
    )
    imgSrc = Field(output_processor=TakeFirst())
    # image_urls = Field()
    # images = scrapy.Field()
    isZillowOwned = Field(output_processor=TakeFirst())
    latitude = Field(output_processor=TakeFirst())
    longitude = Field(output_processor=TakeFirst())
    lotAreaValue = Field(
        input_processor=MapCompose(truncate_float),
        output_processor=TakeFirst()
    )
    lotAreaUnit = Field(output_processor=TakeFirst())
    price = Field(
        input_processor=MapCompose(convert_to_int),
        output_processor=TakeFirst()
    )
    rentZestimate = Field(
        input_processor=MapCompose(convert_to_int),
        output_processor=TakeFirst()
    )
    sgapt = Field(
        input_processor=MapCompose(convert_to_sentence_case),
        output_processor=TakeFirst()
    )
