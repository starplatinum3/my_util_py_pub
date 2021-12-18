# Python3 将GBK转换成utf-8编码，明天继续实现，把*.java文件 *.porperties文件都转成utf-8
import codecs


def ReadFile(filePath, encoding="gbk"):
    try:
        with codecs.open(filePath, "r", encoding) as f:
            return f.read()
    except Exception as e:
        print(filePath,"不是",encoding)



def WriteFile(filePath, u, encoding="utf-8"):
    with codecs.open(filePath, "w", encoding) as f:
        f.write(u)


def UTF8_2_GBK(src, dst):
    content = ReadFile(src, encoding="gbk")
    WriteFile(dst, content, encoding="utf-8")


import os
import os.path

def str_end_with_in_list(string:str,end_with_list):
    for i in end_with_list:
        if(string.endswith(i)):
            return True
    return False

# 递归遍历rootdir目录，把目录中的*.java编码由gbk转换为utf-8
def ReadDirectoryFile(rootdir,end_with_list):
    fail_lst=[]
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
                to_abs=os.path.join(parent, filename)
                ReadFile(from_abs,"utf-8")
                try:
                    # UTF8_2_GBK(os.path.join(parent, filename), os.path.join(parent, filename))
                    UTF8_2_GBK(from_abs, to_abs)
                # print("Java文件")
                except:
                    fail_lst.append(from_abs)
    print("fail_lst",fail_lst)


end_with_list=[".cpp",".java"]

if __name__ == "__main__":
    # ReadDirectoryFile(".")
    
    # root_dir=r"G:\project\javaProj\eclipse_20_08\ccrental\src\cn\edu\zucc\personplan"
    root_dir=r"D:\proj\cpp\data-struct-code-cpp"
    
    ReadDirectoryFile(root_dir,end_with_list)
    print("end")