import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
# import date_util
from date_util import DateUtil

plt.rcParams['font.sans-serif'] = [u'SimHei']
print("start read")
is_read_scv=True
if is_read_scv:

# filename=r"G:\edgeDownload\作家数据模板 (1).xlsx"
# filename=r"G:\project\springbootProj\writer\writer_iot\gitignore\入会时间格式恶心3055.xlsx"
# filename=r"G:\project\springbootProj\writer\writer_iot\gitignore\修改掉恶心的时间.xlsx"
# xlsx 读入的话 很奇怪 日期有问题
# filename=r"G:\project\springbootProj\writer\writer_iot\gitignore\入会时间格式恶心3055.csv"
    filename=r"G:\project\springbootProj\writer\writer_iot\gitignore\修改掉恶心的时间.csv"

    # data=pd.read_csv(filename,encoding="utf-8")
    # data=pd.read_csv(filename)
    data=pd.read_csv(filename,encoding="gbk")
    # data = pd.read_excel(filename)
else:
    filename=r"G:\project\springbootProj\writer\writer_iot\gitignore\修改掉恶心的时间.xlsx"
    # data=pd.read_csv(filename,encoding="gbk")
    data = pd.read_excel(filename)

# data["加入协会日期"].apply(lambda x:parse_date(x))

change_map={
     "宁波市":"宁波市作家协会",
     "宁波市 ":"宁波市作家协会",
     "温州（转会）":"温州市作家协会",
"温州市":"温州市作家协会",

"嘉兴（转会）":"嘉兴市作家协会",
"嘉兴市":"嘉兴市作家协会",
"嘉兴（转会）":"嘉兴市作家协会",
"湖州市":"湖州市作家协会",
"绍兴市":"绍兴市作家协会",
"舟山市":"舟山市作家协会",
"金华市":"金华市作家协会",
"衢州市":"衢州市作家协会",
"台州市":"台州市作家协会",
" 台州市":"台州市作家协会",
"丽水市":"丽水市作家协会",
    "杭州（转会）":"杭州市作家协会",
    "杭州市":"杭州市作家协会",
"杭州市（转会）":"杭州市作家协会",
"杭州市 ":"杭州市作家协会",
"其他高等院校":"在杭其他高校",
"其他高等院校（转会）":"在杭其他高校",
"省出版界（转会）":"省出版界",
"省电力作协":"省电力作家协会",
"省交通作协":"省交通作家协会",
"省金融作协":"省金融作家协会",
"省邮政作协":"省邮政作家协会",

"中央及省直新闻单位":"中央驻浙新闻单位",

}

# team_col=data["所属协会"]
# pandas 修改一个格子 如果

# https://www.jianshu.com/p/36a7c85b7243
for from_word,to_word in change_map.items():
    data["所属协会"].replace(from_word,to_word,inplace=True)
    # print(key+':'+value)
    # data[data["所属协会"]==from_word]=to_word
    # team_col[team_col]

# python 遍历 map 
# for i in change_map:

# data["加入协会日期"]=data["加入协会日期"].apply(lambda x:DateUtil.parse_date(x))
# data[data["所属协会"]=="省作协"]

# print(data[data["所属协会"]=="杭州（转会）"])
# data[data["所属协会"]=="杭州（转会）"]="杭州市作家协会"
# # 不要的字段确实删掉了
# print(data[data["所属协会"]=="杭州（转会）"])

# out_file_name=r"G:\file\学校\python数据分析\writer_date_format.xlsx"
# out_file_name=r"G:\project\springbootProj\writer\writer_iot\gitignore\修改掉恶心的时间.xlsx"
# out_file_name=r"G:\project\springbootProj\writer\writer_iot\gitignore\修改掉恶心的时间.csv"
# out_file_name=r"G:\project\springbootProj\writer\writer_iot\gitignore\名字修改成符合系统的.xlsx"

out_csv=True
if out_csv:
    out_file_name=r"G:\project\springbootProj\writer\writer_iot\gitignore\名字修改成符合系统的.csv"
    # pandas 保存 xlsx
    # data.to_excel(out_file_name,sheet_name="sheetname",index=False)
    # data.to_csv(out_file_name,sheet_name="sheetname",index=False)
    data.to_csv(out_file_name,index=False)
else:
    out_file_name=r"G:\project\springbootProj\writer\writer_iot\gitignore\名字修改成符合系统的.xlsx"
    data.to_excel(out_file_name,sheet_name="sheetname",index=False)

print("write here",out_file_name)