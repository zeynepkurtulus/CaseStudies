# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PetlebiProjectItem(scrapy.Item):
    TITLETEXT = scrapy.Field()
    PRODUCTTEXT = scrapy.Field()
    PRICE = scrapy.Field()
    BARCODE = scrapy.Field()