
# import imp
# from myfile import make_dir_if_not_exists

# import LeetCode
# from LeetCode import LeetCodeUtil
# LeetCodeUtil.printLstMarked([1],[0])

# make_dir_if_not_exists(r"D:\test")
# OSError: [WinError 123] 文件名、目录名或卷标语法不正确。: 'D:\test'

print(3.8*6)
# 22.799999999999997

print(3.8*12)
# 45.599999999999994

print(3.8*16)
# 60.8

print(4.5*12)
# 54.0

print(15*5)

import regex
# import re
strings = [
    "hell(h)o(world)",
    "hel(lo(wor)ld)",
    "hell(h)o(world)blahblahblah"
]
pattern = r"(\((?:[^()]++|(?1))*\))(?=[^()]*$)"
for s in strings:
    print(regex.sub(pattern, "", s))
    # print(re.sub(pattern, "", s))