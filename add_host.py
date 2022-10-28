
addHostStr="""
127.0.0.1   hadoop1
127.0.0.1  hadoop"""
import time

back_dir="/home/app"
def get_now_time_str():
    now_time_str = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    return now_time_str

hosts_path="/etc/hosts"

# with open("")
import os
os.system("cp %s %s"%(hosts_path,back_dir+"/hosts_"+get_now_time_str()))

with open(hosts_path,"a") as f:
    f.write("\n"+addHostStr+"\n")