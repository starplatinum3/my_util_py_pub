

change_map={
    "import androidx.core.app.Fragment;":"import androidx.fragment.app.Fragment;",
    "androidx.core.app.FragmentManager;":"androidx.fragment.app.FragmentManager;",
    "androidx.core.app.FragmentTransaction;":"androidx.fragment.app.FragmentTransaction;",
    "com.snatik.matches.R;":"com.example.whatrubbish.R;"
}

# import 
from myfile import get_src_dst_list_re,backup_proj_src

from_dir=r"D:\project\waibao\what-rubbish-final"
to_dir=r"D:\project\waibao\what-rubbish-final-bak\MigrateX"
from_lst=[]
to_lst=[]
ignore_dir_lst = ["dist", "node_modules", ".git", ".idea","out","target","build","backup","sql"]
# ignore_dir_lst=[".git"]
# re_lst=None
# re_lst=["#="]
re_lst = [".java$"]
# 全部都要
get_src_dst_list_re(from_dir, to_dir, from_lst, to_lst,
                    ignore_dir_lst, re_lst)

print("to_lst[0]")
print(to_lst[0])
def replace_and_cmt(src_str,from_str,to_str):
    cmt_str="//"+from_str
    if "import" not in  to_str:
        to_str="import "+to_str
    replace_str=cmt_str+"\n"+to_str
    return src_str.replace(from_str,replace_str)

def replace_migrate_x_str(input_str):
    out_str=input_str
    for from_str,to_str in change_map.items():
        # out_str=out_str.replace(from_dir,)
        out_str=replace_and_cmt(out_str, from_str, to_str)
    return out_str
from myfile import diff_encode_read,copyfile_lst
# D:\project\waibao\what-rubbish-final\app\src\main\java\com\snatik\matches\fragments\MenuFragment.java
copyfile_lst(from_lst,to_lst)
# backup_proj_src(from_dir,to_dir)
# for i in range(len(from_lst)):
#     from_file=from_lst[i]
#     to_file=to_lst[i]
#     # data=ReadFile(from_file)
#     data=diff_encode_read(from_file)
#     # with open(from_file,"r",encoding="utf-8") as f:
#     # # with open(from_file,"r") as f:
#     #     data=f.read()
#     if data==None:
#         continue
    
#     data=replace_migrate_x_str(data)
#     if "MenuFragment" in from_file:
#         print(data)
#     with open(to_file,"w") as f:
#         f.write(data)
#     # WriteFile(to_file, data)

for i in range(len(from_lst)):
    from_file=from_lst[i]
    to_file=to_lst[i]
    # data=ReadFile(from_file)
    # data=diff_encode_read(from_file)
    data=diff_encode_read(to_file)
    # with open(from_file,"r",encoding="utf-8") as f:
    # # with open(from_file,"r") as f:
    #     data=f.read()
    if data==None:
        continue
    
    data=replace_migrate_x_str(data)
    if "MenuFragment" in from_file:
        print(data)
    try:
        with open(to_file,"w",encoding="utf-8") as f:
            f.write(data)
    except:
        print(to_file)
    # WriteFile(to_file, data)

print("输出",to_dir)