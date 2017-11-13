# SKScrapyWorkSpace
Scrapy Learn  

### 一 getItcastTeacherInfo 项目是第一个 scrapy 项目     
主要是熟悉一下scrapy 项目的流程，之前使用pip 安装scarpy 一直失败 ，今天使用了anaconda 一下就成功了   
1. 创建一个scarpy项目     
> scrapy startproject mySpider  
2. cd到spider文件下面 ，创建一个爬虫文件  
>scrapy genspider firstspider "www.baidu.com"  
3. 代码编写完毕 直接执行
>scrapy crawl firstspider
  
### 二 项目2 ：tencent 项目   
是爬取tencent 网招聘信息的一个简单的项目  
* 自动翻页采集  
* 爬取过程中遇到一个TypeError: Object of type 'bytes' is not JSON serializable 的错误    
  解决方案根据Stack Overflow （https://stackoverflow.com/questions/44682018/typeerror-object-of-type-bytes-is-not-json-serializable）

