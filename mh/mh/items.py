# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RealityIdnes(scrapy.Item):
    # define the fields for your item here like:
    titulo = scrapy.Field()
    contacto = scrapy.Field()
    telefono = scrapy.Field()
    email = scrapy.Field()
    url = scrapy.Field()
