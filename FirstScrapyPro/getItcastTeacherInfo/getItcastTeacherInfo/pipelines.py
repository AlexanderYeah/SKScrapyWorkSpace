# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class GetitcastteacherinfoPipeline(object):
    def __init__(self):
        # 初始化一个写入文件
        self.f = open('teacherinfo.json','wb');

    # 这个方法是必须写的
    def process_item(self, item, spider):
        # 获取到每一个spider 返回的item 进行处理
        # 将item 转换成字典格式
        # 如果字段中有中文的话 会按照Unicode 格式进行处理

        content = json.dumps(dict(item),ensure_ascii= False) + "," + "\n";
        self.f.write(content.encode('utf-8'));
        # 将item 返回给引擎 告知 item数据处理完毕
        return item;

    def close_aspider(self,spider):
        # 关闭文件
        self.f.close();


"""
    管道文件的作用就是处理item 字段的
    json 方法
    dumps是将dict转化成str格式，loads是将str转化成dict格式。

"""