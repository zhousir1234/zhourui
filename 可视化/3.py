import uuid

import requests
import unicodedata
from lxml import html
import pymysql





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
        # 影片详情
        move_content = y.xpath('div[@class="bd"]/p[1]/text()')
        # 导演演员信息
        actor = move_content[0].replace(" ", "").replace("\n", "")
        # 上映日期
        date = move_content[1].replace(" ", "").replace("\n", "").split("/")[0]
        # 制片国家
        country = move_content[1].replace(" ", "").replace("\n", "").split("/")[1]
        # 影片类型
        gener = move_content[1].replace(" ", "").replace("\n", "").split("/")[2]
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
                 unicodedata.normalize('NFKD', actor).encode('utf-8', 'ignore'),
                 unicodedata.normalize('NFKD', date).encode('utf-8', 'ignore'),
                 unicodedata.normalize('NFKD', country).encode('utf-8', 'ignore'),
                 unicodedata.normalize('NFKD', rate).encode('utf-8', 'ignore'),
                 unicodedata.normalize('NFKD', com_count.replace('人评价', '')).encode('utf-8', 'ignore'), index)
        # 加入数组
        movies.append(movie)
        index += 1
# 插入数据库


def insert_movies(movies):
 db = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='movie', charset='utf8')
 cursor = db.cursor()
sql = "INSERT INTO original_douban(id,name,actor,release_date,country,rate,comment_count,rank)\
  VALUES (%s,%s,%s,%s,%s,%s ,%s,%s)"
try:
 cursor.executemany(sql, movies)
 db.commit()
except pymysql.Error:
 db.rollback()
finally:
 cursor.close()
 db.close()