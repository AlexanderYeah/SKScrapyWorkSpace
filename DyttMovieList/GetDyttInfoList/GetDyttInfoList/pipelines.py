# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class GetdyttinfolistPipeline(object):
    def __init__(self):
        self.f = open("dyttMovieList.json", 'wb');


    def process_item(self, item, spider):
        # 处理数据
        content = json.dumps(dict(item),ensure_ascii=False) + "," +"\n"
        self.f.write(content.encode('utf-8'));

    def close_spider(self,spider):
        self.f.close();






