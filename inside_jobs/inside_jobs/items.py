# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class InsideJobsItem(scrapy.Item):
    company = scrapy.Field()
    name = scrapy.Field()
    category = scrapy.Field()
    location = scrapy.Field()
    salary = scrapy.Field()
    url = scrapy.Field()
