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
    baseURL = "http://www.dytt8.net/html/gndy/china/list_4_";
    # 翻页数
    offset = 1;
    start_urls = ['http://www.dytt8.net/html/gndy/china/list_4_1.html'];

    def parse(self, response):
        # 获取响应 证明是有东西的
        # print(response.body);

        # 取得所有的节点
        nodes_list = response.xpath('//table[@class="tbspan"]');
        # 验证一下长度
       # print("alex fuck length" + str(len(nodes_list)));

        # 循环遍历
        for node in nodes_list:
            print(node.xpath(".//a[@class='ulink'][2]/text()").extract()[0]);
            # 创建item
            item = GetdyttinfolistItem();
            # 填充内容
            # 电影名字
            item["movieName"] = node.xpath(".//a[@class='ulink'][2]/text()").extract()[0]
            # 电影上映时间
            item["movieTime"] = node.xpath(".//font/text()").extract()[0]
            # 电影详情的url 要拼接上  http://www.dytt8.net/
            mainUrl = "http://www.dytt8.net/";
            item["movieLink"] = mainUrl + node.xpath(".//a[@class='ulink'][2]/@href").extract()[0];

            yield  item;

        # 进行翻页操作
        if self.offset < 20:
            # 页数加1 构建请求
            self.offset += 1;
            url = self.baseURL + str(self.offset)+".html";
            # 使用yield 将构建的请求直接发送出去
            yield scrapy.Request(url,callback= self.parse)







