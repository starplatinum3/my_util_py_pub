import os
import PyMySQL

# newfit-vue
git_url="https://gitee.com/starplatinum111/newfit-vue"

download_path=r"D:\newfit\newfit_vue"

print("开始clone")
print("从 "+git_url)
print("下载到",download_path)

os.chdir(download_path)

os.system(f"git clone {git_url}")