
# coding:utf-8
import uuid

import requests
import unicodedata
from lxml import html


# import db_douban


def list_douban_top250():
    print('正在获取豆瓣TOP250影片信息并存入数据库...')


movies = []
index = 1
page_count = 10
for i in range(page_count):
    url = 'https://movie.douban.com/top250?start={}&filter='.format(i * 25)
    url_content = requests.get(url).content
    # 内容节点
    doc = html.fromstring(url_content)
    for y in doc.xpath('//div[@class="info"]'):
        # 影片名称
        name = y.xpath('div[@class="hd"]/a/span[@class="title"]/text()')[0]
        # 评分
        rate = y.xpath('div[@class="bd"]/div[@class="star"]/span[2]/text()')[0]
        # 评论人数
        com_count = y.xpath('div[@class="bd"]/div[@class="star"]/span[4]/text()')[0]
        # UUID
        move_id = uuid.uuid1().hex
        # 执行log
        print('TOP%s--%s--评分%s--人数%s' % (str(index), name, rate, com_count.replace('人评价', '')))
        # 生成影片对象
        movie = (unicodedata.normalize('NFKD', move_id).encode('utf-8', 'ignore'),
                 unicodedata.normalize('NFKD', name).encode('utf-8', 'ignore'),
                 unicodedata.normalize('NFKD', rate).encode('utf-8', 'ignore'),
                 unicodedata.normalize('NFKD', com_count.replace('人评价', '')).encode('utf-8', 'ignore'), index)
        # 加入数组
        movies.append(movie)
        index += 1
# 插入数据库
# db_douban.insert_movies(movies)
# print('任务执行完成！')


list_douban_top250()
