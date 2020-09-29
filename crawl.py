import io
import time

import requests
from PIL import Image
from bs4 import BeautifulSoup
import json



class Crawl(object):

    def __init__(self):
        self. headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0',
        }
        self.session = requests.session()

    def get_captcha(self):

        imgr = self.session.get('https://zd.winnermedical.com/captcha', headers=self.headers, stream=True, allow_redirects=False)
        im = Image.open(imgr.raw)
        imgByteArr = io.BytesIO()
        # im.show()
        im.save(imgByteArr, format='PNG')
        imgByteArr = imgByteArr.getvalue()
        return imgByteArr

    def login(self, username="hbwj@zhedao.net", password="hbwj@2020", code=None):
        # self.get_captcha()
        # code = input("input:")
        data = {"username": username, "password": password, "captcha": code}
        mySession = self.session.post("https://zd.winnermedical.com/users/login", headers=self.headers, data=data)
        # print(mySession.text)
        bs = BeautifulSoup(mySession.text, 'lxml')
        retTitle = bs.find(name="h2", class_="ret-title").text
        # print(retTitle)
        return retTitle

    def search(self, time_range="", process=0, qrcode_id="", rows=100000, page=1, sort="time_cr", order="desc", _=int(time.time()*1000)):
        if time_range != "":
            time_range = "&time_range=" + time_range
        if process != 0:
            process= "&process=" + str(process)

        if qrcode_id != "" or qrcode_id is not None:
            qrcode_id = "&qrcode_id=" + qrcode_id
        url1 = 'https://zd.winnermedical.com/admin/zd-batches/showQrcode.json?id=1601279100756&status=1&rows=10&page=1&sort=qrcode_id&order=asc&_=1601281846943'
        url = "https://zd.winnermedical.com/admin/zd-production-process-output-reports." \
              "json?rows={0}&page={1}&sort={2}&order={3}&_={4}{5}{6}{7}"\
            .format( rows, page, sort, order, _, process, qrcode_id, time_range)
        json_data = self.session.get(url).content
        print(bytes.decode(json_data))
        if len(json_data) > 0:
            return json.loads(bytes.decode(json_data))
        else:
            return {"data":[],"page":1,"rows":20,"records":0,"code":1,"message":"操作成功"}

if __name__ == '__main__':
    crawl = Crawl()
    print(crawl.login("hbwj@zhedao.net", "hbwj@2020"))

    print(crawl.search("2020.09.11~2020.09.11"))
