import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
# import date_util
from date_util import DateUtil

plt.rcParams['font.sans-serif'] = [u'SimHei']

# filename=r"G:\edgeDownload\作家数据模板 (1).xlsx"
# filename=r"G:\project\springbootProj\writer\writer_iot\gitignore\入会时间格式恶心3055.xlsx"
filename=r"G:\project\springbootProj\writer\writer_iot\gitignore\入会时间格式恶心3055.csv"
# data=pd.read_csv(filename,encoding="utf-8")
# data=pd.read_csv(filename)
data=pd.read_csv(filename,encoding="gbk")
# data = pd.read_excel(filename)

# data["加入协会日期"].apply(lambda x:parse_date(x))


data["加入协会日期"]=data["加入协会日期"].apply(lambda x:DateUtil.parse_date(x))

# out_file_name=r"G:\file\学校\python数据分析\writer_date_format.xlsx"
# out_file_name=r"G:\project\springbootProj\writer\writer_iot\gitignore\修改掉恶心的时间.xlsx"
out_file_name=r"G:\project\springbootProj\writer\writer_iot\gitignore\修改掉恶心的时间.csv"
# pandas 保存 xlsx
# data.to_excel(out_file_name,sheet_name="sheetname",index=False)
# data.to_csv(out_file_name,sheet_name="sheetname",index=False)
data.to_csv(out_file_name,index=False)

print("write here",out_file_name)