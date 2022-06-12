from selenium import webdriver


# driver = webdriver.Firefox()   # Firefox浏览器
# # driver = webdriver.Firefox("驱动路径")

# driver = webdriver.Chrome()    # Chrome浏览器

# driver = webdriver.Ie()        # Internet Explorer浏览器

# driver = webdriver.Edge()      # Edge浏览器
driver = webdriver.Edge(r"D:\software\edgedriver_win64\msedgedriver.exe")    
# "D:\software\edgedriver_win64\msedgedriver.exe"

# driver = webdriver.Opera()     # Opera浏览器

# driver = webdriver.PhantomJS()   # PhantomJS
url="http://www.baidu.com"
# 打开网页
driver.get(url) # 打开url网页 比如 driver.get("http://www.baidu.com")