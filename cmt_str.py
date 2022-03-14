

import os

# from pyparsing import lineEnd

# from sympy import li


def cmt_str(abs_path):
    with open(abs_path,"r",encoding="utf-8") as f:
        data=f.read()
    lines=data.split("\n")
    cmt_data=""
    # cmt_line_mark=default
    # 'product="default"'
    cmt_line_mark='product="nosdcard"'
    # 'product="default"'
    for line in lines:
        if cmt_line_mark in line :
            # line=
            cmt_data+="<!-- "+line+" -->"
            # cmt_line()
        else:
            cmt_data+=line
        cmt_data+="\n"
    print(cmt_data)
    with open(abs_path,"w+",encoding="utf-8") as f:
        f.write(cmt_data)

# root_dir=r"D:\proj\Android\recorder_res\res"
root_dir=r"D:\proj\Android\recorder_res\res_def\res"

lstDir=os.listdir(root_dir)
for dir in lstDir:
    if dir.startswith("value"):
        # abs_dir=os.path.join(lstDir,dir,"strings.xml")
        abs_file=os.path.join(root_dir,dir,"strings.xml")
        cmt_str(abs_file)

print("end here",root_dir)
