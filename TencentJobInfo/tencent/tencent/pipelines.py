# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class TencentPipeline(object):

    def __init__(self):
        self.f = open("tencentJob.json",'wb');

    def process_item(self, item, spider):

        # 内容转化过来
        content = json.dumps(dict(item),ensure_ascii=False)+","+"\n";
        # 写入到本地
        self.f.write(content.encode('utf-8'));
        # 管道文件写完之后 去setting 文件启用管道
        return item



    # 爬虫结束 关闭操作句柄
    def close_spider(self,spider):
        self.f.close();