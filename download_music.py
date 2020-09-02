import requests
from lxml import etree
import os
from multiprocessing import Pool
from lxml import html
from html.parser import HTMLParser

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}

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


# 创建存储路径
pathname = 'F://数据采集课设-音乐网站/下载的音乐信息/云音乐iTunes榜/'
if not os.path.exists(pathname):
    os.mkdir(pathname)
# 获取歌曲链接的函数
def get_urls(url):
    try:
        response = requests.get(url=url,headers=headers)
        music = etree.HTML(response.text)
        music_decode= html.tostring(music[0],encoding = 'utf-8').decode("utf-8")
        music_urls = music.xpath('//ul[@class="f-hide"]/li')
        music_urls_decode = html.tostring(music_urls[0],encoding = 'utf-8').decode("utf-8")
        musiclist=[]
        for music_url in music_urls:
            url = music_url.xpath('./a/@href')[0]
            name = music_url.xpath('./a/text()')[0]
            musiclist.append({'key':name,'url':'https://link.hhtjim.com/163/'+url.split('=')[-1]+'.mp3'})
        #  多进程启动爬取
        pool.map(get_music,musiclist)
    except Exception:
        print('get_urls failed')
# 下载歌曲的函数
def get_music(url):
    try:
        # 判断歌曲是否已下载，避免网络问题导致重新爬取
        if os.path.exists(pathname+url['key']+'.mp3'):
            print('歌曲已存在')
        else:
            response = requests.get(url=url['url'],headers=headers)
            with open(pathname+url['key']+'.mp3','wb') as f:
                f.write(response.content)
                print('正在下载：'+url['key'],url['url'])
    except Exception:
        print('get_music failed')

if __name__ == '__main__':
    # 爬取的url的源代码路径
    url = 'https://music.163.com/discover/toplist?id=11641012'
    # 开启进程池
    pool = Pool()
    get_urls(url)


  # from lxml import html
        # from html.parser import HTMLParser
        #
        # # 转为string
        # tree1 = html.tostring(tree[0])
        # # 编码'utf-8'
        # tree2 = HTMLParser().unescape(tree1.decode('utf-8'))
        # print(tree2)
        # 上面的代码等价于：
        #
        # tree3 = html.tostring(tree[0], encoding='utf-8').decode('utf-8')
        # print(tree3)