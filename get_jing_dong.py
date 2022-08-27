#encoding='utf-8

import requests
import re


def getHTMLText(url):
    try:  # 利用前面的代码框架返回页面的text
        r = requests.get(url, timeout=30, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}, cookies={
                         'cookie': '你的cookie'})
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''


def parsePage(ilt, html):
    try:
        # 商品价格由数字和小数点组成所以用[\d.]*\.[\d]*来表示
        plt = re.findall(r'\<i\>[\d]*\.[\d]*\<\/i\>', html)
        tlt = re.findall(r'\<em\>.*相机.*\<\/em\>', html)
        for i in range(len(plt)):
            price = plt[i][3:-4]  # 直接利用python字符串特性得到价格
            if re.findall(r'.*京品数码.*', tlt[i]) or re.findall(r'.*京东国际.*', tlt[i]) or re.findall(r'.*京东超市.*', tlt[i]):
                # 通过最小匹配来得到第一个<之前的内容
                title = re.findall(r'span\>.*?\<', tlt[i])[0][5:-1]+'相机'
            else:
                # 同样的方法获得其他类型商品名称
                title = re.findall(r'em\>.*?\<', tlt[i])[0][3:-1]+'相机'
            ilt.append([price, title])
    except:
        print("")


def printGoodLists(ilt):
    tplt = "{:4}\t{:8}\t{:16}"  # 给出打印模板，第一个长度为4，第二个长度为8，最后一个长度为16
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for goods in ilt:
        count += 1
        print(tplt.format(count, goods[0], goods[1]))
    print("")


goods = '相机'
depth = 3
startUrl = 'https://search.jd.com/Search?keyword='+goods+'&enc=utf-8'
infoList = []
for i in range(depth):  # 这里通过循环来查询多个页面并保存再infoList中
    try:
        page = i*2+1
        url = startUrl+'&page='+str(page)  # 利用之前观察的页面url来设定每个页面的url
        html = getHTMLText(url)
        parsePage(infoList, html)
    except:
        continue
printGoodLists(infoList)
