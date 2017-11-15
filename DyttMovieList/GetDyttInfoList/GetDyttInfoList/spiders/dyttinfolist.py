# -*- coding: utf-8 -*-
import scrapy
import re
from GetDyttInfoList.items import GetdyttinfolistItem

"""

    以上是国产电影列表的第一页
    http://www.dytt8.net/html/gndy/china/list_4_1.html

"""
class DyttinfolistSpider(scrapy.Spider):
    name = 'dyttinfolist'
    allowed_domains = ['dytt8.net']
    # base URL
    baseURL = "http://www.dytt8.net/html/gndy/china/list_4";

    start_urls = ['http://www.dytt8.net/html/gndy/china/list_4_1.html'];

    def parse(self, response):
        # 获取响应 证明是有东西的
        # print(response.body);

        # 取得所有的节点
        nodes_list = response.xpath('//table[@class="tbspan"]');
        # 验证一下长度
        print("alex fuck length" + str(len(nodes_list)));
        # 循环遍历
        for node in  nodes_list:
            # 创建item
            item = GetdyttinfolistItem();
            # 再取对应的元素
            """

                /tbody/tr[2]/td[2]/b/a[@class='ulink'][2]
            """
            item["movieName"] = node.xpath("./tbody/tr[2]/td[2]/b/a[@class='ulink'][2]/text()").extract()[0];
            item["movieLink"] = node.xpath("./tbody/tr[2]/td[2]/b/a[2]/@href").extract()[0];
            item["movieTime"] = node.xpath("./tbody/tr[3]/td[2]/font/text()").extract()[0];

            # r_url = re.compile('<b>.*?<as*href="(.*?)"s*class="ulink">', re.DOTALL);

            # 给管道处理
            yield  item;





