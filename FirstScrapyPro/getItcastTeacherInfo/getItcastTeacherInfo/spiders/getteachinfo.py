# -*- coding: utf-8 -*-
import scrapy

# 从getItcastTeacherInfo 文件夹下 item.py 中引入 定义的类
from getItcastTeacherInfo.items import GetitcastteacherinfoItem




class GetteachinfoSpider(scrapy.Spider):

    # 爬虫的名字 启动爬虫的时候参数
    name = 'getteachinfo'
    # 爬取域的范围
    allowed_domains = ['itcast.cn']
    # 请求列表 要手动添加
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    """
    解析的方法，每个初始URL完成下载后将被调用，调用的时候传入从每一个URL传回的Response对象来作为唯一参数，主要作用如下：

    1》负责解析返回的网页数据(response.body)，提取结构化数据(生成item)
    2》生成需要下一页的URL请求。

    """
    def parse(self, response):

        #从响应中 获取节点
        node_list = response.xpath("//div[@class='li_txt']");

        # 用来存储所有的item 字段
        for node in node_list:

            # 创建item字段对象 用来存储信息
            item = GetitcastteacherinfoItem();
            # .extract() 方法将xpath 对象转换为 Unicode 字符串
            name = node.xpath('./h3/text()').extract();
            title = node.xpath('./h4/text()').extract();
            info = node.xpath('./p/text()').extract();

            # 将数据放到item 内
            item["name"] = name[0];
            item["title"] = title[0];
            item["info"] = info[0];

            # 返回提取到的每一个item 给管道文件处理，同时还会继续回来执行此代码
            # item 直接进行返回 scrapy 会判断，如果是item 直接给管道文件处理
            yield item;



