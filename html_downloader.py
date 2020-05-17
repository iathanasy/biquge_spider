# coding utf-8

# 下载器
import urllib.request


class HtmlDownloader(object):

    def __init__(self):
        self.headrs = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
        }
        self.timeout = 10

    #下载
    def download(self, url):
        if url is None:
            return None
        try:
            request = urllib.request.Request(url, headers=self.headrs)
            response = urllib.request.urlopen(request, timeout=self.timeout)

            if response.code != 200:
                return None

            return response.read().decode("utf-8")
        except Exception as e:
            print("download error ",e)
            return None