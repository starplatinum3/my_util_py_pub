
# copcy 

from myfile import copyfile_lst, get_src_dst_list_re

# from_path
# node_m
node_modules_dir=r"D:\proj\springShort\white\White-Jotter\wj-vue\node_modules"
# D:\proj\springShort\white\White-Jotter\wj-vue\node_modules
import os

# import os
import shutil

files=os.listdir(node_modules_dir)
# os. 
dst_path_root =r"D:\nodeFiles2"
for f in files:
    
    if "sass" in f:
        abs_path=os.path.join(node_modules_dir,f)
        # print(f)
        print(abs_path)
        from_path=abs_path
        # dst_path
        dst_path=os.path.join(dst_path_root,f)
        file_lst=[]
        dst_lst=[]
        ignore_dir_lst=[]
        re_lst=None
        # get_src_dst_list_re(from_path, dst_path, file_lst, dst_lst,
        #                 ignore_dir_lst, re_lst)
        # print("file_lst", file_lst)
        # print("dst_lst", dst_lst)
        print("from_path",from_path)
        print("dst_path",dst_path)
        # shutil.copytree(from_path, dst_path)
        # print('copy dir finished!')


# source_path = os.path.abspath(r'E:\Projects\source_dir')
# target_path = os.path.abspath(r'E:\Projects\new folder\target_dir')

# if not os.path.exists(target_path):
#     # 如果目标路径不存在原文件夹的话就创建
#     os.makedirs(target_path)

# if os.path.exists(source_path):
#     # 如果目标路径存在原文件夹的话就先删除
#     shutil.rmtree(target_path)

# shutil.copytree(source_path, target_path)
# print('copy dir finished!')

# python 复制整个文件夹
# get_src_dst_list_re(from_path, dst_path, file_lst, dst_lst,
#                         ignore_dir_lst, re_lst)

# from_path =node_modules_dir
# dst_path =r"D:\nodeFiles2"
# file_lst=[]
# dst_lst=[]
# ignore_dir_lst=[]
# re_lst=["sass"]
# get_src_dst_list_re(from_path, dst_path, file_lst, dst_lst,
#                         ignore_dir_lst, re_lst)

#                         # python  创建文件夹
# print("file_lst", file_lst)
# print("dst_lst", dst_lst)
# copyfile_lst(file_lst,dst_lst)