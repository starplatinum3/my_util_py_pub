
import os
fileDir=r"D:\Dump20220818-ry激励 (1)"

import time


def get_now_time_str():
    now_time_str = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    return now_time_str

# os.path.dirname
# os.path.join(fileDir)
# os.path.
# os.path.split(fileDir)
# os.path.splitext(fileDir)
# python 遍历文件夹下所有文件
#  filenames=os.listdir(r'E:\test')

# =os.listdir(r'E:\test')
all_data=""
for root, dirs, files in os.walk(fileDir):
    # print(root)
    # print(dirs)
    print(files)
    for fi in files:
        abs_path=os.path.join(root,fi)
        with open(abs_path,"r",encoding='utf-8') as f:
            data=f.read()
        all_data+=data+"\n"
print("all_data")
print(all_data)

# def 
# def 
# 删除注释
def rm_comment(data):
    lines=data.split("\n")
    out=""
    for line in lines:
        if line.startswith("--") or line.startswith("/*"):
            continue
        out+=line+"\n"
    return out

all_data=rm_comment(all_data)
# all_data.split
    # os.path.join(root,)
    # with open()
# now_time_str=os.path.split(fileDir)[1]
abs_out_file_path=os.path.join(fileDir,f"all_data_{get_now_time_str()}.sql")
# with open(abs_out_file_path,"w",encoding='utf-8') as f:
#     f.write(all_data)
# encoding='utf-8'
# encoding='gbk'
with open(abs_out_file_path,"w",encoding='gbk') as f:
    f.write(all_data)

print("abs_out_file_path")
print(abs_out_file_path)
