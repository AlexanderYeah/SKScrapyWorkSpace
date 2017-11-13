# -*- coding: utf-8 -*-
import scrapy

from tencent.items import TencentItem
class TencentjobSpider(scrapy.Spider):
    name = 'tencentJob'
    allowed_domains = ['tencent.com']
    # 这种网页是翻页的
    baseURL =  'http://hr.tencent.com/position.php?&start=';
    # 翻页数
    offset = 0;
    # 请求列表
    start_urls = [baseURL + str(offset)];


    def parse(self, response):

        # 获取存储信息的每一个节点
        node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']");

        # for循环遍历节点
        """
            一次for循环会返回10个信息
            可以去拼接连接
        """
        for node in node_list:

            # 创建一个item 对象
            item =  TencentItem();

            # 1 职位名
            item['positionName'] = node.xpath("./td[1]/a/text()").extract()[0];
            # 2 连接
            item['positionLink'] = node.xpath("./td[1]/a/@href").extract()[0];


            # 3 类别 有的岗位可能没有写类别 所以要做一个判断,有值再去处理 没有值的话 给一个空的字符串

            if len(node.xpath("./td[2]/text()")):
                item['positionType'] = node.xpath("./td[2]/text()").extract()[0];
            else:
                item['positionType'] = '';


            # 4 人数
            item['positionNumber'] = node.xpath("./td[3]/text()").extract()[0];
            # 5 地点
            item['positionLocation'] = node.xpath("./td[4]/text()").extract()[0];
            # 6 时间
            item['positionTime'] = node.xpath("./td[5]/text()").extract()[0];

            # 将item 交给管道处理
            yield  item;




        # 一页数据处理完毕 进行翻页操作
        # 进行判断到尾页 什么时候结束
        if self.offset < 200:
            self.offset += 10;
            url = self.baseURL + str(self.offset);
            # 构建一个新的请求 并且发送出去
            """
                第一个参数是 url 地址
                第二个参数是 回调函数 回调函数确定了 那个函数处理response

            """
            # 使用yield 将构建的请求直接发送出去 引擎会判断 是个 请求的话直接交给调度器进行处理
            yield scrapy.Request(url,callback = self.parse);



