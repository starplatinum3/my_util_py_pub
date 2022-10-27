
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

# import regex
# # import re
# strings = [
#     "hell(h)o(world)",
#     "hel(lo(wor)ld)",
#     "hell(h)o(world)blahblahblah"
# ]
# pattern = r"(\((?:[^()]++|(?1))*\))(?=[^()]*$)"
# for s in strings:
#     print(regex.sub(pattern, "", s))
    # print(re.sub(pattern, "", s))


# print(290+230+388)
# 908

# print(53.8/2)
# 26.9

# print(1.5/22)
# print(22/1.5)
# print(19.9/(6*0.2))
# 14.666666666666666
# 16.58333333333333

# print(16.9/(50*15))
# 0.022533333333333332

# print( 24.50 / (60 * 12) )
# 0.034027777777777775

# print( 29.9 / (60 * 24) )
# 0.020763888888888887

# print(hex(248))
# 0xf8
print(bin(248))
# 0b 1111 1000

# 0b1111011
print(bin(123))
# 0b 0111 1011

#  0111 1
print(int("0b01111000", 2))
# 120

import datetime

now = datetime.datetime.now() # 当前时间
from_date=datetime.datetime(2022,7,25)
ago = now-datetime.timedelta(days=30) # 当前时间往前推30天

# later = now+datetime.timedelta(days=30) # 当前时间往后推30天

# later = now+datetime.timedelta(days=30*3) # 当前时间往后推30天
later = from_date+datetime.timedelta(days=30*3) # 当前时间往后推30天
# later = from_date+datetime.timedelta(days=30*3) # 当前时间往后推30天
# 2022-10-23 00:00:00
print("later")
print(later)
# later
# 2022-10-23 00:00:00
# 2022-12-23 10:53:08.290978


aa=100-66+22
print(aa)
# 56

# 4.9598。  4.62/5  4.57/5。
score=4.9598+ 4.62+4.57
score/=3
print("score",score)
#  4.716600000000001

print(11/7)
# 1.5714285714285714

print(10/6)
# 1.6666666666666667

# 吃饭一小时
print(11/8)
# 1.375

# 442.2 /10 *2
print(442.2 /10 *2)
# 88.44