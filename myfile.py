import os
# from os.path import getsize

# import requests
# https://www.jianshu.com/p/546a0c1d89e7
from strUtil.strUtil import sub_strs_start_end_all
# import os
# import direction
# from .direction import *
import sys
import strUtil.strUtil


# !/usr/bin/python

# import os
# import sys


# import myUtil.direction


def lst_file(dir):
    for i in os.listdir(dir):
        if '.cpp' in i:
            print(i)


def lst_file_with_name(name, dir=None):
    lst = []
    for i in os.listdir(dir):
        if name in i:
            lst.append(i)
    # print(lst)
    return lst


def get_dir_files_abs_name(with_word, dir):
    filenames_relative = lst_file_with_name(with_word, dir)
    filenames_abs = [get_absolute_path(dir, filename) for filename in filenames_relative]
    return filenames_abs


def test():
    # base_dir=r"D:\人口普查"
    base_dir = "D:/人口普查"
    # 左斜线 也是可以为路径的
    lst_file_with_name(".xlsx", base_dir)


# def rename_file(old_name,new_name):
#     file=open(old_name)


# https://www.py.cn/jishu/jichu/14726.html
def rename_files_in_path(input_path,
                         output_path, dont_want="", suffix=".mp4"):
    # os.rename(os.path.join(path,old_name),os.path.join(path,mark+old_name))  #子文件夹重命名

    # mark = 'test-'  #准备添加的前缀内容
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    old_names = os.listdir(input_path)  # 取路径下的文件名，生成列表

    for old_name in old_names:  # 遍历列表下的文件名

        if old_name != sys.argv[0]:  # 代码本身文件路径，防止脚本文件放在path路径下时，被一起重命名
            new_path = os.path.join(output_path, strUtil.strUtil.make_str_4_0(old_name.replace(dont_want, ""))) + suffix
            # print("new_path:",new_path)
            os.rename(os.path.join(input_path, old_name), new_path)  # 子文件夹重命名

            # print (old_name,"has been renamed successfully! New name is: ",mark+old_name)

    print("done")


# https://www.cnblogs.com/windysai/p/10150041.html
def print_files(path):
    lsdir = os.listdir(path)
    dirs = [i for i in lsdir if os.path.isdir(os.path.join(path, i))]
    if dirs:
        for i in dirs:
            print_files(os.path.join(path, i))
    files = [i for i in lsdir if os.path.isfile(os.path.join(path, i))]
    for f in files:
        print(os.path.join(path, f))


# def print_files_if(path, cond_func):
#     lsdir = os.listdir(path)
#     dirs = [i for i in lsdir if os.path.isdir(os.path.join(path, i))]
#     if dirs:
#         for i in dirs:
#             print_files_if(os.path.join(path, i), cond_func)
#     files = [i for i in lsdir if os.path.isfile(os.path.join(path, i))]
#     for f in files:
#         if cond_func(f):
#             print(os.path.join(path, f))

# https://www.cnblogs.com/yunguoxiaoqiao/p/7626992.html
# https://blog.csdn.net/shahuzi/article/details/81211763
def print_files_if(path, cond_func, **kwargs):
    # print("print_files_if  kwargs:",kwargs)
    lsdir = os.listdir(path)
    dirs = [i for i in lsdir if os.path.isdir(os.path.join(path, i))]
    if dirs:
        for i in dirs:
            print_files_if(os.path.join(path, i), cond_func, **kwargs)
    files = [i for i in lsdir if os.path.isfile(os.path.join(path, i))]
    for f in files:
        # 文件名字 像什么
        if cond_func(f, kwargs["like_what"]):
            abs_path = os.path.join(path, f)
            # print(os.path.join(path, f))
            print(abs_path)


# def get_files_if(path, file_lst: list, cond_func, **kwargs):
#     lsdir = os.listdir(path)
#     dirs = [i for i in lsdir if os.path.isdir(os.path.join(path, i))]
#     if dirs:
#         for dir in dirs:
#             if "ignore_dir_lst" in kwargs:
#                 ignore_dir_lst = kwargs["ignore_dir_lst"]
#                 # if cond_name_like(dir,"")
#                 if dir in ignore_dir_lst:
#                     continue
#             # for ignore_dir in ignore_dir_lst:
#             #     # if cond_name_like(dir,ignore_dir):
#             #     if dir==ignore_dir:
#             #         continue
#             get_files_if(os.path.join(path, dir), file_lst, cond_func, **kwargs)
#     files = [i for i in lsdir if os.path.isfile(os.path.join(path, i))]
#     for f in files:
#         # 文件名字 像什么
#         print("f", f)
#         if cond_func(f, kwargs["like_what"]):
#             abs_path = os.path.join(path, f)
#             # print(os.path.join(path, f))
#             print(abs_path)
#             file_lst.append(abs_path)


def get_files_if(path, file_lst: list, like_str_lst: list, ignore_dir_lst: list):
    lsdir = os.listdir(path)
    dirs = [i for i in lsdir if os.path.isdir(os.path.join(path, i))]
    print("path", path)
    if dirs:
        for dir in dirs:
            # ignore_dir_lst = kwargs["ignore_dir_lst"]
            # if cond_name_like(dir,"")
            if dir in ignore_dir_lst:
                continue
            # print()
            # if "ignore_dir_lst" in kwargs:
            #     ignore_dir_lst = kwargs["ignore_dir_lst"]
            #     # if cond_name_like(dir,"")
            #     if dir in ignore_dir_lst:
            #         continue
            # for ignore_dir in ignore_dir_lst:
            #     # if cond_name_like(dir,ignore_dir):
            #     if dir==ignore_dir:
            #         continue
            # get_files_if(os.path.join(path, dir), file_lst, cond_func, **kwargs)
            get_files_if(os.path.join(path, dir), file_lst, like_str_lst, ignore_dir_lst)
            # 深入一层
    files = [i for i in lsdir if os.path.isfile(os.path.join(path, i))]
    for f in files:
        # 文件名字 像什么
        # print("f", f)
        for like_str in like_str_lst:
            if cond_name_like(f, like_str):
                abs_path = os.path.join(path, f)
                # print(os.path.join(path, f))
                # print(abs_path)
                file_lst.append(abs_path)
        # if cond_func(f, kwargs["like_what"]):
        #     abs_path = os.path.join(path, f)
        #     # print(os.path.join(path, f))
        #     print(abs_path)
        #     file_lst.append(abs_path)


# def get_src_dst_list(src, dst, src_lst: list, dst_lst: list,
#                      like_str_lst: list, ignore_dir_lst: list, ignore_filename_lst):
#     lsdir = os.listdir(src)
#     dirs = [i for i in lsdir if os.path.isdir(os.path.join(src, i))]
#     print("path", src)
#     print("dst", dst)
#     if dirs:
#         for dir in dirs:
#             # ignore_dir_lst = kwargs["ignore_dir_lst"]
#             # if cond_name_like(dir,"")
#             if dir in ignore_dir_lst:
#                 continue
#             # print()
#             # if "ignore_dir_lst" in kwargs:
#             #     ignore_dir_lst = kwargs["ignore_dir_lst"]
#             #     # if cond_name_like(dir,"")
#             #     if dir in ignore_dir_lst:
#             #         continue
#             # for ignore_dir in ignore_dir_lst:
#             #     # if cond_name_like(dir,ignore_dir):
#             #     if dir==ignore_dir:
#             #         continue
#             # get_files_if(os.path.join(path, dir), file_lst, cond_func, **kwargs)
#             get_src_dst_list(os.path.join(src, dir),
#                              os.path.join(dst, dir), src_lst,
#                              dst_lst, like_str_lst, ignore_dir_lst, ignore_filename_lst)
#             # dst  也相应的 增加 后面的 后缀
#             # 深入一层
#     # files=[]
#     # dst_files=[]
#     # for i in lsdir:
#     #     if os.path.isfile(os.path.join(src, i)):
#     #         files.append(i)
#     #         dst_files.append()
#     files = [i for i in lsdir if os.path.isfile(os.path.join(src, i))]
#     # dst_files = [i for i in lsdir if os.path.isfile(os.path.join(dst, i))]
#     idx = 0
#     for f in files:
#         # 文件名字 像什么
#         # print("f", f)
#         for like_str in like_str_lst:
#             if cond_name_like(f, like_str) and f not in ignore_filename_lst:
#                 abs_path = os.path.join(src, f)
#                 abs_path_dst = os.path.join(dst, f)
#                 # print(os.path.join(path, f))
#                 # print(abs_path)
#                 src_lst.append(abs_path)
#                 dst_lst.append(abs_path_dst)
#         idx += 1


def get_src_dst_list(src, dst, src_lst: list, dst_lst: list,
                     ignore_dir_lst: list, ignore_filename_lst):
    lsdir = os.listdir(src)
    dirs = [i for i in lsdir if os.path.isdir(os.path.join(src, i))]
    print("path", src)
    print("dst", dst)
    if dirs:
        for dir in dirs:
            # ignore_dir_lst = kwargs["ignore_dir_lst"]
            # if cond_name_like(dir,"")
            if dir in ignore_dir_lst:
                continue
            # print()
            # if "ignore_dir_lst" in kwargs:
            #     ignore_dir_lst = kwargs["ignore_dir_lst"]
            #     # if cond_name_like(dir,"")
            #     if dir in ignore_dir_lst:
            #         continue
            # for ignore_dir in ignore_dir_lst:
            #     # if cond_name_like(dir,ignore_dir):
            #     if dir==ignore_dir:
            #         continue
            # get_files_if(os.path.join(path, dir), file_lst, cond_func, **kwargs)
            get_src_dst_list(os.path.join(src, dir),
                             os.path.join(dst, dir), src_lst,
                             dst_lst, ignore_dir_lst, ignore_filename_lst)
            # dst  也相应的 增加 后面的 后缀
            # 深入一层
    # files=[]
    # dst_files=[]
    # for i in lsdir:
    #     if os.path.isfile(os.path.join(src, i)):
    #         files.append(i)
    #         dst_files.append()
    files = [i for i in lsdir if os.path.isfile(os.path.join(src, i))]
    # dst_files = [i for i in lsdir if os.path.isfile(os.path.join(dst, i))]
    idx = 0
    for f in files:
        # 文件名字 像什么
        # print("f", f)
        if f not in ignore_filename_lst:
            # for like_str in like_str_lst:
            #     if cond_name_like(f, like_str) and f not in ignore_filename_lst:
            abs_path = os.path.join(src, f)
            abs_path_dst = os.path.join(dst, f)
            # print(os.path.join(path, f))
            # print(abs_path)
            src_lst.append(abs_path)
            dst_lst.append(abs_path_dst)
        idx += 1


def get_src_dst_list_re(src, dst, src_lst: list, dst_lst: list,
                        ignore_dir_lst: list, re_lst):
    lsdir = os.listdir(src)
    dirs = [i for i in lsdir if os.path.isdir(os.path.join(src, i))]
    # print("path", src)
    # print("dst", dst)
    if dirs:
        for dir in dirs:
            # ignore_dir_lst = kwargs["ignore_dir_lst"]
            # if cond_name_like(dir,"")
            if dir in ignore_dir_lst:
                continue
            # print()
            # if "ignore_dir_lst" in kwargs:
            #     ignore_dir_lst = kwargs["ignore_dir_lst"]
            #     # if cond_name_like(dir,"")
            #     if dir in ignore_dir_lst:
            #         continue
            # for ignore_dir in ignore_dir_lst:
            #     # if cond_name_like(dir,ignore_dir):
            #     if dir==ignore_dir:
            #         continue
            # get_files_if(os.path.join(path, dir), file_lst, cond_func, **kwargs)
            get_src_dst_list_re(os.path.join(src, dir),
                                os.path.join(dst, dir), src_lst,
                                dst_lst, ignore_dir_lst, re_lst)
            # dst  也相应的 增加 后面的 后缀
            # 深入一层
    # files=[]
    # dst_files=[]
    # for i in lsdir:
    #     if os.path.isfile(os.path.join(src, i)):
    #         files.append(i)
    #         dst_files.append()
    files = [i for i in lsdir if os.path.isfile(os.path.join(src, i))]
    # dst_files = [i for i in lsdir if os.path.isfile(os.path.join(dst, i))]
    # idx = 0
    for f in files:
        # 文件名字 像什么
        # print("f", f)
        if re_lst is None:
            # 如果是 none 的话，就不管什么样子都放进去了
            abs_path = os.path.join(src, f)
            abs_path_dst = os.path.join(dst, f)
            # print(os.path.join(path, f))
            # print(abs_path)
            src_lst.append(abs_path)
            dst_lst.append(abs_path_dst)
            continue

        for re_str in re_lst:
            if re.search(re_str, f):
                abs_path = os.path.join(src, f)
                abs_path_dst = os.path.join(dst, f)
                # print(os.path.join(path, f))
                # print(abs_path)
                src_lst.append(abs_path)
                dst_lst.append(abs_path_dst)

        # if f not in ignore_filename_lst:
        #     # for like_str in like_str_lst:
        #     #     if cond_name_like(f, like_str) and f not in ignore_filename_lst:
        #     abs_path = os.path.join(src, f)
        #     abs_path_dst = os.path.join(dst, f)
        #     # print(os.path.join(path, f))
        #     # print(abs_path)
        #     src_lst.append(abs_path)
        #     dst_lst.append(abs_path_dst)
        # idx += 1


# def print_files_if_name_like(path,like_what):
#     # todo
#     print_files_if(path,cond_func=cond_name_like)
# 中间传递的时候 需要kwargs
def print_files_if_name_like(path, **kwargs):
    # todo
    # print("kwargs:",kwargs)
    print_files_if(path, cond_func=cond_name_like, **kwargs)


def get_files_if_name_like(path, file_lst: list, **kwargs):
    # todo
    # print("kwargs:",kwargs)
    get_files_if(path, file_lst, cond_func=cond_name_like, **kwargs)
    # return file_lst


def print_files_if_name_like_ignore_case(path, **kwargs):
    # todo
    # print("kwargs:",kwargs)
    print_files_if(path, cond_func=cond_name_like_ignore_case, **kwargs)


# def cond_name_like(**kwargs):
#     filename=kwargs["filename"]
#     like_what=kwargs["like_what"]
#     return filename.find(like_what)!=-1

# 最后不用kwargs 只要对号入座就好了
def cond_name_like(filename, like_what):
    return filename.find(like_what) != -1
    # https://www.runoob.com/python/att-string-find.html


# python ignore_case 字符串
# python lower
def cond_name_like_ignore_case(filename, like_what):
    filename = str.lower(filename)
    like_what = str.lower(like_what)
    return filename.find(like_what) != -1


def print_files_if_kind(path, kind):
    lsdir = os.listdir(path)
    dirs = [i for i in lsdir if os.path.isdir(os.path.join(path, i))]
    if dirs:
        for i in dirs:
            print_files_if_kind(os.path.join(path, i), kind)
    files = [i for i in lsdir if os.path.isfile(os.path.join(path, i))]
    for f in files:
        if f.endswith(kind):
            print(os.path.join(path, f))


# 如果file 是一个情况
# 递归所有文件
def print_files_if_size(path, size):
    try:
        lsdir = os.listdir(path)
    except  PermissionError as e:
        print(e)
        return
        # https://blog.csdn.net/weixin_44828950/article/details/91471459

    dirs = [i for i in lsdir if os.path.isdir(os.path.join(path, i))]
    if dirs:
        for i in dirs:
            print_files_if_size(os.path.join(path, i), size)
    files = [i for i in lsdir if os.path.isfile(os.path.join(path, i))]
    for f in files:
        abs_file_path = os.path.join(path, f)
        path_size = os.path.getsize(abs_file_path)
        if path_size > size:
            print(abs_file_path)
            print("size:", path_size, "B, ", path_size / 1000, "KB, ", path_size / 1000 / 1000, "MB")


# unit 单位
def print_files_if_size_with_unit(path, size, unit):
    mp = {"MB": 1000000, "KB": 1000}
    if unit not in mp:
        print("单位有错误")
        return
    size *= mp[unit]
    print_files_if_size(path, size)


# print_files(sys.argv[1])

def make_file_3_0():
    input_path = r"E:\1 file\output"
    output_path = r"E:\1 file\output"

    old_names = os.listdir(input_path)  # 取路径下的文件名，生成列表

    for old_name in old_names:  # 遍历列表下的文件名

        if old_name != sys.argv[0]:  # 代码本身文件路径，防止脚本文件放在path路径下时，被一起重命名

            os.rename(os.path.join(input_path, old_name),
                      os.path.join(output_path, strUtil.strUtil.make_str_some_0(old_name, 3)))  # 子文件夹重命名

    print("done")


def add_suffix():
    suffix = ".mp4"
    input_path = r"E:\1 file\output"
    output_path = r"E:\1 file\output"

    old_names = os.listdir(input_path)  # 取路径下的文件名，生成列表

    for old_name in old_names:  # 遍历列表下的文件名

        if old_name != sys.argv[0]:  # 代码本身文件路径，防止脚本文件放在path路径下时，被一起重命名

            os.rename(os.path.join(input_path, old_name),
                      os.path.join(output_path, old_name + suffix))  # 子文件夹重命名

    print("done")




def change_name(output_path):
    dir_get = r"E:\1 file\1"
    dirs = os.listdir(dir_get)  # 取路径下的文件名，生成列表

    # output_path = myUtil.direction.out_put_file_dir
    cnt = 0
    for dir in dirs:
        old_path = os.path.join(dir_get, dir)
        print(old_path)
        if os.path.getsize(old_path) == 131072: continue
        new_path = os.path.join(output_path, str(cnt))
        print("old_path: ", old_path)
        rename_files_in_path(old_path, new_path)
        cnt += 1

    print("all done")


def get_absolute_paths(dir, relative_file_names):
    absolute_paths = []
    for name in relative_file_names:
        absolute_paths.append(os.path.join(dir, name))

    return absolute_paths


def get_absolute_path(dir, file_name):
    return os.path.join(dir, file_name)


def get_absolute_path_by_a_list(dirs):
    path = dirs[0]
    # e:/ doawnloa
    list_len = len(dirs)
    if list_len == 1: return path
    for i in range(1, list_len):
        path += "\\" + dirs[i]
    return path


# 左斜线
def to_back_slash(path_str):
    return path_str.replace("\\", "/")


def cmd():
    """
    #     https://www.jianshu.com/p/cf1e61eb6fc8
    # //截取从头开始的30s
    # ffmpeg -ss 00:00:00 -t 00:00:30 -i keyoutput.mp4 -vcodec copy -acodec copy split.mp4
    # //截取从30s开始的30s
    # ffmpeg -ss 00:00:30 -t 00:00:30 -i keyoutput.mp4 -vcodec copy -acodec copy split1.mp4
    # //进行视频的合并
    # ffmpeg -f concat -i list.txt -c copy concat.mp4
    # https://www.cnblogs.com/qican/p/11468866.html
    :return: 
    """

    cut_start_time = ""
    cut_duration = ""
    resource_file = ""
    cmd = "ffmpeg -ss 00:00:00 -t 00:00:30 -i keyoutput.mp4 -vcodec copy -acodec copy split.mp4"
    os.system(cmd)


def escape_and_escape(str):
    """
    :param orgin :  r"\"
    :param to: r"\\"
    """
    return str.replace("\\", "\\\\")


def backslash_to_forwardslash(backslash):
    return backslash.replace("\\", "/")


def add_cmd(old_str, add_str):
    return old_str + " " + add_str


def absolute_mkdir(dir_name):
    if dir_name.endswith(":"):
        return
    dirs = dir_name.split("\\")
    print(dirs)
    first_dir = dir_name.strip(dirs[-1]).strip("\\")

    print(first_dir)
    absolute_mkdir(first_dir)

    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

    # os.makedirs()


# coding: utf8
import requests


def download_img(img_url, name="img", suffix=".jpg", path="E:\\file\\imgs",
                 api_token="fklasjfljasdlkfjlasjflasjfljhasdljflsdjflkjsadljfljsda"):
    print(img_url)
    header = {"Authorization": "Bearer " + api_token}  # 设置http header，视情况加需要的条目，这里的token是用来鉴权的一种方式
    r = requests.get(img_url, headers=header, stream=True)
    print(r.status_code)  # 返回状态码
    if r.status_code == 200:
        open(os.path.join(path, name) + suffix, 'wb').write(r.content)  # 将内容写入图片
        print("done")
    del r


def if_same_dirs(dir1, dir2):
    dirs1 = os.listdir(dir1)
    dirs2 = os.listdir(dir2)
    same = []
    for dir in dirs1:
        if dir in dirs2:
            same.append(dir)

    print("same:", same)


def file_look():
    root_dir = r"E:\1 file\离散数学"


def download_imgs(src_file="E:\\toDownload.txt"):
    # src_file = "E:\\toDownload.txt"

    file = open(src_file, "r")
    data = file.read()
    jpgs = sub_strs_start_end_all(data, "https", "jpg")
    pngs = sub_strs_start_end_all(data, "https", "png")
    gifs = sub_strs_start_end_all(data, "https", "gif")
    download_list(jpgs)
    download_list(pngs)
    download_list(gifs)
    file.close()


def download_list(url_list):
    cnt = 0
    for url in url_list:
        download_img(url, str(cnt), get_suffix(url))
        cnt += 1


def get_suffix(str: str):
    if str.endswith(".jpg"): return ".jpg"
    if str.endswith(".png"): return ".png"
    if str.endswith(".gif"): return ".gif"


def dir_same_file_cnt(dir: str, file_name_test):
    dir_files = os.listdir(dir)
    cnt = 0
    for file_name in dir_files:
        if file_name.startswith(file_name_test):
            cnt += 1

    return cnt


def create_file_exsists_cnt_plus_1(direction, filename, suffix, content):
    filename_cnt = dir_same_file_cnt(direction, filename)
    true_filename = os.path.join(direction, filename + "_" + str(filename_cnt) + suffix)

    with   open(true_filename, "w", encoding="utf-8") as out_file:
        out_file.write(content)

    print("put at", true_filename)


def if_kind(filename: str, kind):
    return filename.endswith(kind)


def if_is_mp4(filename: str):
    return if_kind(filename, ".mp4")


# https://blog.csdn.net/w55100/article/details/92081182
def getdirsize(dir):
    size = 0
    for root, dirs, files in os.walk(dir):
        size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
    return size


def print_dir_size(dir_path):
    size = getdirsize(dir_path)
    print("size:", size, "B, ", size / 1000, "KB, ", size / 1000 / 1000, "MB")


# dirpath = '/aaa/bbb/'
# sz = getdirsize(dirpath)
# print(sz)

def print_size(
        file_path=r"D:\project\python_project\ALBERT\venv\Lib\site-packages\numpy\.libs\libopenblas.NOIJJG62EMASZI6NYURL6JBKM4EVBGM7.gfortran-win_amd64.dll"
):
    path_size = os.path.getsize(file_path)
    print("size:", path_size, "B, ", path_size / 1000, "KB, ", path_size / 1000 / 1000, "MB")


def print_size_to_txt(read_file_path, out_file_path="file_size.txt"):
    out_data = ""
    with open(read_file_path, "r", encoding="utf-8") as f:
        file_paths = f.read()
    file_paths = file_paths.split("\n")
    for p in file_paths:
        path_size = os.path.getsize(p)
        out_data += p + "\n"
        out_data += "size:" + str(path_size) + "B, " + str(path_size / 1000) + "KB, " + str(
            path_size / 1000 / 1000) + "MB" + "\n"
    # out_file_path = "file_size.txt"
    # https://www.cnblogs.com/zhaochunhui/p/10937690.html
    # https://blog.csdn.net/weixin_39612058/article/details/110553637
    with open(out_file_path, "a", encoding="utf-8") as f:
        f.write(out_data)


def list_files_size(path=r"D:\project"):
    lst_files = os.listdir(path)
    for file in lst_files:
        abs_path = os.path.join(path, file)
        if os.path.isdir(abs_path):
            continue
        print(abs_path)
        print_size(abs_path)


def list_dir_size(path=r"D:\project"):
    # print_dir_size
    lst_files = os.listdir(path)
    for file in lst_files:
        abs_path = os.path.join(path, file)
        if os.path.isfile(abs_path):
            continue
        print(abs_path)
        print_dir_size(abs_path)


# def list_dir_if_have_file()

from strUtil.strUtil import front_del_str
from shutil import copyfile


def rename_zip_and_copy_one_dir(abs_path, out_dir, name):
    file_lst = os.listdir(abs_path)
    for file in file_lst:
        if file.startswith("31901077"):
            if "111" in file:
                continue
           
            out_file = os.path.join(out_dir, name + ".zip")
            src_file = os.path.join(abs_path, file)
            copyfile(src_file, out_file)


def rename_zip_and_copy(src_root_dir=r"E:\file\学校\web", out_dir=r"E:\web_out_dir"):
    file_lst = os.listdir(src_root_dir)
    for file in file_lst:
        print(file)
        # os.path.isfile()
        if file.startswith("实验"):
            abs_path = os.path.join(src_root_dir, file)
            rename_zip_and_copy_one_dir(abs_path, out_dir, file)


# https://www.jb51.net/article/169026.htm

src_dir = r"G:\file\学校\python应用\share"
greped_dir = r"G:\file\学校\python应用\exs_grep"


def grep_exs_ex_level(ex_abs_path, greped_dir):
    for filename in os.listdir(ex_abs_path):
        if filename.endswith(".py") or filename.endswith(".csv") or \
                filename.endswith(".ipynb") or filename.endswith(".png") \
                or filename.endswith(".mhtml"):
            abs_path = os.path.join(ex_abs_path, filename)
            copyfile(abs_path, )


def grep_exs(src_dir, greped_dir):
    for ex in os.listdir(src_dir):
        ex_abs_path = os.path.join(src_dir, ex)
        for filename in os.listdir(ex_abs_path):
            if filename.endswith(".py") or filename.endswith(".csv") or \
                    filename.endswith(".ipynb") or filename.endswith(".png") \
                    or filename.endswith(".mhtml"):
                abs_path = os.path.join(ex_abs_path, filename)


# python gitignore
# python 以 结尾的 文件

import os, re, time


# https://www.cnblogs.com/monogem/p/11367914.html
# def find_end_of():
#
#     name = 'linuxday01'
#     flags = True
#     # 文件夹bi_test中的文件列表
#     dir_path='E:\\bi_test'
#     # print (os.listdir('E:\\bi_test'))
#     while flags:
#         for f in os.listdir(dir_path):
#             # 寻找以name开头，以.download结尾的文件
#             if re.search(name + '\.(.*)\.download$', f):
#                 print f
#                 print '没有完成'
#                 time.sleep(5)
#     #flags =False
#     print '完成'
#     # 当前时间print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
#
# gitignore 不想复制
# 想备份的只有代码 .java
def test_re():
    # str1="hidahidhai.download"
    str1 = ".hidahidhai.download"
    # python  正则
    # .(%s).
    # res = re.search('\.(.*)\.download$', str1)
    # print("str1", str1)
    # print("res", res)
    # https://zhidao.baidu.com/question/265872507.html
    # str1="hidahidhai.download"
    # res None
    # str1 .hidahidhai.download
    # res <re.Match object; span=(0, 20), match='.hidahidhai.download'>
    # print(res.group())
    # print(res.group(0))
    # str1 .hidahidhai.download
    # res <re.Match object; span=(0, 20), match='.hidahidhai.download'>
    # .hidahidhai.download
    # .hidahidhai.download
    end_with = "download$"
    str_lst = ["31231.zip", "zip."]
    # have  31231.zip
    str2 = "31231.zip"
    for i in str_lst:
        res2 = re.search("zip$", i)
        if res2:
            print("have ", i)
        # zip
        # print(res2.group())
    # str1 = ".hidahidhai.download"


# https://blog.csdn.net/qq_42455710/article/details/88861296
def copy_file_force(src, dst):
    dst_dirname = os.path.dirname(dst)
    if not os.path.exists(dst_dirname):
        os.makedirs(dst_dirname)
    # os.makedirs(dst_dirname)
    copyfile(src, dst)


def copy_file_not_cover(src, dst):
    if os.path.exists(dst):
        print("已经存在", dst)
        return
    copy_file_force(src, dst)
    # dst_dirname = os.path.dirname(dst)
    # if not os.path.exists(dst_dirname):
    #     os.makedirs(dst_dirname)
    # # os.makedirs(dst_dirname)
    # copyfile(src, dst)


def write_list_to_file(filename, lst, split):
    data = ""
    for i in lst:
        data += i + split
    with open(filename, "w") as f:
        # f.writelines(ignore_dir_lst)
        # 这没有回车啊
        f.write(data)


# def write_list_to_file_test():
#     write_list_to_file("copy_file_pattern/ignore_dir_lst.txt", ignore_dir_lst, "\n")
#     # with open("copy_file_pattern/ignore_dir_lst.txt","w") as f:
#     #     f.writelines(ignore_dir_lst)
#     #     # 这没有回车啊
#     #     data=""
#     #     for i in ignore_dir_lst:
#     #         data+=i+"\n"
#     write_list_to_file("copy_file_pattern/like_str_list.txt", like_str_list, "\n")
#     write_list_to_file("copy_file_pattern/ignore_filename_lst.txt", ignore_filename_lst, "\n")
#     # with open("copy_file_pattern/like_str_list.txt", "w") as f:
#     #     f.writelines(like_str_list)
#     # with open("copy_file_pattern/ignore_filename_lst.txt", "w") as f:
#     #     f.writelines(ignore_filename_lst)


def copyfile_lst(src_lst, dst_lst):
    idx = 0
    for src in src_lst:
        dst = dst_lst[idx]
        copy_file_not_cover(src, dst)
        idx += 1


def backup_proj_src():
    # proj_path = r"G:\project\springbootProj\writer\writer-vue-new\writer-vue-new"
    # proj_path = r"G:\project\springbootProj\writer-new2\writer-new"
    # proj_path = r"G:\project\Android\LoginApplication\LoginApplication"
    # proj_path = r"G:\project\Android\AccountingMainLayoutSteps"
    # proj_path = r"G:\project\Android\moments"
    # proj_path = r"G:\project\springbootProj\kinect3"
    
    
    # proj_path = r"G:\project\javaProj\gaoji"
    # dst_path = r"G:\考公"
    # dst_path = r"G:\project\springbootProj\writer-new2\backup2021年10月10日153506"
    # dst_path = r"G:\project\Android\LoginApplication\handout"
    # dst_path = r"G:\file\学校\Android\lab5"
    # dst_path = r"G:\file\学校\Android\lab5\AccountingMainLayoutSteps"
    # dst_path = r"G:\file\学校\Android\lab6\moments"
    # dst_path = r"G:\运动项目\没有log 服务器的log是 warn"


    # proj_path = r"G:\project\Android\LoginApplication\LoginApplication"
    # dst_path = r"G:\project\Android\LoginApplicationX"

    # proj_path = r"G:\project\Android\LoginApplication\handout\loginApllication"
    # dst_path = r"G:\project\Android\LoginApplicationX2"
    
    # proj_path = r"G:\project\Android\LoginApplication\handout\loginApllication"
    # dst_path = r"G:\project\Android\backup\LoginApplicationV7"

    # proj_path = r"G:\project\vue\newfit_vue"
    # dst_path = r"G:\project\vue\origin_flight"
    # proj_path = r"G:\project\Android\LoginApplication\handout\loginApllication"
    # dst_path = r"G:\file\学校\Android\lab7\LoginApplicationDb"

    # proj_path = r"G:\project\Android\moments"
    # dst_path = r"G:\project\Android\moments_sensen"
    
    # proj_path = r"G:\project\Android\moments"
    # dst_path = r"D:\project\android\moments"

    # proj_path = r"G:\project\springbootProj\kinect3"
    # dst_path = r"D:\project\android\moments"

    # proj_path = r"G:\project\Android\moments"
    # dst_path = r"G:\file\学校\Android\拓展实验1\moments"
    # G:\project\Android\moments\app\src\main\java\com\example\moments\repository\CommentRepository.java

    proj_path = r"G:\project\Android\LoginApplication\handout\loginApllication"
    dst_path = r"G:\project\Android\LoginApplication3_stash"
    
    
    
    
    # dst_path = r"G:\project\javaProj\gaoji_back"
    file_lst = []
    dst_lst = []
    ignore_dir_lst = ["dist", "node_modules", ".git", ".idea","out","target","build","backup","sql"]

    ignore_filename_lst = ["dist (5).zip"]
    # re_lst = ["\.java$"]
    re_lst = None
    # 所有文件都查找
    # re_lst = [".java$"]

    like_str_list = ["zip", "js"]
    # get_files_if_name_like(proj_path, file_lst, like_what="zip", ignore_dir_lst=ignore_dir_lst)
    # get_files_if_name_like(proj_path, file_lst, like_what="zip")
    # print("file_lst", file_lst)

    # get_files_if(proj_path, file_lst, like_str_list, ignore_dir_lst)

    # 文档：file_lst ['GprojectspringbootProjwri...
    # 链接：http://note.youdao.com/noteshare?id=d71a7878f1df64c6e4b5f2c4f5b352c9&sub=A2D946DC1D294977A7551DF617922A62
    # copy_files_if(proj_path, dst_path, file_lst, like_str_list, ignore_dir_lst)
    # print("file_lst", file_lst)
    # get_src_dst_list(proj_path, dst_path, file_lst,dst_lst, like_str_list,
    #                  ignore_dir_lst,ignore_filename_lst)

    # get_src_dst_list(proj_path, dst_path, file_lst,dst_lst,
    #                  ignore_dir_lst,ignore_filename_lst)
    # print("file_lst", file_lst)
    # print("dst_lst", dst_lst)
    # dst_file = 'G:\\考公\\src\\api\\album.js'
    # src_file = 'G:\\project\\springbootProj\\writer\\writer-vue-new\\writer-vue-new\\src\\api\\album.js'
    # dst_sps=os.path.split(dst_lst)
    # os.path.join(dst_lst)
    # dirname = os.path.dirname(dst_file)
    # # dirname G:\考公\src\api
    # print("dirname", dirname)

    # copy_file_force('G:\\project\\springbootProj\\writer\\writer-vue-new\\writer-vue-new\\src\\api\\album.js',
    #                 dst_file )
    # 强制覆盖吗 shutil 复制 如果有文件存在
    # copyfile('G:\\project\\springbootProj\\writer\\writer-vue-new\\writer-vue-new\\src\\api\\album.js',
    #          'G:\\考公\\src\\api\\album.js')
    # copyfile 目录不存在 就创建
    # https://blog.csdn.net/qq_42455710/article/details/88861296
    # copy_file_not_cover(src_file, dst_file)
    # python 解析 gitignore
    # /** 形式正则
    # test_re()
    get_src_dst_list_re(proj_path, dst_path, file_lst, dst_lst,
                        ignore_dir_lst, re_lst)
    print("file_lst", file_lst)
    print("dst_lst", dst_lst)
    copyfile_lst(file_lst,dst_lst)
    print("back up at",dst_path)

if __name__ == "__main__":
    # get_file_names()
    # concat_vedios()
    # pass

    # absolute_mkdir(path)
    # print(escape_and_escape("e:\\doa\\a"))
    # print(escape_and_escape("e:\\\nad\dad"))
    # print(get_absolute_path_by_a_list(["e:\\doan", "bea"]))
    # 下载要的图片

    # api_token = "fklasjfljasdlkfjlasjflasjfljhasdljflsdjflkjsadljfljsda"
    # download_img(img_url, api_token)
    # pass
    # if_same_dirs(dir1=r"D:\project\springBootProject\admin-master\admin-master\src\main\java\com\admin",
    #              dir2=r"D:\out_dir")
    # print(os.path.exists(r"此电脑\gerogerori\内部存储\4"))
    # print(os.path.exists(r"此电脑"))
    # print("C:\\Program Files (x86)\\Microsoft Visual Studio 14.0\\VC\\BIN\\x86_amd64\\".replace("\\\\","\\"))
    # print(os.path.exists(r"f:"))
    # print(os.path.exists(r"gerogerori"))

    # lst_file_with_name(".zip", dir=dir)
    dir_path = r"D:\project\python_project"
    # print_files_if_kind(dir_path, ".mp4")
    # print_files_if(dir_path, if_is_mp4)
    # print_files_if_size(dir_path, 1000000 * 10)
    # print_files_if_kind(dir_path, ".mp4")
    file_path = r"D:\project\python_project\ALBERT\venv\Lib\site-packages\numpy\.libs\libopenblas.NOIJJG62EMASZI6NYURL6JBKM4EVBGM7.gfortran-win_amd64.dll"
    # print(os.path.getsize(file_path))
    # print_size(file_path)
    # B yte 单位
    # print_files_if_size(dir_path,1000000)
    # print_size_to_txt('files.txt')
    # list_files_size(r"D:\project")
    # list_dir_size(r"D:\project")
    # list_dir_path=r"D:\qqfile\2500441778"
    # list_dir_path="D:\\"
    list_dir_path = "C:\\"
    # lst_dir=os.listdir(list_dir_path)
    # print(lst_dir)
    # print_files_if_size_with_unit(list_dir_path,100,"MB")
    # PermissionError: [WinError 5] 拒绝访问。: 'D:\\$RECYCLE.BIN\\S-1-5-18'
    # r"D:\qqfile"
    # download_img("https://raw.githubusercontent.com/qq547276542/blog_image/master/%E7%81%B0%E8%89%B2%E9%A2%84%E6%B5%8B%E6%A8%A1%E5%9E%8B/1.png",
    # "1",".png")
    url_pic = "http://xk.zucc.edu.cn/CheckCode.aspx?SafeKey=3c35dac422e0424a12a0fdcb41ce96c6"
    # download_img(url_pic,"code",".jpg","imgs")
    # search_path = r"D:\project\javaProj\oppHomework"
    search_path = r"G:\file\学校\zju-icicles-master"
    
    # print_files_if_name_like(search_path,like_what="sjc")
    personal_words = []
    # print_files_if_name_like_ignore_case(search_path,like_what=".zip")
    # code_path = r"G:\project\pythonProj\my_util"
    code_path = r"G:\file\学校\Android\lab6\moments"
    
    # print_files_if_size_with_unit(code_path,1,"MB")
#     G:\file\学校\Android\lab6\moments\.gradle\6.1.1\executionHistory\executionHistory.bin
# size: 1874280 B,  1874.28 KB,  1.87428 MB
# G:\file\学校\Android\lab6\moments\.gradle\6.1.1\javaCompile\classAnalysis.bin
# size: 1940172 B,  1940.172 KB,  1.940172 MB

    # test_re()
    # backup_proj_src()


