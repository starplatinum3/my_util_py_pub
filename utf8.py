# Python3 将GBK转换成utf-8编码，明天继续实现，把*.java文件 *.porperties文件都转成utf-8
import codecs
from logging.handlers import RotatingFileHandler


def ReadFile(filePath, encoding="gbk"):
    try:
        with codecs.open(filePath, "r", encoding) as f:
            return f.read()
    except Exception as e:
        print(filePath,"不是",encoding)
        return None



def WriteFile(filePath, data, encoding="utf-8"):
    with codecs.open(filePath, "w+", encoding) as f:
        f.write(data)


def UTF8_2_GBK(src, dst):
    content = ReadFile(src, encoding="gbk")
    WriteFile(dst, content, encoding="utf-8")

def gbk_to_utf8(src, dst):
    content = ReadFile(src, encoding="gbk")
    if None==content:
        return
    WriteFile(dst, content, encoding="utf-8")



import os
import os.path

def str_end_with_in_list(string:str,end_with_list):
    for i in end_with_list:
        if(string.endswith(i)):
            return True
    return False

# 递归遍历rootdir目录，把目录中的*.java编码由gbk转换为utf-8
def ReadDirectoryFile(rootdir,end_with_list,out_root):
    fail_lst=[]
    from_path_lst=[]
    to_abs_lst=[]
    for parent, dirnames, filenames in os.walk(rootdir):
        # case 1:
        for dirname in dirnames:
            pass
            # print("parent folder is:" + parent)
            # print("dirname is:" + dirname)
        # case 2
        for filename in filenames:
            # print("parent folder is:" + parent)
            # print("filename with full path:" + os.path.join(parent, filename))
            # if filename.endswith(".cpp"):
            if(str_end_with_in_list(filename,end_with_list)):
        
            # if filename.endswith(".java"):
                
                from_abs=os.path.join(parent, filename)
                to_abs=os.path.join(out_root,parent, filename)
                # ReadFile(from_abs,"utf-8")
                from_path_lst.append(from_abs)
                to_abs_lst.append(to_abs)
                try:
                    # UTF8_2_GBK(os.path.join(parent, filename), os.path.join(parent, filename))
                    # UTF8_2_GBK(from_abs, to_abs)
                    # gbk_to_utf8(from_abs, to_abs)
                    pass
                # print("Java文件")
                except:
                    fail_lst.append(from_abs)
    print("from_path_lst",from_path_lst)
    print("to_abs_lst",to_abs_lst)
    print("fail_lst",fail_lst)


end_with_list=[".cpp",".java"]

# import myfile
from myfile import backup_proj_src,get_src_dst_list_re

if __name__ == "__main__":
    # ReadDirectoryFile(".")
    
    # root_dir=r"G:\project\javaProj\eclipse_20_08\ccrental\src\cn\edu\zucc\personplan"
    # root_dir=r"D:\proj\cpp\data-struct-code-cpp"
    # G:\project\Android\GameHall_Android2
    # root_dir=r"D:\proj\Android\安卓物理小球滚动游戏源码_爱给网_aigei_com\安卓物理小球滚动游戏源码"
    # dst_path=r"D:\proj\Android\安卓物理小球滚动游戏源码_爱给网_aigei_com\安卓物理小球滚动游戏源码"

    # root_dir=r"G:\project\Android\GameHall_Android2"
    # dst_path=r"G:\project\Android\GameHall_Android2_bak"

    # root_dir=r"G:\project\Android\GameHall_Android2_bak"
    # dst_path=r"G:\project\Android\GameHall_Android2_bak2"

    # root_dir=r"G:\project\Android\GameHall_Android2_bak2"
    # # dst_path=r"G:\project\Android\GameHall_Android2_bak3"
    # back_dir=r"G:\project\Android\GameHall_Android2_bak3"

    root_dir=r"D:\project\waibao\what-rubbish-final\app\src\main\java\com\bn\tl\anzhi"
    back_dir=r"D:\project\waibao\what-rubbish-final-bak\utf-8-2\app\src\main\java\com\bn\tl\anzhi"
    # python 判断path 在不在
        # import os.path
    if not os.path.exists(back_dir):
        print("没有备份目录，创建目录",back_dir)
        # os.mkdirs(back_dir)
        os.makedirs(back_dir)
        # makedirs

    # os.path.ispa
    # os.mkdirs(back_dir)
    from_lst=[]
    to_lst=[]
    ignore_dir_lst=[]
    re_lst=None
    # 全部都要
    get_src_dst_list_re(root_dir, back_dir, from_lst, to_lst,
                        ignore_dir_lst, re_lst)
    # backup_proj_src(root_dir,back_dir)

    print("from_lst",from_lst)
    print("to_lst",to_lst)

    # i=0
    # for f in from_lst:
    #     data=ReadFile(f)
    #     if data==None:
    #         continue
    #         i+=1
    #     WriteFile(to_lst[i], data)
    #     i+=1

    for i in range(len(from_lst)):
        from_file=from_lst[i]
        to_file=to_lst[i]
        data=ReadFile(from_file)
        if data==None:
            continue
        WriteFile(to_file, data)
    
    # print("备份在",back_dir)
    # ReadDirectoryFile(root_dir,end_with_list,back_dir)
    
    print("end")
    # print("备份在",back_dir)
    print("输出utf-8",back_dir)
    # print("out here ",root_dir)