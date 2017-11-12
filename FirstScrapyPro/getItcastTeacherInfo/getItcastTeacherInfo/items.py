# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

"""
    存储字段
"""

class GetitcastteacherinfoItem(scrapy.Item):
    # define the fields for your item here like:
    # 名字
    name = scrapy.Field()
    # 级别
    title = scrapy.Field()
    # 介绍
    info = scrapy.Field()



