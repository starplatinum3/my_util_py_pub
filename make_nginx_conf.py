
import os
# port=8888
# port="8889"
port="8890"
# 阿里云打开
root_path="/home/mqp/wx-sorting_build"

with open("nginx_template.conf","r",encoding="utf-8") as f:
    nginx_template= f.read()

nginx_template:str

out_str=nginx_template.replace("$port$", port)
out_str=out_str.replace("$root_path$", root_path)

# out_path=f"/home/nginx/nginx_{port}.conf"
out_path=f"nginx_{port}.conf"
with open(out_path,"w",encoding="utf-8") as f:
    # nginx_template= f.read()
    f.write(out_str)

print("config write here",out_path)

nginx_root_dir=f"/home/nginx/{port}"
os.system(f"mkdir {nginx_root_dir}")
os.system(f"cp /usr/sbin/nginx  {nginx_root_dir}/nginx")

# os.system(f"mkdir /home/nginx/{port}")
# os.system(f"mkdir /home/nginx/{port}/log")
os.system(f"mkdir {nginx_root_dir}/log")
os.system(f"{nginx_root_dir}/nginx -c {nginx_root_dir}/nginx_{port}.conf")

# os.system(f"/home/nginx/{port}/nginx -c /home/nginx/{port}/nginx_{port}.conf")

