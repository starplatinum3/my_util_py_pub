
import os
# port=8888
# port="8889"
# port="8890"
# 阿里云打开
root_path="/home/mqp/wx-sorting_build"
#/home/mqp/wx-sorting_build_web_desktop

# root_path="/home/mqp/wx-sorting_build_web_desktop"

#/home/mqp/wx-sorting_build_web_desktop

def remove(lst, what=""):
    ret = []
    for val in lst:
        if val == what:
            continue
        ret.append(val)
    return ret

class Config():
    def __init__(self):
        # self.jar_name = "demo-0.0.1-SNAPSHOT.jar"
        # # self.jar_name = "sys-writer-web-0.0.1-SNAPSHOT.jar"
        # self.log_file_name_templete = "log_{}.log"
        # # self.port="80"
        # # self.port = "8088"
        # self.port = "8080"
        # # self.sudo = "sudo "
        # self.sudo=" "
        # # sudo 后面最好有个空格

        # self.jar_name = "/home/mqp/whatRubbish-0.0.1-SNAPSHOT.jar"
        # self.log_file_name_templete = "log_{}.log"
        # self.port = "8889"

        self.jar_name = "/home/mqp/iot/mqp-iot-db-0.0.1-SNAPSHOT.jar"
        self.log_file_name_templete = "log_{}.log"
        # self.port = "8899"
        self.port="8890"
        # self.jar_name = "pz-blog-1.0.jar"
        # self.log_file_name_templete = "log_{}.log"
        # self.port = "8085"
        self.sudo=" "
        self.kill_app_name="nginx"

def kill_app_line(line, config):
    print("kill_app_line")
    # sps=line.split(" ")
    # pid=sps[1]
    sps = line.split(" ")
    # sps.remove("")
    sps = remove(sps, "")
    # print(sps)
    pid = sps[1]
    # os.system('kill '+pid)
    kill_pid = config.sudo + ' kill ' + pid
    print("kill_pid: ", kill_pid)
    out = os.popen(kill_pid)

def kill_app(config):
    # port = "80"
    port = config.port

    # command = 'ping www.baidu.com' #可以直接在命令行中执行的命令
    r = os.popen(config.sudo + ' lsof -i:' + port)
    # r = os.popen(command) #执行该命令
    info = r.readlines()  # 读取命令行的输出到一个list
    have_java = False
    for line in info:  # 按行遍历
        line = line.strip('\r\n')
        # print(line)
        # if line.startswith("java"):
        if line.startswith(config.kill_app_name):
            kill_app_line(line, config)
            return False
    # java 杀完了
    return True

config = Config()
kill_app(config)
port=config.port

with open("nginx_template.conf","r",encoding="utf-8") as f:
    nginx_template= f.read()

nginx_template:str

out_str=nginx_template.replace("$port$", port)
out_str=out_str.replace("$root_path$", root_path)




nginx_root_dir=f"/home/nginx/{port}"

# out_path=f"/home/nginx/nginx_{port}.conf"
out_path=f"{nginx_root_dir}/nginx_{port}.conf"
# out_path=f"nginx_{port}.conf"
with open(out_path,"w",encoding="utf-8") as f:
    # nginx_template= f.read()
    f.write(out_str)

print("config write here",out_path)
print(f"nginx_root_dir {nginx_root_dir}")
print(f"port {port}")

os.system(f"mkdir {nginx_root_dir}")
os.system(f"cp /usr/sbin/nginx  {nginx_root_dir}/nginx")

# os.system(f"mkdir /home/nginx/{port}")
# os.system(f"mkdir /home/nginx/{port}/log")
os.system(f"mkdir {nginx_root_dir}/log")
os.system(f"{nginx_root_dir}/nginx -c {nginx_root_dir}/nginx_{port}.conf")
print("查看nginx 有没有启动")
os.system(f"lsof -i :{port}")
# os.system(f"/home/nginx/{port}/nginx -c /home/nginx/{port}/nginx_{port}.conf")

