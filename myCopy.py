
import os
from  strUtil.strUtil  import one_slash_to_two

root_dir=r"D:\project\waibao\what-rubbish-final\app\src\main\assets\trashBin\small"
two_slash_path=one_slash_to_two(root_dir)
# 这个不对
# cmd=f"copy {two_slash_path}/mario_00.png {two_slash_path}/mario_0{2}.png"
# 这个可以
cmd=f"copy {two_slash_path}\\\\mario_00.png {two_slash_path}\\\\mario_0{2}.png"
# cmd=f"copy {root_dir}/mario_00.png {root_dir}/mario_0{2}.png"
print("cmd",cmd)
# import strUtil.strUtil 

# os.system(f"copy {root_dir}/mario_00.png {root_dir}/mario_0{2}.png")
# os.system(cmd)

cmd=f"copy {two_slash_path}\\\\mario_inv_00.png {two_slash_path}\\\\mario_inv_0{1}.png"
os.system(cmd)

# for i in range(2,7):
#     # cmd=f"copy {two_slash_path}\\\\mario_00.png {two_slash_path}\\\\mario_0{i}.png"
#     # os.system(f"copy {root_dir}/mario_00.png {root_dir}/mario_0{i}.png")
#     cmd=f"copy {two_slash_path}\\\\mario_inv_00.png {two_slash_path}\\\\mario_inv_0{i}.png"
#     os.system(cmd)