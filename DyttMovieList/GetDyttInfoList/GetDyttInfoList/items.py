# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GetdyttinfolistItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 定义字段

    # 名称
    movieName = scrapy.Field();
    # 详情链接
    movieLink = scrapy.Field();
    # 时间
    movieTime = scrapy.Field();
