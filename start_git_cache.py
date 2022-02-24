

jar_path=r"D:\proj\springboot\github-cache\target\eye-0.0.1-SNAPSHOT.jar"

nginx_path=r"D:\software\nginx-1.15.2\nginx.exe"
import os
os.system(f"java -jar {jar_path}")

os.system(nginx_path)
