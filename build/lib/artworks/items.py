# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArtworksItem(scrapy.Item):
    url = scrapy.Field(serializar=str)
    artist = scrapy.Field(serializar=str)
    title = scrapy.Field(serializar=str)
    image = scrapy.Field(serializar=str)
    height = scrapy.Field(serializar=float)
    width = scrapy.Field(serializar=float)
    description = scrapy.Field(serializar=str)
    categories = scrapy.Field(serializar=list)
