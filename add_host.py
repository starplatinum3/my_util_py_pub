
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
back_file=back_dir+"/hosts_"+get_now_time_str()
print(f"cat {back_file}")
cp_cmd="cp %s %s"%(hosts_path,back_file)
print("cp_cmd",cp_cmd)
os.system(cp_cmd)

# io.UnsupportedOperation: not readable
# 

with open(hosts_path,"r") as f:
    hosts_origin=f.read()
    print("hosts_origin",hosts_origin)

out_data=hosts_origin+"\n"+addHostStr+"\n"
print("out_data")
print(out_data)

with open(hosts_path,"w") as f:
    f.write(out_data)
# with open(hosts_path,"a") as f:
#     hosts_origin=f.read()
#     print("hosts_origin",hosts_origin)
#     # hosts_origin++
#     f.write("\n"+addHostStr+"\n")

print(f"cat {hosts_path}")