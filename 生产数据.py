import requests
import time
import pandas as pd
from multiprocessing.pool import Pool


def get_page(rows, page):
    headers = {
        'authority': 'zd.winnermedical.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://zd.winnermedical.com/admin/zd-production-process-output-reports',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'PHPSESSID=7qtdef4hhtd5q5k3agdilnnf80; Hm_lvt_5e68e5f229f8761339c09c3bbcf78d40=1600042527,1600131379,1600215029,1600301695; Hm_lpvt_5e68e5f229f8761339c09c3bbcf78d40=1600301728',
    }
    times = int(time.time())
    params = {
        'rows': rows,
        'page': page,
        'sort': 'process',
        'order': 'asc',
        '_': times,
    }
    global process, qrcode_id, time_range, sort, order
    url = 'https://zd.winnermedical.com/admin/zd-production-process-output-reports.json?process={}&qrcode_id={}&time_range={}&rows={}&page={}&sort={}&order={}&_={}'.format(process, qrcode_id, time_range, rows, page, sort, order, times)
    response = requests.get(
        url,
        headers=headers,
        params=params)
    if response.status_code == 200 and len(response.json()['data']) > 0:
        print(response.json()['data'])
        return response.json()['data'], page
    else:
        raise Exception("没有数据啦...")

# response = requests.get('https://zd.winnermedical.com/admin/zd-production-process-output-reports.json', headers=headers, params=params)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".

def save_data(json, page):
    df = pd.DataFrame(json)
    df.to_csv('生产数据{}.csv'.format(page), encoding='utf-8', mode='w+')

def main(page):
    global rows
    json, page = get_page(rows, page)
    save_data(json, page)

process = 10
qrcode_id=''
time_range=''
rows = 1000
page = 0
sort = 'process'
order = 'asc'
_ = int(time.time())

url = 'https://zd.winnermedical.com/admin/zd-production-process-output-reports.json?process={}&qrcode_id={}&time_range={}&rows={}&page={}&sort={}&order={}&_={}'.format(process, qrcode_id, time_range, rows, page, sort, order, _)
if __name__ == '__main__':

    headers = {
        'authority': 'zd.winnermedical.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://zd.winnermedical.com/admin/zd-production-process-output-reports',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'PHPSESSID=7qtdef4hhtd5q5k3agdilnnf80; Hm_lvt_5e68e5f229f8761339c09c3bbcf78d40=1600042527,1600131379,1600215029,1600301695; Hm_lpvt_5e68e5f229f8761339c09c3bbcf78d40=1600301728',
    }
    times = int(time.time())
    params = {
        'process': process,
        'rows': rows,
        'page': page,
        'sort': process,
        'order': 'asc',
        '_': times,
    }
    url = 'https://zd.winnermedical.com/admin/zd-production-process-output-reports.json?process={}&qrcode_id={}&time_range={}&rows={}&page={}&sort={}&order={}&_={}'.format(process, qrcode_id, time_range, rows, page, sort, order, _)
    response = requests.get(
        url,
        headers=headers,)
    print(response.json())
    records = response.json()['records']
    pages_count = 0
    if records % rows > 0:
        pages_count = int(records / rows + 1)
    else:
        pages_count = int(records / rows)

    pages = [page for page in range(0, int(pages_count))]
    # for page in pages:
    #     main(page)
    pool = Pool(4)
    pool.map(main, pages)

    pool.close()
    pool.join()