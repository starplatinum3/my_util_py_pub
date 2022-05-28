


import requests
# https://blog.csdn.net/qq_37616069/article/details/80376776
kw = {'id':'504481'}

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

# params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
response = requests.get("https://music.163.com/#/song", params = kw, headers = headers)
# 拿不到数据 歌曲的名字

# 查看响应内容，response.text 返回的是Unicode格式的数据
print (response.text)

# 查看响应内容，response.content返回的字节流数据
print (response.content)

# 查看完整url地址
print( response.url)

# 查看响应头部字符编码
print (response.encoding)

# 查看响应码
print (response.status_code)