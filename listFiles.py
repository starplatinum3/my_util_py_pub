
import os

from myfile import make_files_lst

# root_dir=r"G:\file"
# lst_dir=os.listdir(root_dir)
# out_str=""
# for i in lst_dir:
#     abs_path= os.path.join(root_dir,i)
#     out_str+=abs_path+"\n"

# with open("listFiles.txt","w",encoding="utf-8") as f:
#     f.write(out_str)


path=r"D:\school"

out_str=""
res_list=[]
ignore_dir_lst=["node_modules",".git",".gradle"]
make_files_lst(path,res_list,ignore_dir_lst)
# print(res_list)
out_str+=path+"\n"
for i in res_list:
    out_str+=i+"\n"

out_file_name="findFileDSchool.txt"
with open(out_file_name,"w" ,encoding="utf-8") as f:
    f.write(out_str)