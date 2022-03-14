
from time import time
# from tkinter.messagebox import NO
import requests

import os

from time_util import get_now_time_str



def read_key_words():
    # key_words
    path=r"key_words\奥特曼中文关键词检索 - 国语.csv"
    with open(path,"r",encoding="utf-8") as f:
        data=f.read()
    key_words=data.split("\n")
    # key_words.
    # key_words=map(trim,key_words)
    # key_words_trimd=[]
    # for i in key_words:
    #     one=i.strip()
    #     one=one.replace(" ","")
    #     # key_words_trimd.append(i.strip())
    #     key_words_trimd.append(one)
    # print(key_words_trimd)
    return key_words


def get_keywords(word):
    url=f"https://www.baidu.com/sugrec?pre=1&ie=utf-8&json=1&prod=pc&wd={word}"
    html=requests.get(url)
    html=html.json()
    #print(html)
    #print(html['g'])
    key_words=[]
    if 'g' not in html:
        print("此关键词没有找到",word)
        return
    # if html['g']==None
    for key_word in html['g']:
        # print(key_word['q'])
        key_words.append(key_word['q'])
    #print(key_words)
    return key_words

# words=["迪迦","盖亚"]
# words=["特仑苏","AD钙奶"]
# key_words=get_keywords("好人")
# print(key_words)


def  list_to_file(lst):
    out_data=""
    for i in lst:
        out_data+=i+"\n"
    # with open()
    return out_data
    

def  list_to_data(lst):
    out_data=""
    for i in lst:
        out_data+=i+"\n"
    # with open()
    return out_data


import time

def start():
    dir="key_words"
    for word in words:
        key_words=get_keywords(word)
        if key_words==None:
            continue
        data=list_to_data(key_words)
        now_time=get_now_time_str()
        out_path=os.path.join(dir,f"{word}_{now_time}.txt")
        with open(out_path,"w+",encoding="utf-8") as f:
            f.write(data)
        print("文件输出",out_path)
        # time.sle
        # python sleep 
        time.sleep(3)
  


# 好人一生平安
# 好人坏人可否分
# 好人不长命 祸害遗千年,下一句是什么
# 好人好事有哪些
# 好人平安
# 好人卡是什么意思?
# 好人好事
# 好人多的歌词
# 好人有好报
# 好人自有好人报是什么生肖
# ['好人一生平安', '好人坏人可否分', '好人不长命 祸害遗千年,下一句是什么', '好人好事有哪些', '好人平安', '好人卡是什么意思?', '好人好事', '好人多的歌词', '好人有好报', '好人自有好人报是什么生肖']

# key_words=read_key_words()
words=read_key_words()
print("开始")
start()