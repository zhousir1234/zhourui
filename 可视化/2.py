"""
爬取豆瓣电影Top250
"""

import os  #导入os模块
import re  #导入re模块
import time  #导入time模块
import requests  #导入reqquests模块
from bs4 import BeautifulSoup


def download(url, page):
    print(f"正在爬取：{url}")
    html = requests.get(url).text   # 这里不加text返回<Response [200]>
    soup = BeautifulSoup(html, 'html.parser')
    lis = soup.select("ol li")
    for li in lis:
        index = li.find('em').text
        title = li.find('span', class_='title').text
        rating = li.find('span', class_='rating_num').text
        strInfo = re.search("(?<=<br/>).*?(?=<)", str(li.select_one(".bd p")), re.S | re.M).group().strip()
        infos = strInfo.split('/')
        year = infos[0].strip()
        area = infos[1].strip()
        type = infos[2].strip()
        write_fo_file(index, title, rating, year, area, type)
    page += 1
    if page < 5:
        time.sleep(2)
        download(f"https://music.douban.com/top250?start={page}&filter=", page)


def write_fo_file(index, title, rating, year, area, type):
    f = open('音乐top250.csv', 'a')
    f.write(f'{index},{title},{rating},{year},{area},{type}\n')
    f.closed


def main():
    if os.path.exists('音乐top250.csv'):
        os.remove('音乐top250.csv')

    url = 'https://music.douban.com/top250'
    download(url, 0)
    print("爬取完毕。")



if __name__ == '__main__':
    main()