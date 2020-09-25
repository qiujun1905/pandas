import io
import re
import time

from aip.ocr import AipOcr
import os
import requests
from PIL import Image
from bs4 import BeautifulSoup
_APP_ID = '22727944'
_API_KEY = 'qXdwqmLDArj5b8EiCGGh2wSB'
_SECRET_KEY = 'sSPb4NDPstQR2DrXvvkUldGft4Mwg5Et'

client = AipOcr(_APP_ID, _API_KEY, _SECRET_KEY)

class Crawl(object):
# def get_file_content(filePath):
#     with open(filePath, 'rb') as fp:
#         return fp.read()
#

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

    def search(self, time_range, process=10, qrcode_id="", rows=10000, page=1, sort="time_cr", order="desc", _=int(time.time()*1000)):
        if time_range == "~":
            time_range = ""
        url = "https://zd.winnermedical.com/admin/zd-production-process-output-reports.json?process={0}&qrcode_id={1}&time_range={2}&rows={3}&page={4}&sort={5}&order={6}&_={7}".format(process, qrcode_id, time_range, rows, page, sort, order, _)
        json = self.session.get(url).json()
        # records = json['records']
        print(type(json))
        return json
if __name__ == '__main__':
    crawl = Crawl()
    print(crawl.login("hbwj@zhedao.net", "hbwj@2020"))

    print(crawl.search("2020.09.11~2020.09.11"))
