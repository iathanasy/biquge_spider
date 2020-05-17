# coding utf-8

# URL管理器
class UrlManager(object):
    def __init__(self):
        # 待访问urls
        self.new_urls = set()
        # 已访问urls
        self.old_urls = set()

    # 添加新的url
    def add_new_url(self, url):
        if url is None:
            return
        # 不在待访问 和已访问集合中
        if url not in self.new_urls and url not in self.old_urls:
            # 入队
            self.new_urls.add(url)

    # 新的url列表 新增到待爬URL
    def add_new_urls(self, urls):
        if urls is None and len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    #有待爬取的URl？ 是/否
    def has_new_url(self):
        return len(self.new_urls) != 0

    # 获取待爬取url
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
