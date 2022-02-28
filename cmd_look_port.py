

# https://www.jianshu.com/p/3f330c299276

import os
# port="8089"
port="80"
os.system(f"netstat -ano |findstr {port}")

# tasklist|findstr "进程ID" ：查看对应进程的任务；tasklist|findstr 15348
pid=""
# os.system(f"tasklist |findstr {pid}")