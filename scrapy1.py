#coding=utf-8;

# scrapy 框架是一个单纯的为了爬去网站数据的框架 我们只需要指定要爬取得URL，获取数据之后进行解析即可
# 定制几个简单的模块 就可以实现爬虫
# scrapy 使用了Twisted 异步网络框架进行网络通信



# scrapy 框架结构
"""
    1 Scrapy Engine ：引擎，负责Spiders Item Pipeline Downloader Scheduler 中间的通信，信号，数据传递
    2 Scheduler：调度器 他负责接受引擎发送过来的Request 请求，并按照一定的方式进行整理排列，入队，当引擎需要时，还给引擎
    3 Downloader：下载器，负责下载Scrapy Engine 发送的所有Requests 请求，并且将其获取到的response 交还给Scrapy Engine
    4 Spider：爬虫：它负责处理所有的Responses 从中分析获取数据，获取item字段需要的数据，并将需要跟进的URL提供给引擎，再次进入Scheduler
    5 Item Pipeline：管道，他负责处理Spider 中获取到的item，并进行后期处理（详细分析，过滤，存储等操作）
    6 Downloader Middlewares 下载中间器 是在引擎及下载器中间特定的钩子 specific hook，处理Downloader 传递给引擎的response
    7 Spider middlewares  Spider 中间件，是引擎与Spider中间特定的钩子，处理spider的输入 和 输出

"""

"""
    使用一个scrapy 一共需要四个步骤
    1> 创建一个scrapy 项目
    scrapy startproject xxx

    2> 定义Item 容器,编写对应的item.py

    3> 编写爬虫

    制作爬虫spider.py

    4> 存储内容 , 设计管道存储爬取内容 pipelines.py

"""

# 框架文件介绍
"""
    1>scrapy.cfg  项目的配置文件
    2>items.py 项目的item文件
    3>piplines.py 项目中的piplines 文件
    4>settings.py 项目的设置文件
    5>spiders/ 存放spider代码的目录
"""



