# import os
# os.system('lsof -i:80')

# 如何使用 ：
# 2021年9月14日11:11:00 更新
# 需要在Config 类里配置
# kill_java_and_nohup.py  放在 jar包所在目录
#  whereis python 查到python的路径
# 因为linux 一般是默认装的python2 而我这个是python3的
# 所以要确保 linux上有python3 ，假如查到一个python3.6
# 他是在 /usr/bin/python3.6
# 那就直接 python3.6 kill_java_and_nohup.py
# 如果python装的位置不是在bin 底下的
# 那就直接绝对路径
# 比如说python在 /home/aaa/python3.6
# 那么 /home/aaa/python3.6  kill_java_and_nohup.py
# 我这里jar包名字写死了  demo-0.0.1-SNAPSHOT.jar 
# 端口写死了.  需要自己换
# 会有 kill 不掉 java的问题 这样很麻烦
# 很多次都是第一次 kill 不掉，第二次才能kill掉。。
# 在config 里面设置 这三个东西，jar包的位置，最好是绝对路径
# self.jar_name = "/home/mqp/iot/mqp-iot-db-0.0.1-SNAPSHOT.jar"
# log文件的名字模板，需要有个{} 里面我会填充时间
#         self.log_file_name_templete = "log_{}.log"
# 运行的端口
#         self.port = "8899"
# 然后 python3 kill_java_and_nohup.py  跑起来
# 跑起来之后 会打印 cmd : cat log_时间_.log
# 可以复制  cat log_时间_.log 这句命令， 用来查看运行log
# 其实很多情况下他会显示端口已经被占用，但是只要第二次运行 python3 kill_java_and_nohup.py
# 基本上就可以成功

import os

import time


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
        self.port = "8899"
        # self.jar_name = "pz-blog-1.0.jar"
        # self.log_file_name_templete = "log_{}.log"
        # self.port = "8085"
        self.sudo=" "

        


def show_info(out):
    info = out.readlines()
    for line in info:  # 按行遍历
        line = line.strip('\r\n')
        print(line)


def kill_java(config):
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
        if line.startswith("java"):
            kill_java_line(line, config)
            return False
    # java 杀完了
    return True


def kill_java_and_nohup(config):
    # port="80"
    # jar_name="demo-0.0.1-SNAPSHOT.jar"
    # # command = 'ping www.baidu.com' #可以直接在命令行中执行的命令
    # r = os.popen('lsof -i:'+port)
    # # r = os.popen(command) #执行该命令
    # info = r.readlines()  #读取命令行的输出到一个list
    # for line in info:  #按行遍历
    #     line = line.strip('\r\n')
    #     print(line)
    #     if line.startswith("java"):
    #         kill_java_line(line)
    # while kill_java():
    #     # kill_java()
    #     time.sleep(1)

    # kill_java()
    kill_java(config)

    # jar_name = "demo-0.0.1-SNAPSHOT.jar"
    jar_name = config.jar_name

    print("nohup java -jar")
    # log_version=11

    # with open("log_version.txt","r") as f:
    #     data=f.read().strip()
    #     log_version=int(data)

    # log_file_name="kinect85_0.0.1_redpack10.log"
    time_str = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    # print(time_str)
    # log_file_name = "kinect0.0.1_redpack{}.log".format(time_str)
    log_file_name = config.log_file_name_templete.format(time_str)
    # os.system("nohup java -jar  demo-0.0.1-SNAPSHOT.jar   > "+log_file_name+"  &")
    # out=os.popen("nohup java -jar  demo-0.0.1-SNAPSHOT.jar   > "+log_file_name+"  &")
    out = os.popen(config.sudo + " nohup java -jar  " + jar_name + "  > " + log_file_name + "  &")
    # os.system("")
    # out.readlines()
    show_info(out)
    # print(out)
    # print("log_file_name: ", log_file_name)
    print("cmd : cat ", log_file_name)
    # with open("log_version.txt","w") as f:
    #     f.write(str(log_version+1))


# cat kinect85_0.0.1_redpack8.log


def remove(lst, what=""):
    ret = []
    for val in lst:
        if val == what:
            continue
        ret.append(val)
    return ret


def kill_java_line(line, config):
    print("kill_java_line")
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
    # print(out)
    # show_info(out)


def create_version_txt():
    # version_txt_path="test_file.txt"
    version_txt_path = "log_version.txt"
    if not os.path.exists(version_txt_path):
        print("not exists", version_txt_path)
        with open(version_txt_path, "w") as f:
            data = str(1)
            f.write(data)


# create_version_txt()
config = Config()
kill_java_and_nohup(config)

# line="java       659243 root   20u  IPv6 57698716      0t0  TCP *:http (LISTEN)"
# # sps=line.split(" ")
# # sps=line.split("\t")
# sps=line.split(" ")
# # sps.remove("")
# sps=remove(sps,"")
# print(sps)
# pid=sps[1]
# print("pid: ",pid)
# with open("log_version.txt","r") as f:
#     data=f.read().strip()

#     log_version=int(data)
#     print("log_version: ",log_version)
# time_str=time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()) 
# print(time_str)
# D:\project\python_project\my_util>%py37albert% -u "d:\project\python_project\my_util\put_jar_to_web.py"
# 2021_08_18_12_11_39
