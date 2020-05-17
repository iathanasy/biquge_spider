# coding utf-8
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse

# 解析器
class HtmlParser(object):
    def __init__(self):
        self.encoding = "utf-8"
        self.links = re.compile("/book/\d+/\d+.html")

    # 获取页面url
    def get_new_urls(self,url, soup):
        new_urls = set()

        links = soup.find_all("a", href=self.links)
        for link in links:
            new_url = link["href"]
            url_parse = urlparse(url)
            base_url = ""
            scheme = url_parse.scheme
            netloc = url_parse.netloc
            base_url = scheme + "://" + netloc
            new_full_url = base_url + new_url
            new_urls.add(new_full_url)

        return new_urls

    # 获取数据
    def get_new_data(self,url, soup):
        res_data = {}
        try:
            res_data["url"] = url

            chapter_select = soup.select("div[class='bookname'] > h1")
            res_data["chapter"] = chapter_select[0].get_text()

            chapter_select = soup.select("div[id='content']")
            res_data["context"] = chapter_select[0].get_text()
        except Exception as e:
            pass
        return res_data

    # 解析 返回新的url列表、价值数据
    def parse(self,url, html_content):
        if url is None or html_content is None:
            return set(), {}
        soup = BeautifulSoup(html_content, "html.parser", from_encoding=self.encoding)

        new_urls = self.get_new_urls(url, soup)
        new_data = self.get_new_data(url, soup)
        return new_urls, new_data
