# coding utf-8

# 输出应用
class HtmlOutputer(object):
    def __init__(self):
        self.datas=[]

    # 收集数据
    def collect_data(self, data):
        if data is None:
            return None
        self.datas.append(data)

    #输出数据
    def output_html(self):
        fout = open("output.html", "w")
        for data in self.datas:
            # fout.write(data["chapter"].encode("utf8"))
            # fout.write(data["context"].encode("utf8"))
            # fout.write("<br><br>")
            print(data["chapter"].encode("utf8"))
            print(data["context"].encode("utf8"))

        fout.close()