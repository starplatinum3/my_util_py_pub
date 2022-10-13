
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


# path=r"D:\school"
# path=r"D:\download"
# path=r"D:"
# path=r"D:\\"
path="D:\\"
# path=r"D:\人脸"
# out_file_name="findFileD人脸.txt"
out_file_name="findFileDAll.txt"
# "C:\\"
out_str=""
res_list=[]

# D:\aaaa\Pacman\Library\metadata\43\439c018cf4619e94d9a92110ce0aa188.info
# D:\aaaa\BreakTheBricks\Library\ShaderCache\d\d0608dd0c980f8e3db87a9ead9fadf7e.bin
# D:\aaaa\BreakTheBricks\Library\PackageCache\com.unity.textmeshpro@2.0.1\Scripts\Editor\TMP_FontAssetEditor.cs
ignore_dir_lst=["node_modules",".git",".gradle","$RECYCLE.BIN","target",".AndroidStudio","PackageCache","ShaderCache"]
make_files_lst(path,res_list,ignore_dir_lst)
# print(res_list)
out_str+=path+"\n"
for i in res_list:
    out_str+=i+"\n"

# out_file_name="findFileDSchool.txt"
# out_file_name="findFileDDownload.txt"
# out_file_name="findFileDAll.txt"
with open(out_file_name,"w" ,encoding="utf-8") as f:
    f.write(out_str)