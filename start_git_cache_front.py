

jar_path=r"D:\proj\springboot\github-cache\target\eye-0.0.1-SNAPSHOT.jar"

nginx_path=r"D:\software\nginx-1.15.2\nginx.exe"
nginx_dir=r"D:\software\nginx-1.15.2"
conf_path="conf/nginx_gitCache.conf"
import os

os.chdir(nginx_dir)
# os.system("nginx")
print(f"开启 nginx 配置路径 {conf_path}")
os.system(f"nginx -c {conf_path}")
# http://localhost:8082
# port="80"
addr="http://localhost"
# addr="http://localhost:8082"
print("start at ",addr)

brower_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe"
# proj_net_url=
# python 打开网页
# https://www.php.cn/python-tutorials-425154.html
# os.system('"C:/Program Files/Internet Explorer/iexplore.exe" http://www.baidu.com')
os.system(f'"{brower_path}" {addr}')

# os.system(f"java -jar {jar_path}")
# 前后端貌似都需要在前台 所以会阻塞。。
