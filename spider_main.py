# coding utf-8

'''
   爬虫运行流程
调度器       |   URL管理器       |     下载器       |        解析器       |        应用

 ---有待爬取的URl?-->
 <-- 是/否----
 ---获取一个待爬取的URL-->
 <-- URL---

    -----------下载url内容------------>
    <----------URL内容-----------------

    ----------------------解析URL内容--------------------------->
    <--------------新的URL列表、价值数据---------------------------

    ----------------------------------收集价值数据---------------------------------->

 --新增到待爬URL-->

    ----------------------------------输出价值数据---------------------------------->
'''

## 调度器
import html_downloader
import html_outputer
import html_parser
import url_manager


class SpiderMain(object):
    # 初始化
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()


    # 爬虫调度
    def craw(self, root_url):
        count = 1

        #初始添加新的url
        self.urls.add_new_url(root_url)
        # 有待爬取的URl？ 是/否
        while self.urls.has_new_url():
            try:
                #获取待爬取url
                new_url = self.urls.get_new_url()
                print("craw %d : %s" %(count, new_url))
                #下载
                html_content = self.downloader.download(new_url)
                #解析  返回新的url列表、价值数据
                new_urls, new_data = self.parser.parse(new_url, html_content)
                #将新的url列表 新增到待爬URL
                self.urls.add_new_urls(new_urls)
                print(new_data.get("chapter", "None"))
                # 收集数据
                #self.outputer.collect_data(new_data)

                count = count + 1
            except Exception as e:
                print("craw error ", e)

        # 输出数据
        #self.outputer.output_html()



if __name__ == '__main__':
    # root_url = "https://www.biquge.com.cn/book/7586/30896.html"
    root_url = "https://www.biquge.com.cn/book/7586/31135.html"
    # root_url = "https://www.biquge.com.cn/book/7586/"
    # 启动爬虫
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)