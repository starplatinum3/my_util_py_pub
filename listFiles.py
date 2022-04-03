
import os

root_dir=r"G:\file"
lst_dir=os.listdir(root_dir)
out_str=""
for i in lst_dir:
    abs_path= os.path.join(root_dir,i)
    out_str+=abs_path+"\n"

with open("listFiles.txt","w",encoding="utf-8") as f:
    f.write(out_str)
