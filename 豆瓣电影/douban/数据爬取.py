import pandas as pd
import requests
from lxml import html

encoding="utf-8"
def get_douban_top250():
    print('正在获取豆瓣TOP250影片信息`并保存至本地...')
    rank = 0
    page_count = 10
    em_df=pd.DataFrame(columns=["rank","name","dates","country","type", "chractor","remark","score","count"])
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
        # 上映日期
           dates = move_content[1].replace(" ", "").replace("\n", "").split("/")[0]
           dates = dates.replace("\xa0", "").replace("\xee", "").replace("\xf6", "").replace("\u0161", "").replace("\xf4"
            "", "").replace("\xfb", "").replace("\u2027", "")
           date = str(dates)
        # print(date)
        # 制片国家
           country = move_content[1].replace(" ", "").replace("\n", "").split("/")[1].replace("\xa0", "")
        # 影片类型
           type = move_content[1].replace(" ", "").replace("\n", "").split("/")[2]
           type = type.replace("\xa0", "").replace("\xee", "").replace("\xf6", "").replace("\u0161", "").replace(
            "\xf4", "").replace("\xfb", "").replace("\u2027", "")
        # 导演及演员信息
           chractor = move_content[0].replace(" ", "").replace("\n", "")
           chractor = chractor.replace("\xa0", "").replace("\xee", "").replace("\xf6", "").replace("\u0161",
            "").replace("\xf4", "").replace("\xfb", "").replace("\u2027", "").replace("\xe5", "").replace("\u22ef", "")
        # 影片描述
           remark = y.xpath('div[@class="bd"]/p[@class="quote"]/span[@class="inq"]/text()')
           remark = str(remark)
           remark = remark.replace("[", "").replace("]", "").replace("'", "").replace("\u22ef", "")
        # 评分
           score = y.xpath('div[@class="bd"]/div[@class="star"]/span[2]/text()')[0]
        # 评论人数
           count = y.xpath('div[@class="bd"]/div[@class="star"]/span[4]/text()')[0]
        # 排名
           rank = rank+1
           # rank=y.xpath('//*[@id="content"]/div/div[1]/ol/li[1]/div/div[1]/em/text()')
           dict={
               "rank": rank,
               "name":name,
               "dates":dates,
               "country":country,
               "type":type,
               "chractor":chractor,
               "remark":remark,
               "score":score,
               "count":count,
           }
           df=pd.DataFrame(data=dict,index=[0],columns=["rank","name","dates","country","type", "chractor","remark","score","count"])
           print(df)
           em_df=em_df.append(df)
           df1=em_df.reset_index(drop=True)
           # df1.index=np.arrange(1,len(df1)+1)
           df1.to_csv('data.csv',encoding='utf-8')
# 执行get_douban_top250方法
get_douban_top250()
