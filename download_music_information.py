import requests
import sys
import json
import time
import importlib
importlib.reload(sys)
import  pandas as pd
from bs4 import BeautifulSoup
import csv


from bs4 import BeautifulSoup


url1 = 'https://music.163.com/discover/toplist?id=3112516681'
#https://music.163.com/discover/toplist?id=3001890046#云音乐ACG VOCALOID榜
#https://music.163.com/discover/toplist?id=3001835560#云音乐ACG动画榜
#https://music.163.com/discover/toplist?id=71385702#云音乐ACG音乐榜
#https://music.163.com/discover/toplist?id=3001795926#云音乐ACG游戏榜
#https://music.163.com/discover/toplist?id=3812895#云音乐Beatport全球电子舞曲榜
#https://music.163.com/discover/toplist?id=120001#云音乐Hit FM Top榜
#https://music.163.com/discover/toplist?id=11641012#云音乐iTunes榜
#https://music.163.com/discover/toplist?id=21845217#云音乐KTV唛榜
#https://music.163.com/discover/toplist?id=180106#云音乐UK排行周榜
#https://music.163.com/discover/toplist?id=19723756#云音乐飙升榜
#https://music.163.com/discover/toplist?id=2006508653#云音乐电竞音乐榜
#https://music.163.com/discover/toplist?id=1978921795#云音乐电音榜
#https://music.163.com/discover/toplist?id=2250011882#云音乐抖音排行榜
#https://music.163.com/discover/toplist?id=27135204#云音乐法国NRJ Vos Hits周榜
#https://music.163.com/discover/toplist?id=71384707#云音乐古典音乐榜
#https://music.163.com/discover/toplist?id=5059642708#云音乐古风榜
#https://music.163.com/discover/toplist?id=10520166#云音乐国电榜
#https://music.163.com/discover/toplist?id=745956260#云音乐韩语榜
#https://music.163.com/discover/toplist?id=60198#云音乐美国billboard周榜
#https://music.163.com/discover/toplist?id=5059661515#云音乐民谣榜
#https://music.163.com/discover/toplist?id=2809513713#云音乐欧美热歌榜
#https://music.163.com/discover/toplist?id=2809577409#云音乐欧美新歌榜
#http://music.163.com/discover/toplist?id=3778678#云音乐热歌榜
#https://music.163.com/discover/toplist?id=60131#云音乐日本Oricon数字单曲周榜
#https://music.163.com/discover/toplist?id=5059644681#云音乐日语榜
#https://music.163.com/discover/toplist?id=991319590#云音乐说唱榜
#https://music.163.com/discover/toplist?id=112463#云音乐台湾Hito榜
#https://music.163.com/discover/toplist?id=3779629#云音乐新歌榜
#https://music.163.com/discover/toplist?id=2617766278#云音乐新声榜
#https://music.163.com/discover/toplist?id=5059633707#云音乐摇滚榜
#https://music.163.com/discover/toplist?id=2023401535#云音乐英国q杂志中文版周榜
#https://music.163.com/discover/toplist?id=2884035#云音乐原创歌曲榜
#https://music.163.com/discover/toplist?id=5201625538#云音乐云贝推歌榜
#https://music.163.com/discover/toplist?id=3112516681#云音乐中国新乡村音乐排行榜







#UA必須要設置，未设置获取的网页不完整
headers = {
    'Cookie':'__e_=1515461191756; _ntes_nnid=af802a7dd2cafc9fef605185da6e73fb,1515461190617; _ntes_nuid=af802a7dd2cafc9fef605185da6e73fb; JSESSIONID-WYYY=HMyeRdf98eDm%2Bi%5CRnK9iB%5ChcSODhA%2Bh4jx5t3z20hhwTRsOCWhBS5Cpn%2B5j%5CVfMIu0i4bQY9sky%5CsvMmHhuwud2cDNbFRD%2FHhWHE61VhovnFrKWXfDAp%5CqO%2B6cEc%2B%2BIXGz83mwrGS78Goo%2BWgsyJb37Oaqr0IehSp288xn5DhgC3Cobe%3A1515585307035; _iuqxldmzr_=32; __utma=94650624.61181594.1515583507.1515583507.1515583507.1; __utmc=94650624; __utmz=94650624.1515583507.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmb=94650624.4.10.1515583507',
    'Host':'music.163.com',
    'Refere':'http://music.163.com/',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

response = requests.get(url1,headers=headers)
print(response.status_code)

html = response.text
soup = BeautifulSoup(html,'lxml')
update_time = soup.find('span',attrs={'class':'sep s-fc3'}).text
print(update_time)

#找到json数据
textarea = soup.find('textarea').text
i = 1
contents = json.loads(str(textarea))


csv_obj = open('F://数据采集课设-音乐网站/下载的音乐信息/云音乐中国新乡村音乐排行榜/data.csv', 'w', encoding="utf-8",newline = "")
#写入一行标题
csv.writer(csv_obj).writerow(["歌名", "歌手", "时长", "专辑", "发布时间"])
for a in range(len(contents)):
    t1 = time.localtime(contents[a].get('publishTime') / 1000)
    t2 = time.strftime("%Y-%m-%d %H:%M:%S", t1)
    # 歌曲时长
    t3 = contents[a].get('duration') / 1000
    min = str(t3 / 60)
    sec = str(t3 % 60)
    if len(sec) < 2:
        sec = '0' + str(sec)
    # 歌手
    artist = contents[a].get('artists')[0].get('name')
    # 歌名
    music_name = contents[a].get('name')
    # 专辑
    album = contents[a].get('album').get('name')
    mins = round(float(min))
    secs = round(float(sec))
    if contents[a].get('alias'):
        alias = contents[a].get('alias')[0]
    i += 1
    #逐个写入电影信息
    duration = str(mins) + ":"+str(secs)
    csv.writer(csv_obj).writerow([music_name,artist,duration,album,t2])
#关闭
csv_obj.close()











#将数据输出到wangyi.log文件中
# fo = open('wangyi3.log','w',encoding="utf-8")
# sys.stdout = fo
# for a in range(len(contents)):
#     #发行时间
#     t1 = time.localtime(contents[a].get('publishTime')/1000)
#     t2 = time.strftime("%Y-%m-%d %H:%M:%S",t1)
#     #歌曲时长
#     t3 = contents[a].get('duration')/1000
#     min = str(t3/60)
#     sec = str(t3%60)
#     if len(sec)<2:
#         sec = '0'+str(sec)
#     #歌手
#     artist = contents[a].get('artists')[0].get('name')
#     #歌名
#     music_name = contents[a].get('name')
#     #专辑
#     album = contents[a].get('album').get('name')
#     mins = round(float(min))
#     secs = round(float(sec))
#     print(i,'.',music_name,u' 播放时长：',str(mins)+':'+str(secs))
#     #decode('gbk','ignore')
#     #.replace(u'\xa0', u'')
#     print(u'歌手：',artist)
#     print(u'专辑：',album)
#     #其他信息
#     if contents[a].get('alias'):
#         alias = contents[a].get('alias')[0]
#         print(alias)
#     print(u'发行时间：',t2)
#     i += 1
#     print('--------------------------------------------------------------------')


# # import requests
# #
# # url = 'https://m10.music.126.net/20190730085044/771b0fa0b18f4ff8a665512d4b868b93/yyaac/545e/065b/0e52/c4653bbfee11db0fa6039818fe9869d9.m4a'
# #
# # results = requests.get(url).content
# # with open('./hhh.m4a','wb') as f:
# #     f.write(results)
#
#
# import requests
# from lxml import etree
# # 确定url地址
# url = 'https://music.163.com/artist?id=44266'
# base_url = 'https://link.hhtjim.com/163/'
#
# # 请求
# results = requests.get(url).text  #以文本方式显示
# # print(results)
#
# # 筛选数据
# dom = etree.HTML(results)
# ids = dom.xpath('//a[contains(@href,"song")]/@href')
# # print(ids)
#
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0"}
# response=requests.get(url,headers=headers)
# text=response.content.decode("utf-8")
# html=etree.HTML(text)
# singer=html.xpath("//div[@class= 'btm']/h3/@title")
# music_name=html.xpath("//td[@class='']//b/@title")
# print(music_name)
# # for song_id in ids:
# #     #过滤切割
# #     count_id = song_id.strip('/song?id=')
# #     # 过滤$符号
# #     if('$' in count_id )== False:
# #         # print(count_id)
# #         song_url = base_url + '%s'%count_id+'.mp3'
# #         # print(song_url)
# #         song_name = song_url.split('/')[-1]#切割url，以歌的id命名
# #         print(song_name)
# #         music = requests.get(song_url).content
# #         # 写入文件
# #         with open('D://数据采集课设/%s'%song_name,'wb') as file:
# #             file.write(music)
# with open("sina.txt", "a", encoding="utf-8") as fp:
#     fp.write("歌手：" + ("".join(singer)) + "\n")
#     fp.write("歌名：" + ("".join(music_name)) + "\n")