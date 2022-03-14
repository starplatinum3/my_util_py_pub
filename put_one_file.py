

# from posixpath import dirname
from time import time
# from tkinter.messagebox import NO
import requests

import os

from time_util import get_now_time_str
# D:\proj\python\my_util_py_pub\key_words
# os.path.join("key_words")
dir_name="key_words"
files=os.listdir(dir_name)
out_csv_path=os.path.join(dir_name,"all_key_wrods.csv")
for file in files:
    abs_path=os.path.join(dir_name,file)
    