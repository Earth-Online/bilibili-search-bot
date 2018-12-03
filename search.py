#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests


def get_address(av):
    url = "http://9bl.bakayun.cn/API/GetVideoUrl.php?cid={av}&type=json&quality=2"

    ret = requests.get(url.format(av=av))

    return ret.json()['Result']['Url']['Main']


def download(av):
    address = ret.json()['Result']['Url']['Main']
    headers = {
        'user-agent': 'Safari/537.36',
        'referer': "https://www.bilibili.com"
    }
    r = requests.get(adress, headers, stream=True)
    with open(download_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            f.write(chunk)


def search_video(keyword):
    url = "https://api.bilibili.com/x/web-interface/search/type?jsonp=jsonp&search_type=video&highlight=1&keyword={keyword}&order=totalrank&duration=0&single_column=0&tids=&page=1"
    ret = requests.get(url.format(keyword=keyword))
    if ret.ok:
        return ret.json()['data']['result']
    return False
