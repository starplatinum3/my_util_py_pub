# time_ 

from time_util import get_now_time_str
import os

now_time_str=get_now_time_str()
print("now_time_str",now_time_str)

with open("now_time.md",'a') as f:
    f.write("\n"+now_time_str)

# git add .
# now_time.md
os.system("git add .")
os.system(f"git commit -m '{now_time_str}'")
os.system("git push origin master ")